import os
import shutil
import datetime

print("Taking Backup")

# Source and backup directory paths
source_dir = r"C:\Users\tejas\OneDrive\Desktop\My Documents\bin"
backup_parent_dir = r"C:\Users\tejas\OneDrive\Desktop\My Documents\backup"  # Changed from ssh to backup
backup_dir = os.path.join(backup_parent_dir, f"BACKUP_{datetime.datetime.now().strftime('%d%m%Y')}")

# Create the backup directory if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Copy the entire source directory to the backup directory
shutil.copytree(source_dir, os.path.join(backup_dir, os.path.basename(source_dir)))

print("Backup completed on", backup_dir)

# Ask for patch number input
patch_number = input("Enter the patch number: ")
patch_dir = fr"C:\Users\tejas\OneDrive\Desktop\My Documents\patch\PATCH_{patch_number}"

print("Patch Number:", patch_number)
print("Patch Directory:", patch_dir)

# Deployment of patch
for root, dirs, files in os.walk(patch_dir):
    for file_name in files:
        source_file = os.path.join(root, file_name)
        relative_path = os.path.relpath(source_file, patch_dir)
        destination_file = os.path.join(source_dir, relative_path)
        os.makedirs(os.path.dirname(destination_file), exist_ok=True)
        shutil.copy2(source_file, destination_file)

print("Patch Deployment completed")
