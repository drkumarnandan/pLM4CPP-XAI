from pathlib import Path
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
required = [
    "pLM4CPPs_dataset_CPP.xlsx",
    "pLM4CPPs_dataset_Non-CPP.xlsx",
    "kelm_dataset_CPP.csv",
    "kelm_dataset_Non-CPP.csv",
]
missing = [name for name in required if not (root / name).exists()]
if missing:
    print("Missing input files:")
    for name in missing:
        print(" -", name)
    raise SystemExit(1)
print("All four expected input files were found.")
