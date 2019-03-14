from moviepy.editor import *

def EditVideo(videos,output_path):
    trimmed_clips = []
    for video in videos:
        for cut in video.cuts:
            vid = VideoFileClip(video.path).subclip(cut.start/1000.0,cut.stop/1000.0)
            trimmed_clips.append(vid)
        

    #print(GoProVideos)
    final_video = concatenate_videoclips(trimmed_clips)
    final_video.write_videofile(output_path + '\FinalEdit.mp4',fps=60)