#!/bin/sh 
#SBATCH --job-name="amm_purity"
#SBATCH -o /data/ssmith/logs/amm_purity_%A_%a.out
#SBATCH -e /data/ssmith/logs/amm_purity_%A_%a.err
#SBATCH --array=1-6,7,9,12-15,17-26,29-32
#SBATCH -N 1
#SBATCH -n 4
#"$SLURM_ARRAY_TASK_ID"
vcftools \
--gzvcf /data/ssmith/drone_data/cldata/annotation_results/S"$SLURM_ARRAY_TASK_ID".genotyped.vcf.gz \
--out /data/ssmith/drone_data/cldata/annotation_results/S"$SLURM_ARRAY_TASK_ID" \
--positions /data/ssmith/scripts/vcftools_positions.txt \
--recode --recode-INFO-all \
--minDP 5
