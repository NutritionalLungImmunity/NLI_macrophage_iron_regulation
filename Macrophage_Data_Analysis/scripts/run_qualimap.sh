# Ran qualimap to check  the alignment of the reads. 

#!/bin/bash
#PBS -q batch
#PBS -l nodes=1:ppn=8
#PBS -l walltime=72:00:00
#PBS -N qualimaprun1run2
#PBS -l mem=50G 
#PBS -m ea
#PBS -j oe
#PBS -M badhikari@uchc.edu

cd /where_your_aligned_reads_are/

module load qualimap/2.2.1

for i in *Aligned.sortedByCoord.out.bam; do
qualimap 
rnaseq --java-mem-size=50G 
-bam /where_your_aligned_reads_are/$i 
--sequencing-protocol strand-specific-reverse  
-gtf your_genome_folder_GrCh38_Genome_v96/Homo_sapiens.GRCh38.96.gtf 
-oc /where_you_want_output_saved/qualimap_mergedrun1run2/$i.counts 
-outdir /where_you_want_output_saved/qualimap_mergedrun1run2 
-pe -outfile $i.qualimapreport.pdf

done
