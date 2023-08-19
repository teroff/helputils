import shutil
import sys
from os import listdir, path, mkdir
from getpass import getuser
from os.path import isfile, join

FILES_STRUCTURE = {
    "Documents": "pdf pptx docx",
    "Music": "mp3",
    "Pictures": "jpg png gif"
}


def get_files(file_ext, folder_path):
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.endswith(file_ext)]


def create_folder(folder_name: str):
    mkdir(folder_name)


def is_folder(folder_name: str) -> bool:
    return path.isdir(folder_name)


def build_user_path() -> str:
    platform = sys.platform

    if platform == "linux" or platform == "linux2":
        return f"/usr/{getuser()}"
    elif platform == "darwin":
        return f"/Users/{getuser()}"
    elif platform == "win32":
        pass
        # Windows...


if __name__ == '__main__':
    try:
        userPath = f'{build_user_path()}/{sys.argv[1]}'

        for folder, extensions in FILES_STRUCTURE.items():
            folder = f'{userPath}/{folder}'
            extensions = extensions.split(" ")
            for extension in extensions:
                files = get_files(extension, userPath)
                if files:
                    if not is_folder(folder): create_folder(folder)
                    [shutil.move(f'{userPath}/{file}', folder) for file in files]

    except IndexError:
        print("You need to specify the folder where you want to file organization to happen")
        print(f"Usage: python3 {sys.argv[0]} folder")
        print(f"Example: python3 {sys.argv[0]} Download")
