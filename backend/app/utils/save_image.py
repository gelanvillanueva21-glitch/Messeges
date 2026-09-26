

import shutil
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


def create_filepath(data_dir: Path, extension: str) -> Path:
    data_dir.mkdir(parents=True, exist_ok=True)
    while True:
        random = secrets.token_hex(6)
        file_path = f"{random}{extension}"
        url_path = data_dir / file_path

        if not url_path.exists():
            return url_path


def file_security(file):
    if not file or not getattr(file, "filename", None) or not file.filename.strip():
        return None
    allowed_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
    extension = Path(file.filename).suffix.lower()
    if extension not in allowed_extensions:
        raise ValueError("Invalid image extension. Allowed extensions: .jpg, .jpeg, .png, .webp, .gif")
    return create_filepath(DATA_DIR, extension)


def save_file(file):
    if not file or not getattr(file, "filename", None) or not file.filename.strip():
        return None
    file_path = file_security(file)
    if not file_path:
        return None

    try:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        raise ValueError("Failed to save image file")
    return file_path.name

