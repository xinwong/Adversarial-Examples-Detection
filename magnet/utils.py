import os
import numpy as np
import pickle


def prepare_data(dataset, idx):
    """
    Extract data from index.

    dataset: Full, working dataset. Such as MNIST().
    idx: Index of test examples that we care about.
    return: X, targets, Y
    """
    return dataset.test_data[idx], dataset.test_labels[idx], np.argmax(dataset.test_labels[idx], axis=1)


def save_obj(obj, name, directory='./attack_data/'):
    with open(os.path.join(directory, name + '.pkl'), 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name, directory='./attack_data/'):
    if name.endswith(".pkl"): name = name[:-4]
    with open(os.path.join(directory, name + '.pkl'), 'rb') as f:
        return pickle.load(f)
