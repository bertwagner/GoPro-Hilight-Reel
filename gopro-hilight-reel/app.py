import HiLightExtractor, CutCalculator, MovieCreator
import os

if __name__ == '__main__':
    # CONFIG
    video_folder_path = 'E:\Documents\GitHub\GoPro-HiLight-Reel\gopro-hilight-reel'
    seconds_pre = 5000
    seconds_post = 5000
    output_width=1920
    output_height=1080
    

    #videos = HiLightExtractor.get_video_properties(video_folder_path)
    #print(videos)
    #videos = CutCalculator.CalculateCuts(videos, seconds_pre, seconds_post)
    #MovieCreator.EditVideo(videos,video_folder_path,output_height,output_width)

    os.system('python e:\Documents\GitHub\GoPro-HiLight-Reel\gopro-hilight-reel\YouTubeUpload.py --file="e:\Documents\GitHub\GoPro-HiLight-Reel\gopro-hilight-reel\FinalEdit.mp4" \
                       --title="Volleyball Match 2019-03-24" \
                       --privacyStatus="unlisted"')

    

    


