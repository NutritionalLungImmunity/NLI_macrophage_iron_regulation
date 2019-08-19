### Python 2.7.16 

os.chdir("/Users/banditaadhikari/Desktop/backup_to_googleDrive/Aspergillus/may_analysis_trimmomatic/run1run2_combined")
cwd = os.getcwd()

files = sorted([file for file in os.listdir(cwd) if file.endswith('.tab')])

filename = files[0].strip("_STARout75_may_ReadsPerGene.out.tab")
filename

dff = pd.read_csv(files[0], sep = "\t", header = None)[4:]

filename = files[0].strip("_STARout75_may_ReadsPerGene.out.tab")
coll = ["geneid", "both", "rr", filename] # you want column 4 coz this is stranded
dff.columns = coll
drt = dff.iloc[:,[0, 3]]
drtt = drt.set_index("geneid")

for file in files[1:]:
    name = file.strip("_STARout75_may_ReadsPerGene.out.tab")
    dfr = pd.read_csv(file, sep = "\t", header = None)[4:]
    lcoll = ["geneid", "both", "rr", name]
    dfr.columns = lcoll
    ldrt = dfr.iloc[:,[0, 3]]
    ldrtt = ldrt.set_index('geneid')
    drtt = drtt.merge(ldrtt,on='geneid')
drtt.to_csv("/Users/banditaadhikari/Desktop/backup_to_googleDrive/Aspergillus/may_analysis_trimmomatic/run1run2_combined/countmatrix_col4.csv", header=True, index=True, sep='\t')
