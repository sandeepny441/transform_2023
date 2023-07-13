import os 

for file in os.listdir():
  print(file)
  if file[-2:] == 'py':
    print(100)
    this_file = file[:-2] + 'ipynb'
    with open(this_file, 'w') as f:
      f.write('import os')
