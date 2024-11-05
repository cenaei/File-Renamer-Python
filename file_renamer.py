import os

# Specify the directory containing your files
directory = "/path/to/your/files"  # Replace with the path to your folder

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename starts with "[SPOTDOWNLOADER.COM] "
    if filename.startswith("[SPOTDOWNLOADER.COM] "):
        # Create the new filename by removing the prefix
        new_filename = filename.replace("[SPOTDOWNLOADER.COM] ", "", 1)
        
        # Get the full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: "{filename}" to "{new_filename}"')