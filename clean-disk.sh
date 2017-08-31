#!/usr/bin/env bash

# CLEAN FIRST GPT TABLE
#
echo "Cleaning first GPT table of \"${1}\""
dd if=/dev/zero of=/dev/${1} bs=$(cat /sys/block/${1}/queue/hw_sector_size) count=34

# CLEAN BACKUP GPT TABLE
#
echo "Cleaning backup GPT table of \"${1}\""
dd if=/dev/zero of=/dev/${1} bs=$(cat /sys/block/${1}/queue/hw_sector_size) seek=$(( $(cat /sys/block/${1}/size)-34 )) count=34

# RE-READ block devices
#
echo "Re-read partion table of \"${1}\""
blockdev --rereadpt /dev/${1}
