import os
import shutil

# Define the target folder
target_folder = 'Data'
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Get all .csv files in the current directory
for file in os.listdir():
    if file.endswith('.csv'):
        shutil.move(file, os.path.join(target_folder, file))


