<<<<<<< HEAD
<<<<<<< HEAD
from translation import translate_Vi_En
import speech_recognition as sr
import sys

# Force UTF-8 output in terminal
sys.stdout.reconfigure(encoding='utf-8')

# Initialize recognizer
r = sr.Recognizer()

# Vietnamese characters for language detection
VI_CHARS = (
    "ăâđêôơưÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÉÈẺẼẸÊẾỀỂỄỆ"
    "ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÍÌỈĨỊÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
    "áàảãạăắằẳẵặâấầẩẫậđéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵ"
)


def guess_language(text: str) -> str:
    """
    Guess whether the given text is Vietnamese or English.

    Args:
        text (str): The input text to check.

    Returns:
        str: "vi" if text contains Vietnamese characters, "en" otherwise.
    """
    # Check if any character in the text is a Vietnamese character
    for ch in text:
        if ch in VI_CHARS:
            return "vi"

    # Default to English if no Vietnamese characters are found
    return "en"


def listen() -> str | None:
    """
    Listen to microphone input and detect speech in English or Vietnamese.

    The function:
    1. Captures audio from the microphone.
    2. Uses Google Speech Recognition to convert speech to text.
    3. Detects the language using `guess_language`.
    4. Prints the text in its original language.
    5. If the language is Vietnamese, also prints the English translation.

    Returns:
        str | None: The recognized text in lowercase, or None if no speech
        could be recognized.
    """
    with sr.Microphone() as source:
        # Adjust for ambient noise (makes recognition more accurate)
        r.adjust_for_ambient_noise(source, duration=0.6)

        # Listen for the first phrase (blocking call)
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        # show_all=True returns detailed info including alternatives
        result = r.recognize_google(
            audio, language="vi-VN,en-US", show_all=True)

        if not result:
            print("No speech detected")
            return None

        # Take the best alternative (highest confidence)
        best = result["alternative"][0]
        text = best["transcript"]

        # Detect language using Vietnamese character check
        lang = guess_language(text)

        # Print based on detected language
        if lang == "en":
            print("English:", text)
        elif lang == "vi":
            print("Vietnamese:", text)
            # Translate Vietnamese to English
            print("English:", translate_Vi_En(text))
        else:
            print("Unknown language:", text)

        # Return text in lowercase for consistency
        return text.lower()

    except sr.UnknownValueError:
        # Speech was unintelligible
        return None
    except sr.RequestError:
        # API request failed
        print("API unavailable")
        return None
=======
from translation import translate_Vi_En
import speech_recognition as sr
import sys

# Force UTF-8 output in terminal
sys.stdout.reconfigure(encoding='utf-8')

# Initialize recognizer
r = sr.Recognizer()

# Vietnamese characters for language detection
VI_CHARS = (
    "ăâđêôơưÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÉÈẺẼẸÊẾỀỂỄỆ"
    "ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÍÌỈĨỊÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
    "áàảãạăắằẳẵặâấầẩẫậđéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵ"
)


def guess_language(text: str) -> str:
    """
    Guess whether the given text is Vietnamese or English.

    Args:
        text (str): The input text to check.

    Returns:
        str: "vi" if text contains Vietnamese characters, "en" otherwise.
    """
    # Check if any character in the text is a Vietnamese character
    for ch in text:
        if ch in VI_CHARS:
            return "vi"

    # Default to English if no Vietnamese characters are found
    return "en"


def listen() -> str | None:
    """
    Listen to microphone input and detect speech in English or Vietnamese.

    The function:
    1. Captures audio from the microphone.
    2. Uses Google Speech Recognition to convert speech to text.
    3. Detects the language using `guess_language`.
    4. Prints the text in its original language.
    5. If the language is Vietnamese, also prints the English translation.

    Returns:
        str | None: The recognized text in lowercase, or None if no speech
        could be recognized.
    """
    with sr.Microphone() as source:
        # Adjust for ambient noise (makes recognition more accurate)
        r.adjust_for_ambient_noise(source, duration=0.6)

        # Listen for the first phrase (blocking call)
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        # show_all=True returns detailed info including alternatives
        result = r.recognize_google(
            audio, language="vi-VN,en-US", show_all=True)

        if not result:
            print("No speech detected")
            return None

        # Take the best alternative (highest confidence)
        best = result["alternative"][0]
        text = best["transcript"]

        # Detect language using Vietnamese character check
        lang = guess_language(text)

        # Print based on detected language
        if lang == "en":
            print("English:", text)
        elif lang == "vi":
            print("Vietnamese:", text)
            # Translate Vietnamese to English
            print("English:", translate_Vi_En(text))
        else:
            print("Unknown language:", text)

        # Return text in lowercase for consistency
        return text.lower()

    except sr.UnknownValueError:
        # Speech was unintelligible
        return None
    except sr.RequestError:
        # API request failed
        print("API unavailable")
        return None
>>>>>>> 57c02483a769b2b1c793f10614ac540529af5839
=======
from translation import translate_Vi_En
import speech_recognition as sr
import sys

# Force UTF-8 output in terminal
sys.stdout.reconfigure(encoding='utf-8')

# Initialize recognizer
r = sr.Recognizer()

# Vietnamese characters for language detection
VI_CHARS = (
    "ăâđêôơưÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÉÈẺẼẸÊẾỀỂỄỆ"
    "ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÍÌỈĨỊÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
    "áàảãạăắằẳẵặâấầẩẫậđéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵ"
)


def guess_language(text: str) -> str:
    """
    Guess whether the given text is Vietnamese or English.

    Args:
        text (str): The input text to check.

    Returns:
        str: "vi" if text contains Vietnamese characters, "en" otherwise.
    """
    # Check if any character in the text is a Vietnamese character
    for ch in text:
        if ch in VI_CHARS:
            return "vi"

    # Default to English if no Vietnamese characters are found
    return "en"


def listen() -> str | None:
    """
    Listen to microphone input and detect speech in English or Vietnamese.

    The function:
    1. Captures audio from the microphone.
    2. Uses Google Speech Recognition to convert speech to text.
    3. Detects the language using `guess_language`.
    4. Prints the text in its original language.
    5. If the language is Vietnamese, also prints the English translation.

    Returns:
        str | None: The recognized text in lowercase, or None if no speech
        could be recognized.
    """
    with sr.Microphone() as source:
        # Adjust for ambient noise (makes recognition more accurate)
        r.adjust_for_ambient_noise(source, duration=0.6)

        # Listen for the first phrase (blocking call)
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        # show_all=True returns detailed info including alternatives
        result = r.recognize_google(
            audio, language="vi-VN,en-US", show_all=True)

        if not result:
            print("No speech detected")
            return None

        # Take the best alternative (highest confidence)
        best = result["alternative"][0]
        text = best["transcript"]

        # Detect language using Vietnamese character check
        lang = guess_language(text)

        # Print based on detected language
        if lang == "en":
            print("English:", text)
        elif lang == "vi":
            print("Vietnamese:", text)
            # Translate Vietnamese to English
            print("English:", translate_Vi_En(text))
        else:
            print("Unknown language:", text)

        # Return text in lowercase for consistency
        return text.lower()

    except sr.UnknownValueError:
        # Speech was unintelligible
        return None
    except sr.RequestError:
        # API request failed
        print("API unavailable")
        return None
>>>>>>> 57c02483a769b2b1c793f10614ac540529af5839
