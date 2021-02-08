(wgs_env) [ssmith@lugh ena]$ more retrydlena.sh 
#!/bin/sh 
#SBATCH --job-name="redlena"
#SBATCH -o /data/ssmith/logs/redlena_%A_%a.out
#SBATCH -e /data/ssmith/logs/redlena_%A_%a.err
#SBATCH -N 1
#SBATCH -n 6
#SBATCH -p MSC
mainFile=/data3/ssmith/ena/download_failed.txt
touch /data3/ssmith/ena/download_failed.temp.txt
cat $mainFile | while read line;
do
	firstFile=$(basename $line)
	wget -P /data3/ssmith/ena/ --tries=5 $line
		
	ls /data3/ssmith/ena > /data3/ssmith/ena/ena_dir.txt
	
	if grep -q $firstFile /data3/ssmith/ena/ena_dir.txt; then
        	echo $firstFile exists on lugh after downloading
	else
        	echo $line >> /data3/ssmith/ena/download_failed.temp.txt
	fi

done

rm /data3/ssmith/ena/download_failed.txt
mv /data3/ssmith/ena/download_failed.temp.txt /data3/ssmith/ena/download_failed.txt

if [ -s /data3/ssmith/ena/download_failed.txt ]
then
	sbatch /data3/ssmith/ena/retrydlena.sh
else
	echo file is empty, all downloads complete.
fi
