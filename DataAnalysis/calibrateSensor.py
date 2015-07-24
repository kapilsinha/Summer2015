import numpy as np
calibrationData = []
fileName = open("/home/chronos/data_files/typicalLoadTest/typicalLoadTest-1.txt")
#sensorData = open("home/chronos/data_files/vrefs.txt",'w')

for line in fileName:
    line = eval(line)
    adc4 = []
    adc0 = []
    sensorId = int(line['source_addr'].encode('hex'))

    for sample in line['samples']:
        adc4.append(sample['adc-4'])
        np.mean(adc4)

    calibrationData[sensorId] += np.mean(adc4)
print calibrationData