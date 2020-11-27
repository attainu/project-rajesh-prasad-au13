import os
from pathlib import Path

def organize_by_File_extension(path_of_file):
    DIRECTORIES = { 
        "HTML": [".html5", ".html", ".htm", ".xhtml"], 
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
                ".heif", ".psd"], 
        "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
                ".qt", ".mpg", ".mpeg", ".3gp"], 
        "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
                    ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
                    ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
                    "pptx"], 
        "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
                    ".dmg", ".rar", ".xar", ".zip"], 
        "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
                ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
        "PLAINTEXT": [".txt", ".in", ".out"], 
        "PDF": [".pdf"], 
        "PYTHON": [".py"], 
        "XML": [".xml"], 
        "EXE": [".exe"], 
        "SHELL": [".sh"] 
    } 

    FILE_FORMATS = {file_format: directory 
                    for directory, file_formats in DIRECTORIES.items() 
                    for file_format in file_formats} 

    for entry in os.scandir(path_of_file):         
        if entry.is_dir(): 
            continue            #if we encounter a directory leave it and continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS: 
            directory_path = Path(FILE_FORMATS[file_format])
            path1 = os.path.join(path_of_file, 'Organized')
            path2 = os.path.join(path1, directory_path)
            
            try:
                os.mkdir(path1) 
            except:
                pass
            try:
                os.mkdir(path2) 
            except:
                pass
            os.rename(path_of_file + '/' + str(entry.name), 
            path1 + '/' + str(directory_path) + '/' + str(entry.name))

        else:
            path1 = os.path.join(path_of_file, 'Organized')
            path2 = os.path.join(path1, 'Other_Files')
            
            try:
                os.mkdir(path1) 
            except:
                pass
            try:
                os.mkdir(path2) 
            except:
                pass
            os.rename(path_of_file + '/' + str(entry.name), 
            path2 + '/' + str(entry.name))

    print('done')