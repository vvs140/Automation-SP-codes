import os

def rename_files_to_uppercase(directory):
    """Rename all files in the specified directory to uppercase."""
    for filename in os.listdir(directory):
        old_file_path = os.path.join(directory, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(old_file_path):
            # Convert the filename to uppercase
            new_filename = filename.upper()
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    # Define the directory containing the files
    directory = r"C:\Users\Abc\Downloads\Advanced Textile Printing Technology"  # Replace with your folder path
    
    # Rename files
    rename_files_to_uppercase(directory)
