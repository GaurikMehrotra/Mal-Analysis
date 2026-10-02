import json
import requests


def analyze_with_qwen(report):

    prompt = f"""
You are a senior malware analyst.

Analyze this static analysis report.

Return:

1. Classification
2. Risk Score (0-100)
3. Suspicious Indicators
4. Analyst Assessment

Report:

{json.dumps(report, indent=2)}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]