#!/usr/bin/env python

from subprocess import call
import subprocess, json, requests, os, time, sys, re
from subprocess import check_output
from subprocess import Popen
from os.path import exists
final_dict = {}

#optional --daemon code; if you want to keep running this script, keep this code
#this is to prevent memory leaks.
if len(sys.argv) > 1:
    if sys.argv[1] == "--daemon":
        print "starting daemon ...\n"
        while True:
            os.system(os.path.realpath(__file__))
            time.sleep(300)
        print "here"
        sys.exit()



output = subprocess.check_output("sudo -s virsh list --all", shell=True)
output_array = output.split("\n")

#remove first two and last two; theyre headers
del output_array[0]
del output_array[0]
output_array.pop()
output_array.pop()

#look at running VMs and look at data
running_vms = []
allocated_memory = 0
for vm in output_array:
    id, name, state = vm.split()
    vm_information=subprocess.check_output("sudo virsh dominfo "+str(name), shell=True)
    lines = vm_information.split("\n")
    one_vm={}

    if exists(os.path.join(os.path.dirname(__file__), 'pcpu')):
        one_vm["cpu_usage"] = subprocess.check_output("./pcpu "+ str(name), shell=True).strip()
    #separate information for each vm. every line contains one vm
    for info in lines:
        if len(info) == 0:
            continue
        else:
            stat, value = info.split(":",1)
            one_vm[stat]=value.strip()
    running_vms.append(one_vm)
final_dict["running_vms"] = running_vms

#look through memory memory
memory_dict = {}
try:
    with open('/proc/meminfo', 'r') as f:
        for line in f.readlines():
            if line.startswith("MemTotal"):
                word1, word2 = line.split(":")
                memory_dict["total"] = word2[:-3].strip()
            if line.startswith("MemFree"):
                word1, word2 = line.split(":")
                memory_dict["free"] = word2[:-3].strip()
    memory_dict["allocated"] = allocated_memory
    final_dict["memory"] = memory_dict

    #load_average
    with open('/proc/loadavg', 'r') as f:
        for line in f.readlines():
            array_line = line.split()
        array_line.pop()
        array_line.pop()
        load_average = " ".join(array_line)
    final_dict["load_average"] = load_average


    print json.dumps(final_dict, sort_keys=True, indent=4, separators=(',',': '))
except KeyError:
    print KeyError
