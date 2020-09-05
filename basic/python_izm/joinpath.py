# os.join.path
import os

PROJECT_DIR = 'C:\python-izm'
SETTING_FILE = 'setting.ini'

print(os.path.join(PROJECT_DIR, SETTING_FILE))
print(os.path.join(PROJECT_DIR, 'setting_dir', SETTING_FILE))
