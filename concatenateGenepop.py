#Concatnate R1 and R2 files for Genepop
from itertools import izip
#Enter files
R1_input = raw_input('Enter R1 file: ')
R2_input = raw_input('Enter R2 file: ')
R1_open = open(R1_input, 'r')
R2_open = open(R2_input, 'r')

#create an empty list to include all,including duplicates, for R1 and R2 files
R1R2_sample_pool = []
#create an empty list to store samples from R1 or R2 file
R1_samples = []
R2_samples = []

#for loop to find sample ID in R1 and R2 files, and append to lists
for R1_line in R1_open:
	if 'pop' in R1_line.lower():
		continue
	elif 'locus' in R1_line.lower():
		#save R1 locus name as a string for later use
		R1_loci = R1_line.replace('LocusNumber','R1_Locus') 
	else:
		R1_sample = R1_line.split()[0].rstrip(',')
		R1_samples.append(R1_sample)
		R1R2_sample_pool.append(R1_sample)
R1_no_loci = len(R1_loci.split())
#print (R1_samples)
#print (len(R1_samples))

for R2_line in R2_open:
	if 'pop' in R2_line.lower():
		continue
	elif 'locus' in R2_line.lower():
		#save R2 locus name as a string for later use
		R2_loci = R2_line.replace('LocusNumber','R2_Locus')
	else:
		R2_sample = R2_line.split()[0].rstrip(',')
		R2_samples.append(R2_sample)
		R1R2_sample_pool.append(R2_sample)
R2_no_loci = len(R2_loci.split())
#print (R2_samples)
#print (len(R2_samples))

#create a list to store unique samples
R1R2_uniqueSamples = []
for each_sample in R1R2_sample_pool:
	if each_sample not in R1R2_uniqueSamples:
		R1R2_uniqueSamples.append(each_sample)
#print (R1R2_uniqueSamples)
#print (len(R1R2_uniqueSamples))

#create a list to store common samples
R1R2_commonSamples = []
for one_sample in R1R2_uniqueSamples:
	if one_sample in R1_samples and one_sample in R2_samples:
		R1R2_commonSamples.append(one_sample)
#print (R1R2_commonSamples)
total_no_sample = len(R1R2_commonSamples)

#Create temporary files to write
commonSamples_R1 = open('tempFileR1.txt', 'w')
commonSamples_R2 = open('tempFileR2.txt', 'w')

R1_open = open(R1_input, 'r')
R1_temp_list = []
for R1_line in R1_open:
	if R1_line.split()[0].rstrip(',') in R1R2_commonSamples:
		R1_temp_list.append(R1_line)
R1_temp_list = sorted(R1_temp_list)
for R1_item in R1_temp_list:
	commonSamples_R1.write(R1_item)
commonSamples_R1.close()

R2_open = open(R2_input, 'r')
R2_temp_list = []
for R2_line in R2_open:
	if R2_line.split()[0].rstrip(',') in R1R2_commonSamples:
		R2_temp_list.append(R2_line)
R2_temp_list = sorted(R2_temp_list)
for R2_item in R2_temp_list:
	commonSamples_R2.write(R2_item)
commonSamples_R2.close()

#Merge R1 and R2 temporary files
with open('tempFileR1.txt', 'r') as f1, open('tempFileR2.txt', 'r') as f2, open('GenepopInput_R1R2comb.txt','w') as res:
	res.write('Genepop Input file \n')
	res.write(R1_loci.rstrip()+', '+R2_loci)
	for line1, line2 in izip(f1,f2):
		res.write(line1.rstrip())
		res.write('\t')
		line2_loci = line2[line2.find(',')+1:]#grab loci after sample id from R2
		res.write(line2_loci.strip())
		res.write('\n')

total_no_loci = R1_no_loci + R2_no_loci
print ('R1 file has %d loci' %R1_no_loci)
print ('R2 file has %d loci' %R2_no_loci)
print ('Total number of loci is %d' %total_no_loci)
print ('Total number of individuals is %d' %total_no_sample)

