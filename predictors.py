# predictors.py

import numpy as np

class GsharePredictor:
    def __init__(self, history_bits, table_size=1024):
        self.history_bits = history_bits
        self.GHR = 0  # Global history register
        self.PHT = [1] * table_size  # Pattern History Table with 2-bit counters

    def predict(self, pc):
        index = (pc ^ self.GHR) % len(self.PHT)
        return self.PHT[index] >= 2  # Predict taken if counter is 2 or more

    def update(self, pc, taken):
        index = (pc ^ self.GHR) % len(self.PHT)
        if taken:
            self.PHT[index] = min(self.PHT[index] + 1, 3)  # Increase counter
        else:
            self.PHT[index] = max(self.PHT[index] - 1, 0)  # Decrease counter
        self.GHR = ((self.GHR << 1) | taken) & ((1 << self.history_bits) - 1)

class PerceptronPredictor:
    def __init__(self, num_weights, history_length):
        self.history_length = history_length
        self.history = [0] * history_length
        self.weights = np.zeros((num_weights, history_length))

    def predict(self, pc):
        index = pc % len(self.weights)
        prediction = np.dot(self.weights[index], self.history)
        return prediction >= 0  # Predict taken if the sum is non-negative

    def update(self, pc, taken):
        index = pc % len(self.weights)
        prediction = np.dot(self.weights[index], self.history) >= 0
        if prediction != taken:
            self.weights[index] += [1 if taken else -1] * np.array(self.history)
        self.history.pop(0)
        self.history.append(1 if taken else -1)
