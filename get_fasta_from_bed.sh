#!/bin/sh 
#SBATCH --job-name="tabix"
#SBATCH -o /data/ssmith/logs/tabix_%A_%a.out
#SBATCH -e /data/ssmith/logs/tabix_%A_%a.err
#SBATCH --array=1
#SBATCH -N 1
#SBATCH -n 2
#"$SLURM_ARRAY_TASK_ID"

bedtools getfasta -fi /data/ssmith/c_l_genome/apis_c_l_genome.fa -bed /data/ssmith/scripts/drone_analysis/cl_genes.bed -fo /data/ssmith/scripts/drone_analysis/genes.fasta.out -name
