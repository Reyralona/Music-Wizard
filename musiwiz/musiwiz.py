import random
from play import play_note
from time import sleep
from numpy import roll
import os
import copy

class Musiwiz:

    CHROMATIC_SCALE_SHARPS = {
        'oct1' : ['c1','c#1','d1','d#1','e1','f1','f#1','g1','g#1','a1','a#1','b1'],
        'oct2' : ['c2','c#2','d2','d#2','e2','f2','f#2','g2','g#2','a2','a#2','b2'],
        'oct3' : ['c3','c#3','d3','d#3','e3','f3','f#3','g3','g#3','a3','a#3','b3'],
        'oct4' : ['c4']
    }
    CHROMATIC_SCALE_FLATS = {
        'oct1' : ['c1', 'db1', 'd1', 'eb1', 'e1', 'f1', 'gb1', 'g1', 'ab1','a1', 'bb1', 'b1'],
        'oct2' : ['c2', 'db2', 'd2', 'eb2', 'e2', 'f2', 'gb2', 'g2', 'ab2','a2', 'bb2', 'b2'],
        'oct3' : ['c3', 'db3', 'd3', 'eb3', 'e3', 'f3', 'gb3', 'g3', 'ab3','a3', 'bb3', 'b3'],
        'oct4' : ['c4']
    }

    INTERVALS = {"u": 0,"min2": 1,"maj2": 2,"min3": 3,"maj3" : 4,"p4": 5,"trit": 6,"p5": 7,"m6": 8
    ,"maj6": 9,"min7": 10,"maj7": 11,"oct": 12,"min9": 13,"9": 14,"#9": 15,"min10": 16,"11": 17
    ,"#11": 18,"12": 19,"b13": 20,"13": 21,"#13": 22,"b15": 23,"15": 24
    }

    STRUCTURES = {
        'triads' : {"5" : ["u", "p5"],
                    "major": ["u", "maj3", "p5"],
                    "minor": ["u", "min3", "p5"],
                    "diminished": ["u", "min3", "trit"],
                    "diminished 5th": ["u", "maj3", "trit"],
                    "augmented": ["u", "maj3", "m6"],
                    "suspended 4th": ["u", "p4", "p5"],
                    "suspended 2th": ["u", "maj2", "p5"]
        },

        'tetrads' : {"dominant 7th": ["u", "maj3", "p5", "min7"],
                    "minor 7th": ["u", "min3", "p5", "min7"],
                    "major 7th": ["u", "maj3", "p5", "maj7"],
                    "minor major 7th": ["u", "min3", "p5", "maj7"],
                    "suspended 7th": ["u", "p4", "p5", "min7"],
                    "augmented 7th": ["u", "maj3", "m6", "min7"],
                    "augmented major 7th": ["u", "maj3", "m6", "maj7"],
                    "7th augmented ninth": ["u", "maj3", "p5", "min7", "min10"],
                    "half diminished 7th": ["u", "min3", "trit", "min7"],
                    "major 7th 11" : ["u", "maj3", "p4", "maj7"],
                    "major 7th #11th" : ["u", "maj3", "trit", "maj7"],
                    "minor major 7th #11th" : ["u", "min3", "trit", "maj7"],
                    "dominant 7th #11th" : ["u", "maj3", "trit", "min7"],
                    "diminished 7th": ["u", "min3", "trit", "maj6", "min7"],
                    "7th diminished 5th": ["u", "maj3", "trit", "m6"],
                    "7th flat nine": ["u", "maj3", "p5", "m6", "9"],
                    "6" : ["u", "maj3", "p5", "maj6"],
                    "minor 6th": ["u", "min3", "p5", "maj6"],
                    "6/9" : ["u", "maj3", "p5", "maj6", "9"],
                    "major 9th": ["u", "maj3", "p5", "maj7", "9"],
                    "minor 9th": ["u", "min3", "p5", "min7", "9"],
                    "dominant 9th": ["u", "maj3", "p5", "min7", "9"],
                    "11th" : ["u", "maj3", "p5", "min7", "9", "11"],
                    "minor 11th": ["u", "min3", "p5", "min7", "9", "11"],
                    "13th" : ["u", "maj3", "p5", "min7", "9", "11", "13"],
                    "minor 13th" : ["u", "min3", "p5", "min7", "9", "11", "13"],
                    "major 13th" : ["u", "maj3", "p5", "maj7", "9", "11", "13"],
                    "add9" : ["u", "maj3", "p5", "9"],
                    "add2" : ["u", "maj2", "maj3", "p5"],
                    "add4" : ["u", "maj3", "p4", "p5"],
                    "add11": ["u", "maj3", "p5", "11"]
        }
    }

    class Chord:

        

        def __init__(self, notes, chord_name=""):
            self.notes = notes
            self.chord_name = chord_name

        def play(self, delay=0):
            for note in output:
                play_note(note)
                sleep(delay)
            sleep(2)

        ##############################################

        def all_possible_chords():

            global all_possible_chords
            all_possible_chords = {}

            flats = (sum(Musiwiz.CHROMATIC_SCALE_FLATS.values(), []))
            sharps = (sum(Musiwiz.CHROMATIC_SCALE_SHARPS.values(), []))

            

            # generate all possible flat chords 
            for tonic in flats:
                for triad_name, triad_intervals in Musiwiz.STRUCTURES['triads'].items():
                    all_possible_chords[(tonic[:-1], triad_name)] = Musiwiz.Chord.create_chord(tonic[:-1], triad_name)
            for tonic in flats:
                for tetrad_name, tetrad_intervals in Musiwiz.STRUCTURES['tetrads'].items():
                    all_possible_chords[(tonic[:-1], tetrad_name)] = Musiwiz.Chord.create_chord(tonic[:-1], tetrad_name)

            # generate all possible sharp chords 
            for tonic in sharps:
                for triad_name, triad_intervals in Musiwiz.STRUCTURES['triads'].items():
                    all_possible_chords[(tonic[:-1], triad_name)] = Musiwiz.Chord.create_chord(tonic[:-1], triad_name)
            for tonic in sharps:
                for tetrad_name, tetrad_intervals in Musiwiz.STRUCTURES['tetrads'].items():
                    all_possible_chords[(tonic[:-1], tetrad_name)] = Musiwiz.Chord.create_chord(tonic[:-1], tetrad_name)

            return all_possible_chords

        ##############################################

        def create_chord(tonic, chord_type):
            
            flats = sum(Musiwiz.CHROMATIC_SCALE_FLATS.values(), [])
            sharps = sum(Musiwiz.CHROMATIC_SCALE_SHARPS.values(), [])

            if tonic + '1' in flats:
                scale = flats
            elif tonic + '1' in sharps:
                scale = sharps
            else: scale = random.choice([flats, sharps])

        
            if chord_type in Musiwiz.STRUCTURES['triads'].keys():
                structure = Musiwiz.STRUCTURES['triads'][chord_type]
            elif chord_type in Musiwiz.STRUCTURES['tetrads'].keys():
                structure = Musiwiz.STRUCTURES['tetrads'][chord_type]

            interval_indexes = []
            output = []
            

            for interval in structure:
                if interval in Musiwiz.INTERVALS.keys():
                    interval_indexes.append(Musiwiz.INTERVALS[interval])

            scale = (scale[scale.index(tonic + '1'):])
            

            for each in interval_indexes:
                output.append(scale[each])

            return output

        ##############################################

        def flat_or_sharp(self):
            # CHECK FOR '#' OR 'b'

            notes = list(self.notes)
            scale_type = ""
            for each in notes:
                if len(each) == 2:
                    if list(each[1]) == ['b']:
                        scale_flat_or_sharp = Musiwiz.CHROMATIC_SCALE_FLATS
                        scale_type = 'flat'
                        break
                    elif list(each[1]) == ['#']:
                        scale_flat_or_sharp = Musiwiz.CHROMATIC_SCALE_SHARPS
                        scale_type = 'sharp'
                        break
                else:
                    scale_flat_or_sharp = random.choice([Musiwiz.CHROMATIC_SCALE_SHARPS,Musiwiz.CHROMATIC_SCALE_FLATS])

            return copy.deepcopy(scale_flat_or_sharp)

        ##############################################

        def intervals(self):

            global out_newscale
            out_newscale = [] # for calculating intervals later
        
            scale = self.flat_or_sharp() # copy of original list
            newscale = []
            
        
            offset = scale['oct1'].index(self.notes[0] + '1') # calculate offset based on first note
            newscale = scale['oct1'][offset:], scale['oct2'], scale['oct3'], scale['oct4']
            out_newscale = sum(newscale, [])
            newscale_no_nums = []
            
            
            for octave in newscale:
                newscale_no_nums.append(octave)
            for octave in newscale_no_nums:
                for note in octave:
                    octave[octave.index(note)] = note[:-1] 


            global output #assign correct note values, requires octaves separated in lists
            output = []
            counter = 0
            octave_counter = 0
        
            try:
                # FOR NUMBER OF NOTES 
                for i in range(len(self.notes)):
                    # FOR OCTAVE, CALCULATE THE STEPS
                    for steps, octave_note in enumerate(newscale[octave_counter]):
                        # IF USER note == note FROM OCTAVE
                        if self.notes[counter] == octave_note:
                            # APPEND THE note EQUIVALENT OF INDEX (STEPS) + 1 FOR CORRECT OCTAVE 
                            output.append(newscale[octave_counter][steps] + str(octave_counter + 1))
                            counter += 1
                    octave_counter += 1
            except:
                pass

            return output

        ##############################################

        def get_chord_by_notes(self): 

            interval_indexes = []
            interval_output = []

            for index, note in enumerate(out_newscale):
                for user_note in output:
                    if user_note == note:
                        interval_indexes.append(index)

            for interval in interval_indexes:
                for interval_name, interval_count in Musiwiz.INTERVALS.items():
                    if interval == interval_count:
                        interval_output.append(interval_name)

            if interval_output in Musiwiz.STRUCTURES['triads'].values() or Musiwiz.STRUCTURES['tetrads'].values():
                for chord_name, structure in Musiwiz.STRUCTURES['triads'].items():
                    if interval_output == structure:
                        return f'{self.notes[0]} {chord_name}'
                for chord_name, structure in Musiwiz.STRUCTURES['tetrads'].items():
                    if interval_output == structure:
                        return f'{self.notes[0]} {chord_name}'
            return ' '.join(interval_output)

        ##############################################

#Musiwiz.Chord.all_possible_chords()
#
#for chord, notes in Musiwiz.Chord.all_possible_chords().items():
#    chord = " ".join(list(map(str.capitalize, chord)))
#    notes = " - ".join(list(map(str.title, notes)))
#    print(f'{chord:<30} {notes}')
#    sleep(0.01)


c1 = Musiwiz.Chord(notes=['c','e','g','b'])
c1.intervals()
print(c1.get_chord_by_notes())
c1.play(delay=0.1)
#c1.play(delay=0.4)

