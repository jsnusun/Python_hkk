#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 8:48
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 操作文件和目录.py

# # 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
#
# # 如果要在Python程序中执行这些目录和文件的操作怎么办？
# # 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，
# # Python内置的os模块也可以直接调用操作系统提供的接口函数。
#
# import os
# print(os.name)  # nt
#
# # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
#
# # 要获取详细的系统信息，可以调用uname()函数：
# # print(os.uname())
# # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
#
# # 环境变量
# # 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
# print(os.environ)
#
# # environ({'COMSPEC': 'C:\\windows\\system32\\cmd.exe',
# # 'VS140COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\',
# # 'HOMEPATH': '\\Users\\huang', 'TEMP': 'C:\\Users\\huang\\AppData\\Local\\Temp',
# # 'PROCESSOR_REVISION': '3a09', 'NUMBER_OF_PROCESSORS': '4',
# # 'JAVA_HOME': 'C:\\develop\\jdk1.8.0_144', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-JR1C9NT',
# #  'VS100COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\Common7\\Tools\\',
# # 'PYTHONIOENCODING': 'UTF-8', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel',
# # 'USERDOMAIN': 'DESKTOP-JR1C9NT', 'CLASSPATH': 'C:\\develop\\jdk1.8.0_144\\lib\\dt.jar;"C:\\develop\\jdk1.8.0_144\\lib\\tools.jar;";',
# # 'USERPROFILE': 'C:\\Users\\huang', 'SESSIONNAME': 'Console', 'MOZ_PLUGIN_PATH': 'E:\\SetupSoftware\\FoxitReader\\Foxit Reader\\plugins\\',
# # 'VSSDK140INSTALL': 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VSSDK\\', 'PYCHARM_HOSTED': '1',
# # 'AWE_DIR': 'C:\\Program Files (x86)\\Khrona LLC\\Awesomium SDK\\1.6.6\\', 'APPDATA': 'C:\\Users\\huang\\AppData\\Roaming',
# # 'SYSTEMDRIVE': 'C:', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'COMPUTERNAME': 'DESKTOP-JR1C9NT',
# # 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'PROGRAMW6432': 'C:\\Program Files', 'TMP': 'C:\\Users\\huang\\AppData\\Local\\Temp',
# #  'PYTHONPATH': 'J:\\Python3\\Mybook', 'PROCESSOR_ARCHITECTURE': 'x86',
# # 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
# # 'VS90COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\Common7\\Tools\\',
# #  'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'PUBLIC': 'C:\\Users\\Public',
# # 'LOGONSERVER': '\\\\DESKTOP-JR1C9NT', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'WINDIR': 'C:\\windows',
# # 'ASL.LOG': 'Destination=file', 'ONEDRIVE': 'F:\\OneDrive', 'SYSTEMROOT': 'C:\\windows', '
# # PATH': 'C:\\develop\\jdk1.8.0_144\\bin;C:\\develop\\jdk1.8.0_144\\jre\\bin;
# # C:\\windows\\system32;C:\\windows;C:\\windows\\System32\\Wbem;C:\\windows\\System32\\WindowsPowerShell\\v1.0\\;
# # c:\\Program Files (x86)\\Microsoft SQL Server\\100\\Tools\\Binn\\;c:\\Program Files\\Microsoft SQL Server\\100\\Tools\\Binn\\;
# # c:\\Program Files\\Microsoft SQL Server\\100\\DTS\\Binn\\;E:\\SetupSoftware\\Git\\cmd;
# # c:\\Program Files (x86)\\Microsoft SQL Server\\90\\Tools\\binn\\;
# # C:\\Program Files (x86)\\Microsoft SQL Server\\100\\Tools\\Binn\\VSShell\\Common7\\IDE\\;
# # C:\\Program Files (x86)\\Microsoft SQL Server\\100\\DTS\\Binn\\;
# # C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\Common7\\IDE\\PrivateAssemblies\\;
# # E:\\SetupSoftware\\MySQL\\MySQL Server 5.5\\bin;
# # C:\\Program Files (x86)\\MySQL\\MySQL Server 5.5\\bin;
# # C:\\windows\\system32\\config\\systemprofile\\.dnx\\bin;C:\\Program Files\\Microsoft DNX\\Dnvm\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\Microsoft SQL Server\\130\\Tools\\Binn\\;C:\\Qt\\4.7.3\\bin;C:\\Users\\huang\\AppData\\Local\\Microsoft\\WindowsApps;', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PYTHONUNBUFFERED': '1', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'LOCALAPPDATA': 'C:\\Users\\huang\\AppData\\Local', 'OS': 'Windows_NT', 'HOMEDRIVE': 'C:', 'PROGRAMDATA': 'C:\\ProgramData', 'PROCESSOR_LEVEL': '6', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'USERNAME': 'huang'})
#
# # 要获取某个环境变量的值，可以调用os.environ.get('key')
# print(os.environ.get('PATH'))
# # C:\develop\jdk1.8.0_144\bin;C:\develop\jdk1.8.0_144\jre\bin;C:\windows\system32;C:\windows;C:\windows\System32\Wbem;C:\windows\System32\WindowsPowerShell\v1.0\;c:\Program Files (x86)\Microsoft SQL Server\100\Tools\Binn\;c:\Program Files\Microsoft SQL Server\100\Tools\Binn\;c:\Program Files\Microsoft SQL Server\100\DTS\Binn\;E:\SetupSoftware\Git\cmd;c:\Program Files (x86)\Microsoft SQL Server\90\Tools\binn\;C:\Program Files (x86)\Microsoft SQL Server\100\Tools\Binn\VSShell\Common7\IDE\;C:\Program Files (x86)\Microsoft SQL Server\100\DTS\Binn\;C:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies\;E:\SetupSoftware\MySQL\MySQL Server 5.5\bin;C:\Program Files (x86)\MySQL\MySQL Server 5.5\bin;C:\windows\system32\config\systemprofile\.dnx\bin;C:\Program Files\Microsoft DNX\Dnvm\;C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\;C:\Program Files\Microsoft SQL Server\130\Tools\Binn\;C:\Qt\4.7.3\bin;C:\Users\huang\AppData\Local\Microsoft\WindowsApps;
#
#
# # 操作文件和目录
# # 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
#
# # 查看当前目录的绝对路径
# print(os.path.abspath('.'))  # J:\Python3\Mybook\廖雪峰教程\IO编程
#
# # 在某个目录下创建一个新的目录,
# # 首先把新目录的完整路径表示出来
# # print(os.path.join('J:\Python3\Mybook\廖雪峰教程\IO编程', 'my_test'))
# # J:\Python3\Mybook\廖雪峰教程\IO编程\my_test
# my_payh = os.path.join('J:\Python3\Mybook\廖雪峰教程\IO编程', 'my_test')
# print(my_payh)
#
# # 然后创建这个目录
#
# os.mkdir(my_payh)
# # Traceback (most recent call last):
# #   File "J:/Python3/Mybook/廖雪峰教程/IO编程/操作文件和目录.py", line 77, in <module>
# #     os.mkdir(my_payh)
# # FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'J:\\Python3\\Mybook\\廖雪峰教程\\IO编程\\my_test'
#
# # 然后创建这个目录  没有返回值
# # make_dir = os.mkdir(my_payh)
# # print(make_dir)  # None
#
# # 删除掉一个目录
# os.rmdir(my_payh)
# # Traceback (most recent call last):
# #   File "J:/Python3/Mybook/廖雪峰教程/IO编程/操作文件和目录.py", line 89, in <module>
# #     os.rmdir(my_payh)
# # OSError: [WinError 145] 目录不是空的。: 'J:\\Python3\\Mybook\\廖雪峰教程\\IO编程\\my_test'
#
# # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# # 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# # part-1/part-2
#
# # 而Windows下会返回这样的字符串：
# # part-1\part-2
#
# # 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
#
# print(os.path.split('J:\Python3\Mybook\廖雪峰教程\IO编程\my_test\test.txt'))
#
# # os.path.splitext()  # 可以直接让你得到文件扩展名，很多时候非常方便：
#
# print(os.path.splitext('J:\Python3\Mybook\廖雪峰教程\IO编程\my_test\test.txt'))

import os
# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# 对文件重命名:
# os.rename('test.txt', 'test.py')

# 删掉文件:
# os.remove('test.py')

# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))
# 移除
os.remove("J:/Python3/Mybook/廖雪峰教程/IO编程/test.py")
# 移除后列出目录
print("移除后 : %s" % os.listdir(os.getcwd()))

# 目录为: ['my_test', 'StringIO和BytesIO.py', 'test.py', 'test.txt', '操作文件和目录.py']
# 移除后 : ['my_test', 'StringIO和BytesIO.py', 'test.txt', '操作文件和目录.py']
# ['my_test']
# ['StringIO和BytesIO.py', '操作文件和目录.py']


# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
# 最后看看如何利用Python的特性来过滤文件。
#
# 比如我们要列出当前目录下的所有目录，只需要一行代码：
print([x for x in os.listdir('.') if os.path.isdir(x)])
# ['my_test']

# 要列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
# ['操作文件和目录.py']