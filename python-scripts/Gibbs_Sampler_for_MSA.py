###############################################################################
#                     A GIBBS SAMPLER ALGORITHM FOR MSA                       #
#                       Author: Andrea Laguillo Gomez                         #
#                                13-01-2018                                   #
###############################################################################

###############################################################################
#                          IMPORT NECESSARY MODULES                           #
###############################################################################

import random
import numpy
import functools
import os

###############################################################################
#                         DEFINE NECESSARY FUNCTIONS                          #
###############################################################################

def readSequences(fasta):
    """Reads all sequences of a FASTA file 
       returns a dictionary, ID is key, sequence is value"""  
    with open(fasta, 'r') as f:
        diccionario = {}
        list_sequences = f.read().split('>') #separate by sequence
        for seq in list_sequences[1:]: #remove empty space at beginning
            seq_lines = seq.splitlines()
            identifier = seq_lines[0].split()[0]
            sequence = []  
            for line in seq_lines[1:]:
                sequence.append(line.replace(' ','').upper())
            diccionario[identifier] = ''.join(sequence)
    return diccionario

def randomSegments(sequences, patternLength):
    '''Chooses one random segment of the specified length 
       from each input sequence'''
    segments = {}
    for sequence in sequences:
        segment_start = random.randint(0,
                                       len(sequences[sequence])
                                       - patternLength)
        segment_end = segment_start + patternLength
        temp_seq = sequences[sequence] # So that we can slice it
        segment = temp_seq[segment_start:segment_end]
        segments[sequence] = segment
    return(segments) # segments.values() to get only segments

def constructProfiles(segments):
    profile = {}
    '''Constructs a profile by removing one entry from segments dictionary'''
    to_remove = random.choice(list(segments.keys()))
    for segment in segments:
        if segment != to_remove:
            profile[segment] = segments[segment]
    return(profile)

def scoreProfile(profile):
    ''' Scores the profile and constructs the consensus sequence'''
    profile_seqs = list(profile.values())
    consensus_list = []
    profile_seqs_as_list = []
    for seq in profile_seqs:
        seq_as_list = list(seq)
        profile_seqs_as_list.append(seq_as_list)
    base_matrix = numpy.matrix(profile_seqs_as_list)
    base_matrix_t = numpy.transpose(base_matrix)
    prob_matrix = numpy.zeros((len(seq), len(profile)))
    row_counter = 0 # counter for the prob_matrix
    for row in base_matrix_t:
        bases_dict = {}
        row_list = numpy.matrix.tolist(row)
        bases_dict["A"] = row_list[0].count("A")
        bases_dict["T"] = row_list[0].count("T")
        bases_dict["G"] = row_list[0].count("G")
        bases_dict["C"] = row_list[0].count("C")
        prob_matrix[row_counter, 0] = bases_dict["A"] / len(profile)
        prob_matrix[row_counter, 1] = bases_dict["C"] / len(profile)
        prob_matrix[row_counter, 2] = bases_dict["G"] / len(profile)
        prob_matrix[row_counter, 3] = bases_dict["T"] / len(profile)
        bases_v = list(bases_dict.values())
        bases_k = list(bases_dict.keys())
        consensus_list.append(bases_k[bases_v.index(max(bases_v))])
        consensus_string = ''.join(consensus_list)
        row_counter = row_counter + 1
    return(consensus_string, prob_matrix)

def getProbability(prob_matrix, removed_sequence, patternLength): 
    '''Computes probabilities for all possible l-mers of the
       removed sequence and returns the highest fragment, its probability
       and its starting position within the sequence'''
    possible_fragments = {}
    for i in range(0, len(removed_sequence) - patternLength):
        possible_fragments[removed_sequence[i:i + patternLength]] = i
    probability_dict = {}
    for fragment in list(possible_fragments.keys()):
        sequence_list = list(fragment)
        probabilities = []
        position = 0
        for base in sequence_list:
            if base == "A":
                probabilities.append(prob_matrix[position, 0])
            if base == "C":
                probabilities.append(prob_matrix[position, 1])
            if base == "G":
                probabilities.append(prob_matrix[position, 2])
            if base == "T":
                probabilities.append(prob_matrix[position, 3])
        result = functools.reduce(lambda x, y: x*y, probabilities)
        probability_dict[fragment] = result
    prob_list = list(probability_dict.values())
    fragment_list = list(probability_dict.keys())
    max_prob = max(prob_list)
    max_fragment = list(fragment_list)[list(prob_list).index(max_prob)]
    starting_position = possible_fragments[max_fragment]
    return(max_fragment, max_prob, starting_position)

