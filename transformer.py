from elevenlabs import generate, save, set_api_key
from moviepy.audio.fx import audio_normalize
from moviepy.editor import *
import requests
import random
import json
import cv2


def backgroundClip(length):
    background = VideoFileClip(f'backgrounds/background{random.randint(1, 13)}.mp4')
    background = background.volumex(0)
    background = background.resize((1080, 960))
    background = background.loop(duration=length)

    return background


def subtitleGenerator(text, fontsize, color, startTime, duration, height, strokeColor='black'):
    clipStroke = TextClip(text, font='Volkswagen-Serial-Black', fontsize=fontsize, color=strokeColor, stroke_color=strokeColor, stroke_width=25, method='caption', size=(1080, 1920))
    clipStroke = clipStroke.set_start(startTime)
    clipStroke = clipStroke.set_duration(duration)
    clipStroke = clipStroke.set_position((540 - int(clipStroke.size[0] / 2), height))

    clip = TextClip(text, font='Volkswagen-Serial-Black', fontsize=fontsize, color=color, stroke_width=0, method='caption', size=(1080, 1920))
    clip = clip.set_start(startTime)
    clip = clip.set_duration(duration)
    clip = clip.set_position((540 - int(clip.size[0] / 2), height))

    return clipStroke, clip


def chooseAPIkey():
    url = "https://api.elevenlabs.io/v1/user/subscription"

    with open("eleven.txt", "r") as f:
        keys = f.readlines()
    keys = [key.replace("\n", "") for key in keys]

    best = [keys[0], 10001]
    for key in keys:
        headers = {"Accept": "application/json", "xi-api-key": key}
        response = requests.get(url, headers=headers)

        if json.loads(response.text)["character_count"] < best[1]:
            best = [key, json.loads(response.text)["character_count"]]

    return best[0]


def subtitlesClips(length, unit, facts, option):
    set_api_key(chooseAPIkey())

    if option == 'name':
        choices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    elif option == 'month':
        choices = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    elif option == 'color':
        choices = ['black', 'white', 'red', 'lime', 'blue', 'yellow', 'cyan', 'magenta', 'silver', 'gray', 'maroon', 'olive', 'green', 'purple', 'teal', 'navy']
    else:
        raise SystemExit(0)

    with open("traits.txt", 'r') as f:
        traits = f.readline()
    traits = traits.split()

    with open("funny.txt", 'r') as f:
        funnys = f.readline()
    funnys = funnys.split()

    clips = []
    tts = []
    for i in range(facts):
        choice = random.choice(choices)
        choices.remove(choice)

        if random.randint(0, 1) == 0:
            trait = random.choice(traits)
            traits.remove(trait)
        else:
            trait = random.choice(funnys)
            funnys.remove(trait)
            trait = trait.replace("_", " ")

        if option == 'name':
            ttsAudio = generate(text=f'If your name starts with {choice}, it means you are {trait}.', voice="Michael", model="eleven_monolingual_v1")
        elif option == 'month':
            ttsAudio = generate(text=f'If you were born in {choice}, it means you are {trait}.', voice="Michael", model="eleven_monolingual_v1")
        elif option == 'color':
            ttsAudio = generate(text=f'If your favorite color is {choice}, it means you are {trait}.', voice="Michael", model="eleven_monolingual_v1")
        else:
            raise SystemExit(0)

        save(ttsAudio, 'tts.mp3')
        ttsClip = AudioFileClip('tts.mp3')
        ttsClip = ttsClip.set_start(i * unit)
        tts.append(ttsClip)

        if option == 'name':
            clips += subtitleGenerator("if your NAME starts with", 72, 'red', i * unit, unit, 200 - 960)
        elif option == 'month':
            clips += subtitleGenerator("if you were BORN in", 72, 'red', i * unit, unit, 200 - 960)
        elif option == 'color':
            clips += subtitleGenerator("if your favorite COLOR is", 72, 'red', i * unit, unit, 200 - 960)
        else:
            raise SystemExit(0)

        if option == 'color':
            if choice == 'black':
                clips += subtitleGenerator(choice, 94, choice, i * unit + 0.5, unit - 0.5, 375 - 960, strokeColor='white')
            else:
                clips += subtitleGenerator(choice, 94, choice, i * unit + 0.5, unit - 0.5, 375 - 960)
        else:
            clips += subtitleGenerator(choice, 94, 'green', i * unit + 0.5, unit - 0.5, 375 - 960)

        clips += subtitleGenerator("it means YOU are", 72, 'red', i * unit, unit, 568 - 960)

        if option == 'color':
            if choice == 'black':
                clips += subtitleGenerator(trait, 86, choice, i * unit + 1.5, unit - 1.5, 750 - 960, strokeColor='white')
            else:
                clips += subtitleGenerator(trait, 86, choice, i * unit + 1.5, unit - 1.5, 750 - 960)
        else:
            clips += subtitleGenerator(trait, 86, 'white', i * unit + 1.5, unit - 1.5, 750 - 960)

    clips += subtitleGenerator("comment what I should do NEXT!", 72, 'cyan', 0, length, 400)

    with open("outros.txt", 'r') as f:
        outros = f.readline()
    outros = outros.split()

    outro = random.choice(outros).replace("_", " ")
    ttsAudio = generate(text=f'Send this video to a friend who {outro}!', voice="Michael", model="eleven_monolingual_v1")

    save(ttsAudio, 'tts.mp3')
    ttsClip = AudioFileClip('tts.mp3')
    ttsClip = ttsClip.set_start(length - unit)
    tts.append(ttsClip)

    clips += subtitleGenerator("send this video to a friend who", 72, 'red', length - unit, unit, 325 - 960)
    clips += subtitleGenerator(outro, 86, 'yellow', length - unit, unit, 650 - 960)

    return CompositeVideoClip(clips), CompositeAudioClip(tts)


