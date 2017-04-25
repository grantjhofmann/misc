import csv

f = open('wholefoods_tweets.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
n = open('wholefoods_edit.csv', 'w')
writer = csv.writer(n, delimiter=',', quotechar='"')
count = 0
for row in reader:
    count += 1
    if count % 2 != 0:
        stringtowrite = row[2]
        stringtowrite = stringtowrite[2:]
        stringtowrite = stringtowrite[:-1]
        stringtowrite.replace('"',"")
        stringarray = [stringtowrite]
        writer.writerow(stringarray)
f.close()
n.close()
