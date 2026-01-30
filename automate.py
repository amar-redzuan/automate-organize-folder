import os
import shutil

userName = "user1"
srcPath = "Downloads"
pathFolder = f"C:/Users/{userName}/{srcPath}"

def namaPath(namaFolder):
    targetFolder = os.path.join(pathFolder,namaFolder)
    return targetFolder

def moveFile(file,fileFrom, fileTo):
    srcPath = os.path.join(namaPath(fileFrom), file)
    dstPath = os.path.join(namaPath(fileTo), file)
    shutil.move(srcPath,dstPath)
    print(f"{srcPath} dipindah ->{dstPath}")


work_key = """
4c11
ip
AP
MOP
UAT
4g4
JDN
"""
holiday_key = """
XL254172
half day
"""

resume_key ="""
resume
"""

uitm_key = """
cs259
AMAR_CS2595ADE
AMAR_CS2597A
DEGREE
"""
sourceFolder = "JUGGLE"
destinationFolder = "TEST[REAL]"
os.makedirs(namaPath(destinationFolder), exist_ok=True)
semua_fail = os.listdir(namaPath(sourceFolder)) # Letak nama folder yang ingin disusun
fileNo = 0
while fileNo < 3:
    select_file = semua_fail[fileNo]
    fileNo += 1
    print(f"file {fileNo} : {select_file} \n")
    # Work Key
    if any(select_file.lower() in k.strip().lower() for k in work_key):
        # os.makedirs(namaPath(folder), exist_ok=True)  nanti tambah
        moveFile(select_file, sourceFolder, "Semua Kerja")
        print(f"file {select_file} -> Semua Kerja")
    # Holiday Key
    elif(any(select_file.lower() in k.strip().lower() for k in holiday_key)):
        moveFile(select_file, sourceFolder, "Semua Cuti")
        print(f"file {select_file} -> Semua Cuti")
    # Resume Key
    elif(any(select_file.lower() in k.strip().lower() for k in resume_key)):
        moveFile(select_file, sourceFolder, "Resume")
        print(f"file {select_file} -> Resume")
        # Resume Key
    elif(any(select_file.lower() in k.strip().lower() for k in uitm_key)):
        moveFile(select_file, sourceFolder, "UiTM File")
        print(f"file {select_file} -> UiTM File")
    # No Key
    else:
        print("Sorry Bos, fail takda :( \n")
        moveFile(select_file, sourceFolder, destinationFolder)
