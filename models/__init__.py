import os
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
