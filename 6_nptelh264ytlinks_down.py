# just cheking the the pull request
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
    'https://youtu.be/6I7W_96kk2I'
]






download_folder = 'c:/Users/Abc/Downloads/AI'  # Set the path to Downloads folder
download_videos(video_links, download_folder)

