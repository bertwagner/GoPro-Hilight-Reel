from moviepy.editor import *

def EditVideo(videos,output_path,output_height,output_width):
    trimmed_clips = []
    #Color  clip to flash  in between cuts
    color_clip =  ColorClip((output_height,output_width),[0,0,0],False,.3,None)
    for video in videos:
        for cut in video.cuts:
            vid = VideoFileClip(video.path).subclip(cut.start/1000.0,cut.stop/1000.0)
            trimmed_clips.append(vid)

            # Don't add a flash after clips that carryover from one video to the next
            if (cut.stop != video.duration):
                trimmed_clips.append(color_clip)

    #print(GoProVideos)
    final_video = concatenate_videoclips(trimmed_clips)
    final_video.write_videofile(output_path + '\FinalEdit.mp4',fps=60)