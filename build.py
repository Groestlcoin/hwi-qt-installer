import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '--onefile',
    '--windowed',
    '--add-binary=%s;.' % os.path.join('libs', '*.dll'),
    '--hidden-import=hwilib.devices.trezor',
    '--hiddenimport=hwilib.devices.ledger',
    '--hidden-import=hwilib.devices.keepkey',
    '--hidden-import=hwilib.devices.digitalbitbox',
    '--hidden-import=hwilib.devices.coldcard',
    '--icon=%s' % os.path.join('icon', 'icon.ico'),
    os.path.join('venv', 'Lib', 'site-packages', 'hwi-qt.py'),
])
