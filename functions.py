#Basic File Matching:
Command: glob.glob('*.txt')

#Explanation: This command finds all files in the current directory that end with the .txt extension. It's a simple wildcard pattern match.

#Recursive Search:
Command: glob.glob('**/*.txt', recursive=True)

#Explanation: This command searches for files ending in .txt not only in the current directory but also in all its subdirectories. The recursive=True argument enables this deeper search.

#Multiple File Types:
Command: glob.glob('*.[txt,pdf]')

#Explanation: This command locates files in the current directory that have either a .txt or .pdf extension. The square brackets define a set of possible matches.

#Complex Pattern Matching:
Command: glob.glob('data/202*/sales_*.csv')

#Explanation: This command searches the "data" directory for files starting with "sales_" and ending with ".csv" within any subdirectories that start with 202 (so, 2024 or 2025, or even 2026-preview). It combines wildcard characters with specific directory and filename patterns.

With glob, you can easily automate tasks that involve working with large numbers of files. It's particularly useful for batch processing (performing the same operation on many files at once) or for situations where you need to locate files with specific characteristics.

Creating and Deleting: With os, you have the power to create new folders (or directories) using os.mkdir(), just like adding a new shelf to your library. And when a folder is no longer needed, os.rmdir() lets you remove it. Similarly, you can create empty files (think of them as blank books) with os.mknod() and delete them with os.remove().

Renaming and Moving: Need to rearrange your library? os.rename() allows you to change a file's name or even move it to a different location, just like shifting a book to a new shelf.

Navigating the File System: Lost in the stacks? os.getcwd() tells you exactly where you are in the file system (your current working directory), and os.chdir() lets you move to a different location. You can also get a list of all the "books" (files and folders) in a particular directory using os.listdir().

File Information: Like a librarian's card catalog, the os module provides functions like os.stat() to give you detailed information about a file. You can find out its size, when it was last modified,  file permissions, and more. 

Path Manipulation: File paths can get a bit messy, like long and winding library aisles. The os.path submodule helps you navigate these paths with ease. You can join different parts of a path together using os.path.join(), extract just the filename from a path with os.path.basename(), and even check if a particular path exists using os.path.exists().

The shutil module
Think of the shutil module as your helpful file management assistant. While the os module provides the basic tools for interacting with the file system, shutil takes it a step further, offering convenient shortcuts for common tasks. It's like having a librarian who can quickly copy entire bookshelves, move them to new locations, or even clear out outdated sections of the library.

Copying files and directories: Need to duplicate a file? shutil.copy() is your go-to. It's like photocopying a book. And if you need to copy an entire folder and all its contents, shutil.copytree() does the job, recursively copying the whole directory structure.

Moving files and directories: Want to relocate a file or folder? shutil.move() is like a library cart, allowing you to easily transport your files to a new destination within the file system.

Deleting files and directories: Time for some spring cleaning? shutil.rmtree() is equivalent to clearing an entire section of the library. It removes a directory and everything inside it, so use it with caution!

With shutil, you can efficiently manage your files and directories, freeing up your time to focus on the more creative aspects of your Python projects.
