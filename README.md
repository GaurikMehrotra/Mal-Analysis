# Mal-Analysis

An AI-assisted malware analysis framework that performs static analysis of Windows PE files, maps findings to MITRE ATT&CK techniques, generates YARA detection rules, calculates risk scores, and produces analyst-friendly reports.

## Features

- PE Header Analysis
- Import Table Analysis
- Suspicious API Detection
- Capability Detection
- MITRE ATT&CK Mapping
- String Extraction
- Entropy Analysis
- Risk Scoring
- Automatic YARA Rule Generation
- AI-Powered Threat Assessment (Qwen via Ollama)
- JSON and Markdown Report Generation

---

## Architecture

```text
Sample.exe
    │
    ▼
PE Analyzer
    │
    ▼
Import Analyzer
    │
    ▼
Capability Analyzer
    │
    ▼
MITRE ATT&CK Mapper
    │
    ▼
String Analyzer
    │
    ▼
Entropy Analyzer
    │
    ▼
Risk Scorer
    │
    ▼
YARA Generator
    │
    ▼
AI Threat Agent (Qwen)
    │
    ▼
Final Reports
```

---

## Project Structure

```text
src/
├── agents/
│   ├── threat_agent.py
│   └── report_ai.py
│
├── analyzers/
│   ├── pe_analyzer.py
│   ├── import_analyzer.py
│   ├── capability_analyzer.py
│   ├── mitre_mapper.py
│   ├── string_analyzer.py
│   ├── entropy_analyzer.py
│   └── risk_scorer.py
│
├── orchestrator.py
├── report_generator.py
├── report_builder.py
├── yara_writer.py
└── main.py

reports/
data/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/GaurikMehrotra/Mal-Analysis.git
cd Mal-Analysis
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Analysis

Place a PE executable inside:

```text
data/samples/
```

Run:

```bash
python src/main.py
```

---

## Generated Outputs

### Analysis Report

```text
reports/analysis_report.json
```

Contains:

- PE Information
- Suspicious Capabilities
- MITRE ATT&CK Techniques
- Risk Score
- Interesting Strings
- Entropy Metrics

### YARA Rule

```text
reports/detection_rule.yar
```

Automatically generated from detected suspicious capabilities.

### Markdown Report

```text
reports/final_report.md
```

Executive-level malware analysis report.

---

## Example Findings

### Detected Capabilities

- Process Creation
- Persistence

### MITRE ATT&CK Techniques

- T1106 — Native API
- T1547 — Boot or Logon Autostart Execution

### Risk Score

```text
50 / 100
```

---

## Future Improvements

- VirusTotal Integration
- Dynamic Malware Analysis
- IOC Extraction
- PDF Report Generation
- Threat Intelligence Enrichment
- Multi-Agent Security Workflow
- Malware Family Classification

---

## Author

Gaurik Mehrotra


