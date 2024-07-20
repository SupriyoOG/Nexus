
import pyttsx3
class TTS:
    engine = None

    @classmethod
    def get_engine(cls):
        if cls.engine is None:
            cls.engine = pyttsx3.init('sapi5')
            voices = cls.engine.getProperty('voices')
            cls.engine.setProperty('voice', voices[0].id)
            cls.engine.setProperty('rate', 170)
        return cls.engine
        
def speak(text):
    engine = TTS.get_engine()
    engine.say(text)
    engine.runAndWait()