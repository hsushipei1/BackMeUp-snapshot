#!/bin/bash

#=================================================
#          BackMeUp Starter for UNIX
#=================================================
# In this script,
#   check kernel(linux, BSD, or Darwin)
#   check os release
#   check python, if not installed, show command
#   check ruby, if not installed, show command
#   ask for path to main.py

#   Launch BackMeUp if the above things are ready!

### Define functions
# Def function of press enter to continue
function enter_2_continue()
{
	# Yup...press ENTER to continue
	read -p "Press ENTER to continue"
}

function print_color()
{
    # Let's print some colors on terminal.
    # Usage:
    #   print_color [color_avail] [some text]
    #   e.g. print_color "red" "Print some red text~"
    # For more detailed info: 
    #   http://misc.flogisoft.com/bash/tip_colors_and_formatting
    # Available colors: default, black, red, green, yellow, blue, white

    if [ "$1" == "default" ]; then
		echo -en "\e[39m"$2"\e[39m"
    elif [ "$1" == "black" ]; then
        echo -en "\e[30m"$2"\e[39m"
    elif [ "$1" == "red" ]; then
        echo -en "\e[31m"$2"\e[39m"
    elif [ "$1" == "green" ]; then
        echo -en "\e[32m"$2"\e[39m"
    elif [ "$1" == "yellow" ]; then
        echo -en "\e[33m"$2"\e[39m"
    elif [ "$1" == "blue" ]; then
        echo -en "\e[34m"$2"\e[39m"
    elif [ "$1" == "white" ]; then
        echo -en "\e[97m"$2"\e[39m"
    fi
}

function clear_console()
{
	# clear console....
	clear
}

### Clear console at the begining
clear_console

### Welcome message
echo " "
echo "Welcome to BackMeUp Starter for UNIX"
echo " " 

### Start
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
py=$(command -V python2)

if [ "$py" != "" ]; then
	print_color "green" "[PASS] Python2 is installed with=> " ; $(python --version)
else
    print_color "red" " *** Python2 is not install! \n" 
	print_color "blue" " Your operating system is=> $os_rels" 
	echo " "
	echo "# To install python2 from software repository..."
	echo "* For Ubuntu, Debian, Mint=> apt-get install python"
	echo "* For CentOS, RHEL, Fedora=> yum install python"
	echo "* For openSUSE, SUSE Linux Enterprise=> zypper install python"
	exit 0
fi 

# Check if ruby is installed, or show the command to install it.
rb=$(command -V irb)

if [ "$rb" != "" ]; then
	print_color "green" "[PASS] Ruby is installed with=> " ; $(ruby --version)
else
    print_color "red" " *** Ruby is not install! \n"
	print_color "blue" " Your operating system is=> $os_rels"
    echo " "
    echo "# To install Ruby from software repository..."
    echo "* For Ubuntu, Debian, Mint=> apt-get install ruby"
    echo "* For CentOS, RHEL, Fedora=> yum install ruby"
    echo "* For openSUSE, SUSE Linux Enterprise=> zypper install ruby"
    exit 0
fi

