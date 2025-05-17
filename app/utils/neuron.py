from collections import deque
import numpy as np

class CTMNeuron:
    """
    A Continuous Thought Machine-style neuron that:
    - Processes inputs using a memory buffer
    - Applies weighted temporal processing
    - Uses a simulated phase value to model synchronization
    """

    def __init__(self, memory_size=5, weights=None, phase=0, neuron_id=0):
        self.id = neuron_id
        self.memory_size = memory_size
        self.history = deque(maxlen=memory_size)
        self.phase = phase  # Phase for simulated synchronization (0 to N)
        self.weights = weights if weights is not None else np.ones(memory_size) / memory_size
        self.last_output = 0

    def receive_input(self, value):
        """Append new input value to the neuron's history."""
        self.history.append(value)

    def process(self):
        """Apply weighted history to simulate memory-based activation."""
        if len(self.history) < self.memory_size:
            return 0  # Not enough data yet
        self.last_output = float(np.dot(self.weights, list(self.history)))
        return self.last_output

    def is_in_sync(self, global_phase):
        """Check if this neuron is synchronized with the global phase."""
        return self.phase == global_phase

    def reset(self):
        """Clear the neuron's memory and output."""
        self.history.clear()
        self.last_output = 0

    def __repr__(self):
        return f"<CTMNeuron id={self.id} phase={self.phase} output={self.last_output:.2f}>"
