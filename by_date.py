import os
import datetime
import shutil


def organize_by_date(path):
    def checkFile(filename):
        d = os.path.basename(__file__)
        if filename==d:
            return True
        return False

    """getting only files and No directory"""
    all_files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))] 
    
    """discarding our current file from all_files"""
    f = [file for file in all_files if checkFile(file)==False]    

    for i in f:
        mtime = (os.stat(os.path.join(path, i)).st_atime)
        timestamp = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
        d1 = datetime.date(int(timestamp[:4]), int(timestamp[5:7]), int(timestamp[8:]))
        d2 = datetime.date(int(cur_date[:4]), int(cur_date[5:7]), int(cur_date[8:]))
        d3 = str(d2-d1)
        d4 = d3.split(",")[0]

        path_to_organized_folder = os.path.join(path, 'Organized')
        try:
            os.mkdir(path_to_organized_folder)
        except:
            pass

        if d4[-4:] == "days":
            if int(d3[:-14]) < 10:
                if not os.path.exists(os.path.join(path_to_organized_folder, "Less than 10 Days")):
                    os.mkdir(os.path.join(path_to_organized_folder, "Less than 10 Days"))
                shutil.move(os.path.join(path, i), os.path.join(path_to_organized_folder, "Less than 10 Days"))
            elif int(d3[:-14]) < 20:
                if not os.path.exists(os.path.join(path_to_organized_folder, "Less than 20 Days")):
                    os.mkdir(os.path.join(path_to_organized_folder, "Less than 20 Days"))
                shutil.move(os.path.join(path, i), os.path.join(path_to_organized_folder, "Less than 20 Days"))
            else:
                if not os.path.exists(os.path.join(path_to_organized_folder, "More than 20 Days")):
                    os.mkdir(os.path.join(path_to_organized_folder, "More than 20 Days"))
                shutil.move(os.path.join(path, i), os.path.join(path_to_organized_folder, "More than 20 Days"))
        else:
            if not os.path.exists(os.path.join(path_to_organized_folder, "Less than 10 Days")):
                os.mkdir(os.path.join(path_to_organized_folder, "Less than 10 Days"))
            shutil.move(os.path.join(path, i), os.path.join(path_to_organized_folder, "Less than 10 Days"))

    print("done")