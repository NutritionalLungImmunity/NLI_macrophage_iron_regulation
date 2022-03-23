##	Run STAR alignment. 

cd where_your_reads_to_be_aligned_are
for r1 in *_R1.fq.gz ;do
SAMPLE=$(echo $r1 | cut -d "_" -f 1)
r2=${r1/R1/R2}
echo "
#!/bin/bash
#PBS -q batch
#PBS -l nodes=1:ppn=8
#PBS -l walltime=30:00:00
#PBS -N star$(echo $r1 | cut -d "_" -f 1)
#PBS -l mem=50G
#PBS -m ea
#PBS -j oe
#PBS -e where_you_want_job_info/name.err
#PBS -o where_you_want_job_info/name.o 
#PBS -M badhikari@uchc.edu

module load STAR/2.5.3
cd where_your_reads_to_be_aligned_are
STAR --runMode alignReads --readFilesCommand zcat --genomeDir your_genome_folder_GrCh38_Genome_v96/star-genome75bp --readFilesIn "$r1" "$r2" --outSAMtype BAM SortedByCoordinate --twopassMode Basic --outSAMattrIHstart 0 --outReadsUnmapped Fastx --quantMode GeneCounts TranscriptomeSAM --outWigType wiggle --outFileNamePrefix ${SAMPLE}_

exit
">/path_where_you_want_script_saved/star_$SAMPLE.sh

qsub /path_where_you_want_script_saved/star_$SAMPLE.sh
done
echo "jobs succesfully submitted"
exit
