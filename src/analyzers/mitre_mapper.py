MITRE_MAPPING = {
    "CreateProcessW": {
        "technique": "T1106",
        "name": "Native API"
    },

    "RegCreateKeyExW": {
        "technique": "T1547",
        "name": "Boot or Logon Autostart Execution"
    },

    "RegSetValueExW": {
        "technique": "T1547",
        "name": "Boot or Logon Autostart Execution"
    },

    "URLDownloadToFileW": {
        "technique": "T1105",
        "name": "Ingress Tool Transfer"
    },

    "InternetOpenUrlW": {
        "technique": "T1071",
        "name": "Application Layer Protocol"
    },

    "WinExec": {
        "technique": "T1059",
        "name": "Command and Scripting Interpreter"
    }
}


def map_to_mitre(capabilities):

    results = []

    for item in capabilities:

        api = item["api"]

        if api in MITRE_MAPPING:

            results.append({
                "api": api,
                "technique": MITRE_MAPPING[api]["technique"],
                "name": MITRE_MAPPING[api]["name"]
            })

    return results
