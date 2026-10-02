from analyzers.capability_analyzer import detect_capabilities
from analyzers.mitre_mapper import map_to_mitre

sample_imports = [
    {"dll": "KERNEL32.dll", "api": "CreateProcessW"},
    {"dll": "ADVAPI32.dll", "api": "RegCreateKeyExW"},
    {"dll": "ADVAPI32.dll", "api": "RegSetValueExW"}
]

caps = detect_capabilities(sample_imports)

mitre = map_to_mitre(caps)

for item in mitre:
    print(item)
