import matplotlib.pyplot as plt
from chord import Chord
from note import Note
import helpers


plt.style.use('ggplot')


# Create a chord using a root and quality
root = 'C4'
quality = 'major'
title = f'{root}_{quality}'
chord = Chord(root, quality)


# Create a chord with named notes
notes = helpers.get_notes_by_names(['A3', 'B5', 'C7'])
chord = Chord(notes=notes)


# Create a chord with notes of any frequency
notes = [Note(frequency=200),
         Note(frequency=250),
         Note(frequency=300)]
chord = Chord(notes=notes)


# Create a chord with notes of any frequency & velocity, this creates a sawtooth wave
notes = [Note(frequency=100, velocity=1),
         Note(frequency=200, velocity=0.5),
         Note(frequency=300, velocity=0.35),
         Note(frequency=400, velocity=0.3),
         Note(frequency=500, velocity=0.25),
         Note(frequency=600, velocity=0.2),
         Note(frequency=700, velocity=0.18),
         Note(frequency=800, velocity=0.15),
         Note(frequency=900, velocity=0.12),
         Note(frequency=1000, velocity=0.09)]
chord = Chord(notes=notes)


sample_rate = 44100
duration = 3
title = 'Cool Chord'

waveform = chord.get_waveform(sample_rate, duration)
waveform.plot(title)
waveform.to_wav(f'{title}.wav')


chord = Chord('B8', 'major')