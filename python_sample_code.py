import csv
import glob
import os
import shutil

os.chdir(os.path.join('C:\\', 'Users\\', 'pberry\\', 'Desktop\\', 'Python'))

myfiles = (("MA_Exer_PikesPeak_Males", ' '), ("MA_Exer_PikesPeak_Females", "F"))

for file, gender in myfiles:
    with open((file + ".txt"), 'r+') as f, open("All_PikesPeak1_participants.csv", 'ab') as csvfile:
        conversion = "[]'-.$"
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        # 分隔符为\t  tab
        pen = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
        for row in reader:
            row = str(row)
            row = row.replace('/', '&')
            row = row.replace('#', '')
            row = row.replace('*', '')
            row = row.replace("\t", '')
            row = [''.join("" if c in conversion else c for c in entry) for entry in row]
            row.append(' &' + gender)
            pen.writerow(row)

source = os.getcwd()
dest = os.path.join('C:\\', 'Users\\', 'pberry\\', 'Desktop\\', 'Python\\')

files = glob.glob('./*PikesPeak1*.csv')

for f in files:
    shutil.move(source + f, dest)
