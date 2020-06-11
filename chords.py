from waveform import Waveform
from chord import Chord
from note import Note
import helpers


sample_rate = 44100
duration = 2

chord = Chord(root='C4', quality='major')

waveform = chord.get_waveform(sample_rate, duration)
waveform.plot(chord.name)
waveform.to_wav(f'{chord.name}.wav')
