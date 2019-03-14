import HiLightExtractor, CutCalculator, MovieCreator

if __name__ == '__main__':
    # CONFIG
    video_folder_path = 'E:\Documents\GitHub\GoPro-HiLight-Reel\gopro-hilight-reel'
    seconds_pre = 5000
    seconds_post = 5000
    

    videos = HiLightExtractor.get_video_properties(video_folder_path)
    videos = CutCalculator.CalculateCuts(videos, seconds_pre, seconds_post)
    MovieCreator.EditVideo(videos,video_folder_path)
    #UploadToYouTube()

    

    


