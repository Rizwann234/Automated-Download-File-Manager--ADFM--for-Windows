# --------------------------------------------------------------
#      Python Automated File Download Management System
# --------------------------------------------------------------
#                         Version 0.1 
#
# This basic software has been designed with the purpose of 
# organising files downloaded onto your system, into organised 
# folders.
# --------------------------------------------------------------

import os
import sys
import shutil


def main() :

    downloads_directory = input(" please specify the directory of your downloads folder, \n please make sure this does not end with a '/' \n Type directory here : ")

    # Automating the process of making folders
    folders = ['Word Documents', 'PDFs', 'zip', 'Spreadsheets', 'Installers']
        
    for folder in folders :
        os.mkdir(f"{downloads_directory}/{folder}")

    # File sorting code using os and shutil

    for f in os.listdir(downloads_directory) :
        file_extension = os.path.splitext(f'{downloads_directory}/{f}')[1]
    
        if file_extension.lower() == '.docx' :
            shutil.move(f"{downloads_directory}/{f}", f"{downloads_directory}/Word Documents/{f}")

        elif file_extension.lower() == '.pdf' :
            shutil.move(f"{downloads_directory}/{f}", f"{downloads_directory}/PDFs/{f}")

        elif file_extension.lower() == '.zip' :
            shutil.move(f"{downloads_directory}/{f}", f"{downloads_directory}/zip/{f}")

        elif file_extension.lower() in {'.xlsx', '.csv', '.xml', 'xltx'} :
            shutil.move(f"{downloads_directory}/{f}", f"{downloads_directory}/Spreadsheets/{f}")
            
        elif file_extension.lower() in {'.exe', '.msi'} :
            shutil.move(f"{downloads_directory}/{f}", f"{downloads_directory}/Installers/{f}")

if __name__ == '__main__' :
    main()