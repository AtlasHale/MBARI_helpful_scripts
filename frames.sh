#! /bin/bash
cd clips
for f in *; do
    echo $f
    for video in *'.mp4'; do
        mkdir "$video"_frames
        ffmpeg -i $video -vf fps=.5 "$video"_frames/"$video"%04d.png -hide_banner;
    done
done
