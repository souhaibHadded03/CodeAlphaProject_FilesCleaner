import os

def clean_disk(directory):
    
    remove_temporary_files(directory)

    
    remove_empty_directories(directory)

def remove_temporary_files(directory):
    print("Removing temporary files...")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.tmp') or file.endswith('.temp'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted temporary file: {file_path}")

def remove_empty_directories(directory):
    print("Removing empty directories...")
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Deleted empty directory: {dir_path}")


directory_to_clean = input("Enter the directory path to clean: ")


if os.path.exists(directory_to_clean):
    clean_disk(directory_to_clean)
    print("Disk cleanup completed successfully.")
else:
    print("The specified directory does not exist.")
