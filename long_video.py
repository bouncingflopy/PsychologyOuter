from moviepy.editor import *
import os


def generateTile(part):
    return f'$1,000,000 MrBeast vs Andrew Tate COMPILATION! 🔥🥶😲 | Part {part} | Psychology Outer 😸👍🌹'


def generateDescription():
    return "Andrew Tate and Mr Beast are fighting for a lot of money! $1,000,000 - one million dollars! " \
           "This is impossible spam epic insane and so many more words that are interesting and wow and amazing! " \
           "LISTEN HERE. YOU HAVE TO WATCH THIS VIDEO BECAUSE IT IS VERY INTERESTING. " \
           "Find out what your name says about you! You will be surprised! " \
           "Your name can begin with many different letters, such as A, B, C, D, E, F, G, H, I, J, K, L, " \
           "M, N, O, P, Q, R, S, T, U, V, W, X, Y, and Z. This means you can have many different personality traits " \
           "and learn a lot about yourself through this epic psychology fact page. This youtube channel is dedicated to give you " \
           "the best psychology information about what your name means about you, and more specifically, what the first letter of your name means about you. " \
           "#psychology #name #letter #fact #shorts " \
           "👌🤞👍🔥🚒❄🥶🧊😊☺😃😄😸 " \
           "Find out what your month says about you! You will be surprised! " \
           "You can be born in many different months, such as January, February, March, April, May, June, " \
           "July, August, September, October, November, and December. This means you can have many different personality traits " \
           "and learn a lot about yourself through this epic psychology fact page. This youtube channel is dedicated to give you " \
           "the best psychology information about what the month you were born in means about you. " \
           "#psychology #month #birthday #fact #shorts " \
           "👌🤞👍🔥🚒❄🥶🧊😊☺😃😄😸 " \
           "Find out what your favorite color says about you! You will be surprised! " \
           "You can have many different favorite colors, such as black, white, red, lime, blue, yellow, cyan, magenta, silver, " \
           "gray, maroon, olive, green, purple, teal, navy, and more. This means you can have many different personality traits " \
           "and learn a lot about yourself through this epic psychology fact page. This youtube channel is dedicated to give you " \
           "the best psychology information about what your favorite color means about you. " \
           "#psychology #color #favorite #fact #shorts " \
           "👌🤞👍🔥🚒❄🥶🧊😊☺😃😄😸"


def generateTags():
    return f'mrbeast,andrewtate,psychology'


def upload(part):
    description = generateDescription()
    title = generateTile(part)
    tags = generateTags()

    os.system(f'python upload_video.py --file="final.mp4" '
              f'--title="{title}" '
              f'--description="{description}" '
              f'--keywords="{tags}" '
              f'--category="24" '
              f'--privacyStatus="public"')


def longVideo():
    videos = os.listdir("videos/")
    videos = [os.path.join("videos/", video) for video in videos]
    videos.sort(key=lambda x: os.path.getmtime(x))
    videos = videos[:10]

    videoClips = [VideoFileClip(video) for video in videos]
    final = concatenate_videoclips(videoClips)

    final.write_videofile("final.mp4", threads=200, fps=24)

    for video in videos:
        os.remove(video)

    with open("part_long.txt", 'r') as f:
        part = f.readlines()[0]
    with open("part_long.txt", 'w') as f:
        f.write(str(int(part) + 1))

    upload(part)
