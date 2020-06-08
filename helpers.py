import pandas as pd
from note import Note


def get_note_by_name(note_name):
    '''
    Parameters
    ----------
    note_name : str
        The name of the note to get. eg) 'C#4'
        
    Returns
    -------
    Note
        The note corresponding to the given name
    '''
    n = notes_df[notes_df['name'] == note_name]
    
    if n.shape[0] == 0:
        # Check alt_name if no match
        n = notes_df[notes_df['alt_name'] == note_name]
    
    if n.shape[0] == 0:
        raise Exception(f'No note found with name: {note_name}')
    
    n = n.iloc[0]    
    note = Note(n['number'], n['name'], n['alt_name'], n['frequency'])
    return note


def get_notes_by_names(note_names):
    '''    
    Parameters
    ----------
    note_names : list of str
        The names of the notes to get. eg) ['Ab3', 'C#4', 'G5']
        
    Returns
    -------
    list of Note
        The notes corresponding to the given names
    '''
    notes = []
    for note_name in note_names:
        notes.append(get_note_by_name(note_name))
    return notes


def get_note_by_number(note_number):
    '''
    Parameters
    ----------
    note_number : str
        The number of the note to get. eg) 4
        
    Returns
    -------
    Note
        The note corresponding to the given number
    '''
    n = notes_df[notes_df['number'] == note_number]
    
    if n.shape[0] == 0:
        raise Exception(f'No note found with number: {note_number}')
    
    n = n.iloc[0]
    note = Note(n['number'], n['name'], n['alt_name'], n['frequency'])
    return note
    

notes_df = pd.read_csv('notes.csv')

qualities = {
    'major':            (0, 4, 7),
    'minor':            (0, 3, 7),
    'diminished':       (0, 3, 6),
    'major_seventh':    (0, 4, 7, 11),
    'minor_seventh':    (0, 3, 7, 10),
    'dominant_seventh': (0, 4, 7, 10),
    'suspended_2':      (0, 2, 7),
    'augmented_4':      (0, 4, 7),
    'dream':            (0, 5, 6, 7),
    'magic':            (0, 1, 5, 6, 10, 12, 15, 17),
    'mystic':           (0, 6, 10, 16, 21, 26)
}
