#!/bin/bash

#=======================================================
#           BackMeUp Starter Creator for UNIX    
#=======================================================
#                                         by HsuShiPei
# In this script,
#   check kernel(linux, BSD, or Darwin)
#   check os release
#   check python, if not installed, help install it(optional).
#   check ruby, if not installed, help install it(optional).
#   ask for path to main.py

#	Generate "Start_BackMeUp.sh" if the above things are done!

### Define some functions
# Def function of press enter to continue
function enter_2_continue()
{
	# Yup...press ENTER to continue
	read -p "Press ENTER to continue"
}

function clear_console()
{
    # Well...just CLEAR the console....
    clear
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

function install_soft_repo()
{
	# The function
	#   Detect user's operating system and install package with the OS'
	#   package mananger.
	# Function inputs
	#   "$1" => "os_release"=> Your OS release
	#   "$2" => "software"=> Software's name
	# Usage
	#   e.g. install_soft_repo "$os_release" "htop"

	if [ "$1" == "Ubuntu" ] || [ "$1" == "Debian" ]; then
        echo "Will install "\"$2\"" using package manager of your OS."
		echo "Be sure you are in the sudoer list."
		sudo apt-get install $2
	elif [ "$1" == "Fedora" ] || [ "$1" == "CentOS" ]; then
        echo "Will install "\"$2\"" using package manager of your OS."
        echo "Be sure you are in the sudoer list."
        sudo yum install $2
	elif [ "$1" == "openSUSE" ]; then
        echo "Will install "\"$2\"" using package manager of your OS."
        echo "Be sure you are in the sudoer list."
		sudo zypper install $2
	else
		echo "Please install Python2!"
	fi
}

### Clear console at the begining
clear_console

### Welcome message
echo " "
print_color "blue" "Welcome to BackMeUp Starter Creator for UNIX";
printf "\n" ; echo " "
echo "  This starter creater will simplify the pre-startup checking process "
echo "  of BackMeUp in UNIX."
echo "  This script will check if necessary softwares(python2, ruby)"
echo "  are installed. If one of them is not ready, please install it and" 
echo "  re-run this script agin."
echo "  If all things are ready, this creator will generate a starter script."
echo "  To lanuch BackMeUp, just run that starter script!"

echo " "
echo "If you are using following linux distribution "
print_color "green" "  Ubuntu, Debian, Fedora, CentOS, OpenSUSE,"
printf "\n"
echo " this script will help you install it."
echo " "

# press enter to cont and clear console
enter_2_continue
clear_console

### Get some info about the system
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
os_release=$(lsb_release -d|cut -d " " -f 1|cut -c 14-)

### Check if python2 and ruby is installed in the system.
# Check if python 2.7.x is installed, or show the command to install python
py=$(command -V python2)

if [ "$py" != "" ]; then     # python2 is installed
	print_color "green" "[PASS] Python2 is installed with=> " ; $(python --version)
else		# python2 isn't installed, install it with pkg manager.
    print_color "red" " ### Python2 is not installed! \n" 
	print_color "blue" " Your operating system is=> ${os_release}"
	echo " "
		
	install_soft_repo "$os_release" "python"  # Install pkg using function
	exit 0
fi 

# Check if ruby is installed, or show the command to install it.
rb=$(command -V irb)

if [ "$rb" != "" ]; then
	print_color "green" "[PASS] Ruby is installed with=> " ; $(ruby --version)
else
    print_color "red" " ### Ruby is not install! \n"
	print_color "blue" " Your operating system is=> ${os_release}"
    echo " "
    
	install_soft_repo "$os_release" "ruby"  # Install pkg using function
	exit 0
fi

# Show message and tell user that they have met the software requirment.
echo " "
print_color "blue" "### Congratulations!! We've done the verification of neccessary"
print_color "blue" "    softwares."
echo " "

# press enter to cont and clear console
enter_2_continue
clear_console

### Ask the path of directory to BackMeUp and generate starter script
# Ask for path of directory to BackMeUp
echo " "
echo "After checking the prerequisite softwares, we are about to "

echo " "
print_color "red" "# Please enter the path to the directory of BackMeUp" ; echo " "
read -p ">" Path2BackMeUp

# Generate starter script
startScrptNam="Start_BackMeUp.sh"    # Name for starter script

cat > ${startScrptNam} <<EOF
#!/bin/bash

python -B ${Path2BackMeUp}/main.py
EOF

# Clear console after entering the path
clear_console

# After generating starter script
echo " Starter script \"${startScrptNam}\" is generated. Run command"
echo " "
print_color "blue" "sh ${startScrptNam}" ; echo " "
echo " "
echo "to start BackMeUp."

read -p "Press Enter to leave" leave

