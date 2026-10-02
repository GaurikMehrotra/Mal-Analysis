from analyzers.risk_scorer import calculate_risk

report = {
    "capabilities": [
        {"api": "CreateProcessW"},
        {"api": "RegCreateKeyExW"},
        {"api": "RegSetValueExW"}
    ],
    "entropy": 6.48,
    "mitre_attack": [
        {},
        {},
        {}
    ]
}

print(calculate_risk(report))
