# 🧠 Continuous Thought Machines Visualizer

A hands-on project inspired by the [**Continuous Thought Machines (CTM)**](https://doi.org/10.48550/arXiv.2505.05522) paper by Darlow et al.

This interactive simulation demonstrates the behaviour of **biologically-inspired neurons** that:
- Process inputs over time
- Store recent memory
- Fire only when synchronized to a global rhythm

It’s a visual, intuitive way to explore concepts like memory, **temporal weighting**, and **neural phase alignment** — all from a browser.

---

[![Streamlit App](https://img.shields.io/badge/Launch%20App-CTM%20Visualizer-FF4B4B?logo=streamlit)](https://ctm-concept-4fp8qoqrb68ybwflpjhptn.streamlit.app/)

---

## 🚀 What This App Does

- 🧠 **Simulates CTM-style neurons** with short-term memory and weighted history
- 🔄 **Synchronizes neurons** via configurable phase cycles
- ⚙️ **Lets you control** number of neurons, memory size, input stream, and step-by-step simulation
- 🎨 **Visualizes outputs** over time using a dark-themed chart — great for demos or concept teaching

---

## 📌 Key Features

- ✅ Step-by-step **neuron activation** with animation-style controls
- ✅ Dynamic charts reflecting **real-time neuron behavior**
- ✅ Clean Streamlit interface for showcasing machine learning concepts
- ✅ Great starting point for further explorations into **neural dynamics**, **adaptive compute**, or **temporal AI models**

---

## 💡 Why This Project?

Inspired by the 2024 CTM paper, this project bridges the gap between **neuroscience concepts** and **visual, code-based experimentation**.

It’s built for:
- Curious ML engineers
- Students of neural computation
- Anyone who wants to see what "thinking over time" *looks like*

---

## 📦 Getting Started Locally

```bash
git clone https://github.com/calvinx16/ctm-concept.git
cd ctm-concept
pip install -r requirements.txt
streamlit run app/main_app.py
```

---

## 🧠 Tech Stack
Python · Streamlit · NumPy · Matplotlib

Fully modular — core neuron logic lives in utils/neuron.py

No GPU needed, runs entirely in the browser or locally

---

## 📜 Credits

Built with neurons, caffeine, and curiosity  
by **[Calvin Paperwala](https://www.linkedin.com/in/calvin-paperwala-a9536765)**

> This project was inspired by the paper:  
> **Darlow, L., Regan, C., Risi, S., Seely, J., & Jones, L.** (2025).  
> *[Continuous Thought Machines](https://doi.org/10.48550/arXiv.2505.05522)*  
> arXiv:2505.05522

Special thanks to **ChatGPT** for co-developing, debugging, and hyping every neuron of this project. 

---