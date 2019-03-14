# GoPro HiLight Reel

This script takes a folder of GoPro videos tagged with [HiLights (tags)](https://gopro.com/help/articles/Question_Answer/What-is-HiLight-Tagging-and-How-Does-it-Work) and automatically edits them into a single video, trimming the videos 10 seconds before and 3 seconds after each HiLight tag.

The goal was to automatically edit my volleyball game footage in order to be able to watch and learn (and laugh) at highlights.

# Todo
 - Loop over videos in a folder
 - Find HiLight/tag meta data in each video
 - Trim video 10 seconds before and 3 seconds after HiLight
 - Allow parmeterization of trim lead in/lead out
 - Combine all video segments into one final video and save locally
 - Clear out hilights that are too close to each other
 - Auto upload to YouTube
 - Send out tweet