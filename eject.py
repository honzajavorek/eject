#!/usr/bin/env python3

import os
import time
import sys
import signal
import subprocess


ps = subprocess.run(['diskutil', 'list'], capture_output=True, check=True)
diskutil_list = ps.stdout.decode('utf8').split('\n\n')
external_disks = [disk for disk in diskutil_list if 'external' in disk]

if not external_disks:
    print('Found no external drives', file=sys.stderr)
    sys.exit(0)

disk = external_disks[0]
disk_lines = disk.splitlines()
disk_name = disk_lines[0].split()[0]
disk_identifier = disk_lines[3].split()[2]
print(f'Ejecting {disk_name}, {disk_identifier}', file=sys.stderr)

print(f'Going after hanging QuickLook processes', file=sys.stderr)
ps = subprocess.run(['lsof'], capture_output=True, check=True)
lsof_list = ps.stdout.decode('utf8').splitlines()
quicklook_pids = [
    int(line.split()[1]) for line in lsof_list
    if 'QuickLook' in line and f'/Volumes/{disk_identifier}' in line
]
print(f'Found {len(quicklook_pids)} tiny little bastards to kill', file=sys.stderr)

for pid in quicklook_pids:
    os.kill(pid, signal.SIGTERM)
time.sleep(0.5)
for pid in quicklook_pids:
    os.kill(pid, signal.SIGKILL)

print(f'Ejecting the drive', file=sys.stderr)
subprocess.run(['diskutil', 'unmountDisk', disk_name], capture_output=True, check=True)
