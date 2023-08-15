from youtubeUploader import youtubeUpload
from transformer import transform
from long_video import longVideo
import shutil
import random
import os


def main():
    options = ['name', 'month', 'color']
    style = random.randint(0, len(options) - 1)
    option = options[style]

    with open("part.txt", 'r') as f:
        part = f.readlines()[0]
    with open("part.txt", 'w') as f:
        f.write(str(int(part) + 1))

    facts = random.randint(3, 8)

    transform(facts, 4, option)

    shutil.copy("final.mp4", f'videos/{option}{part}.mp4')

    youtubeUpload(part, option)

    if len(os.listdir("videos/")) >= 10:
        longVideo()


if __name__ == '__main__':
    main()
