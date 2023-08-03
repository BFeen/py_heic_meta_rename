# 1. Instruments:
- Python 3.*
- Wand pip
- ImageMagick install
- pathlib for path and rename

# 2. Useful info.
it shows all metadata if you want to set code for another file format
JPG contain another kind of DateTime - exif:DateTime

// py
with Image(filename="filename") as file:
	for metadata in file.metadata:
		print(metadata)
//
