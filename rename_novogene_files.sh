#!/bin/sh

#this script will loop through each directory and rename all files with the extension .gz
#it keeps the S[Sample Number]_ and the read number (read 1 or 2) along with the file extension. 
#You will need to edit this part (S[0-9]_) to match whatever you wanted novogene to name your files, in my case it was simply numerical so [0-9] captures everything.


#NOTE - this command uses the perl rename program, not the built in linux-utils rename
#perl rename can be installed using anaconda. conda install -c bioconda rename


#USE -n AFTER rename TO DO A TEST RUN WHICH WILL SHOW YOU WHAT THE FILE NAME WILL BECOME
#REMOVE THIS -n WHEN YOU ARE SURE THE PATTERN IS CORRECT


dirPath=("/novogene/data")

for dir in $dirPath/*/; do
	
	firstName=$(ls $dir | sed -n 1p)
	secondName=$(ls $dir | sed -n 2p)
	rename 's{(S[0-9]_)[^.]*([12])[^.]*}{$1$2}' $dir$firstName
	rename 's{(S[0-9]_)[^.]*([12])[^.]*}{$1$2}' $dir$secondName
done
