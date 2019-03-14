from dataclasses import dataclass, field
from datetime import timedelta
from moviepy.editor import *
import os
import struct


@dataclass
class GoProVideo():
    name : str
    path: str
    duration: int
    hilight_markers: []

@dataclass
class Atom:
    name: str
    size: int

def get_files(folder, file_type):
    for file_name in sorted(os.listdir(folder)):
        if file_name.lower().endswith(file_type.lower()):
            file_path = os.path.join(folder, file_name)
            clip=VideoFileClip(file_path)
            duration=int(clip.duration*1000)
            clip.close()
            hilights = []
            for millisecond_marker in get_hilights(file_path):
                hilights.append(millisecond_marker)
            yield GoProVideo(file_name, file_path, duration, hilights)

def get_hilights(filename):
    with open(filename, 'rb') as f:
        for atom in yield_box(f):
            if atom.name == b'moov':
                for atom in yield_box(f):
                    if atom.name == b'udta':
                        for atom in yield_box(f):
                            if atom.name == b'HMMT':
                                nb_hilights = int.from_bytes(f.read(4), byteorder='big')
                                if nb_hilights:
                                    return struct.unpack('>' + 'i' * nb_hilights, f.read(4 * nb_hilights))
                                else:
                                    return ()
                            else:
                                move_stream_to(f, atom.size)
                    else:
                        move_stream_to(f, atom.size)
            else:
                move_stream_to(f, atom.size)
    return ()

def yield_box(stream):
    while 1:
        size = stream.read(4)
        if len(size) < 4 : break
        n = int(struct.unpack('>I', size)[0])
        name = stream.read(4)
        yield Atom(name, n-8)

def move_stream_to(stream, n):
    chunks = 64 * (1 << 20)
    while n > chunks:
        stream.seek(chunks, 1)
        n -= chunks
    stream.seek(n, 1)

if __name__ == '__main__':
    # CONFIG
    video_path = 'E:\Documents\GitHub\GoPro-HiLight-Reel\gopro-hilight-reel'
    seconds_pre = 5000
    seconds_post = 5000
    
    GoProVideos = []
    clips = []

    # Return hilight markers for each video
    for video in get_files(video_path, file_type='.MP4'):
        GoProVideos.append(video)
    
        # Edit the clip
        for hilight in video.hilight_markers:

            # Error checking
            
            post = seconds_post
            if hilight+post > video.duration:
                post = video.duration-hilight-500 # add 500ms of extra buffer
            print('hilight', hilight)
            print('post', post)   
            print('duration',video.duration)
            vid = VideoFileClip(video.path).subclip((hilight-seconds_pre)/1000,(hilight+post)/1000)
            clips.append(vid)
        

    #print(GoProVideos)
    final_video = concatenate_videoclips(clips)
    final_video.write_videofile('E:\Documents\GitHub\GoPro-HiLight-Reel\gopro-hilight-reel\edit'+video.name+'.mp4',fps=60)

    


