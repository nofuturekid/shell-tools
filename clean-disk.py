#!/usr/bin/env python
import sys

'''
Nuke GPT on any given block device.
'''

def clear_gpt(target):
      '''
According to http://en.wikipedia.org/wiki/GUID_Partition_Table - GPT
stores partition data in the first and last 34 LBA blocks. A LBA sector
is normally 512 bytes.
      '''
      fd = open(target, "w+")
      fd.seek(0)
      fd.write('\0' * 34 * 512)
      print "done nuking data at the beginning of disk", target
      fd.seek(0, 2) # SEEK_END is 2
      disk_size = fd.tell()
      fd.seek(disk_size - 34*512)
      fd.write('\0' * 34 * 512)
      print "done nuking data at the end of disk", target

if __name__ == '__main__':
      for x in sys.argv[1:]:
              clear_gpt(x)
