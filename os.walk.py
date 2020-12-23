import os
for dirpath, dirname, files in os.walk('..'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)
