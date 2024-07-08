import cv2
import os


def make_timelapse(image_folder, video_name, fps, image_ext=".jpg"):
    image_paths = [
        os.path.join(image_folder, img)
        for img in os.listdir(image_folder)
        if img.endswith(image_ext)
    ]
    image_paths.sort(key=lambda x: os.path.getctime(x))

    frame = cv2.imread(image_paths[0])
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    for image_path in image_paths:
        video.write(cv2.imread(image_path))

    video.release()


if __name__ == "__main__":
    image_folder = "path_to_images"
    video_name = "timelapse.mp4"
    make_timelapse(image_folder, video_name, fps=2)
