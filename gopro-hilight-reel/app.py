import HiLightExtractor, CutCalculator, MovieCreator
import time
import os

# CONFIG
    video_folder_path = os.path.dirname(os.path.realpath(__file__))
    
    seconds_pre = 5
    seconds_post = 3
    output_width=1920
    output_height=1080

    youtube_video_title = f"Volleyball Match {time.strftime("%Y-%m-%d")}"
    youtube_privacy_status = "unlisted"

if __name__ == '__main__':
    videos = HiLightExtractor.get_video_properties(video_folder_path)
    print(videos)
    videos = CutCalculator.CalculateCuts(videos, seconds_pre, seconds_post)
    MovieCreator.EditVideo(videos,video_folder_path,output_height,output_width)

    os.system(f'python {video_folder_path}\YouTubeUpload.py --file="{video_folder_path}\FinalEdit.mp4" \
                      --title="{youtube_video_title}" \
                      --privacyStatus="{youtube_privacy_status}"')

    

    


