import os

for (root, dirs, files) in os.walk('C:\\Users\\hehehe47\\Desktop\\1'):
    for f in files:
        a = os.path.join(root, f)
        if 'start_plcy' in a or 'stop_plcy' in a:
            print(a)
