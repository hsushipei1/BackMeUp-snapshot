#!/usr/bin/ruby

=begin
NT Path Handler

Receive windows path inputs form user and split path into directories, 
separating with comma, and output them to a file. As BackMeUp in windows
asks for path, will read that file.
=end

# Receive NT path(C:\xxx\yyy\zzz\aaa.bb) from user inputs
puts "Please enter ntpath."
ntpath = gets.chomp     # chomp: drop "\n"
#print ntpath+"\n"

# Split ntpath into a list containing each directories
# and combine them with foreward slash.
path = ntpath.split("\\").join("/")  
print path
print "\n"

# Output 
open("RUBY_NTPATH_OUTPUT","w") do |f|
	f << path
end



