import sys
from pathlib import Path

external_dir = Path(__file__).parent / "external"
sys.path.insert(0, str(external_dir))

# Re-export lowtran
try:
    import lowtran
except ImportError:
    raise ImportError("Pre-compiled lowtran-piccia not found in external/")