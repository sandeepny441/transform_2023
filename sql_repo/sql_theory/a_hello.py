import os

folder_path = r'C:\Users\Administrator.DESKTOP-QSF3VEN\Documents\everythin_new\voyager\SolidSan\code_station\transform_2023\sql_repo\sql_theory'

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        new_filename = 'a_' + filename
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
