# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

import os
from pathlib import Path
working_dir = Path(os.path.abspath(SPECPATH))
from PyInstaller.utils.hooks import collect_dynamic_libs


a = Analysis(['app.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('icons/hand.ico', str(Path(working_dir / 'icons' / 'hand.ico')), 'DATA'),
            ('icons/hand.png', str(Path(working_dir / 'icons' / 'hand.png')), 'DATA'),
            ('icons/lightning.png', str(Path(working_dir / 'icons' / 'lightning.png')), 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='app',
          debug=True,
          strip=False,
          upx=True,
          console=True,
		  icon=str(Path(working_dir / 'icons' / 'hand.ico')))

