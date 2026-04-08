# LLM Benchmark Dashboard

## Overview
This project is a **Local LLM Benchmark Dashboard** that compares multiple AI language models based on their performance.

The system runs models locally using Ollama and evaluates them using:
- Latency (response time)
- Memory usage
- Answer quality

The results are visualized using Streamlit.



## Features
- Run multiple local LLMs  
- Compare models using same prompts  
- Measure performance metrics  
- Store results in CSV  
- Interactive dashboard visualization  



## Models Used
- TinyLlama  
- Gemma (2B)  
- Qwen (1.8B / 3B)


##  Project Structure

    LLM-Benchmark-Dashboard/
    │
    ├── Benchmark.py
    ├── dashboard.py
    ├── results.csv

## Installation

### 1. Install Ollama
Download and install from:
https://ollama.ai

---

### 2. Install Python libraries
pip install ollama pandas psutil streamlit plotly

---

### 3. Download models
ollama pull tinyllama
ollama pull gemma:2b
ollama pull qwen:1.8b
## Usage

### Run Benchmark
python Benchmark.py
  
### Run Dashboard
streamlit run dashboard.py
Open in browser:
http://localhost:8501

## Architecture

The architecture of this project shows how different components are connected and how data flows through the system

    User Input (Prompts)
        ↓
    Benchmark.py (Python Script)
        ↓
      Ollama
        ↓
    AI Models (TinyLlama, Gemma, Qwen)
        ↓
    Results (Latency, Memory, Quality)
        ↓
    results.csv
        ↓
    dashboard.py (Streamlit)
        ↓
    Visualization (Graphs & Tables)

## Evaluation Metrics

| Metric | Description |
|------|------------|
| Latency | Time taken to generate response |
| Memory | RAM usage during execution |
| Quality | Response length (word count) |


## Conclusion
This project provides a simple and effective way to compare local AI models based on performance and helps in selecting the best model for different use cases.

---

##  Author
Iniyan S R
