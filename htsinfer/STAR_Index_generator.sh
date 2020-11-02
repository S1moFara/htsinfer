clear
cd $1
STAR --runThreadN $2 --runMode genomeGenerate --genomeDir Prepared_STAR_index --genomeFastaFiles $3 --sjdbGTFfile $4
clear
echo "Done!"
