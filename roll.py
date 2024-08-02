import os
import sys
from pathlib import Path

tab = 1
tab_cun = 1
import_obj = ""


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
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        #print(f"File content: {content}")
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def main(file_path):
    global import_obj
    global tab
    global tab_cun
    if "/" in file_path:
        filename = file_path.split('/')[-1]  # 去除路径，只保留文件名和扩展名
        file_without_extension = filename.split('.')[0]  # 去除扩展名，只保留文件名
    else:
        filename_with_extension = 'file.roll'
        # 直接使用文件名和扩展名
        file_without_extension = filename_with_extension.split('.')[0]

    run = open(f"{file_without_extension}.java", 'w+', encoding='utf-8')
    run.write(f"public class {file_without_extension}" + "{\n")
    run.close()
    run = open(f"{file_without_extension}.java", 'a', encoding='utf-8')

    # 打开文件，使用'utf-8'编码以支持中文
    with open(file_path, 'r', encoding='utf-8') as file:
        # 逐行读取文件
        for line in file:
            # 去除行尾的换行符并检查是否为空白行
            line = line.strip()
            if line:  # 如果行不为空
                # 打印每一行，这里可以进行其他操作，比如处理每一行的数据
                # print(line.rstrip('\n'))  由于已经用strip()去除了空白，不需要end=''
                x = line.split(" ")
                if x[0] == "import":
                    import_file = x[1] + ".java"
                    import_obj += x[1]
                    while tab >= 1:
                        run.write("    ")
                        tab -= 1
                    tab = tab_cun
                    run.write(f"{read_file_from_appdata("./ROLL/" + import_file)}\n\n")
                elif x[0] == "main()":
                    while tab >= 1:
                        run.write("    ")
                        tab -= 1
                    tab = tab_cun
                    run.write("public static void main(String[] args)\n")
                elif x[0] == "main":
                    if x[1] == "{":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write("public static void main(String[] args)\n")
                elif x[0] == "{":

                    while tab >= 1:
                        run.write("    ")
                        tab -= 1
                    tab = tab_cun
                    tab += 1
                    tab_cun += 1
                    run.write("{\n")
                elif x[0] == "}":
                    tab -= 1
                    tab -= 1
                    while tab >= 1:
                        run.write("    ")
                        tab -= 1
                    tab = tab_cun

                    run.write("}\n")
                else:
                    if x[0].split(".")[0] in import_obj:
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(line + ";\n")
    run.write("}\n")
    run.close()
    os.system(f"javac {file_without_extension}.java")
    os.system(f"java {file_without_extension}")
    os.remove(f"{file_without_extension}.java")


# 示例使用
"""
create_folder_in_appdata('MyNewFolder')
create_file_in_appdata('MyNewFile.txt', 'Hello, this is a test file.')
content = read_file_from_appdata('MyNewFile.txt')
"""

if __name__ == "__main__":
    zl_all = sys.argv[1:]
    if zl_all[0] == "run":
        # 获取文件的后缀
        file_suffix = zl_all[1].split(".")[-1]
        # 判断后缀是否合法
        if file_suffix.replace(" ", "") != "roll":
            print("ERR：你的文件名不合法!")
            exit()
        main(zl_all[1])
