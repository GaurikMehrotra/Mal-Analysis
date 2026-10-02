def build_markdown_report(report, ai_summary, yara_rule):

    md = "# Malware Analysis Report\n\n"

    md += "## Executive Summary\n\n"
    md += f"**File:** {report['file']}\n\n"
    md += f"**Risk Score:** {report['risk_score']['score']}/100\n\n"

    md += "## Risk Reasons\n\n"

    for reason in report["risk_score"]["reasons"]:
        md += f"- {reason}\n"

    md += "\n## Capabilities\n\n"

    for cap in report["capabilities"]:
        md += f"- {cap['capability']} ({cap['api']})\n"

    md += "\n## MITRE ATT&CK\n\n"

    for item in report["mitre_attack"]:
        md += f"- {item['technique']} : {item['name']}\n"

    md += "\n## Entropy\n\n"
    md += f"{report['entropy']}\n\n"

    md += "## Detection Rule\n\n"
    md += "```yara\n"
    md += yara_rule
    md += "\n```\n\n"

    md += "## AI Analyst Assessment\n\n"
    md += ai_summary

    return md
