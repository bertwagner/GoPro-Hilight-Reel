from dataclasses import dataclass, field
from datetime import timedelta
from moviepy.editor import *

@dataclass
class CutMarkers():
    start: int
    stop: int

def CalculateCuts(videos,seconds_pre, seconds_post):
    milliseconds_pre = seconds_pre * 1000
    milliseconds_post = seconds_post * 1000
    previous_clip = None
    # If a hilight occurs right at the start or end of a video 
    # and needs to be carried forward to then ext clip
    milliseconds_pre_carryover = 0
    milliseconds_post_carryover = 0

    for v,video in enumerate(videos):
        cuts = []

        for hilight in video.hilight_markers:
            # If we had carryover from the previous clip
            if milliseconds_post_carryover > 0:
                cuts.append(CutMarkers(0,milliseconds_post_carryover))
                milliseconds_post_carryover = 0

            # Error checking
            delta_pre = milliseconds_pre
            delta_post = milliseconds_post

            #If a hilight occurs early in the video
            if hilight - delta_pre < 0:
                delta_pre = hilight
                milliseconds_pre_carryover = milliseconds_pre-delta_pre
                #If we had carryover from the previous clip
                videos[v-1].cuts.append(CutMarkers(previous_clip.duration-milliseconds_pre_carryover,milliseconds_pre_carryover))
                
                milliseconds_pre_carryover = 0

            #If a hilight occurs late in the video
            if hilight+delta_post > video.duration:
                delta_post = video.duration-hilight
                milliseconds_post_carryover = milliseconds_post - delta_post

            cuts.append(CutMarkers(hilight-delta_pre,hilight+delta_post))
            previous_clip = video
        video.cuts = cuts
    return videos