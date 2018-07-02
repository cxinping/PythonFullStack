import os
import re

loadAvg = os.popen('uptime').readlines()
loadAvgStr = ''.join(loadAvg)
loadAvgStr = loadAvgStr.replace(' ', '')
pattern = re.compile(r'loadaverage:\s*(\d+\.*\d+),\s*(\d+\.*\d+),\s*(\d+\.*\d+)')
match = pattern.search(loadAvgStr)
output = ''
sep = ','
if match:
    #print(match.groups())
    data = match.groups()
    avg1 = data[0]
    avg5 = data[1]
    avg15 = data[2]
    output = 'Instance' + sep + 'LoadAvg1' + sep + 'LoadAvg5' + sep + 'LoadAvg15' + '\n';
    output += 'total' + sep + avg1 + sep + avg5 + sep + avg15
print(output)

