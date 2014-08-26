#!/usr/bin/ruby

=begin
NT Path Handler

Receive windows path inputs from user and split path into directories, 
separating with comma, and output them to a file. As BackMeUp in windows
asks for path, will read that file.
=end

# Receive one or more NT paths(C:\xxx\yyy\zzz\aaa.bb) from user inputs
# and split them with comma.
ntpaths_in = gets.chomp     # chomp: drop "\n"
ntpaths_split=ntpaths_in.split(",")  # Split multiple paths into list

foreslash_path_array = []     # Create empty array to hold multi-path

# Replace the backslash with foreward slash of each path and then append
# them into array "foreslash_path_array"
ntpaths_split.each do |each_path|
	foreslash_path = each_path.split("\\").join("/")
	foreslash_path_array << foreslash_path
end

# Write the array to file and python will read it later on
open("POST_HANDLED_NT_PATHs","w") do |f|
	f << foreslash_path_array
end



