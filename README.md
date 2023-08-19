# helputils

So, I am lazy, I don't like to do the same operation manually over and over again.
I decided to "automate" some boring routines using `Python` & || `Bash Script.` 

My philosophy is very simple:
- start with something simple that works
- update as the needs come

## folder_organize.py
Keeps your messy folder in a more organized state. You have to specify a destination folder starting from `~/`
The script will check the folder and move all the files to the respective folders inside the provided path

```
"Documents": "pdf pptx docx",
"Music": "mp3",
"Pictures": "jpg png gif"
```

**Usage**
```commandline
python3 folder_organize.py folder
```
**Example**
```commandline
python3 folder_organize.py Downloads
```
