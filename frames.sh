#! /bin/bash
shopt -s nullglob
cd $1
mkdir all_frames
for concept in *; do
	echo $concept
	cd $concept
	for tape in *; do
		echo $tape
		cd $tape
		for video in *.mov; do
			temp=${video%.*}
			ffmpeg -y -re -i $video -vf fps=10 ../../all_frames/"$concept"_"$temp"%03d.png -hide_banner;
		done
		cd ..
	done
	cd ..
done

