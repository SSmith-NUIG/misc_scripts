
#!/bin/sh 
#SBATCH --job-name="dlena"
#SBATCH -o /data/ssmith/logs/dlena_%A_%a.out
#SBATCH -e /data/ssmith/logs/dlena_%A_%a.err
#SBATCH -p MSC
#SBATCH -N 1
#SBATCH -n 16

mainFile=/data3/ssmith/ena/americanbees_pooled_ena.txt

awk '{print $8'} $mainFile > /data3/ssmith/ena/ftp_only.txt
tail -n +2 /data3/ssmith/ena/ftp_only.txt > /data3/ssmith/ena/ftp_only.txt.tmp && mv /data3/ssmith/ena/
ftp_only.txt.tmp /data3/ssmith/ena/ftp_only.txt

fastqFtpOnly=/data3/ssmith/ena/ftp_only.txt
rm /data3/ssmith/ena/download_failed.txt
cat $fastqFtpOnly | while read line;
do
	LineIn=(${line//;/ })
	echo getting first file ${LineIn[0]}
	firstFile=$(basename ${LineIn[0]})
	ls /data3/ssmith/ena/ > ena_dir.txt
	if grep -q $firstFile /data3/ssmith/ena/ena_dir.txt; then
        	echo "$firstFile exists on lugh already."
	else 
		wget -P /data3/ssmith/ena/ --tries=5 ${LineIn[0]}
	fi
		
	ls /data3/ssmith/ena > /data3/ssmith/ena/ena_dir.txt

	if grep -q $firstFile /data3/ssmith/ena/ena_dir.txt; then
		echo $firstFile exists on lugh after downloading
	else
		echo ${LineIn[0]} >> /data3/ssmith/ena/download_failed.txt
	fi

	echo getting second file ${LineIn[1]}
	secondFile=$(basename ${LineIn[1]})

	if grep -q $secondFile /data3/ssmith/ena/ena_dir.txt; then
        	echo "$secondFile exists on lugh already."
	else 
        	wget -P /data3/ssmith/ena/ --tries=5 ${LineIn[1]}
	fi

	ls /data3/ssmith/ena > /data3/ssmith/ena/ena_dir.txt
	
	if grep -q $secondFile /data3/ssmith/ena/ena_dir.txt; then
        	echo $secondFile exists on lugh after downloading
	else
        	echo ${LineIn[1]} >> /data3/ssmith/ena/download_failed.txt
	fi

done
