
#Setting the terminal
set terminal png size 800, 600
set output outputname

#Y axis settings
set lmargin 10
set ylabel "Mean size of Consumption History" offset -0.5,0 font ",20"
set yrange [0:maxy]
set ytics font ",20"

#X axis settings
set bmargin 5
set xlabel "Metric Percentil" offset -1,-2.2  font ",20"

# Make the x axis labels easier to read.
set xtics offset -1, -3.2 rotate by 45 font ",20"

#set title "Unexpectedness metrics x Average User History size"
set key inside
set key font ",20"
set key spacing 1.5

# Select histogram data
set style data histogram

# Give the bars a plain fill pattern, and draw a solid line around them.
set style fill solid border

set style histogram clustered
plot for [COL=2:6] datafile using COL:xticlabels(1) title columnheader
