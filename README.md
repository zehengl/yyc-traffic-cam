<div align="center">
    <img src="https://cdn4.iconfinder.com/data/icons/internet-security-flat-2/32/Internet_Security_Camera_cctv_technology_secure_surveillance-512.png" alt="logo" height="128">
</div>

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

## Credits

- [Logo][1] by [Kmg Design][2]

[1]: https://www.iconfinder.com/icons/5172951/camera_cctv_internet_secure_security_surveillance_technology_icon
[2]: https://www.iconfinder.com/kmgdesignid
