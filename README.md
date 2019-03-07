# GoPro Hilight Reel

This script takes a folder of GoPro videos tagged with [HiLights](https://gopro.com/help/articles/Question_Answer/What-is-HiLight-Tagging-and-How-Does-it-Work) and automatically edits them into a single video, trimming the videos 10 seconds before and 3 seconds after each HiLight tag.

The goal was to automatically edit my volleyball game footage in order to be able to watch and learn (and laugh) at highlights.

# Todo
 - Loop over videos in a folder
 - Find HiLight meta data in each video
 - Trim video 10 seconds before and 3 seconds after HiLight
 - Allow parmeterization of trim lead in/lead out
 - Combine all video segments into one final video and save locally
 - Auto upload to YouTube