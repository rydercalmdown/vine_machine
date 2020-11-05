import os
import subprocess
import random
import time
import RPi.GPIO as GPIO


def get_vines():
    """Returns a list of all vines"""
    audio_dir = '/home/pi/vine_machine/audio'
    list_of_vines = []
    for file in os.listdir(audio_dir):
        if file.endswith('.mp3'):
            list_of_vines.append(os.path.join(audio_dir, file))
    return list_of_vines


def play_vine():
    random_vine = random.choice(get_vines())
    print('playing vine {}'.format(random_vine))
    subprocess.call(['mpg321', random_vine], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def listen_for_switch_pull():
    """Continuously listens for state change of GPIO"""
    pin_number = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
        while True:
            pin_current = GPIO.input(pin_number)
            if pin_current == 1:
                play_vine()
            else:
                play_vine()
            while GPIO.input(pin_number) == pin_current:
                # waits until the state changes
                time.sleep(0.5)
    except KeyboardInterrupt:
	    GPIO.cleanup()


listen_for_switch_pull()
