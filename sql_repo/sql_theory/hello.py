import os

folder_path = r'C:\Users\Administrator.DESKTOP-QSF3VEN\Documents\everythin_new\voyager\SolidSan\code_station\transform_2023\sql_repo\sql_theory'

files = os.listdir(folder_path)




for filename in files:
    if filename.startswith("a_"):
        new_filename = "0" + filename[2:]
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))