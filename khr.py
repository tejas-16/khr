import os
import shutil
import datetime

# Preparation

# Declared Variables
print("Taking Backup")

source_dir = r"C:\Users\tejas\OneDrive\Desktop\My Documents\bin"
backup_dir = fr"C:\Users\tejas\OneDrive\Desktop\My Documents\ssh\BACKUP_{datetime.datetime.now().strftime('%d%m%Y')}"

# Creating today's date Directory and taking the entire source directory as backup
shutil.copytree(source_dir, backup_dir)

print("Backup completed on", backup_dir)

# Finding the latest patch directory
patch_base_dir = r"C:\Users\tejas\OneDrive\Desktop\My Documents\patch"
latest_patch = max(os.listdir(patch_base_dir),
                   key=lambda x: os.path.getmtime(os.path.join(patch_base_dir, x)))

patch_dir = os.path.join(patch_base_dir, latest_patch)

# Get patch number from the directory name
cn = latest_patch.split("_")[-1]
print("Patch Number:", cn)
print("Patch Directory:", patch_dir)

# Copying Patch
for root, dirs, files in os.walk(patch_dir):
    for file_name in files:
        source_file = os.path.join(root, file_name)
        relative_path = os.path.relpath(source_file, patch_dir)
        destination_file = os.path.join(source_dir, relative_path)
        os.makedirs(os.path.dirname(destination_file), exist_ok=True)
        shutil.copy2(source_file, destination_file)

print("Patch Deployment completed")
