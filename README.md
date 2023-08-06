# 1. Instruments:
- Python 3.*
- Wand pip
- ImageMagick install
- pathlib for path and rename

# 2. Useful info.
it shows all metadata if you want to set code for another file format

with Image(filename="filename") as file:
	for metadata in file.metadata:
		print(metadata)

#3. Usage.
After installing all instruments from 1., put your images inside the folder with name 'img' 
near the main.py and start the program. 
