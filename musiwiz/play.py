from pygame import mixer
from time import sleep

mixer.init()
mixer.set_num_channels(40)
def play_note(note, delay=0):
    sleep(delay)
    engage = mixer.Sound(f'musiwiz/notes/{note.title()}.wav')
    return mixer.Sound.play(engage)



