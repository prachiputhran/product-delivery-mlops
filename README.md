# ⚙️ Experiment 03: Automating ML Training with Jenkins

> **Experiment 03 · MLOps / CI-CD & Training Automation**

An experiment exploring how **Jenkins can automate machine learning workflows**, using a Jenkins pipeline to execute testing and model-training tasks through a repeatable CI/CD process.

The experiment begins with a **local Jenkins setup** and is designed to extend toward triggering managed machine learning workflows on **Google Cloud Vertex AI**.

---

## 🎯 Objective

The goal of this experiment was to understand how traditional CI/CD automation tools such as **Jenkins** can be integrated into machine learning workflows.

Instead of manually running:

```text id="7p2nqj"
Write Code
   ↓
Run Tests
   ↓
Train Model
   ↓
Check Output
```

the workflow moves toward:

```text id="6cnq0r"
Code Change
    ↓
Jenkins
    ↓
Automated Tests
    ↓
Training Script
    ↓
Model / Outputs
```

This introduces automation and repeatability into the model development lifecycle.

---

## 🏗️ Pipeline Architecture

```text id="e8k4w7"
                 Git Repository
                      │
                      ▼
                 Jenkins Job
                      │
             ┌────────┴────────┐
             ▼                 ▼
        Install Deps       Run Tests
             │                 │
             └────────┬────────┘
                      ▼
                Train Model
                      │
                      ▼
                Model Output
                      │
                      ▼
             Optional Cloud Step
                      │
                      ▼
                 Vertex AI
```

The local Jenkins pipeline establishes the automation layer, while **Vertex AI Pipelines** provides a potential cloud-based extension for managed ML workflows.

---

## 💻 Offline Setup — Jenkins Locally

The initial implementation uses a locally running Jenkins instance.

The Jenkins pipeline is defined through a `Jenkinsfile`, allowing the workflow to be version-controlled alongside the source code.

```text id="6x9xkq"
product-delivery-mlops/
│
├── src/
├── requirements.txt
├── Jenkinsfile
└── README.md
```

This approach keeps the CI/CD configuration close to the application code and makes the pipeline reproducible.

---

## 🔄 Jenkins Pipeline

The pipeline can automate stages such as:

### 1. Environment Setup

Jenkins prepares the Python environment and installs the required dependencies.

### 2. Testing

Automated tests are executed before continuing with the ML workflow.

### 3. Training

The training script can be triggered automatically rather than being executed manually.

### 4. Output Generation

The resulting model or experiment outputs can then be passed to subsequent stages of the pipeline.

This creates a repeatable training workflow that can be triggered whenever the project changes.

---

## ☁️ Online Setup — Vertex AI

The cloud extension of this experiment explores triggering **Google Cloud Vertex AI** workflows from Jenkins.

The conceptual flow is:

```text id="8e7c2s"
Git Push
   ↓
Jenkins
   ↓
Pipeline Validation
   ↓
Training Trigger
   ↓
Google Vertex AI
   ↓
ML Pipeline
   ↓
Training / Evaluation
```

Vertex AI can provide managed infrastructure for executing machine learning pipelines, while Jenkins acts as the automation and orchestration layer.

This separation allows CI/CD tooling and cloud ML infrastructure to work together.

---

## 🧠 Modeling

The experiment is designed around a Python-based ML workflow and can support common machine learning frameworks such as:

* **Scikit-learn**
* **TensorFlow / Keras**
* **PyTorch**

The emphasis of this experiment, however, is not on developing a complex model. The primary focus is **automating the process surrounding model training**.

---

## 📁 Repository Structure

```text id="2q0yga"
product-delivery-mlops/
│
├── src/
│   └── ...
│
├── Jenkinsfile
├── requirements.txt
└── README.md
```

The `Jenkinsfile` defines the CI/CD pipeline, while `src/` contains the project implementation.

---

## 🧩 Why Jenkins for ML?

Machine learning projects frequently involve repetitive steps:

> **Test → Train → Evaluate → Package → Deploy**

Running these steps manually makes workflows harder to reproduce and increases the possibility of human error.

Jenkins provides a way to turn these steps into an **automated pipeline**.

This experiment helped connect traditional software engineering practices with machine learning development:

```text id="r8e9nq"
Software Engineering
        │
        ▼
     Jenkins
        │
        ▼
   ML Automation
        │
        ▼
 Training Pipeline
        │
        ▼
   Cloud ML Systems
```

---

## 🧠 What I Learned

The key takeaway from this experiment was that **ML automation requires more than a training script**.

A training script answers:

> *How do I train the model?*

A CI/CD pipeline answers:

> *When should training happen, what should happen before it, and how can the process be repeated reliably?*

Jenkins provides the automation layer needed to turn individual ML scripts into a more structured workflow.

---

## 🛠️ Technologies

* **Jenkins**
* **Jenkins Pipeline**
* **Jenkinsfile**
* **Python**
* **Scikit-learn**
* **TensorFlow / Keras**
* **PyTorch**
* **Google Cloud Vertex AI**
* **Git**

---

## 📚 Reference

* [Vertex AI Pipelines — Google Cloud Documentation](https://cloud.google.com/vertex-ai/docs/pipelines?utm_source=chatgpt.com)

---roader journey from **local ML experimentation toward production-oriented MLOps**.
