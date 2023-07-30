from pathlib import Path
from wand.image import Image

path = Path(__file__).parent

# PATH + WAND
names = []
length = len(list(enumerate(path.glob('*.heic'))))

for i, path in enumerate(path.glob('*.heic')):
    create_date = ''

    with Image(filename=path.name) as file:
        create_date = file.metadata["exif:DateTime"]
        create_date = create_date.replace(":", ".")

    #составление нового имени файла
    new_name = create_date + path.suffix
    #проверка на уникальность имени файла
    if new_name in names:
        new_name = create_date + '_1' + path.suffix
    
    names.append(new_name)
    
    # полезная информация
    length -= 1
    print(f'{new_name} - done, осталось переименовать: {length} файлов')
    # path.rename(new_name)