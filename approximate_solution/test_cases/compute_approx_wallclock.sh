# Clear previous times
> wallclock_times.txt

for file in small_graph.txt medium_graph.txt large_graph.txt non_optimal.txt
do
    echo "Timing $file..." | tee -a wallclock_times.txt
    
    total_time=0
    runs=100   # Repeat 100 times

    for i in $(seq 1 $runs)
    do
        t=$( { /usr/bin/time -p python3 ../cs412_minvertexcover_approx.py "$file" 1>/dev/null; } 2>&1 | grep real | awk '{print $2}')
        total_time=$(echo "$total_time + $t" | bc)
    done

    avg_time=$(echo "scale=4; $total_time / $runs" | bc)
    echo "Average Time: $avg_time seconds" | tee -a wallclock_times.txt
done
