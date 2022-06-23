# %%
from pathlib import Path
from tqdm import tqdm
import cv2

locations = list(Path("images").glob("*/"))


# %%
bad_files = []
for loc in tqdm(locations, desc="Validating images"):
    imgs = sorted(list(loc.glob("*.jpg")))
    for img in imgs:
        try:
            i = cv2.imread(str(img))
            size = i.shape
        except:
            bad_files.append(img)

# %%
if bad_files:
    for f in tqdm(bad_files, desc="Removing invalid images"):
        f.unlink()
