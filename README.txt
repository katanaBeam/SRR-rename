COMMAND TO RUN SCRIPT: py SRR-rename.py [SraExperimentPackage.XML] [FileIdentifier] [FileExtension]

PARAMENTERS:
[SraExperimentPackage.XML] : .XML file of the SRA experiment
[FileIdentifier]: characters that identify the files to rename
[FileExtension]: the extension of the files to rename

REQUISITES:
1-The command to run the script should be used in the shell and on the directory that the script is located
2-The script SRR-rename.py should be in the same directory as the [SraExperimentPackage.XML] and the files to rename
3-[SraExperimentPackage.XML] should have the TAG 'RUN' and its attributes 'alias' and 'accession'
EXAMPLE:
<RUN accession="SRR15599038" alias="WA_Jefferson_Duckabush_ADL5013_R1_.fastq.gz">
4-The files to rename must have the name equal to the attribute 'accession' in the [SraExperimentPackage.XML]
EXAMPLE:
accession="SRR15599038"
file to rename = "SRR15599038.fastq"
5-The number of files to rename and the number of 'accession' and 'alias' must be equal, or else a exception is raised
EXAMPLE:
Exception: There are 0 files but 87 new names.

Result:
Files name change.