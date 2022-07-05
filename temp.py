import os
import re

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pth = str(resource_path('icons/iam.png')).replace('\\','/')
border_image = '"border-image: url(' + pth + ');"'
print(border_image)