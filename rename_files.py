import os


def bulk_rename_files(folder):
    count=1
    files_list=os.listdir(folder)
    for filename in files_list:
        splitted_name=filename.split(".")
        print(splitted_name)
        extension=splitted_name[-1]
        #add your prefered keyword in place of photo
        os.rename(folder+filename, folder+"photo"+str(count)+"."+str(extension))
        count +=1

if __name__=="__main__":
    folder = r'\Images\\' #Add the name of the folder in which the files you need to rename in bulk

    bulk_rename_files(folder)