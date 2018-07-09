import os


def find(de):
    '''
    迭代遍历所有文件夹，查找
    :param de: 根目录
    :return: None
    '''
    if de != '新建文件夹':
        if os.path.isdir(de):
            os.chdir(de)
            for i in os.listdir(os.getcwd()):
                find(i)
            os.chdir('..')
        else:
            if '占位' not in de and 'readme' not in de:
                print(de)


find('D:\\Manager\\riskdb')
