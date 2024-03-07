import requests
from pathlib import Path
import os


current_wd = Path.cwd()
print(os.chdir(current_wd))