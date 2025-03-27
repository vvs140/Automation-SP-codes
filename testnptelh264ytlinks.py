import os
import yt_dlp

def download_video(video_url, download_folder, retry_count=3):
    safe_download_folder = os.path.abspath(download_folder)
    ydl_opts = {
        'geo-bypass': True,
        'outtmpl': os.path.join(safe_download_folder, '%(title)s.%(ext)s'),
        'format': 'bv*[vcodec^=avc]+ba[ext=m4a]/b[ext=mp4]',  # Ensure H.264 video
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Output format
        }],
        'noplaylist': True,
    }
    
    for attempt in range(retry_count):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return True  # Return success
        except Exception as e:
            print(f'Error downloading {video_url}: {e}. Retrying {attempt + 1}/{retry_count}...')
    return False  # Return failure after retries

def download_videos(video_urls, download_folder):
    missed_files = []

    for video_url in video_urls:
        success = download_video(video_url, download_folder)
        if not success:
            missed_files.append(video_url)

    # Report missed files
    if missed_files:
        print('The following videos could not be downloaded:')
        for url in missed_files:
            print(url)
    else:
        print('All videos downloaded successfully.')

# Example usage with your video links
video_links = [
    'https://youtu.be/Ex8dRE7X498',
    'https://youtu.be/cHIk4zKKkxc',
    'https://youtu.be/_GoR75Plxec',
    'https://youtu.be/ELHj5nCaIz0',
    'https://youtu.be/B0P2IUBPfh4',
    'https://youtu.be/s_GTc88Hkbc',
    'https://youtu.be/PR0_WHYnFzE',
    'https://youtu.be/o9n4XmtClFk',
    'https://youtu.be/0dT-v2YzrP0',
    'https://youtu.be/Cptv9jBA82I',
    'https://youtu.be/uI-Q3FJOCeM',
    'https://youtu.be/UYxfSH6q3MQ',
    'https://youtu.be/Qt5yP_SibuY',
    'https://youtu.be/P9wM00NorKk',
    'https://youtu.be/Aq1wYkS51zw',
    'https://youtu.be/SfFmFNikpaM',
    'https://youtu.be/TBTZzh_xW4M',
    'https://youtu.be/6GZh2bYdbOk',
    'https://youtu.be/3D2K4PGMA6U',
    'https://youtu.be/xT_viCzCKcE',
    'https://youtu.be/jYIX__VdGBA',
    'https://youtu.be/acOauJOR0BQ',
    'https://youtu.be/aOL1oePSqIA',
    'https://youtu.be/0jVlYwa7Lv8',
    'https://youtu.be/6A7ItecUUVc',
    'https://youtu.be/-PXGcJoDNOk',
    'https://youtu.be/MMq93OWgx0w',
    'https://youtu.be/NaCyAQUCY5g',
    'https://youtu.be/ozE_j03iDlQ',
    'https://youtu.be/u2N9Nd4F4d0',
    'https://youtu.be/39A8cD7U_rc',
    'https://youtu.be/UXR70sQ7yLA',
    'https://youtu.be/xrydU0zpV8E',
    'https://youtu.be/VZOyjwWb0_E',
    'https://youtu.be/Ic2ByvDEuMg',
    'https://youtu.be/sZ7xgusCETs',
    'https://youtu.be/kjsSVQuZ28Y',
    'https://youtu.be/MRO2GoL6iFg',
    'https://youtu.be/7Lq5KOdZYNQ',
    'https://youtu.be/00suuUO-YUI',
    'https://youtu.be/ApF9NzmBtAo',
    'https://youtu.be/r4bVGkCtKLo',
    'https://youtu.be/_MfwJBrQjXo',
    'https://youtu.be/6uTvbm8Is8I',
    'https://youtu.be/gMApfIIhfR8',
    'https://youtu.be/Vt77j9TKUUk',
    'https://youtu.be/HXgKYNeVaI8',
    'https://youtu.be/9UlzjK7AieM',
    'https://youtu.be/6I7W_96kk2I'
]






download_folder = 'c:/Users/Abc/Downloads/AI'  # Set the path to Downloads folder
download_videos(video_links, download_folder)
