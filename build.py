import PyInstaller.__main__
import os
import sys

def _find_file(filename):
    for root, dirs, files in os.walk(r'.'):
        for name in files:
            if name == filename:
                return os.path.abspath(os.path.join(root, name))

    return ""


qt_py = ""
bin_extension = ""

if len(sys.argv) < 2:
    qt_py = _find_file("hwi-qt.py")
else:
    qt_py = sys.argv[1]

if os.name == "nt":
    bin_extension = '--add-binary=%s;.' % os.path.join('libs', '*.dll')
elif os.name == "posix":
    bin_extension = '--add-binary=%s:.' % os.path.join('libs', '*.so')

PyInstaller.__main__.run([
    '--onefile',
    '--windowed',
    bin_extension,
    '--hidden-import=hwilib.devices.trezor',
    '--hiddenimport=hwilib.devices.ledger',
    '--hidden-import=hwilib.devices.keepkey',
    '--hidden-import=hwilib.devices.digitalbitbox',
    '--hidden-import=hwilib.devices.coldcard',
    # comment this line if you build the standart HWI
    '--hidden-import=hwilib.devices.checksig',
    '--icon=%s' % os.path.join('icon', 'icon.ico'),
    qt_py,
])
