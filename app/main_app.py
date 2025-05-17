import streamlit as st
import numpy as np
from utils.neuron import CTMNeuron

# ---- Config ----
NUM_NEURONS = 3
MEMORY_SIZE = 5
PHASE_CYCLE = [0, 1, 2]
STREAM_LENGTH = 15

# ---- UI Header ----
st.title(" Continuous Thought Machine Visualizer")
st.markdown("This interactive dashboard simulates CTM-style neurons with memory and synchronization.")

# ---- Generate Inputs ----
st.sidebar.header("Simulation Settings")
seed = st.sidebar.slider("Random Seed", 0, 100, 42)
np.random.seed(seed)
input_stream = np.random.randint(1, 10, size=STREAM_LENGTH)

# ---- Init Neurons ----
neurons = [CTMNeuron(memory_size=MEMORY_SIZE, phase=i, neuron_id=i) for i in range(NUM_NEURONS)]

# ---- Run Simulation ----
st.subheader(" Simulation Steps")

for step, value in enumerate(input_stream):
    global_phase = PHASE_CYCLE[step % len(PHASE_CYCLE)]
    st.markdown(f"### Step {step + 1} | Input = `{value}` | Global Phase = `{global_phase}`")

    for neuron in neurons:
        neuron.receive_input(value)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(f"**Neuron {neuron.id}**")
            st.write(f"Phase: `{neuron.phase}`")

        with col2:
            st.write(f"History: {list(neuron.history)}")

        with col3:
            if neuron.is_in_sync(global_phase):
                output = neuron.process()
                st.success(f"✅ In Sync → Output: `{output:.2f}`")
            else:
                st.warning("❌ Out of Sync")

    st.markdown("---")
