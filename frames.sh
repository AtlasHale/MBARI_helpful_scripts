#! /bin/bash
cd clips
shopt -s nullglob
for f in *; do
	cd $f
	echo $f
	for video in *.mov; do
		echo $video
		mkdir "$video"_frames
		ffmpeg -i $video -vf fps=.5 "$video"_frames/"$video"%04d.png -hide_banner;
	done
	cd ..
done

