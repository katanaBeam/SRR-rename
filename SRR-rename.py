'''
Script done by:
Bruno Lopes 202000210
Gonçalo Cachado 202000190
Ioana Chichirita 202000180
Rodrigo Silva 202000193
Samuel Correia 202000094
Turma: Binf21
'''
import sys
import glob
import os
import bs4
from bs4 import BeautifulSoup as bs

file_name = sys.argv[1]
file_identifier = sys.argv[2]
file_extension = sys.argv[3]
pattern = file_identifier + ('*' + file_extension)

def read_file(file_name):
    '''
    Opens the file with the name passed through the parameter file_name.
    Reads the file_name file and stores the lines in the list file_lines.
    The list file_lines is returned.
    '''
    with open(file_name) as user_file:
        file_lines = user_file.readlines()
    user_file.close()
    return(file_lines)

def XML_normalizer(file_lines):
    '''
    Gets the file lines passed through the parameter file_lines.
    Join all lines from the list file_lines and saves it in file_lines.
    bs() is used for web scraping in the format xml from file_lines and its content
    is saved in bs_content.
    All "RUN" elements are found from the xml from bs_content list and saved in experiment. 
    The list experiment is iterated for each "RUN" in run. During each iteration is appended 
    the "alias" (SRR number) and "accession" (file name) to the respective alias_list and accession_list.
    The SRR numbers in alias_list and file names in accession_list are returned. 
    '''    
    file_lines = "".join(file_lines)
    bs_content = bs(file_lines,"xml")
    experiment = bs_content.find_all("RUN")
    alias_list = []
    accession_list = []
    for run in experiment:
        alias_list.append(run.get('alias')) 
        accession_list.append(run.get('accession') + '.fastq')   
    return(alias_list, accession_list)

def find_files(pattern):
    '''
    Gets the pattern of the files through the parameter pattern.
    Searches for the all files containing the pattern (the file identifier and the file extension)
    and saves them in list files.
    The list containing all the files with a certain pattern (files) is returned
    '''
    files = glob.glob(pattern)
    return(files)

def check_sizes(files,alias_list):
    '''
    Gets all the files with a certain pattern and SRR numbers through the respective
    parameters files and alias_list.
    The files and SRR numbers amount is calculated and saved in the respective variables :
    amount_files and amount_names.
    The amount of files and amount SRR numbers are checked if they are equal. In the case
    they aren't equal a exception is raised. 
    '''
    amount_files = len(files)
    amount_names = len(alias_list)
    if(amount_files == amount_names):
        print('Found new names for all files.')
    else:
        raise Exception('There are ' + str(amount_files) + ' files but ' +
              str(amount_names) + ' new names.')

def rename_file(files,alias_list,accession_list):
    '''
    The files list, their new name list and SRR numbers list are received through the
    respective parameters: files, alias_list and accession_list.
    The files list is iterated for each file. During each iteration the index of
    file in the accession_list is saved in index, the new_name for the file is
    found in the list alias_list in position of the index.
    The extension .gz is removed from the new name and the file is renamed to
    the new name.
    '''
    for file in files:
        index = accession_list.index(file)
        old_name = file
        new_name = alias_list[index]
        new_name = new_name.replace('.gz','')
        os.rename(old_name, new_name)
        print(old_name, ' was renamed to: ', new_name)
    print('Finished renaming.')


file_lines = read_file(file_name)
new_names, old_names =  XML_normalizer(file_lines)

files = find_files(pattern)
file_error = check_sizes(files, new_names)

rename_file(files,new_names, old_names)
