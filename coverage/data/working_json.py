import json
import urllib.request

json_data = '/home/aberhe/pythonMasterClass/coverage/data/temperature_anomaly.json'
# json_data = 'https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json'

with open(json_data, 'r') as data:
# with urllib.request.urlopen(json_data) as json_output:
    # data = json_output.read().decode('utf-8')
    anomalies = json.load(data)

# print(anomalies)
# print("*" * 200)

# print(anomalies['citation'])

for key,value in anomalies['description'].items():
    print(key, value)