def constructAlignment(sequences, starting_positions):
    '''Writes alignment to a file'''
    segment_list = []
    with open("myseqs_aligned.fasta", 'w') as f:
        f.write("Gibbs Sampling")
        f.write("\n" + "ID" + "\t" + "Position" + "\t" + "Sequence")
        for sequence in sequences:
            begins = starting_positions[sequence]
            bases = sequences[sequence]
            segment = bases[begins:begins + pattern_length]
            segment_list.append(segment)
            f.write("\n" + sequence +
                    "\t" + str(begins) +
                    "\t" + "\t" + segment)
            consensus_string = ""
            seq_lists = []
            consensus_list = []
            for seq in segment_list:
                seq_as_list = list(seq)
                seq_lists.append(seq_as_list)
            base_matrix = numpy.matrix(seq_lists)
            base_matrix_t = numpy.transpose(base_matrix)
            row_counter = 0 # counter for the prob_matrix
            for row in base_matrix_t:
                bases_dict = {}
                row_list = numpy.matrix.tolist(row)
                bases_dict["A"] = row_list[0].count("A")
                bases_dict["T"] = row_list[0].count("T")
                bases_dict["G"] = row_list[0].count("G")
                bases_dict["C"] = row_list[0].count("C")
                bases_v = list(bases_dict.values())
                bases_k = list(bases_dict.keys())
                consensus_list.append(bases_k[bases_v.index(max(bases_v))])
                consensus_string = ''.join(consensus_list)
                row_counter = row_counter + 1
        f.write("\n" + "Consensus: " + "\t" + "\t" + consensus_string)
    return(print("Alignment file created"))

###############################################################################
#                               GIBBS SAMPLING                                #
###############################################################################

# 1. Read the sequences from a FASTA file and choose pattern length
os.chdir("path") # path where FASTA is located
                                    # results will be saved here too
mysequences = readSequences("file") # FASTA file name
pattern_length = 8

# FROM HERE IT WILL BE REPEATED IN N ITERATIONS UNTIL NO IMPROVEMENT
iteration_counter = 0 #increased by one if no improvement in round, reset if so
max_iterations = 20 # with no improvement in probability score
starting_positions = {} # Create a dict of sequences and starting positions
for ID in mysequences:
    starting_positions[ID] = 0 # Fill it with zeroes which we'll change in
                               # step 6 if a better alignment is found
while iteration_counter < 20:
    # 2. Choose one random segment of length L from each sequence
    result_randomSegments = randomSegments(mysequences,
                                           pattern_length)
    
    # 3. Remove one segment and construct profile with remaining segments
    result_constructProfiles = constructProfiles(result_randomSegments)
    
    # 4. Get the removed sequence
    removed_id = ''.join(set(mysequences.keys()) -
                         set(result_constructProfiles.keys()))
    removed_seq = mysequences[removed_id]
    
    # 5. Score the profile and construct the consensus sequence
    result_scoreProfile = scoreProfile(result_constructProfiles)
    
    # 6. Compute probabilities for all possible fragments of the removed
    #    sequence and return the highest fragment
    result_getProbability = getProbability(result_scoreProfile[1],
                                           removed_seq,
                                           pattern_length)
    
    # 7. Check if we should modify starting_positions dictionary
    
    if result_getProbability[2] >= starting_positions[removed_id]:
        starting_positions[removed_id] = result_getProbability[2]
        iteration_counter = 0 # reset
    else: # no improvement
        iteration_counter = iteration_counter + 1

# 8. Construct the alignment with the starting_positions dictionary
constructAlignment(mysequences, starting_positions)
