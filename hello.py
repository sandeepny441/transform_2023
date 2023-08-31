import os
import pandas as pd 

# Replace with the path to your master folder
master_folder_path =r'C:\Users\Administrator.DESKTOP-QSF3VEN\Documents\everythin_new\\voyager\SolidSan\code_station\Transform_2023'

for folder_name in os.listdir(master_folder_path):
    folder_path = os.path.join(master_folder_path, folder_name)

    # Check if it's a folder
    if os.path.isdir(folder_path):
        file_path = os.path.join(folder_path, 'hello.py')

        # Create and immediately close the file
        open(file_path, 'w').close()


#match 
import re
print(re.match('a', 'abc'))  # Matches
print(re.match('a', 'bac'))  # Does not match


# findall
import re
print(re.findall('a', 'abcabc'))  # Returns ['a', 'a']


def sales_person(sales_person: pd.DataFrame, 
                company: pd.DataFrame, 
                orders: pd.DataFrame) -> pd.DataFrame:
  c_id=company[company['name']=='RED']
  print(c_id)
  s_id=orders[orders['com_id'].isin(c_id['com_id'])]
  print(s_id)
  res=sales_person[~sales_person['sales_id'].isin(s_id['sales_id'])]
  return res[['name']]






