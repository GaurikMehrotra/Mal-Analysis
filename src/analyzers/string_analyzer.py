import re


def extract_strings(path):

    with open(path, "rb") as f:
        data = f.read()

    strings = re.findall(
        rb"[ -~]{4,}",
        data
    )

    return [
        s.decode(
            errors="ignore"
        )
        for s in strings
    ]


def find_interesting_strings(strings):

    keywords = [
        "http",
        "https",
        "cmd.exe",
        "powershell",
        ".onion",
        "discord",
        "telegram",
        "bitcoin",
        "wallet"
    ]

    findings = []

    for s in strings:

        lower = s.lower()

        for keyword in keywords:

            if keyword in lower:

                findings.append(s)
                break

    return findings