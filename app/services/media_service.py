import yt_dlp
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from io import BytesIO

def get_youtube_info(url: str) -> dict:
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True, # Important: Do not download video
        'extract_flat': True,  # Faster extraction
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "id": info.get('id'),
                "title": info.get('title'),
                "uploader": info.get('uploader'),
                "duration": info.get('duration'),
                "view_count": info.get('view_count'),
                "thumbnail": info.get('thumbnail'),
                "webpage_url": info.get('webpage_url'),
                "upload_date": info.get('upload_date')
            }
    except Exception as e:
        raise Exception(f"Failed to fetch YouTube info: {str(e)}")

def get_decimal_from_dms(dms, ref):
    degrees = dms[0]
    minutes = dms[1]
    seconds = dms[2]

    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)

    if ref in ['S', 'W']:
        decimal = -decimal

    return decimal

def get_exif_data(image_data: bytes) -> dict:
    try:
        image = Image.open(BytesIO(image_data))
        exif_raw = image._getexif()

        if not exif_raw:
            return {"error": "No EXIF data found"}

        exif_data = {}
        gps_info = {}

        for tag_id, value in exif_raw.items():
            tag = TAGS.get(tag_id, tag_id)

            # Handle GPS Data specifically
            if tag == "GPSInfo":
                for gps_tag_id in value:
                    gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                    gps_info[gps_tag] = value[gps_tag_id]
            else:
                # Convert bytes to string for JSON serialization
                if isinstance(value, bytes):
                    try:
                        value = value.decode()
                    except:
                        value = str(value)
                exif_data[tag] = str(value) # Safely stringify everything else

        # Calculate Coordinates if available
        lat = None
        lon = None
        if gps_info:
            if 'GPSLatitude' in gps_info and 'GPSLatitudeRef' in gps_info:
                lat = get_decimal_from_dms(gps_info['GPSLatitude'], gps_info['GPSLatitudeRef'])
            if 'GPSLongitude' in gps_info and 'GPSLongitudeRef' in gps_info:
                lon = get_decimal_from_dms(gps_info['GPSLongitude'], gps_info['GPSLongitudeRef'])

            exif_data['gps'] = {
                "latitude": lat,
                "longitude": lon,
                "raw_info": {str(k): str(v) for k, v in gps_info.items()} # Serialize keys/values
            }

        return exif_data

    except Exception as e:
         raise Exception(f"Failed to extract EXIF: {str(e)}")
