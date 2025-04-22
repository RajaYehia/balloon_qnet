import subprocess
import sys
from pathlib import Path

def build_lowtran():
    repo_url = "https://github.com/francescopiccia/lowtran-piccia.git"
    repo_dir = Path("lowtran-piccia")

    # Clone if not already present
    if not repo_dir.exists():
        subprocess.run(["git", "clone", repo_url], check=True)

    # Build (replace with actual build commands)
    subprocess.run(["make"], cwd=repo_dir, check=True)  # Example

    # Install in development mode
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", str(repo_dir)], check=True)

if __name__ == "__main__":
    build_lowtran()