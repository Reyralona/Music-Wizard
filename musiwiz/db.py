CHROMATIC_SCALES = {
    'sharps': ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b','c'],
    'flats' : ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b','c']
}

SCALES = {
    'ionian pentatonic'     : ['u', 'maj3', 'p4'  , 'p5'  , 'maj7', 'oct'],
    'dorian pentatonic'     : ['u', 'maj2', 'min3', 'p5'  , 'maj6', 'oct'],
    'phrygian pentatonic'   : ['u', 'min2', 'p4'  , 'p5'  , 'min7', 'oct'],
    'lydian pentatonic'     : ['u', 'maj2', 'maj3', 'trit', 'maj6', 'oct'],
    'mixolydian pentatonic' : ['u', 'maj3', 'p4'  , 'p5'  , 'min7', 'oct'],
    'locrian pentatonic'    : ['u', 'min3', 'p4'  , 'trit', 'min7', 'oct'],
    'minor pentatonic'      : ['u', 'min3', 'p4'  , 'p5'  , 'min7', 'oct'],
    'major pentatonic'      : ['u', 'maj2', 'maj3', 'p5'  , 'maj6', 'oct'],
    'major'                 : ['u', 'maj2', 'maj3', 'p4'  , 'p5'  , 'maj6', 'maj7',  'oct'],
    'minor'                 : ['u', 'maj2', 'min3', 'p4'  , 'p5'  , 'm6'  , 'min7',  'oct'],
    'harmonic minor'        : ['u', 'maj2', 'min3', 'p4'  , 'p5'  , 'm6'  , 'maj7',  'oct'],
    'melodic minor'         : ['u', 'maj2', 'min3', 'p4'  , 'p5'  , 'maj6', 'maj7',  'oct'],
    'dorian'                : ['u', 'maj2', 'min3', 'p4'  , 'p5'  , 'maj6', 'min7',  'oct'],
    'phrygian'              : ['u', 'min2', 'min3', 'p4'  , 'p5'  , 'm6'  , 'min7',  'oct'],
    'lydian'                : ['u', 'maj2', 'maj3', 'trit', 'p5'  , 'maj6', 'maj7',  'oct'],
    'mixolydian'            : ['u', 'maj2', 'maj3', 'p4'  , 'p5'  , 'maj6', 'min7',  'oct'],
    'locrian'               : ['u', 'min2', 'min3', 'p4'  , 'trit', 'm6'  , 'min7',  'oct'],
}

INTERVALS = {
"u": 0,"min2": 1,"maj2": 2,"min3": 3,"maj3" : 4,"p4": 5,"trit": 6,"p5": 7,"m6": 8,
"maj6": 9,"min7": 10,"maj7": 11,"oct": 12,"min9": 13,"9": 14,"#9": 15,"min10": 16,
"11": 17,"#11": 18,"12": 19,"b13": 20,"13": 21,"#13": 22,"b15": 23,"15": 24
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