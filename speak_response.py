<<<<<<< HEAD
import pyttsx3
import pygame

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 0.9)


def speak(text):
    # save current pygame music volume
    old_volume = pygame.mixer.music.get_volume()

    # temporarily lower the music volume (example: 40% of old volume)
    pygame.mixer.music.set_volume(old_volume * 0.4)

    # speak
    engine.say(text)
    engine.runAndWait()

    # restore old music volume
    pygame.mixer.music.set_volume(old_volume)
=======
import pyttsx3
import pygame

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 0.9)


def speak(text):
    # save current pygame music volume
    old_volume = pygame.mixer.music.get_volume()

    # temporarily lower the music volume (example: 40% of old volume)
    pygame.mixer.music.set_volume(old_volume * 0.4)

    # speak
    engine.say(text)
    engine.runAndWait()

    # restore old music volume
    pygame.mixer.music.set_volume(old_volume)
>>>>>>> 57c02483a769b2b1c793f10614ac540529af5839
