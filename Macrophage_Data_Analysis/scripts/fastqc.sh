#	Run FastQC on Orginal files. 

#!/bin/bash
#PBS -q batch
#PBS -l nodes=1:ppn=8
#PBS -l walltime=30:00:00
#PBS -N fastqc
#PBS -l mem=50G
#PBS -m ea
#PBS -j oe
#PBS -M c-adhikb@jax.org
cd /where_your_unzipped_fastq_files_are/
module load fastqc/0.11.5
for f in $(find . -name *.fastq); do fastqc $f; done
