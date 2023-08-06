from pathlib import Path
from wand.image import Image

source_folder = Path('img/')

# PATH + WAND
names = []
length = len(list(enumerate(source_folder.glob('*.*'))))

for i, path in enumerate(source_folder.glob('*.*')):
    create_date = ''
# Extracting metadata with creation date from file
    with Image(filename=path) as file:
        try:    
            create_date = file.metadata["exif:DateTime"]
            create_date = create_date.replace(":", ".")
        except Exception:
            print(f'Файл {path} не имеет сведений о дате создания')
            continue
# Creating new file name
    new_name = "img/" + create_date + path.suffix
    print(new_name)
# Check for unique file name
    if new_name in names:
        new_name = create_date + '_1' + path.suffix
    
    names.append(new_name)
    
# Additional info
    length -= 1
    print(f'{new_name} - done, осталось переименовать: {length} файлов')
    path.rename(new_name)
