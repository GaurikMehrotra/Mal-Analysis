from orchestrator import run_analysis
from report_generator import save_report

from analyzers.yara_generator import generate_yara
from yara_writer import save_yara

from agents.report_ai import generate_ai_summary

from report_builder import build_markdown_report
from report_writer import save_markdown_report


sample_path = "data/samples/sample.exe"

# Run analysis
report = run_analysis(sample_path)

# Save JSON report
save_report(
    report,
    "reports/analysis_report.json"
)

# Generate YARA
yara_rule = generate_yara(
    report["capabilities"]
)

save_yara(
    yara_rule,
    "reports/detection_rule.yar"
)

# Generate AI summary
ai_summary = generate_ai_summary(report)

# Build final markdown report
markdown_report = build_markdown_report(
    report,
    ai_summary,
    yara_rule
)

# Save markdown report
save_markdown_report(
    markdown_report,
    "reports/final_report.md"
)