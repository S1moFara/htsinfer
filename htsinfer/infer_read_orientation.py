"""Infer read orientation from sample data."""

from typing import Union


def infer(
    file_1: str,  # pylint: disable=unused-argument
    file_2: str = None,  # pylint: disable=unused-argument
    organism: Union[int, str] = "hsapiens",  # pylint: disable=unused-argument
) -> str:
    """Infers read orientation for single- or paired-ended sequencing libraries
    in FASTQ format.

    Args:
        file_1: File path to read/first mate library.
        file_2: File path to second mate library.
        organism: Source organism of the sequencing library; either a short
            name (string, e.g., `hsapiens`) or a taxon identifier (integer,
            e.g., `9606`).

    Returns:
        LIBTYPE string according to Salmon documentation, cf.
        https://salmon.readthedocs.io/en/latest/library_type.html
    """
    # implement logic
    return "U"


    def Generate_STAR_Index(pathTempDir, ThreadN, FastaFiles, gtf):
        
        '''
        Function for the issue 26
	    The function will call a bash script for executing STAR, that will index the input files
	    The first argument is the path for the temporary directory
	    The second argument is the number of threads the user wants to use
	    The third argument is the path for the input fasta files
	    The fourth argument is the path for the annotation file (i.e. gtf file)
    
	    The function will create a variable containing the path to the resulting index folder
	    '''
    
	    import subprocess
	    import os
	    subprocess.call(['bash', './STAR_Index_generator.sh', pathTempDir, ThreadN, FastaFiles, gtf])
	    os.chdir(pathTempDir)
	    outputpath = os.path.abspath('Prepared_STAR_index')
	    return outputpath
    
	    '''
	    The function has been tested with the following input files:
	    ftp://ftp.ensembl.org/pub/release-101/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.chromosome.1.fa.gz (input fasta files)
	    ftp://ftp.ensembl.org/pub/release-101/gtf/homo_sapiens/Homo_sapiens.GRCh38.101.gtf.gz (gtf file)
	    '''
    
