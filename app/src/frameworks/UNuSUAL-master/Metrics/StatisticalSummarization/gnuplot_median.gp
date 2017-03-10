#Setting the terminal
set terminal png
set output outputname

#Y axis settings
set ylabel "Median" font ",14"
set yrange [0:maxy]
set ytics font ",14"

#X axis settings
set xlabel "Metrics" font ",14"
set key font ",14"

#set title
set title "Median of each metric"
set key font ",13"

# Select histogram data
set style data histogram

# Give the bars a plain fill pattern, and draw a solid line around them.
set style fill solid border

set style histogram clustered
plot datafile using 2:xticlabels(1) notitle
