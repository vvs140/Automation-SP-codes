import gdown
import os

# List of Google Drive file links
links = [
    "https://drive.google.com/file/d/1zG8B6FJujeDrjwuWfkWwRuV0GN3bGIo1/view?usp=drive_link",
    "https://drive.google.com/file/d/1alCKQs9nl4zzbURmKtERcBSoxY3Xlpr1/view?usp=drive_link",
    "https://drive.google.com/file/d/1Jo96KuYIwATEH9XDKQnG4c_fjv9mktyH/view?usp=drive_link",
    "https://drive.google.com/file/d/1C-uGVHmUe2vXwIkUrXE-FlJJ6UMT8lvg/view?usp=drive_link",
    "https://drive.google.com/file/d/1d7Uu0dQ76K-BumCK0GKxeSJhTLL82_xT/view?usp=drive_link",
    "https://drive.google.com/file/d/17GfFF6fYSaeuwLMTm_6j8ZnqM7MNy_lt/view?usp=drive_link",
    "https://drive.google.com/file/d/1zUowvRJI-kr5t_UxMV57d6pFZoSiwSU2/view?usp=drive_link",
    "https://drive.google.com/file/d/1ah0LW8APLBv3g6zuSLFz1l41CP76Mwu_/view?usp=drive_link",
    "https://drive.google.com/file/d/1BnGqGJadnN3n-zfuIY-zUbILDBiv_na8/view?usp=drive_link",
    "https://drive.google.com/file/d/1sbNaHdXPUHZB9Fof_uafDrGAD_Qvpnq_/view?usp=drive_link",
    "https://drive.google.com/file/d/186YUkwDiyWffxIbs6JGbS9W6x6S3jEo-/view?usp=drive_link",
    "https://drive.google.com/file/d/16vis8YIvh8lRDmPdvmcqVdCBeMJcyMB4/view?usp=drive_link",
    "https://drive.google.com/file/d/1R8PoOw12kPkaNdrvzIDHq9WtK1hGJCrV/view?usp=drive_link",
    "https://drive.google.com/file/d/1oJCzMOF2rxuPWyl6tj8lTH4ngM9MICq6/view?usp=drive_link",
    "https://drive.google.com/file/d/1suBy6qJSxfdwPoRK3OcswBYcLvcLXcjd/view?usp=drive_link",
    "https://drive.google.com/file/d/1m0vT1UyK6lUgAASRJrly0jsLmSR5S75H/view?usp=drive_link",
    "https://drive.google.com/file/d/1xycfQ41hFJX2-cuMrywMq0y7G1udHYk5/view?usp=drive_link",
    "https://drive.google.com/file/d/1o5LWWguNyhosiXY3J8h-AFYJUtO1AcKw/view?usp=drive_link",
    "https://drive.google.com/file/d/1tyc1-HDzZAAa4a0xmZSrs_2v8xPr0IKF/view?usp=drive_link",
    "https://drive.google.com/file/d/1tG20K7IftEcoepcHJzJJFA78_joWgb31/view?usp=drive_link",
    "https://drive.google.com/file/d/1rJJgrH2haxrknsMnS3iF_pILnaQs0g9J/view?usp=drive_link",
    "https://drive.google.com/file/d/13zm7UxMR59YOAjUApCWRBfxdRUyXn0-6/view?usp=drive_link",
    "https://drive.google.com/file/d/18ficBazHHo8Yojz8cJzN5fS9fiijg5ym/view?usp=drive_link",
    "https://drive.google.com/file/d/1vA5ynT_VoQlKATtyPaeEH86_Bt3P5Mub/view?usp=drive_link"
]


# Directory to save the downloaded videos
download_folder = r'D:/'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

def extract_file_id(link):
    """Extracts the file ID from a Google Drive sharing link"""
    return link.split('/d/')[1].split('/')[0]

def download_video(file_id):
    """Downloads the video from Google Drive using the file ID"""
    output_path = os.path.join(download_folder, f"{file_id}.mp4")
    
    # Check if file already exists
    if os.path.exists(output_path):
        print(f"File {output_path} already exists. Skipping download.")
        return
    download_url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading: {output_path}")
    gdown.download(download_url, output_path, quiet=False)

# Download all files
for link in links:
    file_id = extract_file_id(link)
    download_video(file_id)

print("Download complete!")
