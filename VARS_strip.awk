awk 'BEGIN {FS="\t"}; {if (length($1)) print $1,FS,$2,FS,$3,FS,$4,FS,$5}' vars_results_filename > output_file
