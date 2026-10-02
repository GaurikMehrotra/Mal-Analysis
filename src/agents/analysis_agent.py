from orchestrator import run_analysis
from analyzers.yara_generator import generate_yara


def analyze_sample(sample_path):

    report = run_analysis(sample_path)

    yara_rule = generate_yara(
        report["capabilities"]
    )

    return {
        "report": report,
        "yara_rule": yara_rule
    }
