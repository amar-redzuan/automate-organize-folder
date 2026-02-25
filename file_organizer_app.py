import streamlit as st
import os
import shutil
st.title('🧹 File Oranizer App')

# st.sidebar.title('huh')
st.header('Work Path')
st.write('Please insert your working directory path.')

# User Form
currentPath = st.text_input("Current Path:", value = "C:/Users/user1/Downloads")
keys_input = st.text_area("Enter one key per line")
keys = [k.strip().lower() for k in keys_input.split("\n") if k.strip()]
st.subheader('Fill the path where the files will be move to.')
targetPath = st.text_input("Target Path:" )
st.subheader('Fill the name of the folder to move file.')
destinationFolder = st.text_input('Target Folder Name:')
dstPath = os.path.join(targetPath, destinationFolder)


# Move file between current & target path
def moveFile(file):
    srcPath = os.path.join(currentPath, file)
    tgtPath = os.path.join(dstPath, file)
    st.success(f'{srcPath} -> {tgtPath}')
    shutil.move(srcPath,tgtPath)

if st.button("Process"):
    if not currentPath.strip() or not targetPath.strip():
        st.warning("Please insert both current and target folder path.")
    elif keys_input.strip() == "":
        st.warning("Please insert a key")
    else:
        try:
            if os.path.abspath(currentPath) == os.path.abspath(dstPath):
                st.error('Current and destination path is the same.')
            # Create folder if not exist
            os.makedirs(os.path.join(targetPath, destinationFolder), exist_ok=True)
            files = os.listdir(currentPath)
            matched = [f for f in files if os.path.isfile(os.path.join(currentPath, f)) and any(key in f.lower() for key in keys)]
            st.success(f"Found {len(matched)} matching files: {matched}")
            # this part is just to check if my logic is true
            for m in matched:
                moveFile(m)
        except Exception as e:
            st.error(f"Error: {e}")

