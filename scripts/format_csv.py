import csv
import datetime as dt


input = 'sonit.csv'
output = 'sonit-time.csv'
year = 2020


if __name__ == "__main__":
    reader = csv.reader(open(input, 'r'), delimiter=',')
    next(reader, None)

    writer = csv.writer(open(output, 'w'), delimiter=',')

    header = ['kw','ts','particles']
    writer.writerow(header)

    for row in reader:
        kw = int(row[0])
        wts = '{year}-W{kw:02d}-1'.format(year=year, kw=kw)
        ts = dt.datetime.strptime(wts, "%Y-W%W-%w")
        particles = row[1]
        if particles == "":
            particles = "null"
        writer.writerow([str(kw), str(ts), particles])
