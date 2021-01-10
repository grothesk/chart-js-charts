import csv
import datetime as dt


input = 'sonit-mdm-2019.csv'
output = 'sonit-mdm-time-2019.csv'
year = 2019


if __name__ == "__main__":
    reader = csv.reader(open(input, 'r'), delimiter=';')
    next(reader, None)

    writer = csv.writer(open(output, 'w'), delimiter=',')

    header = ['kw','ts','particles']
    writer.writerow(header)

    for row in reader:
        kw = int(row[0])
        wts = '{year}-W{kw:02d}-1'.format(year=year, kw=kw)
        ts = dt.datetime.strptime(wts, '%Y-W%W-%w')
        particles = row[1]
        if particles == '':
            particles = 'null'
        else:
            if ',' in particles:
                particles = particles.replace(',', '.')
            particles = '{:.2f}'.format(float(particles))
        writer.writerow([str(kw), str(ts), particles])
