#!/bin/bash

# Use this shell file to manage the backup schedule.

# Check for current crons
crontab -l > myCron        # myCron should be saved in HOME

# Add a job
echo "* * * * * cp -r xxx/yyy/zzz aaa/bbb/ccc" >> myCron
crontab myCron


# Function: (1) add(from main.py), 
#			(2) edit(out of BackMeUp), 
#			(3) delete(out of BackMeUp), and 
#			(4) view(out of BackMeUp)
#		    a new schdule(from main),

