import cv2
import os
import argparse


def make_timelapse(
    image_folder,
    video_name,
    fps,
    duration_per_image,
    image_ext=".jpg",
    width=2316,
    height=3088,
):
    image_paths = [
        os.path.join(image_folder, img)
        for img in os.listdir(image_folder)
        if img.endswith(image_ext)
    ]
    image_paths.sort()

    if not image_paths:
        raise ValueError("No images found in the folder.")

    frame = cv2.imread(image_paths[0])
    desired_size = (width, height)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(video_name, fourcc, fps, desired_size)

    frame_count = int(fps * duration_per_image)

    progress = 0
    for i, image_path in enumerate(image_paths):
        image = cv2.imread(image_path)
        height, width, _ = image.shape
        if width != desired_size[0] or height != desired_size[1]:
            image = cv2.resize(image, desired_size)
        for _ in range(frame_count):
            video.write(image)
        currentProgress = int((i + 1) / len(image_paths) * 100)
        if currentProgress > progress:
            print(f"{currentProgress}%")
            progress = currentProgress

    video.release()

    print("Video created")


def main():
    parser = argparse.ArgumentParser(
        description="Create a timelapse video from images."
    )
    parser.add_argument(
        "--folder",
        "-f",
        type=str,
        default="pictures",
        help="Path to the folder containing images.",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="timelapse.mp4",
        help="Output video file name.",
    )
    parser.add_argument(
        "--fps", type=int, default=30, help="Frames per second in the output video."
    )
    parser.add_argument(
        "--duration",
        "-d",
        type=float,
        default=0.12,
        help="Duration for each image in seconds.",
    )

    parser.add_argument(
        "--ext",
        type=str,
        default=".jpg",
        help="Image extension.",
    )
    parser.add_argument("--width", type=int, default=2316, help="Width of the video.")
    parser.add_argument("--height", type=int, default=3088, help="Width of the video.")

    args = parser.parse_args()

    make_timelapse(
        args.folder,
        args.output,
        args.fps,
        args.duration,
        args.ext,
        args.width,
        args.height,
    )


if __name__ == "__main__":
    main()
