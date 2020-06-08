import numpy as np
import matplotlib.pyplot as plt
import wavio


class Waveform:
    def __init__(self, points, sample_rate=44100):
        '''
        Parameters
        ----------
        points : list of floats
            The points of this waveform
        sample_rate : int
            The sample rate for this waveform
        '''
        self.points = points
        self.sample_rate = sample_rate
        
    
    @staticmethod
    def add(waveform_1, waveform_2):
        '''
        Adds two waveforms together. Both waveforms must have the same duration
        and number points
        
        Parameters
        ----------
        waveform1, waveform2 : Waveform
            The waveforms to add together
        
        Returns
        -------
        Waveform
            The resulting waveform
        '''
        if len(waveform_1.points) != len(waveform_2.points):
            raise Exception(f'Waveforms cannot be added with lengths: {len(waveform_1.points)}, {len(waveform_2.points)}')
            
        if len(waveform_1.points) != len(waveform_2.points):
            raise Exception(f'Waveforms cannot be added with different durations: {waveform_1.duration}, {waveform_2.duration}')
            
        points = waveform_1.points + waveform_2.points
        return Waveform(points, waveform_1.duration)
    
    
    def plot(self, title):
        '''
        Parameters
        ----------
        title : str
            The title of the plot
        '''
        total_ms = len(self.points) / self.sample_rate * 1000
        samples = len(self.points)
        
        # Set up plot
        fig, ax = plt.subplots()
        
        # Set x ticks & labels
        num_ticks = 9
        plt.xticks(np.linspace(0, samples-1, num_ticks)) # samples-1 here to fix issue where last tick doesn't show
        ax.set_xticklabels([round(x, 1) for x in np.linspace(0, total_ms, num_ticks)])
        
        # Add padding to y-axis (I think it looks better when it's not all stretched out)
        ymin = min(self.points) * 1.8
        ymax = max(self.points) * 1.8
        ax.set_ylim([ymin,ymax])
        
        # Set titles & labels
        plt.title(title, fontsize=18)
        plt.xlabel('Time (ms)', fontsize=14)
        plt.ylabel('Amplitude', fontsize=14)
        
        plt.margins(x=0)
        plt.plot(self.points)

    
    def to_wav(self, filename):
        '''
        Creates a .wav file in the /audio folder
        
        Parameters
        ----------
        filename : str
            The name of the wav file
        '''
        wavio.write(f'audio/{filename}', self.points, self.sample_rate, sampwidth=4)
