#!/bin/sh 
#SBATCH --job-name="spider"
#SBATCH -o /data/ssmith/logs/spider_%A_%a.out
#SBATCH -e /data/ssmith/logs/spider_%A_%a.err
#SBATCH -N 1
#SBATCH -n 10
#SBATCH -p highmem

plink \
--vcf /data/ssmith/scripts/drone_analysis/combined_drone_ID.g.vcf \
--recode structure \
--allow-extra-chr \
--out /data/ssmith/scripts/drone_analysis/combined_structure
