#!/usr/bin/python
# -*- coding: utf-8 -*-
# ^^^ The above line specify the encoding of the unicode string (u"__some_unicode_string__") in python

from gtts import gTTS

file_list = list()
en_list = list()
zh_list = list()
#-------------------------------#
# Turn right


#-------------------------------#



mp3_fp = BytesIO()
tts = gTTS('Hello, this is a Google tts directly from your computer.')
# tts = gTTS(text= u'嗨，你好嗎? 9 4 8 7 9 4 狂', lang='zh')

# Save to file
tts.save("test.mp3")
