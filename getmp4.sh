#!/bin/sh
echo 'get mp3 from youtube. if error, check to update youtube-dl and ffmpeg'
echo 'download ...'
youtube-dl --verbose -o temp.mp4 $1 
exit 0 
#echo 'transform mp4 to mp3...'
#ffmpeg -i temp.mp4 -b:a 192K -vn temp.mp3
#echo 'finish, please rename the temp.mp3 as you wish'
