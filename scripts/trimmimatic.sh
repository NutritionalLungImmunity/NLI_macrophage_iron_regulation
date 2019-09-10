#	Trim files as necessary using trimmomatic. Assuming you have two different runs in separate folders. Below is example for run1, do the same for run 2. 
#Trimmomatic adapter files uploaded in data folder.

cd /where_your_fastqc_files_are/

for r1 in M*_R1_001.fastq.gz ;do
SAMPLE=$(echo $r1 | cut -d "_" -f 1)
sname=${SAMPLE}_run1
r2=${r1/R1/R2}
echo "
#!/bin/bash
#PBS -q batch
#PBS -l nodes=1:ppn=1
#PBS -l walltime=8:00:00
#PBS -N name
#PBS -l mem=25G
#PBS -m ea
#PBS -j oe
#PBS -e /where_you_want_your_output_info_sent/file_name.err
#PBS -o /where_you_want_your_output_info_sent/file_name.o 
#PBS -M youremail

module load java/1.8.0

cd /runI
  java -jar 
  where_your_java_source_code_exists/trimmomatic.jar 
  PE -trimlog runI/trimrun1_${SAMPLE}.log 
  where_your_fastqc_files_are/$r1 
  where_your_fastqc_files_are/$r2  
  runI/${sname}_R1_trimmed_P.fq.gz 
  runI/${sname}_R1_trimmed_U.fq.gz 
  runI/${sname}_R2_trimmed_P.fq.gz 
  runI/${sname}_R2_trimmed_U.fq.gz 
  LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 ILLUMINACLIP:data/trimmomatic_PE_adapters.fa:2:30:10

exit
">runI/trimrun1_$SAMPLE.sh

qsub runI/trimrun1_$SAMPLE.sh

done
echo "jobs succesfully submitted"
exit
