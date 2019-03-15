from moviepy.editor import *

def EditVideo(videos,output_path,output_height,output_width):
    trimmed_clips = []
    #Color  clip to flash  in between cuts
    color_clip =  ColorClip((output_height,output_width),[255,255,255],False,.5,None)
    for video in videos:
        for cut in video.cuts:
            vid = VideoFileClip(video.path).subclip(cut.start/1000.0,cut.stop/1000.0)
            trimmed_clips.append(vid)
            trimmed_clips.append(color_clip)

    

    #print(GoProVideos)
    final_video = concatenate_videoclips(trimmed_clips)
    final_video.write_videofile(output_path + '\FinalEdit.mp4',fps=60)