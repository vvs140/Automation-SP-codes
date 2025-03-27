import os

def get_video_files(directory):
    """Return a list of video files in the specified directory."""
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')  # Add more extensions if needed
    return [f for f in os.listdir(directory) if f.lower().endswith(video_extensions)]

def create_name_mapping(old_names, new_names):
    """Create a mapping of old names to new names."""
    if len(new_names) != len(old_names):
        raise ValueError("The number of new names must match the number of old names.")
    
    return dict(zip(old_names, new_names))

def print_mapping(mapping):
    """Print the old-to-new name mapping."""
    print("Old Name -> New Name")
    for old_name, new_name in mapping.items():
        print(f"{old_name} -> {new_name}")

def rename_files(directory, name_mapping):
    """Rename files based on the provided mapping."""
    video_files = get_video_files(directory)
    print("Detected files in directory:")
    for file in video_files:
        print(file)
    
    # Create a dictionary of existing files with their new names
    existing_files = {file_name: name_mapping[file_name] for file_name in video_files if file_name in name_mapping}
    
    # Print the mapping
    print_mapping(existing_files)

    # Ask for permission to proceed
    proceed = input("Do you want to proceed with renaming these files? (yes/no): ").strip().lower()
    
    if proceed != 'yes':
        print("Operation canceled.")
        return

    for old_name, new_name in existing_files.items():
        old_file_path = os.path.join(directory, old_name)
        new_file_path = os.path.join(directory, new_name)

        # Check if the new file name already exists
        if not os.path.exists(new_file_path):
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_name} -> {new_name}')
        else:
            print(f'Error: New file name {new_name} already exists.')

