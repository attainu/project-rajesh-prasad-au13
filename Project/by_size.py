import os

def organize_by_size(path_of_file):
    path_to_organized_folder = os.path.join(path_of_file, 'Organized' )
    os.mkdir(path_to_organized_folder)

    path = os.path.join(path_to_organized_folder, "LessThan1MB")
    os.mkdir(path)

    path = os.path.join(path_to_organized_folder, "1MB_to_10MB")   
    os.mkdir(path)

    path = os.path.join(path_to_organized_folder, "GreatorThan10MB")
    os.mkdir(path)

    for entry in os.scandir(path_of_file):
        size = os.path.getsize(entry)
        try:
            if entry.is_dir():
                continue            #if we encounter a directory leave it and continue
            elif size < 1000000:    #1MB
                os.rename(path_of_file + '/' + str(entry.name), 
            path_to_organized_folder + '/LessThan1MB/' + str(entry.name))

            elif size > 1000000 and size < 10000000:    #1MB to 10MB
                os.rename(path_of_file + '/' + str(entry.name), 
            path_to_organized_folder + '/1MB_to_10MB/' + str(entry.name))
                
            elif size > 10000000:
                os.rename(path_of_file + '/' + str(entry.name), 
            path_to_organized_folder + '/GreatorThan10MB/' + str(entry.name))
                
        except:
            pass
        
    print('done')