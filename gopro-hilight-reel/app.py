import HiLightExtractor, CutCalculator, MovieCreator
import time
import os

# CONFIG
video_folder_path = os.path.join(os.path.dirname(__file__),"VideoFiles")

seconds_pre = 7
seconds_post = 1
output_width=1920
output_height=1080

youtube_video_title = "Volleyball Match " + time.strftime("%Y-%m-%d")
youtube_video_description = ""
youtube_privacy_status = "unlisted"

if __name__ == '__main__':
    # Figure out where the GoPro HiLight tags are in the video
    videos = HiLightExtractor.get_video_properties(video_folder_path)
    
    # Create start and end trim marks for each HiLight tag
    videos = CutCalculator.CalculateCuts(videos, seconds_pre, seconds_post)

    # Piece all of the trimmed clips together
    MovieCreator.EditVideo(videos,video_folder_path,output_height,output_width)

    # Upload to YouTube
    # The first time this runs you will have to authenticate with Google.
    os.system('python '+os.path.join(os.path.dirname(__file__),'YouTubeUpload.py') +' --file="'+os.path.join(video_folder_path,'FinalEdit.mp4')+'" \
                      --title="'+youtube_video_title+'" \
                      --description="'+youtube_video_description+'" \
                      --privacyStatus="'+youtube_privacy_status+'"')

    

    


