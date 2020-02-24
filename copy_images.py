import os
import subprocess
import re
from datetime import datetime


def run_shell_cmd(command):
    """Run shell/bash commands passed as a string using subprocess module."""
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output = process.stdout.read()

    return output.decode('utf-8')


def copy_images(root_path):
    """Copy images.

    Will be done from images directory of subdirectories to images directory
    in the src directory
    """
    subdir_list = []

    # walk through the src directory to find subdirectories named 'images'
    # and copy contents to the 'images' directory in the duplicate src directory
    for root, dirs, files in os.walk(root_path):
        if 'images' in dirs:
            subdir_list.append(root)

    for each in subdir_list:
        if each != root_path:
            print(each)
            run_shell_cmd("cp -R "+each+"/images"+" "+root_path+"/images")

# def extract_header_string():
#     """Extract the latest release's version number and date from CHANGES.md."""
#     # released_versions = []
#     # title = ""
#     # run_shell_cmd("cp ../mkdocs.yml src_copy/mkdocs.yml")

#     with open('src_copy/src/mkdocs.yml', 'r') as file:
#         data = file.readlines()

#     print(data[0])
#     header_string = data[0].split(": ")[1]
#     title = " ".join(header_string.split()[0:4])
#     version_number = header_string.split()[-1]
#     build_date = datetime.today().strftime('%Y-%m-%d')
#     header = " ".join([title, version_number, build_date])
#     print(title)
#     print(version_number)
#     print(build_date)
#     print(header)


if __name__ == '__main__':

    duplicated_src_dir_path = 'src_copy/src'

    # # Step 1: make a copy of the src directory in the current directory
    # copy_src()
    
    # # debug statement 1
    # subprocess.call(["ls", "-a"], shell=True) # src_copy directory successfully created
    
    # # debug statement 2
    # # verify contents of the duplicated src directory 
    # subprocess.call("ls -a ./src_copy/src", shell=True)

    # # Step 2: copy BIDS_logo to images directory of the src_copy directory
    # copy_bids_logo()

    # Step 3: copy images from subdirectories of src_copy directory
    copy_images(duplicated_src_dir_path)
    subprocess.call("mv src_copy/src/images/images/* src_copy/src/images/", shell=True)
    
    # debug statement 3
    # verify if the images from sub dirs of src have been copied 
    # subprocess.call("ls -a ./src_copy/src/images", shell=True)

    # # Step 4: extract the latest version number and date
    extract_header_string()
    # add_header()

    # edit_titlepage()

    # modify_changelog()

    # # Step 5: remove all internal links
    # remove_internal_links(duplicated_src_dir_path, 'cross')
    # remove_internal_links(duplicated_src_dir_path, 'same')