def gameplayClip(length):
    gameplay = VideoFileClip(f'cars/car{random.randint(1, 7)}.mp4')
    startTime = random.uniform(0, gameplay.duration - length)
    gameplay = gameplay.subclip(startTime, startTime + length)
    gameplay = gameplay.resize((1080, 960))
    gameplay = gameplay.fx(vfx.lum_contrast, lum=1.3, contrast=1.1, contrast_thr=100)
    gameplay = gameplay.fl_image(lambda frame: cv2.GaussianBlur(frame, (0, 0), sigmaX=0.4, sigmaY=0.4))
    gameplay = gameplay.volumex(0)

    return gameplay


def musicClip(length):
    music = AudioFileClip(f'music/song{random.randint(1, 14)}.mp3')
    if music.duration < length:
        music = musicClip(length)

    music = music.subclip(0, length)
    music = audio_normalize.audio_normalize(music).volumex(0.1)

    return music


def addonsClips():
    watermark = TextClip("psychology outer", font='Hindsight', fontsize=84, color='white', stroke_color='black', stroke_width=8, method='caption', size=(1080, 1920))
    watermark = watermark.set_opacity(0.8)
    watermark = watermark.set_position((540 - int(watermark.size[0] / 2), 75))

    return watermark


def transform(facts, unit, option):
    length = unit * (facts + 1)

    background = backgroundClip(length)
    subtitles, tts = subtitlesClips(length, unit, facts, option)
    gameplay = gameplayClip(length)
    music = musicClip(length)
    watermark = addonsClips()

    final = clips_array([[background], [gameplay]])
    final = final.resize((1080, 1920))
    final = final.set_duration(length)

    final = CompositeVideoClip([final, subtitles, watermark])
    final = final.set_duration(length)
    final = final.resize((1080, 1920))

    final = final.set_audio(CompositeAudioClip([music, tts]))

    final.write_videofile("final.mp4", threads=200, fps=24)
