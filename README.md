# yyc-traffic-cam

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![GitHub Pages](https://github.com/zehengl/yyc-traffic-cam/actions/workflows/gh-deploy.yml/badge.svg)](https://github.com/zehengl/yyc-traffic-cam/actions/workflows/gh-deploy.yml)

A demo to detect vehicles in traffic cam

## Environment

- Python 3.9

## Install

    python -m venv .venv
    .\.venv\Scripts\activate
    python -m pip install -U pip
    pip install -r requirements.txt

> Configure `--extra-index-url` if CUDA is available, e.g. `pip install --trusted-host download.pytorch.org --extra-index-url https://download.pytorch.org/whl/cu118 -r requirements.txt`.
>
> Use `requirements-dev.txt` for development and docs.

## Usage

### Crawl some traffic cam images

    python crawl.py

### Remove corrupted image files

    python clean.py

### Detect vehicles

    python detect.py

## Docs

    mkdocs serve
