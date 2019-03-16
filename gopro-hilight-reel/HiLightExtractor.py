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
    cuts: []

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
            yield GoProVideo(file_name, file_path, duration, hilights, None)

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

def get_video_properties(video_folder_path):
    videos  = []
    for video in get_files(video_folder_path, file_type='.MP4'):
        videos.append(video)
    return videos