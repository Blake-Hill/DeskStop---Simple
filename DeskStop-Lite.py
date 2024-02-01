import os
import sys
from datetime import date

def main():
    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    documents = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Documents")

    performClean(desktop, documents)
    
'''
This function takes desktopPath a path to the users desktop and documentPath a path to the users documents
It creates a new folder named after the day the program was run, if that folder already exists it adds to it
Finally it sorts all files from desktop path into the appropriate subfolders
'''
def performClean(desktopPath : str, documentPath: str):
    files = os.listdir(desktopPath)
    today = date.today()
    today = today.strftime("%d%b%Y")
    targetDir = f"{documentPath}\\{today}"

    #create todays folder and subfolder to sort files into
    try:
        os.mkdir(f"{documentPath}\\{today}")
        os.mkdir(f"{targetDir}\\office")
        os.mkdir(f"{targetDir}\\office\\excel")
        os.mkdir(f"{targetDir}\\office\\word")
        os.mkdir(f"{targetDir}\\office\\powerpoint")
        os.mkdir(f"{targetDir}\\photos")
        os.mkdir(f"{targetDir}\\videos")
        os.mkdir(f"{targetDir}\\text")
        os.mkdir(f"{targetDir}\\audio")
        os.mkdir(f"{targetDir}\\other")
    except FileExistsError:
        pass

    for file in files:
        #sort based on extension of file
        extension = file.split(".")[-1]
        match extension:
            case "docx":
                    os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\office\\word\\{file}")
            case "doc":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\office\\word\\{file}")
            case "pptx":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\office\\powerpoint\\{file}")
            case "xlsx":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\office\\excel\\{file}")
            case "csv":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\office\\excel\\{file}")
            case "txt":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\text\\{file}")
            case "rtf":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\text\\{file}")
            case "mp4":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\videos\\{file}")
            case "mov":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\videos\\{file}")
            case "wmv":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\videos\\{file}")
            case "jpg":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\photos\\{file}")
            case "jpeg":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\photos\\{file}")
            case "png":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\photos\\{file}")
            case "mp3":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\audio\\{file}")
            case "wav":
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\audio\\{file}")
            case _:
                os.rename(f"{desktopPath}\\{file}", f"{targetDir}\\other\\{file}")
        
if __name__ == "__main__":
    main()