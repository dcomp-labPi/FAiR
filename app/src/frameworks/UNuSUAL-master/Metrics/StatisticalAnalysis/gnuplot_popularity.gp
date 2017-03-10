
#Setting the terminal
set terminal png size 800, 600
set output outputname

#Y axis settings
set ylabel "Average Popularity" font ",14"
set yrange [0:maxy]
set ytics font ",14"

#X axis settings
set xlabel "Metric Percentils" offset -1, 0 font ",14"

# Make the x axis labels easier to read.
set xtics offset -0.5, 0 font ",13"

#set title "Unexpectedness metrics x Popularity"
set key font ",14"

# Select histogram data
set style data histogram

# Give the bars a plain fill pattern, and draw a solid line around them.
set style fill solid border

set style histogram clustered
plot for [COL=2:6] datafile using COL:xticlabels(1) title columnheader
