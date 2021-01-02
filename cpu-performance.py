# pip install -r requirements.txt

import psutil
import platform
from datetime import datetime
import time
import multiprocessing

uname = platform.uname()

print("System: {}".format(uname.system))
print("Computer Name: {}".format(uname.node))
print("Version: {}".format(uname.version))
print("Processor: {}".format(uname.processor))

print("Physical cores: {}".format( psutil.cpu_count(logical=False)))
print("Total cores: {}".format(psutil.cpu_count(logical=True)))
cpufreq = psutil.cpu_freq()
print("Max Frequency: {} Mhz".format(cpufreq.max))
print("Current Frequency: {} Mhz".format(cpufreq.current))

 
def fun_single(input_list):
    for i in range(len(input_list)):
        input_list[i]**1000
 
input_list = [1000]*1000000
 
start_time = time.time()
fun_single(input_list)
end_time = time.time()
 
print("Single processing duration: {:8.2f} s".format(end_time - start_time))
