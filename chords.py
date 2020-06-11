from waveform import Waveform
from chord import Chord
from note import Note
import helpers


# Create a chord using a root and quality
chord = Chord(root='C4', quality='major')


# Create a chord with named notes
notes = helpers.get_notes_by_name(['A3', 'B5', 'C7'])
chord = Chord(notes=notes)


# Create a chord with notes of any frequency
notes = helpers.create_notes_with_frequencies([200, 250, 300])
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


# Random test chords
chord = Chord(root='C4', quality='dominant_11th')

notes = [Note(frequency=100, velocity=1),
         Note(frequency=200, velocity=0.5),
         Note(frequency=300, velocity=1),
         Note(frequency=400, velocity=0.5),
         Note(frequency=500, velocity=1)]
chord = Chord(notes=notes)


notes = [Note(frequency=100, velocity=3),
         Note(frequency=200, velocity=0.25),
         Note(frequency=300, velocity=2),
         Note(frequency=400, velocity=0.5),
         Note(frequency=500, velocity=1)]
chord = Chord(notes=notes)


notes = [Note(frequency=100, velocity=9),
         Note(frequency=200, velocity=0.25),
         Note(frequency=300, velocity=3),
         Note(frequency=400, velocity=0.25),
         Note(frequency=500, velocity=1)]
chord = Chord(notes=notes)


notes = [Note(frequency=50, velocity=7),
         Note(frequency=150, velocity=3),
        Note(frequency=450, velocity=1)]
chord = Chord(notes=notes)


notes = helpers.create_notes_with_frequencies([100, 100, 200, 300, 500, 800, 1300])
chord = Chord(notes=notes)



chord1 = Chord(notes=[Note(frequency=100)])
chord2 = Chord(notes=[Note(frequency=300)])

sample_rate = 44100
duration = 0.05

waveform1 = chord1.get_waveform(sample_rate, duration)
waveform2 = chord2.get_waveform(sample_rate, duration)
waveform = Waveform.add(waveform1, waveform2)

#waveform1

#waveform = chord.get_waveform(sample_rate, duration)
waveform1.plot('Frequency = 100')
waveform2.plot('Frequency = 300')
waveform.plot('Added waveforms')
#waveform.to_wav(f'{chord.name}.wav')
waveform.to_wav(f'{chord.name}.wav')
