import math

def frange(start,end,step):
    while(start < end):
        yield start
        start += step

sample_frequency = 4000.0
delta_time = 1.0 / sample_frequency
nominal_frequency = 60 #Nominal Frequency
testing_frequency = 59
max_voltage = 120 #Amplitude of the test signal
number_of_samples = 10000
x = []
for t in frange(delta_time,number_of_samples * delta_time,delta_time):
    x.append(max_voltage * math.sin(2 * math.pi * nominal_frequency * t))

for voltage in x:
    print voltage
