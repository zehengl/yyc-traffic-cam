# %%
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from time import sleep

import requests
from tqdm import tqdm

images = Path("images")
images.mkdir(exist_ok=True)
url = "https://data.calgary.ca/resource/k7p9-kppz.json"
locations = requests.get(url).json()
camera_urls = [d["camera_url"]["url"] for d in locations]

# %%
parser = ArgumentParser(description="crawl.py")
parser.add_argument(
    "--wait_time",
    type=int,
    default=5,
    help="wait time (in minutes)",
)
args = parser.parse_known_args()[0]
wait_time = args.wait_time

while True:
    for camera_url in tqdm(camera_urls, desc="Getting images"):
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

    print(
        f"Waiting for new images in {wait_time} minute{'s' if wait_time >1 else ''}..."
    )
    sleep(60 * wait_time)
