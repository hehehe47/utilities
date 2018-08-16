def multiple(a, b):
    if len(a) < len(b):
        c = a
        a = b
        b = c
    na = int(a)
    nb = int(b)
    list_a = list(a)
    list_b = list(b)
    list_c, list_d = [], []
    sum = 0
    list_b.reverse()
    count = 0
    for i in list_b:
        list_c.append(int(i) * na)
        list_d.append(int(i) * na)
        if count != 0:
            list_c[count] *= 10 ** count
        sum += list_c[count]
        count += 1
    count = 0
    len_blank = abs(len(list_c) - 2)
    len_total = len('*' + ' ' * (len(a) - len(b) + 2) + b + ' ') + abs(len(list_d) - 3)
    print(' ' * (len_total - len(a) - count) + a)
    print(' ' * (len_total - len(b) - count - len('*' + ' ' * (len(a) - len(b) + 2))) + '*' + ' ' *
          (len(a) - len(b) + 2) + b)
    print('-' * (len_total + 1))
    for j in list_d:
        print(' ' * (len_total - len(str(j)) - count) + str(j))
        count += 1
    print('-' * (len_total + 1))
    print(' ' * (len_total - len(str(sum))) + str(sum))
