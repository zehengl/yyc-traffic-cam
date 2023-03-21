<div align="center">
    <img src="https://cdn4.iconfinder.com/data/icons/internet-security-flat-2/32/Internet_Security_Camera_cctv_technology_secure_surveillance-512.png" alt="logo" height="196">
</div>

# yyc-traffic-cam

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![pages-build-deployment](https://github.com/zehengl/yyc-traffic-cam/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/zehengl/yyc-traffic-cam/actions/workflows/pages/pages-build-deployment)

A demo to detect vehicles in traffic cam

## Environment

- Python 3.9

## Install

> Remove `--extra-index-url https://download.pytorch.org/whl/cu116` in the `requirements.txt` file, if you don't have GPU/CUDA set up.

    python -m venv .venv
    .\.venv\Scripts\activate
    python -m pip install -U pip
    pip install -r requirements.txt

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.
It will also install `jupyterlab` for notebook experience.

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
