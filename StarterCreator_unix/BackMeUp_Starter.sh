#!/bin/bash

# check kernel(linux, BSD, or Darwin)
# check os release
# check python, if not installed, show command
# check ruby, if not installed, show command

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

# Check if python 2.7.x is installed, or show the command to install python
py=$(command -V python)

function print_pyVer()
{
    $(python --version)
}

if [ "$py" != "" ]; then
	 echo -n "Python is installed with=> " ; print_pyVer
else
    echo "python is not install!"
fi 



## Path to main.py
