import wmi
import psutil
import time
w = wmi.WMI()
for disk in w.Win32_LogicalDisk():
    print(disk.Caption)
for cpu in w.Win32_Processor():
    print(cpu.Name)
    print(cpu.MaxClockSpeed)
    print(cpu.NumberOfCores)
#print(psutil.cpu_percent(0))
processes = wmi.WMI().Win32_Process()
for process in processes:
    print("process name:" + process.name + " thread amount: "  + str(process.threadCount) + "process Id:" + str(process.ProcessID))
    print(process)

for i in range(0,16):
    print(psutil.cpu_percent(0)) 
    time.sleep(0.05) 