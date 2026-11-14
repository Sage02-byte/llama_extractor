# Local LLM Structured Extractor & Support Intake Bot

A production-grade pipeline that bridges the gap between unstructured human conversation and deterministic backend databases. This project utilizes local LLM inference (`llama.cpp`), Python, and strict JSON Schema enforcement (`strict: True`) to extract 100% type-safe JSON objects without regex or cleaning scripts.

---

## 🚀 Key Features

* **Local High-Efficiency Serving:** Runs locally via Docker using `llama.cpp` backend-agnostic `/v1` endpoints.
* **Deterministic JSON Schema Enforcement:** Compiles context-free grammars (CFGs) on the fly to guarantee output structure (integers, booleans, arrays, nested objects).
* **AI Support Intake Bot:** Combines a multi-turn conversational chat agent with a trigger-based extraction pipeline (`"extract"` command).
* **Zero Cloud Dependency:** Runs entirely on local hardware (GPU accelerated via CUDA).

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Inference Engine:** `llama.cpp` (Docker container with CUDA support)
* **Client Library:** `huggingface_hub` (OpenAI-compatible client)
* **Data Validation:** JSON Schema (`additionalProperties: False`)

---

## ⚙️ Quick Start Guide

### 1. Start the Local LLM Server (Docker)
Spin up your local `llama.cpp` server container using your GGUF model:

```powershell
docker run --gpus all -v C:/Users/jazzy/Downloads/LLM/models:/models -p 8080:8080 ghcr.io/ggml-org/llama.cpp:server-cuda -m /models/SmolLM2-1.7B-Instruct-Q4_K_M.gguf --host 0.0.0.0 --port 8080 --n-gpu-layers 33
