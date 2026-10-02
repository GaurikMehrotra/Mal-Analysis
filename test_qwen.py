from src.agents.threat_agent import analyze_with_qwen
from agents.threat_agent import analyze_with_qwen
report = {
    "entropy": 6.4,
    "capabilities": [
        {
            "api": "CreateProcessW",
            "capability": "Process Creation"
        }
    ]
}

result = analyze_with_qwen(report)

print(result)