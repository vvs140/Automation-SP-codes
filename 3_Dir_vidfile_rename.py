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
    
    ]



    new_names = [
    "Telugu bhasha - Saahityam - Vyaktitva vikasam.mp4",
    "Telugu bhasha - Sambhashana naipunyaanlu.mp4",
    
    ]





    # Create a mapping of old names to new names
    try:
        name_mapping = create_name_mapping(old_names, new_names)
    except ValueError as e:
        print(e)
        exit(1)
    
    rename_files(directory, name_mapping)
