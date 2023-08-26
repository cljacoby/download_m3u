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
> python3 download_m3u.py playlists/cs7210_1080.m3u -o videos

Preparing to download 179 files.
Downloading (1/179) CS7210_Course_Introduction.mp4 ...
    Saved 16.74 mb, Total 16.74 mb
Downloading (2/179) Lesson_1_Introduction.mp4 ...
    Saved 4.53 mb, Total 21.27 mb
Downloading (3/179) Examples_of_Distributed_Systems.mp4 ...
    Saved 6.86 mb, Total 28.13 mb
Downloading (4/179) What_is_a_Distributed_System.mp4 ...
    Saved 24.72 mb, Total 52.84 mb
Downloading (5/179) A_Simple_Model_of_a_Distributed_System.mp4 ...
```
