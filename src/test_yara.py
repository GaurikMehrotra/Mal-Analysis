from analyzers.yara_generator import generate_yara

caps = [
    {"api": "CreateProcessW"},
    {"api": "RegCreateKeyExW"},
    {"api": "RegSetValueExW"}
]

print(generate_yara(caps))
