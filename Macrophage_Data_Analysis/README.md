Files are arranged as follows in this repository. Any files that are mentioned in the documentation but are not present in this repository are not public yet. 

```bash
├── data 
│   ├── design
│     ├──rseq_counts.csv
│     ├── samples.txt
├── scripts
│   ├──unzip.sh
│   ├──fastqc.sh
│   ├──trimmomatic.sh
│   ├──pool_reads_from_runs.sh
│   ├──star_index_genome.sh
│   ├──star_align.sh
│   ├──run_qualimap.sh
│   ├──mergecounts_col4.py
│   ├──dse2_pairwise_control_treatment.Rmd
├── README.md
├── LICENSE.md
└── .gitignore
```

Below are the steps used for macrophage data analysis. 

1. Unzip fastq files (/scripts/unzip.sh)
2. Run FastQC on files to check the quality on raw fastq files.(/scripts/fastqc.sh)
3. Use FastQC_Manual.pdf to check the quality of the reads. (/FastQC_Manual.pdf)
4. Use Trimmomatic to trim adapters.(/scripts/trimmomatic.sh)
5. Run FastQC on trimmed files. (Step 3 and 4 need to be repeated until reads look good). 
6. Use STAR to align the reads onto the reference genome(GrCh38v96, downloaded from NCBI). 
  a. Index the reference genome. (/scripts/star_index_genome.sh)
  b. Run STAR aligner.(/scripts/star_align.sh)
6. Run Qualimap to check the quality of the alignment.(/scripts/run_qualimap.sh)
7. Make a count matrix combining appropriate column (column 4 in our case due to the strandedness of the data) from readspergene.out.tab files. (/scripts/mergecounts_col4.py)
8. Run differential expression analysis. We have used DEseq2 for this analysis. We have also used ERCC spike-in controls as internal controls for RNA-seq. We did not use it in our analysis with DEseq2 though. R code resides here "dse2_pairwise_control_treatment.Rmd". Code uses this design file - "sample4h.txt".(/scripts/dse2_pairwise_control_treatment.Rmd)
