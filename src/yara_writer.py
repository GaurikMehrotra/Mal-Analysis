def save_yara(rule_text, output_file):

    with open(output_file, "w") as f:
        f.write(rule_text)

    print(f"YARA rule saved to {output_file}")
