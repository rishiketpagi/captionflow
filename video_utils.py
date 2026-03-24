from moviepy import VideoFileClip
import os

def extract_audio_from_video(video_path, audio_path):
    clip = VideoFileClip(video_path)
    
    if clip.audio is None:
        raise Exception("No audio track found in the uploaded video.")

    clip.audio.write_audiofile(audio_path, logger=None)
    clip.close()

    return audio_path