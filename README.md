# CrimeVision AI - Intelligent Multimodal Forensic Analysis Platform
**Skill Wallet Capstone Project 2**  
*Senior Forensic Systems Architecture Specification*

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Forensic Standard](https://img.shields.io/badge/Forensic_Standard-NIST_SP_800--86-green.svg)](https://csrc.nist.gov/)
[![PDF Engine](https://img.shields.io/badge/PDF_Engine-ReportLab_5.0-red.svg)](https://www.reportlab.com/)

---

## 🏛️ Executive Summary

**CrimeVision AI** is an enterprise-grade forensic intelligence platform designed for digital forensics investigators, crime scene analysts, and law enforcement prosecutors. The platform unifies visual object detection, acoustic telemetry & witness speech recognition, temporal CCTV progression tracking, and cross-modal evidence fusion into an interactive tactical command center. 

All analyses are bound by a cryptographically verifiable **Forensic Chain-of-Custody** (SHA-256 integrity hashing), a **zero-hallucination Grounded RAG interrogation engine**, and **1-click court-admissible ReportLab PDF dossier generation**.

---

## 🚀 Key Modules & Epic Architecture

### 🛡️ Core 1: Configuration, Security & Chain of Custody
- **Dual-Engine Architecture**: Operates in **Live Multimodal AI Mode** (using user-supplied Groq / Gemini API keys) or **Autonomous Forensic Intelligence Mode** (offline deterministic fallback with 0 API keys required).
- **Forensic Chain-of-Custody Indicators**: Real-time HUD banner displaying Case ID (`CV-2026-9042-CRIME`), Lead Investigator sign-off, credential badges, and immutable timestamped audit events.
- **Cryptographic Evidence Fingerprinting**: Calculates bit-stream SHA-256 hashes for all photographic, acoustic, and video assets to ensure legal admissibility under Federal Rules of Evidence (FRE 901/902) and Indian Evidence Act Section 65B.

### 📷 Tab 1: Crime Scene Visual Evidence Tagger (Epic 2)
- **RT-DETR Multimodal Object Detection**: Detects persons, firearms, edged weapons, biological blood spatter (arterial spray and pooling), breaching crowbars, spent casings, and forced entry points.
- **Interactive Coordinate Visualizer**: Real-time bounding box overlays with tactical HUD corner crosshairs, confidence percentages, and normalized spatial coordinates `[x1, y1, x2, y2]`.
- **Structured Forensic Appraisal**: Threat level grading (*Low / Medium / High / Critical*), scene classification (*Burglary / Homicide / Vandalism / Armed Assault*), and prioritized ballistic/DNA investigative leads.

### 🎙️ Tab 2: Witness Audio Transcription & Timeline (Epic 3)
- **Whisper Speech Recognition & Diarization**: Auto-tags speakers (`[DISPATCHER 911]`, `[CALLER (WITNESS #1)]`, `[INTERROGATOR]`) with chronological timeline markers.
- **Acoustic Stress & Vocal Urgency Scoring**: Evaluates vocal tremors, cadence changes, and acoustic shock to score emotional/urgency threat levels.
- **Entity & Tactical Clue Extraction**: Recovers suspect descriptors, weapons cycling sounds, vehicle escape routes, and contraband mentions directly from 911 dispatch transmissions.

### 📹 Tab 3: CCTV Video Analysis & Event Progression (Epic 4)
- **Temporal Trajectory Tracking**: Samples progression frames across seconds (`T+00s`, `T+46s`, `T+86s`, `T+213s`, `T+252s`), tracking intruder entry, weapon draws, and getaway vehicle kinematics.
- **Statutory Penal Code Classification**: Automatically maps video observations to legal penal statutes (e.g., *Armed Burglary - Penal Code § 459 / IPC 454*, *Assault with Deadly Weapon - Penal Code § 245 / IPC 326*, *Larceny / Robbery - Penal Code § 211 / IPC 392*).
- **Surveillance Keyframe Scrubber**: Interactive visual inspection scrubber with motion vector annotations.

### 🧩 Tab 4: Multimodal Fusion & Grounded Evidence Chat (Epic 5)
- **Master Forensic Event Ledger**: Merges visual photography (`EVD-IMG-001`), witness dispatch audio (`EVD-AUD-001`), and CCTV surveillance (`EVD-VID-001`) into a single time-indexed ledger.
- **Cross-Modal Discrepancy & Corroboration**: Verifies witness statements against CCTV video timestamps and physical crime scene recoveries.
- **Grounded RAG Interrogation**: Natural language question-answering with **strict Evidence ID citation** (`[EVD-IMG-001]`, `[EVD-AUD-001]`, `[EVD-VID-001]`) and **zero hallucination** (unsubstantiated claims trigger explicit uncorroborated alerts).

### 📄 Tab 5: Automated Forensic PDF Export (Epic 6)
- **Court-Admissible Dossier Generation**: Uses ReportLab to compile high-resolution, certified PDF documents with division seals, case metadata, SHA-256 integrity tables, detection inventories, and legal disclaimers.
- **Digital Investigator Sign-off**: Formal certification section adhering to NIST SP 800-86 standards with one-click direct download.

---

## 💻 Installation & Quickstart

### Prerequisites
- Python 3.10, 3.11, or 3.12
- Standard pip package manager

### 1. Clone or Open Workspace
```bash
cd D:\TurnKey
```

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Launch the Platform
```bash
python -m streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## ☁️ Zero-Database Community Cloud Deployment

CrimeVision AI is designed with **zero external database dependencies**:
- State management operates natively inside Streamlit's in-memory `st.session_state`.
- All sample assets (high-resolution crime scene photography, emergency radio audio wave files, surveillance keyframes) are synthesized deterministically in-memory.
- Deploy in seconds to **Streamlit Community Cloud** simply by connecting your GitHub repository with `app.py` as the entrypoint.

---

## 🔒 Forensic Compliance & Legal Standards
- **NIST SP 800-86**: Guide to Integrating Forensic Techniques into Incident Response.
- **Federal Rules of Evidence (FRE)**: Rule 901 (Authenticating Evidence) & Rule 902 (Self-authenticating electronic records).
- **Section 65B Compliance**: Electronic record integrity certified via SHA-256 hash digests.
