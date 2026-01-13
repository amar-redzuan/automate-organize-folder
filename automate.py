import os
import shutil

DOWNLOADS = "C:/Users/user1/Downloads"


# for filename in os.listdir(DOWNLOADS):
#     print(filename)



baru = "TEST[REAL]"
TARGET = os.path.join(DOWNLOADS, baru)
os.makedirs(TARGET, exist_ok=True)
print(f"folder {baru} dijana!")
print(f"Folder diletak di {TARGET}")

FILE1 = (os.listdir(DOWNLOADS)[0])

# print(test)
source = os.path.join(DOWNLOADS,FILE1)
print(f"fail terlibaT: {FILE1}")
print("Fail dipindah DARI: ", source)
print("--------------KE------------------")
print("Fail dipindah KEPADA: ", TARGET)

if os.path.isfile(source):
    shutil.move(source,TARGET)
    print("siap bro, apa susah")
else:
    print("kau merepek apa ni")





# shutil.move(source, "C:/Users/user1/Downloads/TEST")
