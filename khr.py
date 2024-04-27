import os
from datetime import datetime
import shutil

# Preparation

# Declared Variables
print("Taking Backup")

today_date = datetime.now().strftime("%d%m%Y")
source_dir = "C:\Users\tejas\OneDrive\Desktop\My Documents\bin"
backup_dir = f"C:\Users\tejas\OneDrive\Desktop\My Documents\ssh\BACKUP_{today_date}"

# Creating today's date Directory and taking current KHR Bin file's backup
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

for file_name in os.listdir(source_dir):
    source_file = os.path.join(source_dir, file_name)
    backup_file = os.path.join(backup_dir, file_name)
    shutil.copy2(source_file, backup_file)

print("Backup completed on", backup_dir)

# Entering patch details from the user and reading the entered details
# finding patch details and path

print("Enter Patch Details *****")

cn = input("Enter patch number: ")
patch_dir = f"C:\Users\tejas\OneDrive\Desktop\My Documents\patch\KIAS2000_PR_{cn}"

print(cn)
print(patch_dir)

input("Verify the Patch details. Press [Enter] key to continue...")

# Copying Patch
patch_files = os.listdir(os.path.join(patch_dir, "bin"))
for file_name in patch_files:
    source_file = os.path.join(patch_dir, "bin", file_name)
    destination_file = os.path.join(source_dir, file_name)
    shutil.copy2(source_file, destination_file)

print("Patch Deployment completed")
