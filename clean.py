# %%
import pickle
from pathlib import Path

import cv2
from tqdm import tqdm

locations = list(Path("images").glob("*/"))


# %%
bad_files = []
new_files = 0
for loc in tqdm(locations, desc="Validating images"):
    with open(loc / "clean.cache", "rb") as f:
        clean_imgs = pickle.load(f)

    imgs = sorted(list(loc.glob("*.jpg")))
    imgs = [img for img in imgs if img not in clean_imgs]
    new_files += len(imgs)
    for img in imgs:
        try:
            i = cv2.imread(str(img))
            size = i.shape
        except:
            bad_files.append(img)

print(f"Found {new_files} new file{'s' if new_files>1 else ''}")

# %%
if bad_files:
    for f in tqdm(bad_files, desc="Removing invalid images"):
        f.unlink()
    print(f"Removed {len(bad_files)} file{'s' if len(bad_files)>1 else ''}")

# %%
for loc in tqdm(locations, desc="Cacheing clean images"):
    imgs = sorted(list(loc.glob("*.jpg")))
    with open(loc / "clean.cache", "wb") as f:
        pickle.dump(imgs, f)
