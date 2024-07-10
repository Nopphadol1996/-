from songline import Sendline

token = 'oT5OnnE9KCFQW1Ygl18nro08FrLnMBXiTZJpkHssDHW'
messenger = Sendline(token)

#send message
# messenger.sendtext('Hello world')

# #send sticker
# messenger.sticker(12,1)

#send image
messenger.sendimage('https://cdn.pixabay.com/photo/2017/09/01/00/15/png-2702691_640.png')