
import os
import sys

__author__ = 'Andreas'


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller
        https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
