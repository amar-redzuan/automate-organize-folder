import os
import shutil

# DOWNLOADS = "C:/Users/user1/Downloads"

# for filename in os.listdir(DOWNLOADS):
#     print(filename)

# baru = "TEST[REAL]"
# TARGET = os.path.join(DOWNLOADS, baru)
# os.makedirs(TARGET, exist_ok=True)
# print(f"folder {baru} dijana!")
# print(f"Folder diletak di {TARGET}")

# FILE1 = os.listdir(DOWNLOADS)[0]

# # print(test)
# source = os.path.join(DOWNLOADS,FILE1)
# print(f"fail terlibaT: {FILE1}")
# print("Fail dipindah DARI: ", source)
# print("--------------KE------------------")
# print("Fail dipindah KEPADA: ", TARGET)

# if os.path.isfile(source):
#     shutil.move(source,TARGET)
#     print("siap bro, apa susah")
# else:
#     print("kau merepek apa ni")

# # Sekarang semua file dalam baru tu kita juggle ke tepi pula hehe

# juggle= os.path.join(DOWNLOADS,"JUGGLE")
# os.makedirs(juggle, exist_ok=True)

# pegang = os.listdir(TARGET)[0]
# print(f"pegang kuat2 jangan lepas {pegang}")
# tangan = os.path.join(TARGET,pegang)
# if os.path.isfile(tangan):
#     shutil.move(tangan,juggle)
#     print(f"betul ke kat target ni?, letak si {pegang} kat juggle")
# else:
#     print("HAAA mana dia pergi?")

# # sekarang nak susun for real haha, started at 3.02 pm markas 4g 14/1/2026

# susun_fail = os.listdir(juggle)[0:10]
# cuti_key = ["XL254172", "half day"]
# work_key = ["4c11", "ip", "AP", "MOP", "UAT","4g4"]
# cuti_file = []
# work_file =[]
# print("")
# print("-- HASIL PENCARIAN HARI INI --")
# for f in susun_fail:

#     if any(c.lower() in f.lower() for c in cuti_key):
#         cuti_file.append(f)
#         print(f"CUTI JUMPA ---- {f}")
#     elif any(w.lower() in f.lower() for w in work_key):
#         work_file.append(f)
#         print(f"HUHUH KERJA / ->")
#     else:
#         print(f"WADUH XXXXX  lain lah bos {f.lower()} XXXXX")

# folder_cuti = "Semua Cuti"
# print(f"Pindah ke Folder -> {folder_cuti}")
# path_cuti = os.path.join(DOWNLOADS,folder_cuti)
# os.makedirs(path_cuti, exist_ok=True)
# path_juggle = ""
# os.makedirs(os.path.join(DOWNLOADS,"Semua Kerja"), exist_ok=True)


# for i in cuti_file:
#      path_juggle = os.path.join(juggle,i)
#      shutil.move(path_juggle,path_cuti)
#      print(f"{i} dah masuk dalam {path_cuti}")

# for i in work_file:
#      path_juggle = os.path.join(juggle,i)
#      shutil.move(path_juggle, os.path.join(DOWNLOADS,"Semua Kerja"))
#      print(f"{i} dah masuk dalam {os.path.join(DOWNLOADS,"Semua Kerja")}")

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
        os.makedirs(namaPath(folder), exist_ok=True)
        moveFile(select_file, sourceFolder, "Semua Kerja")
        print(f"file {select_file} -> Semua Kerja")
    # Holiday Key
    elif(any(select_file.lower() in k.strip().lower() for k in holiday_key)):
        moveFile(select_file, sourceFolder, "Semua Cuti")
        print(f"file {select_file} -> Semua Cuti")
    # No Key
    else:
        print("Sorry Bos, fail takda :( \n")
        moveFile(select_file, sourceFolder, destinationFolder)