import argparse
from by_size import organize_by_size
from by_extension import organize_by_File_extension
from by_date import organize_by_date

def main():  
    parser = argparse.ArgumentParser()

    """
    asking for the path of the directory if not provided by user then it will take current directory as default
    """
    parser.add_argument('--path', default = './', help = 'Which directory to organize?')

    """
    asking for the oranize depends like ext or size or date
    """
    parser.add_argument('--o', default = 'extension', help = 'Organize by?', 
                        choices = ['extension', 'size', 'date'])

    args = parser.parse_args()
    path = args.path
    organizeBy = args.o

    if organizeBy =="extension":
        organize_by_File_extension(path)
    elif organizeBy =="size":
        organize_by_size(path)
    elif organizeBy =="date":
        organize_by_date(path)