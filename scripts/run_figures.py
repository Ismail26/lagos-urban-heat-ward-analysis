import json
import os
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
NOTEBOOK = REPO_ROOT / "notebooks" / "generate_rsase_figures.ipynb"

os.environ.setdefault("MPLBACKEND", "Agg")
os.chdir(REPO_ROOT)

nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
figure_dir = REPO_ROOT / "figures"
figure_dir.mkdir(parents=True, exist_ok=True)
namespace = {
    "__name__": "__main__",
    "REPO_ROOT": REPO_ROOT,
    "FIGURE_DIR": figure_dir,
}
start_cell = int(os.environ.get("RSASE_START_CELL", "0"))
end_cell = int(os.environ.get("RSASE_END_CELL", str(10**9)))

for index, cell in enumerate(nb.get("cells", [])):
    if cell.get("cell_type") != "code":
        continue
    if index < start_cell:
        continue
    if index > end_cell:
        continue
    source = "".join(cell.get("source", []))
    print(f"Running notebook cell {index}...")
    exec(compile(source, f"{NOTEBOOK.name}:cell_{index}", "exec"), namespace)

print("All selected RSASE figures completed.")
