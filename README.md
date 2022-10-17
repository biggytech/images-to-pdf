# Images To PDF Converter

This tool generates a pdf file from provided images of any size.

## Requirements
- Python3 installed
- [Pillow](https://pillow.readthedocs.io/en/latest/installation.html#basic-installation) lib installed

## Running

`python3 script.py <images_path> <extension> <from_range> <to_range> <output_file_path>`

For example you want to compose images on paths from './data/1.jpg' to './data/3.jpg' into pdf file './result.pdf'. Then your command would look like this:

`python3 script.py ./data/ jpg 1 3 ./result.pdf`

> **Note**
> If the `output_file_path` contains a directory, then this directory should exist before the script run.