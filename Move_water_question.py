import time

t1 = time.time()


def swap(x, y):
    t = x
    x = y
    y = t
    return x, y


def print_f(x, y):
    if swap_flag:
        print('(' + str(y) + ',' + str(x) + ')')
    else:
        print('(' + str(x) + ',' + str(y) + ')')


def fill(x, y, Max_x, Max_y, z):
    while x != Max_x or y != Max_y:
        if y == z or x == z:
            return True
        else:
            if x == 0:
                x = Max_x
                print_f(x, y)
                continue
            elif y < Max_y:
                if x + y > Max_y:
                    tmp = x + y - Max_y
                    y = Max_y
                    x = tmp
                    print_f(x, y)
                    continue
                else:
                    y += x
                    x = 0
                    print_f(x, y)
                    continue
            elif y == Max_y:
                y = 0
                continue
    return False


swap_flag = 0
x, y = 0, 0
Max_x, Max_y, z = map(int, input('x=?,y=?,z=?').split(','))
if z > Max_x and z > Max_y:
    print('error')
    exit(0)
if Max_x > Max_y:
    swap_flag = 1
    Max_x, Max_y = swap(Max_x, Max_y)
print(fill(x, y, Max_x, Max_y, z))
# if not os.path.exists('logs'):
# os.mkdir('logs')
# file = open('logs/move_water.txt')
for Max_x in range(1, 101):
    for Max_y in range(Max_x + 1, 101):
        for z in range(Max_x, Max_y + 1):
            flag = fill(x, y, Max_x, Max_y, z)
            print(str(Max_x), str(Max_y), str(z))
            if Max_x > Max_y:
                swap_flag = 1
                Max_x, Max_y = swap(Max_x, Max_y)
            # if not flag:
            # file.write(str(Max_x) + ' ' + str(Max_y) + ' ' + str(z) + '\n')

# file.close()
# time2 = time.time()
# print(time2 - t1)
