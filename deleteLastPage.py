import os
import zipfile
import rarfile
import tempfile

def delete_last_page(file_name):
    """
    Deletes the last page from a .cbr or .cbz file.
    
    Args:
        file_name (str): The name of the .cbr or .cbz file.
    
    Raises:
        ValueError: If the file extension is not .cbr or .cbz.
        FileNotFoundError: If the file does not exist.
    """
    # Get the file path in a cross-platform way
    file_path = os.path.abspath(file_name)
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Determine file type by extension
    file_extension = os.path.splitext(file_name)[1].lower()

    if file_extension == '.cbz':
        # Handle .cbz (ZIP) file
        with zipfile.ZipFile(file_path, 'r') as cbz_file:
            # Get the list of files in the archive, sorted naturally
            file_list = sorted(cbz_file.namelist())
            
            # Check if archive is empty
            if not file_list:
                raise ValueError("Archive is empty")
            
            # Exclude the last file
            file_list = file_list[:-1]

            # Create a new .cbz file without the last page
            new_cbz_path = os.path.splitext(file_path)[0] + '_modified.cbz'
            with zipfile.ZipFile(new_cbz_path, 'w') as new_cbz_file:
                for file in file_list:
                    new_cbz_file.writestr(file, cbz_file.read(file))

    elif file_extension == '.cbr':
        # Handle .cbr (RAR) file by converting to ZIP
        with rarfile.RarFile(file_path, 'r') as cbr_file:
            # Get the list of files in the archive, sorted naturally
            file_list = sorted(cbr_file.namelist())
            
            # Check if archive is empty
            if not file_list:
                raise ValueError("Archive is empty")
            
            # Exclude the last file
            file_list = file_list[:-1]
            
            with tempfile.TemporaryDirectory() as temp_dir:
                # Create a new ZIP file (converting CBR to CBZ)
                new_cbz_path = os.path.splitext(file_path)[0] + '_modified.cbz'
                with zipfile.ZipFile(new_cbz_path, 'w') as new_cbz_file:
                    for file in file_list:
                        # Extract individual file and add to new archive
                        cbr_file.extract(file, temp_dir)
                        file_path_in_temp = os.path.join(temp_dir, file)
                        new_cbz_file.write(file_path_in_temp, arcname=file)
    else:
        raise ValueError("Unsupported file format. Please provide a .cbz or .cbr file.")

def main():
    """Main function for command-line usage."""
    file_name = input("Enter the .cbr or .cbz file name: ")
    try:
        delete_last_page(file_name)
        print(f"Successfully created modified file: {os.path.splitext(file_name)[0]}_modified.cbz")
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
