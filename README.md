# download_m3u
Download all files from m3u playlist

## Usage
```
usage: m3u_download [-h] [-o OUTPUT_DIR] m3u_path

Download all files from M3U playlist file.

positional arguments:
  m3u_path              Path to input M3U file.

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory to save files.
```

## Example
```bash
python3 download_m3u.py playlists/cs7210_1080.m3u -o videos
```
