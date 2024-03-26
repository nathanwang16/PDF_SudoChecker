import os
import shutil

def duplicate_and_delete_pdf(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.pdf'):
                original_path = os.path.join(root, file)
                duplicate_path = os.path.join(root, "temp_" + file)
                shutil.copy2(original_path, duplicate_path)  # Create a temporary duplicate
                os.remove(original_path)  # Delete the original PDF
                os.rename(duplicate_path, original_path)  # Rename the duplicate to the original file's name

if __name__ == "__main__":
    root_folder = '/Users/wangxiaoyu/Desktop/MIT-open'  # Current directory
    duplicate_and_delete_pdf(root_folder)

