# Parallel-Concatenate-2-Genepop-Files
Parallel concatenate two large Genepop input files for population genetic analysis

1. Combine two Genepop input files that have different set of loci but have identical individuals (or partially identical). 
2. The program will find and output the common individuals (based on sample id) in two Structure files. For example, if one file has sample id A, B, C, D, E, and the other has B, C, D, E, F, the concatenated file will have sample B, C, D, and E. Sample A and F will be excluded.
3. All the loci from two Genepop files will be concatenated.
4. Your input Genepop files must include one head line and has a 'pop' in anywhere of the line.
5. The second line should be locus names. Each locus name must contain 'LocusNumber'. If not, either edit your Genepop files or edit the script Line 21 and 35 accordingly. 
6. By default, the locus name ('LocusNumber') of first and second files will be replaced with 'R1_Locus' and 'R2_Locus', respectively. If locus names have locus number in the end of 'LocusNumber', the number will be retained. (e.g., LocusNumber101 -> R1_Locus101 or R2_Locus101)
7. It doesn't matter if there are 'pop' characters to divide the groups. The final ouput will not separate your samples by population. You need to manually add 'pop' for your populations in final output files.

To run the script,

1. Download 'concatenateGenepop.py' file and save it under the folder that has your Genepop files. 
2. Open terminal or command prompt and change path to the folder (using 'cd your_path_to_folder').
3. Then enter 'python concatenateGenepop.py' to execute the script.
4. It will then ask you to enter your Genepop file names (R1 and R2). And hit enter.
5. The program will start to concatenate two files and print out numbers of loci and individuals in the console.
