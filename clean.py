# %%
import operator
import pickle
from argparse import ArgumentParser
from functools import reduce
from pathlib import Path

import cv2
from tqdm import tqdm

# %%
parser = ArgumentParser(description="crawl.py")
parser.add_argument(
    "--data",
    type=str,
    default="images",
    help="location of crawled images",
)
parser.add_argument(
    "--show_details",
    action="store_true",
    default=False,
    help="show details",
)
args = parser.parse_known_args()[0]
images_data = args.data
show_details = args.show_details


# %%
locations = list(Path(images_data).glob("*/"))
bad_files, new_files = {}, {}

for loc in tqdm(locations, desc="Validating images"):
    try:
        with open(loc / "clean.cache", "rb") as f:
            clean_imgs = pickle.load(f)
    except:
        clean_imgs = []

    imgs = sorted(list(loc.glob("*.jpg")))
    imgs = [img for img in imgs if img not in clean_imgs]

    if imgs:
        new_files[loc] = len(imgs)
        for img in imgs:
            try:
                i = cv2.imread(str(img))
                size = i.shape
            except:
                if loc in bad_files:
                    bad_files[loc].append(img)
                else:
                    bad_files[loc] = [img]


# %%
if len(bad_files):
    for f in tqdm(
        reduce(operator.concat, bad_files.values()), desc="Removing invalid images"
    ):
        f.unlink()

# %%
updates = set(new_files.keys()) | set(bad_files.keys())
if updates:
    for loc in tqdm(updates, desc="Caching clean images"):
        imgs = sorted(list(loc.glob("*.jpg")))
        with open(loc / "clean.cache", "wb") as f:
            pickle.dump(imgs, f)


# %%
def summary(files, label):
    num_cameras = len(files)
    if label == "bad":
        num_images = len(reduce(operator.concat, files.values())) if files else 0
    else:
        num_images = sum(files.values()) if files else 0

    actions = {"new": "Found", "bad": "Removed"}
    if num_images:
        print(
            f"{actions[label]} {num_images} {label} image{'s' if num_images>1 else ''}",
            f"in {num_cameras} camera{'s' if num_cameras>1 else ''}",
        )
    else:
        print(f"{actions[label]} no {label} image")


if show_details:
    print()
    summary(new_files, "new")
    summary(bad_files, "bad")
