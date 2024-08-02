import os
import shutil
import sys
from pathlib import Path

def create_folder_in_appdata(folder_name):
    """
    在AppData中创建文件夹
    :param folder_name: 文件夹相对路径
    :return:null
    """
    # 获取AppData目录路径
    appdata_path = Path.home() / 'AppData' / 'Local'
    # 创建文件夹路径
    folder_path = appdata_path / folder_name
    # 如果文件夹不存在，则创建
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"Folder created at: {folder_path}")


def create_file_in_appdata(file_name, content=''):
    """
    在AppData中创建文件
    :param file_name: 文件的相对路径
    :param content: 初始化内容
    :return: null
    """
    # 获取AppData目录路径
    appdata_path = Path.home() / 'AppData' / 'Local'
    # 创建文件路径
    file_path = appdata_path / file_name
    # 写入内容到文件
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File created at: {file_path}")


def read_file_from_appdata(file_name):
    """
    读取AppData中的文件内容
    :param file_name: 文件相对路径
    :return: null
    """
    # 获取AppData目录路径
    appdata_path = Path.home() / 'AppData' / 'Local'
    # 构建文件路径
    file_path = appdata_path / file_name
    try:
        # 读取文件内容
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"File content: {content}")
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


if __name__ == "__main__":
    # 创建文件夹
    create_folder_in_appdata("ROLL")
    folder_path = './roll/java/'
    # 复制文件
    shutil.copy("./roll/java/io.java", Path.home() / 'AppData' / 'Local' / 'ROLL')
