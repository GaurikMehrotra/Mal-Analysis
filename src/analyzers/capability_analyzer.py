from utils.suspicious_apis import SUSPICIOUS_APIS


def detect_capabilities(imports):

    findings = []

    for item in imports:

        api = item["api"]

        if api in SUSPICIOUS_APIS:

            findings.append(
                {
                    "api": api,
                    "capability": SUSPICIOUS_APIS[api]
                }
            )

    return findings