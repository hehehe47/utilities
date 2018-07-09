'''
加密算法采用 将大小写数字字符分成四组，将每位字母的ASCII码与密文的ASCII码相加
所得的和余4选择组别 余（选好组别的长度）选择自负
判断是否已存在在密码序列中，若存在 组别index各+1
'''


def encoding(context):
    num = None
    if ',' in context:
        context, num = context.split(',')
    else:
        context = context
    lower_index, upper_index, number_index, mark_index = [], [], [], []
    # 97~123小写字母 65~91 大写字母 48~58 数字 33~127 标点
    # 32 :   33 : ! 34 : " 35 : # 36 : $ 37 :  % 38 : & 39 : ' 40 : ( 41 : ) 42 : * 43 : + 44 : , 45 : - 46 : .
    # 47 : / 58 : : 59 : ; 60 : < 61 : = 62 : > 63 : ? 64 : @ 91 : [ 92 : \ 93 : ] 94 : ^ 95 : _ 96 : ` 123 : { 124 : |
    # 125 : } 126 : ~

    for i in range(97, 123):
        lower_index.append(chr(i))
    for i in range(65, 91):
        upper_index.append(chr(i))
    for i in range(48, 58):
        number_index.append(chr(i))
    for i in range(33, 123):
        if chr(i) not in lower_index and chr(i) not in upper_index and chr(i) not in number_index:
            if i != 0 and i != 1:
                mark_index.append(chr(i))
    index_list = [lower_index, upper_index, number_index, mark_index]
    j = 0
    name = 'hehehe47123'
    if len(name) > len(context):
        cycle = int(len(name) / len(context))
        added = len(name) % len(context)
        context = context * cycle + context[:added]
    else:
        cycle = int(len(context) / len(name))
        added = len(context) % len(name)
        name = name * cycle + name[:added]
    output = ''
    for i in range(len(name)):
        sub2 = ord(name[i]) + ord(context[i])
        index_choose_list = sub2 % 4
        index_choose_index = sub2 % index_list[index_choose_list].__len__()
        key = index_list[index_choose_list][index_choose_index]
        i = 0
        while key in output:
            index_choose_list = (index_choose_list + 1) % 4
            index_choose_index = (1 + index_choose_index) % index_list[index_choose_list].__len__()
            key = index_list[index_choose_list][index_choose_index]
            i += 1
            if i == 100:
                break
        output += key
    if num:
        print(output[:int(num)])
    else:
        print(output[:11])


context = input('输入格式：[加密文字，需要密码长]（不输入按默认11位）\n')
while context:
    encoding(context)
    context = input('输入格式：[加密文字，需要密码长]（不输入按默认11位）\n')
