from play import play_note
from time import sleep
from os import system
from db import *
from numpy import roll as nproll
from itertools import permutations as ipermu

class Chord: 
    def __init__(self, notes, *type):
        self.notes = notes
        self.tonic = self.notes[0]
        #newScale = CHROMATIC_SCALE[CHROMATIC_SCALE.index(tonic):] + CHROMATIC_SCALE * 2 + CHROMATIC_SCALE[:CHROMATIC_SCALE.index(tonic)] + [tonic]
    
    def sharpOrFlat(self):
        # scale cannot contain the same note twice, e.g: e, eb | d, d#
        pass

    def generateChromatic(tonic):
        if type(tonic) == list:
            for note in tonic:
                if note.find("#") != -1:
                    sharp_or_flat = "sharps"
                    break
                sharp_or_flat = "flats"
      
        elif type(tonic) == str:
            sharp_or_flat = "sharps" if "#" in tonic else "flats"

        tonic = tonic[0]
        scale = CHROMATIC_SCALES[sharp_or_flat]
        return Chord.separateOctaves(scale[scale.index(tonic):] + scale[1:] * 2)

    def generateScale(tonic, scaleType):
        out = []
        intervals = []
        scale = Chord.generateChromatic()

        for interval in SCALES[scaleType]:
            intervals.append(INTERVALS[interval])
        for each in intervals:
            out.append(scale[each])
        return out, scale
    
    def separateOctaves(notes):
        out = [notes[0] + '1']
        octave_counter = 1
        for note in (notes[1:]):
            if note == 'c':
                octave_counter += 1
            out.append(note + str(octave_counter)) 
        return out
            
    def splitOctavesLists(tonic):
        scale = Chord.generateChromatic(tonic)
        numberofoctaves = scale[-1][-1:]

        octaveDict = {}

        for i in range(1, int(numberofoctaves) + 1):
            octaveDict[str(i)] = []

        for note in scale:
            octaveDict[note[-1:]].append(note)
        
        return octaveDict

    def play(self, delay=0):
        for note in Chord.separateOctaves(self.notes)[0]:
            try:
                play_note(note)
                sleep(delay)
            except:
                pass
        sleep(2)

    def printAllScales():
        for note in CHROMATIC_SCALES['sharps']:
            for scale in SCALES.keys():
                sharpScales = Chord.generateScale(note, scale)
                print(note.title(), scale.title(), "Scale: \n", " - ".join([note[:-1].title() for note in sharpScales]))
        for note in CHROMATIC_SCALES['flats']:
            for scale in SCALES.keys():
                flatScales = Chord.generateScale(note, scale)
                print(note.title(), scale.title(), "Scale: \n", " - ".join([note[:-1].title() for note in flatScales]))

    def assignIntervals(notes):
        chromatic = Chord.generateChromatic(notes)
        octaves = list(Chord.splitOctavesLists(notes).values())
        
        mynotes = []
    
        counter = 0
        octave_counter = 0
        for octave in octaves:
            for i in range(len(octave)):
                octave[i] = octave[i][:-1]

        try:
            # FOR NUMBER OF NOTES 
            for i in range(len(notes)):
                # FOR OCTAVE, CALCULATE THE STEPS
                for steps, octave_note in enumerate(octaves[octave_counter]):
                    # IF USER note == note FROM OCTAVE
                    if notes[counter] == octave_note:
                        # APPEND THE note EQUIVALENT OF INDEX (STEPS) + 1 FOR CORRECT OCTAVE 
                        mynotes.append(octaves[octave_counter][steps] + str(octave_counter + 1))
                        counter += 1
                octave_counter += 1
        except:
                pass     
                
        intervalNameIndex = {}
        
        #assign intervals
        for note in mynotes:
            for iname, ivalue in INTERVALS.items():
                if ivalue == chromatic.index(note):
                    intervalNameIndex[note] = iname

        return intervalNameIndex

    def findChord(notes):
        intervals = list(Chord.assignIntervals(notes).values())
        tonic = notes[0]
        outputString = []

        for name, structure in STRUCTURES['triads'].items():
            if intervals == structure:
                outputString.append(tonic)
                outputString.append(name)
        
        for name, structure in STRUCTURES['tetrads'].items():
            if intervals == structure:
                outputString.append(tonic)
                outputString.append(name)

        if outputString:
            return outputString
        
    def chordConstructor(notes):

        outputString = Chord.findChord(notes)    
    
        if outputString:
            return outputString
        else:
            # construct
            for inversion in Chord.tryInversions(notes):
                out = Chord.findChord(inversion)
                if out:
                    return out

            return Chord.assignIntervals(notes)


    def tryInversions(notes):

        inversions = []

        for i in range(1, 100):
            out = (list(nproll(notes, i)))
            if out == notes:
                break
            inversions.append(out)

        for perm in ipermu(notes):
            perm = list(perm)
            if perm == notes:
                pass
            else:
                inversions.append(perm)
            
        return inversions
    


#print(Chord.chordConstructor(chord.notes))
#print(Chord.tryInversions(['c','e','g','b']))
print(Chord.chordConstructor(['a','c','g','e',]))
