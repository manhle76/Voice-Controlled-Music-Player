<<<<<<< HEAD
import os
from mutagen.mp3 import MP3


def load_playlist(folder):
    """
    Scans the specified folder and returns a list of all MP3 file paths.

    Parameters:
    ----------
    folder : str
        The path to the folder containing MP3 files.

    Returns:
    -------
    list of str
        A list of full paths to MP3 files in the folder.

    Example:
    -------
    >>> load_playlist("C:/Music")
    ['C:/Music/song1.mp3', 'C:/Music/song2.mp3']
    """
    playlist = []
    for file in os.listdir(folder):
        if file.endswith("mp3"):
            playlist.append(os.path.join(folder, file))
    return playlist


def song_list(playlist):
    """
    Extracts and returns the names of songs from a playlist of MP3 file paths.

    Parameters:
    ----------
    playlist : list of str
        A list of MP3 file paths.

    Returns:
    -------
    list of str
        A list of song names without the ".mp3" extension.

    Example:
    -------
    >>> song_list(['C:/Music/song1.mp3', 'C:/Music/song2.mp3'])
    ['song1', 'song2']
    """
    name_song = []
    for path in playlist:
        filename = os.path.basename(path)
        name_song.append(filename.replace(".mp3", ""))
    return name_song


def convert_time(time):
    """
    Converts time in seconds to a tuple of minutes and seconds.

    Parameters:
    ----------
    time : int or float
        Time in seconds.

    Returns:
    -------
    tuple of int
        A tuple (minutes, seconds) representing the time.

    Example:
    -------
    >>> convert_time(125)
    (2, 5)
    """
    minute = int(time / 60)
    second = int(time % 60)
    return (minute, second)
=======
import os
from mutagen.mp3 import MP3


def load_playlist(folder):
    """
    Scans the specified folder and returns a list of all MP3 file paths.

    Parameters:
    ----------
    folder : str
        The path to the folder containing MP3 files.

    Returns:
    -------
    list of str
        A list of full paths to MP3 files in the folder.

    Example:
    -------
    >>> load_playlist("C:/Music")
    ['C:/Music/song1.mp3', 'C:/Music/song2.mp3']
    """
    playlist = []
    for file in os.listdir(folder):
        if file.endswith("mp3"):
            playlist.append(os.path.join(folder, file))
    return playlist


def song_list(playlist):
    """
    Extracts and returns the names of songs from a playlist of MP3 file paths.

    Parameters:
    ----------
    playlist : list of str
        A list of MP3 file paths.

    Returns:
    -------
    list of str
        A list of song names without the ".mp3" extension.

    Example:
    -------
    >>> song_list(['C:/Music/song1.mp3', 'C:/Music/song2.mp3'])
    ['song1', 'song2']
    """
    name_song = []
    for path in playlist:
        filename = os.path.basename(path)
        name_song.append(filename.replace(".mp3", ""))
    return name_song


def convert_time(time):
    """
    Converts time in seconds to a tuple of minutes and seconds.

    Parameters:
    ----------
    time : int or float
        Time in seconds.

    Returns:
    -------
    tuple of int
        A tuple (minutes, seconds) representing the time.

    Example:
    -------
    >>> convert_time(125)
    (2, 5)
    """
    minute = int(time / 60)
    second = int(time % 60)
    return (minute, second)
>>>>>>> 57c02483a769b2b1c793f10614ac540529af5839
