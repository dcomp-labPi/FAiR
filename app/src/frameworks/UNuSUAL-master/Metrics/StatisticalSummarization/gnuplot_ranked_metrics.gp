#Setting the terminal
set terminal png
set output outputname

#Y axis settings
set lmargin 10
set ylabel "Normalized Unexpectedness Score" font ",20"
set yrange [0:1]
set ytics font ",20"

#X axis settings
set xlabel "Rank" offset -1,-0.5 font ",20"
set xtics (20000, 40000, 60000, 70000)
set xtics offset -1.5,-0.2 font ",20"
set key font ",20"
set key spacing 1.5

plot datafile using 1:2 title "M1", datafile using 1:3 title "M2", datafile using 1:4 title "M3", datafile using 1:5 title "M4", datafile using 1:6 title "M5"
