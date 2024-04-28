import os
import shutil
import datetime

print("Taking Backup")

source_dir = r"C:\Users\tejas\OneDrive\Desktop\My Documents\bin"
backup_dir = fr"C:\Users\tejas\OneDrive\Desktop\My Documents\backup\BACKUP_{datetime.datetime.now().strftime('%d%m%Y')}"

bshutil.copytree(source_dir, backup_dir)

print("Backup completed on", backup_dir)

# Ask for patch number input
patch_number = input("Enter the patch number: ")
patch_dir = fr"C:\Users\tejas\OneDrive\Desktop\My Documents\patch\PATCH_{patch_number}"

print("Patch Number:", patch_number)
print("Patch Directory:", patch_dir)

for root, dirs, files in os.walk(patch_dir):
    for file_name in files:
        source_file = os.path.join(root, file_name)
        relative_path = os.path.relpath(source_file, patch_dir)
        destination_file = os.path.join(source_dir, relative_path)
        os.makedirs(os.path.dirname(destination_file), exist_ok=True)
        shutil.copy2(source_file, destination_file)

print("Patch Deployment completed")
