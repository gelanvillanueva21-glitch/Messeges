

import shutil
import secrets
from pathlib import Path


def create_filepath(DATA_URL, extension):
    while True:
        random = secrets.token_hex(6)
        file_path = f"{random}{extension}"
        URL_PATH = DATA_URL / file_path

        if not URL_PATH.exists():
            return URL_PATH



def file_security(file):
    DATA_URL = Path("../data")
    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
    EXTENSION = Path(file.filename).suffix.lower()
    if EXTENSION not in ALLOWED_EXTENSIONS:
        raise ValueError()
    return create_filepath(DATA_URL, EXTENSION)



def save_file(file):
    if not file:
        return None
    file_path = file_security(file)

    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        raise ValueError()
    return file_path.name
