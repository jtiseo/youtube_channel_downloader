#!/usr/bin/python
"""
YouTube Channel Downloader
"""
 
import sys, os
from datetime import date
from subprocess import call
import urllib, json

print "--------------------------"
print "YouTube Channel Downloader"
print "--------------------------"
print ""
while True:
    try:
        author = raw_input("Enter username of YouTube channel: ")
        break
    except ValueError:
        print "Please enter a valid username"
while True:
    try:
        number_of_videos = int(raw_input("Enter number of videos to download (1-25): "))
        break
    except ValueError:
        print "Please enter a valid number"


inp = urllib.urlopen(r'http://gdata.youtube.com/feeds/api/users/' + author + '/uploads?alt=json')
resp = json.load(inp)
inp.close()

x=0
y=len(resp)
while x < number_of_videos: #25:#1:
	video = resp['feed']['entry'][x]#[0]
	
	# Title of the video
	title = video['title']['$t']
	print title

	# URL of the video
	link = video['link'][0]['href']
	print link
	
	d = date.today().strftime("%Y-%m-%d")

	call(["youtube-dl", "-c", link, "-o", 'downloads/%(title)s-%(upload_date)s']) # send url to youtube-dl
	call(["rm", "-f", "*.part"]) # remove all partial download files

	x = x + 1