import os


def generateTile(part):
    return f'$1,000,000 MrBeast vs Andrew Tate! 🔥🥶😲 | Part {part} | Psychology Outer 😸👍🌹'


def generateDescription(option):
    same = "Andrew Tate and Mr Beast are fighting for a lot of money! $1,000,000 - one million dollars! " \
           "This is impossible spam epic insane and so many more words that are interesting and wow and amazing! " \
           "LISTEN HERE. YOU HAVE TO WATCH THIS VIDEO BECAUSE IT IS VERY INTERESTING. "
    if option == 'name':
        return same + "Find out what your name says about you! You will be surprised! " \
            "Your name can begin with many different letters, such as A, B, C, D, E, F, G, H, I, J, K, L, " \
            "M, N, O, P, Q, R, S, T, U, V, W, X, Y, and Z. This means you can have many different personality traits " \
            "and learn a lot about yourself through this epic psychology fact page. This youtube channel is dedicated to give you " \
            "the best psychology information about what your name means about you, and more specifically, what the first letter of your name means about you. " \
            "#psychology #name #letter #fact #shorts " \
            "👌🤞👍🔥🚒❄🥶🧊😊☺😃😄😸"
    elif option == 'month':
        return same + "Find out what your month says about you! You will be surprised! " \
            "You can be born in many different months, such as January, February, March, April, May, June, " \
            "July, August, September, October, November, and December. This means you can have many different personality traits " \
            "and learn a lot about yourself through this epic psychology fact page. This youtube channel is dedicated to give you " \
            "the best psychology information about what the month you were born in means about you. " \
            "#psychology #month #birthday #fact #shorts " \
            "👌🤞👍🔥🚒❄🥶🧊😊☺😃😄😸"
    elif option == 'color':
        return same + "Find out what your favorite color says about you! You will be surprised! " \
               "You can have many different favorite colors, such as black, white, red, lime, blue, yellow, cyan, magenta, silver, " \
               "gray, maroon, olive, green, purple, teal, navy, and more. This means you can have many different personality traits " \
               "and learn a lot about yourself through this epic psychology fact page. This youtube channel is dedicated to give you " \
               "the best psychology information about what your favorite color means about you. " \
               "#psychology #color #favorite #fact #shorts " \
               "👌🤞👍🔥🚒❄🥶🧊😊☺😃😄😸"
    else:
        raise SystemExit(0)


def generateTags():
    return f'mrbeast,andrewtate,psychology'


def youtubeUpload(part, option):
    description = generateDescription(option)
    title = generateTile(part)
    tags = generateTags()

    os.system(f'python upload_video.py --file="final.mp4" '
              f'--title="{title}" '
              f'--description="{description}" '
              f'--keywords="{tags}" '
              f'--category="24" '
              f'--privacyStatus="public"')
