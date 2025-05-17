import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.neuron import CTMNeuron

st.set_page_config(page_title="CTM Neuron Visualizer", layout="wide")

# ---- Sidebar Controls ----
st.sidebar.title("⚙️ Simulation Settings")

num_neurons = st.sidebar.slider("Number of Neurons", 1, 10, 3)
memory_size = st.sidebar.slider("Memory Size", 2, 10, 5)
stream_length = st.sidebar.slider("Input Stream Length", 5, 30, 15)
seed = st.sidebar.number_input("Random Seed", min_value=0, value=42)

# Auto-generate phase cycle (0, 1, ..., N-1)
phase_cycle = list(range(num_neurons))

# ---- Generate Input Stream ----
np.random.seed(seed)
input_stream = np.random.randint(1, 10, size=stream_length)

# ---- Step Control ----
st.sidebar.subheader("🕹️ Animation Control")
if 'step' not in st.session_state:
    st.session_state.step = 1

if st.sidebar.button("Next Step"):
    st.session_state.step += 1
    if st.session_state.step > stream_length:
        st.session_state.step = 1

current_step = st.session_state.step

# ---- Global Phase ----
global_phase = phase_cycle[(current_step - 1) % len(phase_cycle)]
st.title("🧠 CTM Neuron Visualizer")
st.markdown("This interactive simulation shows CTM-style neurons with memory, processing, and phase sync.")
st.markdown("""
#### What You're Seeing

This simulation brings the **Continuous Thought Machine (CTM)** concept to life.

Each neuron:
- Has a short-term memory (`memory_size`) to process recent inputs
- Only **fires** when it's "in sync" with a global phase — mimicking timing-based coordination seen in biological brains
- Produces outputs based on a weighted history of recent values

Use the **sidebar** to adjust parameters and click **Next Step** to simulate how neurons process data over time and how phase synchronization affects their behavior.

""")
st.markdown(f"### Step {current_step} | Global Phase = `{global_phase}` | Input = `{input_stream[current_step - 1]}`")

# ---- Initialize Neurons ----
neurons = [CTMNeuron(memory_size=memory_size, phase=i, neuron_id=i) for i in range(num_neurons)]
output_history = {neuron.id: [] for neuron in neurons}

# ---- Replay Up to Current Step ----
for step in range(current_step):
    value = input_stream[step]
    phase = phase_cycle[step % len(phase_cycle)]

    for neuron in neurons:
        neuron.receive_input(value)
        if neuron.is_in_sync(phase):
            output = neuron.process()
            output_history[neuron.id].append(output)
        else:
            output_history[neuron.id].append(0)

# ---- Display Neuron Info ----
cols = st.columns(num_neurons)
for i, neuron in enumerate(neurons):
    with cols[i]:
        st.write(f"**Neuron {neuron.id}** (Phase {neuron.phase})")
        st.write(f"History: {list(neuron.history)}")
        if neuron.is_in_sync(global_phase):
            st.success(f"In Sync → `{neuron.last_output:.2f}`")
        else:
            st.warning("Out of Sync")

# ---- Fancy Plot ----
st.subheader("🎨 Neuron Output Chart")
fig, ax = plt.subplots(figsize=(12, 5))
colors = plt.cm.Reds(np.linspace(0.4, 0.9, num_neurons))

for i, outputs in output_history.items():
    ax.plot(
        range(1, current_step + 1),
        outputs[:current_step],
        label=f"Neuron {i}",
        color=colors[i],
        linewidth=2.5,
        marker='o',
        markersize=6
    )

# Dark theme aesthetics
fig.patch.set_facecolor('#000000')
ax.set_facecolor('#000000')
ax.set_title("CTM Neuron Outputs", fontsize=18, weight='bold', color='white')
ax.set_xlabel("Step", fontsize=14, color='white')
ax.set_ylabel("Output", fontsize=14, color='white')
ax.tick_params(colors='white')
ax.grid(True, linestyle="--", alpha=0.3)
ax.legend(frameon=False, fontsize=12, labelcolor='white')

st.pyplot(fig)
