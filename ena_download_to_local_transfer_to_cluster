mainFile=/path/to/ENA_project_TSV_file.txt

awk '{print $8'} $mainFile > /path/to/ftp_links_only.txt

fastqFtpOnly=/path/to/ftp_links_only.txt

cat $fastqFtpOnly | while read line;
do
	sshpass -p 'cluster_password' ssh -n username@cluster.address ls /path/to/folder/on/cluster/which/contains/ena_files > /path/to/ena_files/on/local/machine/ena_dir.txt

	LineIn=(${line//;/ })
	echo getting first file ${LineIn[0]}
	firstFile=$(basename ${LineIn[0]})
	File1=/path/to/folder/which/contains/ena_files/$firstFile

	if grep -q $firstFile /path/to/ena_files/on/local/machine/ena_dir.txt; then
        	echo "$File1 exists on cluster already."
	else 
		wget -P /path/to/ena_files/on/local/machine/ --tries=5 ${LineIn[0]}
		sshpass -p 'cluster_password' scp /path/to/ena_files/on/local/machine/$firstFile username@cluster.address:/path/to/folder/on/cluster/which/contains/ena_files
	fi
		
	sshpass -p 'cluster_password' ssh -n username@cluster.address ls /path/to/folder/on/cluster/which/contains/ena_files > /path/to/ena_files/on/local/machine/ena_dir.txt

	if grep -q $firstFile /path/to/ena_files/on/local/machine/ena_dir.txt; then
		echo $File1 exists on cluster after downloading
		echo deleting local file
		rm $File1
	else
		echo ${LineIn[0]} >> download_failed.txt
	fi

	if [ -f "$File1" ]; then
        	echo "$File1 exists."
	else
		echo ${LineIn[0]} >> Not_transferred.txt
	fi

	echo getting second file ${LineIn[1]}
	secondFile=$(basename ${LineIn[1]})
	File2=/path/to/folder/which/contains/ena_files/$secondFile

	if grep -q $secondFile /path/to/ena_files/on/local/machine/ena_dir.txt; then
        	echo "$File2 exists on cluster already."
	else 
        	wget -P /path/to/ena_files/on/local/machine/ --tries=5 ${LineIn[1]}
        	sshpass -p 'cluster_password' scp /path/to/ena_files/on/local/machine/$firstFile username@cluster.address:/path/to/folder/on/cluster/which/contains/ena_files
	fi

		sshpass -p 'cluster_password' ssh -n username@cluster.address ls /path/to/folder/on/cluster/which/contains/ena_files > ena_dir.txt
	
	if grep -q $secondFile /path/to/ena_files/on/local/machine/ena_dir.txt; then
        	echo $File2 exists on cluster after downloading
        	echo deleting local file
        	rm $File2
	else
        	echo ${LineIn[1]} >> download_failed.txt
	fi

	if [ -f "$File2" ]; then
        	echo "$File2 exists."
	else
        	echo ${LineIn[1]} >> Not_transferred.txt
	fi

done
