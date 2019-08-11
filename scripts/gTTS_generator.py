#!/usr/bin/python
# -*- coding: utf-8 -*-
# ^^^ The above line specify the encoding of the unicode string (u"__some_unicode_string__") in python

from gtts import gTTS
from io import BytesIO
import time


mp3_fp = BytesIO()
tts = gTTS('Hello, this is a Google tts directly from your computer.')
# tts = gTTS(text= u'嗨，你好嗎? 9 4 8 7 9 4 狂', lang='zh')

# Save to file
tts.save("test.mp3")
# Stream to play
tts.write_to_fp(mp3_fp)


mp3_fp.seek(0) # Important! Return the pointer to the head

"""
# The following code does not work
from playsound import playsound
playsound(mp3_fp)
"""

# pygame works; however, the CPU loading is quit high
import pygame
pygame.mixer.init()
pygame.mixer.music.load(mp3_fp)


while True:
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
#
