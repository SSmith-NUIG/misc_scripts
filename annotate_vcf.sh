#!/bin/sh 
#SBATCH --job-name="annotate"
#SBATCH -o /data/ssmith/logs/anno_%A_%a.out
#SBATCH -e /data/ssmith/logs/anno_%A_%a.err
#SBATCH -N 1
#SBATCH -n 6
#"$SLURM_ARRAY_TASK_ID"

source activate /home/ssmith/anaconda3/envs/bcftools_env/

bcftools annotate --set-id +'%CHROM\_%POS' \
/data/ssmith/scripts/drone_analysis/combined_drone.g.vcf \
> /data/ssmith/scripts/drone_analysis/combined_drone_ID.g.vcf
