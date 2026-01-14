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

FILE1 = os.listdir(DOWNLOADS)[0]

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

# Sekarang semua file dalam baru tu kita juggle ke tepi pula hehe

juggle= os.path.join(DOWNLOADS,"JUGGLE")
os.makedirs(juggle, exist_ok=True)

pegang = os.listdir(TARGET)[0]
print(f"pegang kuat2 jangan lepas {pegang}")
tangan = os.path.join(TARGET,pegang)
if os.path.isfile(tangan):
    shutil.move(tangan,juggle)
    print(f"betul ke kat target ni?, letak si {pegang} kat juggle")
else:
    print("HAAA mana dia pergi?")


