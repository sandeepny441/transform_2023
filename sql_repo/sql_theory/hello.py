import os

directory =r'C:\Users\Administrator.DESKTOP-QSF3VEN\Documents\everythin_new\voyager\transform_2023\sql_repo\sql_theory'  # Specify the directory containing the files

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):  # Check if it's a file
        new_filename = os.path.join(directory,  filename[2:])  # Add "00" in front of the original filename
        os.rename(os.path.join(directory, filename), new_filename)  # Rename the file

print("Files renamed successfully.")
