import os
import shutil
from colorama import Fore

def delete_cache():
    """Delete all __pycache__ directories recursively starting from the current directory."""
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if dir == '__pycache__':
                cache_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(cache_path)
                    # print(Fore.GREEN + f"Deleted cache directory: {cache_path}")
                except Exception as e:
                    print(Fore.RED + f"Failed to delete cache directory {cache_path}: {e}")
