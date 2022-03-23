#	STAR: Index the reference genome. 

#!/bin/bash
#PBS -q batch 
#PBS -l nodes=1:ppn=8
#PBS -l walltime=15:00:00
#PBS -N starindexhg75
#PBS -m ea
#PBS -j oe
#PBS -M badhikari@uchc.edu

module load STAR/2.5.3
cd your_ref_genome_folder_GrCh38_Genome_v96
STAR --runMode genomeGenerate --genomeDir star-genome75bp --genomeFastaFiles Homo_sapiens.GRCh38.dna.primary_assembly.fa --sjdbGTFfile Homo_sapiens.GRCh38.96.gtf --sjdbOverhang 75
