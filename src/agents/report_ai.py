def generate_ai_summary(report):

    return f"""
Risk Score: {report['risk_score']['score']}/100

Capabilities Detected:
{', '.join([c['capability'] for c in report['capabilities']])}

MITRE Techniques:
{', '.join([m['technique'] for m in report['mitre_attack']])}

The sample demonstrates suspicious behavior including persistence and process creation capabilities.
"""
