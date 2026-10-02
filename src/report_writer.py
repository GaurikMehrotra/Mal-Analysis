def save_markdown_report(content, output_path):

    with open(output_path, "w") as f:
        f.write(content)

    print(
        f"Markdown report saved to {output_path}"
    )
