import os
def rename_files():
    # get the file name from folder
    file_list = os.listdir(r"H:\DOWNLOADS\alphabet")
    #print(file_list)
    saved_path = os.getcwd()
    print("current working directory is " + saved_path)
    os.chdir(r"H:\DOWNLOADS\alphabet")
    # for each file ,rename filename
    for file_name in file_list:
        print("Old Name -" +file_name)
        print("New Name -" +file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
