# Timelapse Video Creator

This Python script uses OpenCV to create timelapse videos from a sequence of images. Customize the frame rate, resolution, and image duration easily through command-line arguments.

## Requirements

-   Python 3.x
-   OpenCV (`pip install opencv-python`)

## Usage

Run the script with optional arguments to tailor the timelapse video:

```bash
python timelapse_creator.py --folder [path_to_images] --output [output_file_name] --fps [frames_per_second] --duration [image_display_duration] --ext [file_extension] --width [video_width] --height [video_height]
```

### Command Line Arguments

-   `--folder, -f`: Path to image folder (default: `pictures`)
-   `--output, -o`: Output video filename (default: `timelapse.mp4`)
-   `--fps`: Frames per second (default: 30)
-   `--duration, -d`: Duration per image in seconds (default: 0.12)
-   `--ext`: Image file extension (default: `.jpg`)
-   `--width`: Video width (default: 2316)
-   `--height`: Video height (default: 3088)
