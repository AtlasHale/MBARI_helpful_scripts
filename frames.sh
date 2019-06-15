#! /bin/bash
for f in *; do
	cd $f
	for video in *; do
		mkdir "$video"_frames
		ffmpeg -i $video -vf fps=.5 "$video"_frames/"$f"%04d.png -hide_banner;
	done
done

