from dataclasses import dataclass, field
from datetime import timedelta
from moviepy.editor import *

@dataclass
class CutMarkers():
    start: int
    stop: int

def CalculateCuts(videos,seconds_pre, seconds_post):
    
    for video in videos:
        cuts = []
        for hilight in video.hilight_markers:

            # Error checking
            pre = seconds_pre
            post = seconds_post
            if hilight+post > video.duration:
                post = video.duration-hilight

            cuts.append(CutMarkers(hilight-pre,hilight+post))

        video.cuts = cuts
    return videos


    #         vid = VideoFileClip(video.path).subclip((hilight-seconds_pre)/1000,(hilight+post)/1000)
    #         clips.append(vid)
        

    # #print(GoProVideos)
    # final_video = concatenate_videoclips(clips)
    # final_video.write_videofile('E:\Documents\GitHub\GoPro-HiLight-Reel\gopro-hilight-reel\edit'+video.name+'.mp4',fps=60)
    

