#!/bin/sh 
#SBATCH --job-name="smtls"
#SBATCH -o /data/ssmith/logs/smtls_%A_%a.out
#SBATCH -e /data/ssmith/logs/smtls_%A_%a.err
#SBATCH --array=1-6,7,9,12-15,17-26,29-32
#SBATCH -N 1
#SBATCH -n 4
#"$SLURM_ARRAY_TASK_ID"
gatk GenotypeGVCFs \
-R /data/ssmith/c_l_genome/apis_c_l_genome.fa \
-V /data/ssmith/drone_data/cldata/annotation_results/S"$SLURM_ARRAY_TASK_ID".vcf.gz \
-O /data/ssmith/drone_data/cldata/annotation_results/S"$SLURM_ARRAY_TASK_ID".genotyped.vcf.gz
