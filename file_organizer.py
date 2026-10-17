import os
import ctypes
import shutil
def main():
    
    while True:
        folder_name=input("Enter a folder Path:") 
        folder_path=find_folder(folder_name)
        if folder_path is  None:
            print("Folder NOt Found\nEnter a Valid Folder")
            continue
        print("Folder Founded:",folder_path,"\n")
        print("Please verify this is The Correct Folder Before Continue\n")
        list_files=os.listdir(folder_path)
        for files in list_files:
            print(f"{files}",end=",  ")
        print("\n\nType Yes To Proceede\n")
        proceed=input("Yes or No :  ").strip().lower()
        if proceed=="yes":
            create_match_display(folder_path,list_files)
            break
        else:
            print("\nLet's Choose Another Folder\n")
        
        
def create_match_display(folder_path,list_files):
    for r in ["Document","Image","Python","Web","Other"]:
        folder=os.path.join(folder_path,r)
        os.makedirs(folder,exist_ok=True)
    for sfile in list_files:
        source=os.path.join(folder_path,sfile)
        if os.path.isdir(source):
            continue
            # skip sub folder
        name,extension=os.path.splitext(sfile)
        extension=extension.lower()
        match_case(folder_path,extension,sfile,source)
                
    for dirpath,dirname,file_name in os.walk(folder_path):
        print("directory path:",dirpath)
        print("directory name:",dirname)
        print("File name:",file_name)
        print()
def find_folder(folder_name):
        drives=ctypes.windll.kernel32.GetLogicalDrives()
        # window  return the number whose binary bits imdicates which drive letter exists
        # example A:, C:,and D:exist their corrospoinding bit are set
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
            if drives & 1:
                
                drives_path=f"{letter}:/"
                # print(drives_path)
                # it become c:\ or d:\   
                for dir_path,dir_name,file_name in os.walk(drives_path,onerror=lambda error:None)                                                                                       :
                    if os.path.basename(dir_path).lower()==folder_name.lower():
                        # print(os.path.basename("D:/test_folder")) = test_folder
                        # print(os.path.basename("D:/test_folder/Image"))=Image
                        
                        return dir_path
            drives>>=1
        return None

def match_case(folder_path,extension,sfile,source):
    match extension:
        case ".txt"|".pdf"|".docx"|".doc"|".pptx"|".csv"|".ppt"|".xls"|".xlsx"|".rtf"|".odt":
           
            destination=os.path.join(folder_path,"Document",sfile)
            shutil.move(source,destination)
        case ".jpg"|".jpeg"|".png"|".gif" |".svg"|".ico"|".webp"|".bmp":
           
            destination=os.path.join(folder_path,"Image",sfile)
            shutil.move(source,destination)
        case ".py"|".pyw"|".pyc":
           
            destination=os.path.join(folder_path,"Python",sfile)
            shutil.move(source,destination)
            
        case ".js"|".html"|".css"|".json"|".ts"|".jsx"|".php"|".xml"|".tsx":
           
            destination=os.path.join(folder_path,"Web",sfile)
            shutil.move(source,destination)
        case _:
            destination=os.path.join(folder_path,"Other",sfile)
            shutil.move(source,destination)
            
if __name__=="__main__":
    main()