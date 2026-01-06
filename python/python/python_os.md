# os

os: operating system(操作系统)os 模块是 Python 标准库中的一个重要模块，它提供了与操作系统交互的功能。通过 os 模块，你可以执行文件操作、目录操作、环境变量管理、进程管理等任务。os 模块是跨平台的，这意味着你可以在不同的操作系统（如 Windows、Linux、macOS）上使用相同的代码。

## 常用的os操作

1. 获取当前工作目录 os.getcwd()
2. 改变当前工作目录 os.chdir()
3. 列出目录内容 os.listdir(),会列出当前目录下的所有文件和子目录
4. 创建目录 os.mkdir()
5. 删除目录 os.rmdir()
6. 删除文件 os.remov("file.txt")
7. 文件或目录重命名 os.rename("old","new")
8. 获取环境变量 os.getenv(key)
9. 执行系统命令 os.system(command)