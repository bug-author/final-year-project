import numpy as np

def self_attention(input_sequence):
    output = np.zeros(shape=input_sequence.shape)
    for i, pivot_vector in enumerate(input_sequence):
        scores = np.zeros(shape=(len(input_sequence),))
    
    for j, vector in enumerate(input_sequence):
        scores[j] = np.dot(pivot_vector, vector.T)
        scores /= np.sqrt(input_sequence.shape[1])
        scores = softmax(scores)
        new_pivot_representation = np.zeros(shape=pivot_vector.shape)
    
    for j, vector in enumerate(input_sequence):
        new_pivot_representation += vector * scores[j]
    output[i] = new_pivot_representation
    return output


seq = 'The quick brown fox jumped over Ali'
inp_seq = np.fromstring(seq)
self_attention(inp_seq)