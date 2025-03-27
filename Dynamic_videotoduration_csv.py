#To run the code install "pip install moviepy pandas"
#At run time just copy paste the Folder containing videos from Windows File explorer {example = C:\Users\Abc\Documents\TALE 2 Course (or)"C:\Users\Abc\Documents\TALEcourse" }
import os
import pandas as pd
from moviepy.editor import VideoFileClip

def get_video_duration(video_path):
    """Get the duration of a video in seconds."""
    try:
        with VideoFileClip(video_path) as video:
            return video.duration
    except Exception as e:
        print(f"Error reading video file {video_path}: {e}")
        return None

def seconds_to_hhmmss(seconds):
    """Convert seconds to hh:mm:ss format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def scan_videos_in_folder(folder_path):
    """Scan a folder for video files and return their names and durations."""
    if not os.path.isdir(folder_path):
        print(f"Error: The path {folder_path} is not a valid directory.")
        return []

    video_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    data = []

    for video_file in video_files:
        video_path = os.path.join(folder_path, video_file)
        print(f"Processing file: {video_path}")
        duration = get_video_duration(video_path)
        if duration is not None:
            duration_hhmmss = seconds_to_hhmmss(duration)
            data.append({"VideoName": video_file, "Duration (hh:mm:ss)": duration_hhmmss})
    
    return data

def save_to_csv(data, folder_path):
    """Save video data to a CSV file named after the folder."""
    folder_name = os.path.basename(folder_path)
    csv_file_path = os.path.join(folder_path, f"{folder_name}.csv")
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)
    print(f"CSV file saved at: {csv_file_path}")

def main():
    folder_path = input("Enter the path to the folder with videos: ").strip()
    folder_path = folder_path.strip('"')  # Remove any extraneous quotes

    # Debugging line to ensure the path is correct
    print(f"Checking path: {folder_path}")

    if not os.path.isdir(folder_path):
        print("The specified path is not a directory or does not exist.")
        return
    
    data = scan_videos_in_folder(folder_path)
    if data:
        save_to_csv(data, folder_path)
    else:
        print("No video files found in the specified folder.")

if __name__ == "__main__":
    main()
