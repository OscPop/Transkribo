from __future__ import unicode_literals
import yt_dlp
import ffmpeg
import sys
import argparse
import os


def download_from_url(url, preferred_codec):
    ydl.download([url])
    stream = ffmpeg.input('output.m4a')
    #stream = ffmpeg.output(stream, 'output.mp3')
    stream = ffmpeg.output(stream, f"output.{preferred_codec}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download audio from a YouTube video. Input your\
                                     URL in quotes.", 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     epilog="Only 1 video at a time...")
    parser.add_argument("url", metavar="YouTube URL", action="store")
    parser.add_argument("-o", "--output", help="Format of output, either wav or mp3",
                        choices=["wav", "mp3"], default="mp3")
    parser.add_argument("-f", "--filename", help="Name of audio file to be saved (excluding extension)", default="output")
    args = parser.parse_args()

    file_name = args.filename
    preferred_codec = args.output

    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join("Data",file_name+".%(ext)s"),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': preferred_codec,
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        download_from_url(args.url, preferred_codec)