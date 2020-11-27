#
# **Junk File Organizer with Python**

As a lazy programmer my desktop is full of files (Junk Files). Due to the large number of files, it is a daunting task to sit and organize each file. To make that task easy the below Python script comes handy and all the files are organized in a well-manner within seconds.

**Libraries i used:**

- os
- pathlib
- shutil
- datetime
- argparse

**Requirements:**

Python installed on your machine

## **Main functionality of this code**

- Organize files by extension
- Organize files by size
- Organize files by date modified

## **How to use this :**

Firstly ,open your command terminal or git bash terminal and then

-
### **To Organize files based on extensions use below command**
- python runme.py --path &quot;C:\Users\Rajesh\Pictures\sample\_7&quot; --o extension

### **To Organize files based on size use below command**
- python runme.py --path &quot;C:\Users\Rajesh\Pictures\sample\_7&quot; --o size

### **To Organize files based on date modified use below command**
- python runme.py --path &quot;C:\Users\Rajesh\Pictures\sample\_7&quot; --o date

#### **1. Organize by extension**

This option lets users to organize their files by their file extension in a given folder, a folder named &#39;Organized will be created and inside that folders will be created according to file extensions and finally all files will be moved to those folders.

#### **2. Organize by size**

This option lets users organize their files by their file size in a given folder, a folder named &#39;Organized will be created and inside that 3 folders will be created namely Less\_than\_1MB, 1MB\_to\_50MB and Greater\_than\_50MB.Finally all files will be moved to those folders.

### **3. Organize by Last used/accessed date**

This option lets users organize their files by their file&#39;s last used time, a folder named &#39;Organized will be created and inside that 3 folders will be created namely Less\_than\_10Days, Less\_than\_20Days and Greater\_than\_20Days.Finally all files will be moved to those folders.

**Future Improvement:**

Command Line is difficult to understand for beginners,so we can design a user-friendly ui for our program such that a normal user can easily interact with it. We can add more ways to organize our files viz.alphabetical order, date created,etc.We can add an option to delete files which users think of as junk.

**FAQ**

What if you don&#39;t provide arguments (path or way to organize the files) ?

- if the user does not provide the argument then the program will by default perform the operation on the current directory and it will organize the files by extensions.