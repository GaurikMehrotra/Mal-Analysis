import json


def save_report(report, output_path):

    with open(output_path, "w") as f:
        json.dump(
            report,
            f,
            indent=4
        )

    print(
        f"\nReport saved to {output_path}"
    )