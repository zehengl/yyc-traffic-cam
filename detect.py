# %%
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import torch
from tqdm import tqdm

output = Path("output")
output.mkdir(exist_ok=True)
model = torch.hub.load("ultralytics/yolov5", "yolov5s")
model.classes = [2, 3, 5, 7]

# %%
def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx : min(ndx + n, l)]


# %%
parser = ArgumentParser(description="detect.py")
parser.add_argument(
    "--save_runs",
    action="store_true",
    default=False,
    help="export processed images in files",
)
parser.add_argument(
    "--batch_size",
    type=int,
    default=100,
    help="batch size",
)
args = parser.parse_known_args()[0]
save_runs = args.save_runs
batch_size = args.batch_size

locations = list(Path("images").glob("*/"))

for loc in tqdm(locations):
    imgs = sorted(list(loc.glob("*.jpg")))
    timestamps, counts = [], []
    for batch_imgs in batch(imgs, batch_size):
        results = model(batch_imgs)

        if save_runs:
            results.save()

        _timestamps = [f.split(".")[0].split("-")[1:] for f in results.files]
        _timestamps = [datetime(*[int(i) for i in t]) for t in _timestamps]
        _counts = [d.shape[0] for d in results.pandas().xyxy]

        timestamps.extend(_timestamps)
        counts.extend(_counts)

    df = pd.DataFrame(dict(ds=timestamps, count=counts))
    df = df.groupby(df["ds"].dt.hour).mean().reset_index()
    fig = plt.figure(figsize=(10, 6))
    ax = sns.scatterplot(data=df, x="ds", y="count")
    fig.savefig(
        output / f"{loc.stem}.summary.png",
        dpi=600,
        bbox_inches="tight",
    )
    df.to_csv(
        output / f"{loc.stem}.summary.csv",
        index=False,
    )


# %%
