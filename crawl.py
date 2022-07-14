# %%
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from time import sleep

import requests
from tqdm import tqdm


# %%
url = "https://data.calgary.ca/resource/k7p9-kppz.json"
cameras = [
    (d["camera_location"], d["camera_url"]["url"]) for d in requests.get(url).json()
]

# %%
parser = ArgumentParser(description="crawl.py")
parser.add_argument(
    "--wait_time",
    type=int,
    default=5,
    help="wait time (in minutes)",
)
parser.add_argument(
    "--num_cycles",
    type=int,
    help="number of crawling cycles",
)
parser.add_argument(
    "--data",
    type=str,
    default="images",
    help="location of crawled images",
)
args = parser.parse_known_args()[0]
wait_time = args.wait_time
images_data = args.data
num_cycles = args.num_cycles

images = Path(images_data)
images.mkdir(exist_ok=True)

count = 0
while True:
    for camera_name, camera_url in tqdm(cameras, desc="Getting images"):
        r = requests.get(camera_url)
        c = Path(camera_url)

        loc = c.stem
        name = c.name

        (images / loc).mkdir(exist_ok=True)
        now = datetime.now()

        name = name.replace(
            ".jpg",
            f'-{now.strftime(r"%Y-%m-%d-%H-%M-%S")}.jpg',
        )

        with open(images / loc / name, "wb") as f:
            f.write(r.content)

        cname = images / loc / "cname.txt"
        if not cname.exists():
            with open(cname, "w") as f:
                f.write(camera_name)

    count += 1
    if num_cycles and count >= num_cycles:
        break

    print(
        f"Waiting for new images in {wait_time} minute{'s' if wait_time >1 else ''}..."
    )
    sleep(60 * wait_time)
