
#Unzip files

#!/bin/bash
#PBS -q batch
#PBS -l nodes=1:ppn=8
#PBS -l walltime=5:00:00
#PBS -N control
#PBS -m ea
#PBS -j oe
#PBS -M c-adhikb@jax.org
cd /your_directory_where_zipped/alignment_files_are/
gunzip *.gz
