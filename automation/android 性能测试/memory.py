
import subprocess
import StringIO
import time
import sys
import os


# package = 'com.baidu.searchbox'
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
memoryfile = ROOT_PATH + '\MEMORY.txt'
cpufile = ROOT_PATH + '\CPU.txt'
# print ROOT_PATH + '\MEMORY.txt'

def getMemory(package):
    if os.path.exists(memoryfile):
        os.remove(memoryfile)
    fo_write_memory = open(memoryfile, 'w+')
    while True:
        time.sleep(2)
        output = subprocess.check_output("adb shell dumpsys meminfo " + package)
        lines = StringIO.StringIO(output)
        for line in lines.readlines():
            if line.strip().find('TOTAL') > -1:
                print 'PssTotal: ' + line.split()[1]
                fo_write_memory.write('PssTotal: ' + line.split()[1]+'\n')
                break


def getCPU(package):
    if os.path.exists(cpufile):
        os.remove(cpufile)
    fo_write_cpu = open(cpufile, 'w+')
    while True:
        time.sleep(2)
        l = 0
        output = subprocess.check_output("adb shell top -n 1 ")
        lines = StringIO.StringIO(output)
        for line in lines.readlines():
            if 'CPU%' in line.split():
                l = line.split().index('CPU%')
            if package in line.split():
                print line
                print 'CPU: ' + line.split()[l]
                fo_write_cpu.write('CPU: ' + line.split()[l])
                break

if __name__ == "__main__":
    package = 'om.baidu.graph.sdk.demo'
    getMemory(package)
