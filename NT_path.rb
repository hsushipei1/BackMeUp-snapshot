#!/usr/bin/ruby

=begin
NT Path Handler

Receive windows path inputs form user and split path into directories, 
separating with comma, and output them to a file. As BackMeUp in windows
asks for path, will read that file.
=end

# Receive NT path(C:\xxx\yyy\zzz\aaa.bb) from user inputs
#puts "Please enter ntpath."
ntpath = gets.chomp     # chomp: drop "\n"

# Split ntpath into a list containing each directories
# and combine them with foreward slash.
path = ntpath.split("\\").join("/")  
#print path

# Write the path with foreward slash to file and python will read it later on
open("POST_HANDLED_NT_PATH","w") do |f|
	f << path
end



