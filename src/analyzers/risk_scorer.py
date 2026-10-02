def calculate_risk(report):

    score = 0
    reasons = []

    if len(report["capabilities"]) > 0:
        score += len(report["capabilities"]) * 10
        reasons.append(
            f"{len(report['capabilities'])} suspicious capabilities"
        )

    if report["entropy"] > 7:
        score += 20
        reasons.append(
            "High entropy (possible packing/obfuscation)"
        )

    if len(report["mitre_attack"]) > 2:
        score += 20
        reasons.append(
            "Multiple MITRE ATT&CK techniques"
        )

    if score > 100:
        score = 100

    return {
        "score": score,
        "reasons": reasons
    }
