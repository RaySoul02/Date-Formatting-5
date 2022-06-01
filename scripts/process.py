import csv
from datetime import datetime

def transform_date(s: str):
    s = s.split()[2:]
    res = ''
    for i in s:
        res += i + ' '
    return(res[:(len(res) - 3)])

r = csv.reader(open('source.csv', 'r'), delimiter=';')
header = next(r)
with open('result1.csv', 'w') as result:
    writer = csv.writer(result, lineterminator='\n')
    writer.writerow(header)
    for row in r:
        row[0] = datetime.strptime(transform_date(row[0]), '%Y, %B %d').strftime('%Y-%m-%d')
        writer.writerow(row)