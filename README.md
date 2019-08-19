# Macrophage_Data_Analysis

"Scripts" file contains detailed steps for macrophage data analysis. 

1. Unzip fastq files.
2. Run FastQC on files to check the quality on raw fastq files. Use FastQC_Manual.pdf to check the quality of the reads. 
3. Use Trimmomatic to trim adapters.
4. Run FastQC on trimmed files. (Step 3 and 4 need to be repeated until reads look good). 
5. Use STAR to align the reads onto the reference genome(GrCh38v96). 
  a. Index the reference genome. 
  b. Run STAR aligner.
6. Run Qualimap to check the quality of the alignment.
7. Make a count matrix combining appropriate column (column 4 in our case due to the strandedness of the data) from readspergene.out.tab files. Use this python code - "mergecounts_col4.py".
8. Run differential expression analysis. We have used DEseq2 for this analysis. We have also used ERCC spike-in controls as internal controls for RNA-seq. We did not use it in our analysis with DEseq2 though. R code resides here "dse2_pairwise_control_treatment.Rmd". Code uses this design file - "sample4h.txt".