if __name__ == "__main__":
    # Define the directory containing the video files
    directory = r'F:\Pracheena Telugu Kavithvam - Kavya Sudha book - 2nd Language Telugu'

    # Define the old and new names for the video files
    old_names = [
    "1FxPE4drrevYUgOPgtEwMb0i7DLqQhXUu.mp4",
    "1xaDWeENOgAEvmCHVK5y8qu9Os4vVaxDz.mp4",
    "1ioQ_uDNstisLPlM1rlD3oV347N-pJPo_.mp4",
    "1VAvh8Yvq4uVJPZKVhEvt6gP1w0kAL5mR.mp4",
    "1GHp5BWz3bGvtgmxlEd5g6SokXSDmHE-t.mp4",
    "1dYHePe6yTfDtEjgL9j6xuuGSml4oYW6H.mp4",
    "1WJQmLqRL-BlldHoCppg0vD_yV41-mc2J.mp4",
    "1Q1SggTZPC4NkMjiR4NdpMW0lBGRNSvRx.mp4",
    "11nYx4_LJ_A--PHCrjLKJPAD5igizsxxi.mp4",
    "1ECL6efT6-NxfSmGlcrHq51qalu7H9qmO.mp4",
    "1XXIx3zXmkgDX_VG_6LVM7B3FAfHtltfx.mp4",
    "1Qp6W0Vwn1K_YIDQTJU8Dqeg7dhb3m_zT.mp4",
    "1zMs6z1qDxWSBSXivAoTq_j3xeiu3vdB3.mp4",
    "1Fk2S4MEAbXgvpm0cVJKlyBwePnjDUt_0.mp4",
    "1VMnsm7tgcev9MGOgOtQbCdIGwW3zX_lt.mp4",
    "1f423_4bJtbYYEHzcJXAVmsF4hd-Fgy62.mp4",
    "1MQuYcWrdkiqPQW7_r2fxxS2-9uyI502V.mp4",
    "1VZeQH0j22RTs6uHz_gIk4L3ZAwP3NWKc.mp4",
    "1I1zS3ff4DdOytE4e3Z6qWITQek2hPJyP.mp4",
    "1rKpRYCo2sywDu4CLjItNKsTz6oab749m.mp4",
    "1zG8B6FJujeDrjwuWfkWwRuV0GN3bGIo1.mp4",
    "1alCKQs9nl4zzbURmKtERcBSoxY3Xlpr1.mp4",
    "1nwChSLFkvyUoWVhTk9s-hw1NNbeJGAAP.mp4",
    "1Jo96KuYIwATEH9XDKQnG4c_fjv9mktyH.mp4",
    "1C-uGVHmUe2vXwIkUrXE-FlJJ6UMT8lvg.mp4",
    "1d7Uu0dQ76K-BumCK0GKxeSJhTLL82_xT.mp4",
    "17GfFF6fYSaeuwLMTm_6j8ZnqM7MNy_lt.mp4",
    "1zUowvRJI-kr5t_UxMV57d6pFZoSiwSU2.mp4",
    "1ah0LW8APLBv3g6zuSLFz1l41CP76Mwu_.mp4",
    "1BnGqGJadnN3n-zfuIY-zUbILDBiv_na8.mp4",
    "1sbNaHdXPUHZB9Fof_uafDrGAD_Qvpnq_.mp4",
    "186YUkwDiyWffxIbs6JGbS9W6x6S3jEo-.mp4",
    "16vis8YIvh8lRDmPdvmcqVdCBeMJcyMB4.mp4",
    "1R8PoOw12kPkaNdrvzIDHq9WtK1hGJCrV.mp4",
    "1oJCzMOF2rxuPWyl6tj8lTH4ngM9MICq6.mp4",
    "1suBy6qJSxfdwPoRK3OcswBYcLvcLXcjd.mp4",
    "1m0vT1UyK6lUgAASRJrly0jsLmSR5S75H.mp4",
    "1xycfQ41hFJX2-cuMrywMq0y7G1udHYk5.mp4",
    "1o5LWWguNyhosiXY3J8h-AFYJUtO1AcKw.mp4",
    "1tyc1-HDzZAAa4a0xmZSrs_2v8xPr0IKF.mp4",
    "1tG20K7IftEcoepcHJzJJFA78_joWgb31.mp4",
    "1rJJgrH2haxrknsMnS3iF_pILnaQs0g9J.mp4",
    "13zm7UxMR59YOAjUApCWRBfxdRUyXn0-6.mp4",
    "18ficBazHHo8Yojz8cJzN5fS9fiijg5ym.mp4",
    "1vA5ynT_VoQlKATtyPaeEH86_Bt3P5Mub.mp4"
    ]



    new_names = [
    "Telugu bhasha - Saahityam - Vyaktitva vikasam.mp4",
    "Telugu bhasha - Sambhashana naipunyaanlu.mp4",
    "Telugu bhasha - Naayakatva lakshanaalu.mp4",
    "Telugu bhasha - Nirvahanaa saamardhyam.mp4",
    "Raajaneethi Part 1.mp4",
    "Raajaneethi Part 2.mp4",
    "Raajaneethi Part 3.mp4",
    "Raajaneethi Part 4.mp4",
    "Raajaneethi Part 5.mp4",
    "Raajaneethi Part 6.mp4",
    "Dakshayagnam Part 1.mp4",
    "Dakshayagnam Part 2.mp4",
    "Dakshayagnam Part 3.mp4",
    "Dakshayagnam Part 4.mp4",
    "Dakshayagnam Part 5.mp4",
    "Dakshayagnam Part 6.mp4",
    "Dhoumya Dharmopadesam Part 1.mp4",
    "Dhoumya Dharmopadesam Part 2.mp4",
    "Dhoumya Dharmopadesam Part 3.mp4",
    "Dhoumya Dharmopadesam Part 4.mp4",
    "Dhoumya Dharmopadesam Part 5.mp4",
    "Dhoumya Dharmopadesam Part 6.mp4",
    "Dhoumya Dharmopadesam Part 7.mp4",
    "Palanaati Bebbuli Part 1.mp4",
    "Palanaati Bebbuli Part 2.mp4",
    "Palanaati Bebbuli Part 3.mp4",
    "Palanaati Bebbuli Part 4.mp4",
    "Palanaati Bebbuli Part 5.mp4",
    "Sitaraavana Samvaadam Part 1.mp4",
    "Sitaraavana Samvaadam Part 2.mp4",
    "Sitaraavana Samvaadam Part 3.mp4",
    "Sitaraavana Samvaadam Part 4.mp4",
    "Sitaraavana Samvaadam Part 5.mp4",
    "Sitaraavana Samvaadam Part 6.mp4",
    "Sandhulu Part 1.mp4",
    "Sandhulu Part 2.mp4",
    "Sandhulu Part 3.mp4",
    "Sandhulu Part 4.mp4",
    "Sandhulu Part 5.mp4",
    "Sandhulu Part 6.mp4",
    "Sandhulu Part 7.mp4",
    "Sandhulu Part 8.mp4",
    "Sandhulu Part 9.mp4",
    "Samaasamulu Part 1.mp4",
    "Samaasamulu Part 2.mp4"
    ]





    # Create a mapping of old names to new names
    try:
        name_mapping = create_name_mapping(old_names, new_names)
    except ValueError as e:
        print(e)
        exit(1)
    
    rename_files(directory, name_mapping)
