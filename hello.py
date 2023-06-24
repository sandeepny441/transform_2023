import os

# Replace with the path to your master folder
master_folder_path =r'C:\Users\Administrator.DESKTOP-QSF3VEN\Documents\everythin_new\\voyager\SolidSan\code_station\Transform_2023'

for folder_name in os.listdir(master_folder_path):
    folder_path = os.path.join(master_folder_path, folder_name)

    # Check if it's a folder
    if os.path.isdir(folder_path):
        file_path = os.path.join(folder_path, 'hello.py')

        # Create and immediately close the file
        open(file_path, 'w').close()
