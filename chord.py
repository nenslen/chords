import helpers
import numpy as np
from waveform import Waveform


class Chord:
    def __init__(self, root=None, quality=None, name='', notes=None):
        '''
        Parameters
        ----------
        root : str
            The root note of this chord. eg) 'C#4'
        quality : str
            The quality of this chord. eg) 'major'
        notes : list of Note
            Used instead of root/quality if given
        '''
        self.root = root
        self.quality = quality
        self.name = name
        
        self.notes = []
        if notes is None:
            # Assign notes using root/quality
            root_note = helpers.get_note_by_name(self.root)
            
            for offset in helpers.qualities[self.quality]:
                note_number = root_note.number + offset
                note = helpers.get_note_by_number(note_number)
                self.notes.append(note)
                
            # Generate name if not already given
            if name == '':
                self.name = f'{root} {quality}'
        else:
            # Or just use notes if they're given
            self.notes = notes

    
    def get_waveform(self, sample_rate=44100, duration=4):
        '''
        Parameters
        ----------
        sample_rate : int
            How many points will represent the waveform per second
        duration : float
            How long, in seconds, the waveform will be
        
        Returns
        -------
        Waveform
            The waveform for this chord
        '''
        total_samples = sample_rate * duration
        step = duration / total_samples
        index = 0
        for note in self.notes:
            
            t = np.arange(0, duration, step)
            x = np.sin(2 * np.pi * note.frequency * t)

            if index == 0:
                points = np.sin(x) * note.velocity
            else:
                points += np.sin(x) * note.velocity 
        
            index += 1
            
        return Waveform(points, sample_rate)
        
        
    def print_info(self):
        print(self.quality)
        print(self.note_names)
        print(self.note_frequencies)
