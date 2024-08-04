import os
import sys
from pathlib import Path

tab = 1
tab_cun = 1
import_obj = ""
val_name = ""
lines = 1


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
    global lines
    global import_obj
    global tab
    global tab_cun
    """if "/" in file_path:
        filename = file_path.split('/')[-1]  # 去除路径，只保留文件名和扩展名
        file_without_extension = filename.split('.')[0]  # 去除扩展名，只保留文件名
    else:
        filename_with_extension = 'file.roll'
        # 直接使用文件名和扩展名
        file_without_extension = filename_with_extension.split('.')[0]
    """
    # 使用os.path.basename获取文件名和后缀
    file_name_with_extension = os.path.basename(file_path)

    # 使用os.path.splitext分割文件名和后缀
    file_name, file_extension = os.path.splitext(file_name_with_extension)

    # file_name现在就是不包含后缀的文件名
    # file_extension是文件的后缀，包括点（.）

    # 使用os.path.dirname获取文件所在目录
    directory = os.path.dirname(file_path)

    """print("不包含后缀的文件名:", file_name)
    print("后缀:", file_extension)
    """

    run = open(f"{file_name}.java", 'w+', encoding='utf-8')
    run.write(f"public class {file_name}" + "{\n")
    run.close()
    run = open(f"{file_name}.java", 'a', encoding='utf-8')

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
                elif x[0] == "var": # var name str give "Hello"
                    var_name = x[1]
                    test = "".join(x[4::])
                    if x[2] == "str":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"String {var_name} = {test};\n")
                    elif x[2] == "int":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"int {var_name} = {test};\n")
                    elif x[2] == "boo":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"boolean {var_name} = {test};\n")
                    elif x[2] == "dou":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"double {var_name} = {test};\n")
                    else:
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"{x[2]} {var_name} = {test}")
                elif x[0] == "val": # val name str give "Hello"
                    var_name = x[1]
                    test = "".join(x[4::])
                    if x[2] == "str":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"final String {var_name} = {test};\n")
                    elif x[2] == "int":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"final int {var_name} = {test};\n")
                    elif x[2] == "boo":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"final boolean {var_name} = {test};\n")
                    elif x[2] == "dou":
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"final double {var_name} = {test};\n")
                    else:
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(f"final {x[2]} {var_name} = {test}")
                else:
                    if x[0].split(".")[0] in import_obj:
                        while tab >= 1:
                            run.write("    ")
                            tab -= 1
                        tab = tab_cun
                        run.write(line + ";\n")
                        continue
                    else:
                        print(f"ERR({lines}):没有导入的模块")
        lines += 1
    run.write("}\n")
    run.close()
    os.system(f"javac {file_name}.java")
    os.system(f"java {file_name}")
    # os.system(f"javap -c {file_name}")
    os.remove(f"{file_name}.java")


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
