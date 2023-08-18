import shutil
import sys
from os import listdir, getcwd, path, mkdir
from getpass import getuser
from os.path import isfile, join

FILES_STRUCTURE = {
    ["pdf, pptx"] : "Documents"
}


def get_files(file_ext, folder_path):
    return [f for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.endswith(file_ext)]

def is_folder_created(folder_name: str) -> str:
    if not path.isdir(folder_name):
        mkdir(folder_name)
    return folder_name

def build_general_path() -> str:
    platform = sys.platform

    if platform == "linux" or platform == "linux2":
        return f"/usr/{getuser()}"
    elif platform == "darwin":
        return f"/Users/{getuser()}"
    elif platform == "win32":
        pass
        # Windows...


def move_files_to_folder(file_to_move, destination_folder):
    shutil.move(file_to_move, is_folder_created(destination_folder))


if __name__ == '__main__':
    userPath = f'{build_general_path()}/Downloads'
    for file_ext, folder in FILES_STRUCTURE.items():
        files = get_files(file_ext, userPath)
        if files:
            for file in files:
                file_path = f'{userPath}/{file}'
                des_folder = f'{userPath}/{folder}'
                print(file_path, des_folder)
                move_files_to_folder(f'{userPath}/{file}', f'{userPath}/{folder}')
