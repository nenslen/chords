# chords
 Create, visualize, and generate wav files for chords.

# Creating chords
There are a few different ways to create chords, depending on what you're doing.

### Create a chord using a root and quality
```python
chord = Chord(root='C4', quality='major')
```

### Create a chord with notes of any frequency
```python
notes = helpers.create_notes_with_frequencies([200, 250, 300])
chord = Chord(notes=notes)
```

### Create a chord with notes of any frequency & velocity
This example creates a sawtooth wave
```python
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
```


# Visualizing chords
Once you've created a chord, you might want to visualize it and see what it looks like. The waveforms you'll be generating here will most likely be hundreds or thousands of hertz, so you'll want a very short duration - this example is just 250ms!
```python
sample_rate = 44100
duration = 0.25

waveform = chord.get_waveform(sample_rate, duration)
waveform.plot(chord.name)
```


# Generating .wav files
```python
sample_rate = 44100
duration = 4

waveform = chord.get_waveform(sample_rate, duration)
waveform.to_wav(f'{chord.name}.wav')
```
