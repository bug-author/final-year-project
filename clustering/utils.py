import numpy as np

def create_dataset(data, steps):
  features, labels = [], []
  for i in range(len(data)-steps):
    data_seq = data[i: i+steps]
    features.append(data_seq)

    seq_label = data[i+steps]
    labels.append(seq_label)

  return np.array(features), np.array(labels)