#!/bin/sh 
#SBATCH --job-name="angsd"
#SBATCH -o /data/ssmith/logs/angsd_%A_%a.out
#SBATCH -e /data/ssmith/logs/angsd_%A_%a.err
#SBATCH -N 4
#SBATCH -n 8
source activate wgs_env

angsd -out GenotypeLikelihoods -bam /data/ssmith/scripts/drone_analysis/bamfile_list.txt \
-GL 1 \
-doGlf 2 \
-doMaf 1 \
-doMajorMinor 1 \
-nThreads 8 \
-SNP_pval 1e-6
