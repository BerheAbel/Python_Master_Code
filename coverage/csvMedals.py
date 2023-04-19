import csv

csv_file = '/home/aberhe/pythonMasterClass/coverage/data/OlympicMedals_2020.csv'
# with open(csv_file, encoding='utf-8', newline='') as csv_reading:
#     headrs = csv_reading.readlines().strip('\n').split(',')
#     print(f'columns headers: {headrs}')
#     data = csv.reader(csv_reading)
    # data2 = [line.strip('\n') for line in csv_reading.readlines()]
    
    # print(data2.split(','))
    # data2 = csv_reading.readlines().strip('\n')
    # print(data2)
with open(csv_file) as data:
    loader = csv.DictReader(data)
    print(loader)
    for row in loader:
        print(row['Country'])