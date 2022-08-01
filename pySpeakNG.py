import json
import subprocess
import shlex
from pathlib import Path

HERE = Path(__file__).parent.resolve()

with open(HERE/'data/voices.json', 'r') as f:
    VOICES = json.load(f)

with open(HERE/'data/langs.json', 'r') as f:
    LANGUAGES = json.load(f)


def speak(text: str, language='en-us', voice='f1', pitch=50,
          speed=125, gap=10, amplitude=50, fp=None) -> None:
    """A thin wrapper around the eSpeak-NG speech synthesizer.

    Args:
        text (str, required): A string for eSpeak-NG to synthesize.
        language (str, optional): Language code for synth voice.
            Defaults to 'en-us'. See LANGUAGES for options.
        voice (str, optional): Synth voice model. Defaults to 'f1'.
            See VOICES for options.
        pitch (int, optional): Pitch adjustment, 0-99. The default
            of 50 is the default pitch for the selected voice.
        speed (int, optional): 25-250 words per minute.
            Defaults to 125.
        word_gap (int, optional): Pause between words, in units of
            10ms at the default speed. Defaults to 10 as 175wpm.
        amplitude (int, optional): 0-100. Defaults to 60. Don't blow
            your speakers.
        fp (path-like, optional): Location to save .wav file output of
            the synthesized speech. When present, audio is not played.
    """

    if fp:
        command = shlex.split(
            "espeak-ng -v{}+{} -p {} -s {} -g {} -a {} -w {} \"[[{}]]\""
            .format(language, voice, pitch, speed, gap, amplitude, fp, text)
        )
    else:
        command = shlex.split(
            "espeak-ng -v{}+{} -p {} -s {} -g {} -a {} \"[[{}]]\""
            .format(language, voice, pitch, speed, gap, amplitude, text)
        )
        subprocess.run(command)
