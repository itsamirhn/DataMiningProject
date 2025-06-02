import logging
import shutil
from pathlib import Path

import kagglehub

logger = logging.getLogger(__name__)

download_path = kagglehub.dataset_download("yelp-dataset/yelp-dataset")

logger.info(f"Download path: {download_path}")

target_directory_path = Path(__file__).parent / "data"
downloaded_file_path = Path(download_path) / "yelp_academic_dataset_review.json"

assert downloaded_file_path.exists(), "Downloaded file does not exist."

if not target_directory_path.exists():
    target_directory_path.mkdir(parents=True, exist_ok=True)

shutil.copy(downloaded_file_path, target_directory_path / downloaded_file_path.name)
logger.info(f"File copied to: {target_directory_path / downloaded_file_path.name}")
