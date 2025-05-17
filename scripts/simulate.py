from app.utils.neuron import CTMNeuron
import numpy as np
import time

# Simulation config
NUM_NEURONS = 3
MEMORY_SIZE = 5
PHASE_CYCLE = [0, 1, 2]  # simulate clock ticks
STREAM_LENGTH = 10

# Create neurons with different phases
neurons = [
    CTMNeuron(memory_size=MEMORY_SIZE, phase=i, neuron_id=i)
    for i in range(NUM_NEURONS)
]

# Simulated input stream (random or pattern-based)
input_stream = np.random.randint(1, 10, size=STREAM_LENGTH)

print("\n CTM Neuron Simulation Start\n")

for step, value in enumerate(input_stream):
    global_phase = PHASE_CYCLE[step % len(PHASE_CYCLE)]

    print(f"\n Step {step + 1} | Input: {value} | Global Phase: {global_phase}")

    for neuron in neurons:
        neuron.receive_input(value)

        if neuron.is_in_sync(global_phase):
            output = neuron.process()
            print(f" Neuron {neuron.id} IN SYNC → Output: {output:.2f} | History: {list(neuron.history)}")
        else:
            print(f" Neuron {neuron.id} OUT OF SYNC | Phase: {neuron.phase} | History: {list(neuron.history)}")

    time.sleep(0.5)  # slow it down to watch behavior
