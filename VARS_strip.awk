awk 'BEGIN {FS="\t"}; {if (length($10)) print $1,FS,$7,FS,$8,FS,$9}' vars_results_filename > output_file
