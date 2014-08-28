#!/bin/bash

# check kernel(linux, BSD, or Darwin)
# check os release
# check python
# check ruby

# Check user's kernel type
kernel="unknown"
uname_str=$(uname)
if [[ "$uname_str" == "Linux" ]]; then
	kernel="Linux"
elif [[ "$uname_str" == "FreeBSD" ]]; then
    kernel="FreeBSD"
elif [[ "$uname_str" == "Darwin" ]]; then
    kernel="Darwin"
fi

# Check OS release
os_rels=$(lsb_release -d)

echo $os_rels


exit 0

# Check and print version of python
#py_version=$(pythons)
#echo $py_version
#if [ "$(hash python5)" = "沒有找到" ]; then
#	echo "python沒有安裝"
#fi

## Path to main.py
