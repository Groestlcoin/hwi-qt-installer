# hwi-qt-installer

Set of scripts to create a self contained hwi-qt executable

## Requirements

Create a virtual environment fully working for hwi-qt:

- git clone https://github.com/checksig-custody/hwi-qt-installer.git
- cd hwi-qt-installer
- python3.8 -m venv venv
- venv\Scripts\activate.bat (or source venv/bin/activate on Linux)
- pip install pyside2
- pip install hwi (or pip install -e [HWI_PATH] if you have a local copy)
- pip install pyinstaller

Try to execute the command **hwi-qt** and if something is not working fix it.
When **hwi-qt** is fully working execute **python build.py** or **python build.py [path_to_hwi-qt.py]**.
After the build process the final executable will be in the *dist* folder.

a