import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]:%(message)s:')

from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO)

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    if filepath.parent != Path('.'):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f'Creating directory: {filepath.parent} for file: {filepath.name}')

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f'Created empty file: {filepath.name}')
    else:
        logging.info(f'{filepath.name} already exists')



