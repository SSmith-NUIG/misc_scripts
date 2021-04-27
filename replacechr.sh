#!/bin/sh 
#SBATCH --job-name="replace"
#SBATCH -o /data/ssmith/logs/replace_%A_%a.out
#SBATCH -e /data/ssmith/logs/replace_%A_%a.err
#SBATCH -N 1
#SBATCH -n 2
while IFS=$'\t' read -r -a myArray
do
	sed -i "s/${myArray[1]}/${myArray[0]}/g" cl_genes.bed	
done < /data/ssmith/scripts/drone_analysis/chr2acc


while IFS=$'\t' read -r -a myArray
do
        sed -i "s/${myArray[1]}/${myArray[0]}/g" cl_genes.bed
done < /data/ssmith/scripts/drone_analysis/mit2acc
