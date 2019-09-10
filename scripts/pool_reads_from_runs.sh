#	Merge R1 files from run1 and run2 into one single fastq file and R2s into another single file. Example for merging R1 files from run1 and run2 given below. Run the same script for R2 reads after changing names.

#!/bin/bash
#PBS -q batch
#PBS -l nodes=1:ppn=8
#PBS -l walltime=5:00:00
#PBS -N mergefiles
#PBS -m ea
#PBS -j oe
#PBS -M badhikari@uchc.edu

cd where_your_trimmed_reads_for_runI_are/
for r1 in *run1_R1_trimmed_P.fq.gz; do
        oth=${r1/run1_R1/run2_R1}
        RR1="path_to_where_your_trimmed_reads_are_for_runI/"$r1
        RR2="path_to_where_your_trimmed_reads_are_for_runII/"$oth
        output=$(echo $r1 |cut -d "_" -f 1)
        cat $RR1 $RR2 > "path_to_where_you_want_merged_files_saved/"${output}"_Pmerged_R1.fq.gz"
        
done
