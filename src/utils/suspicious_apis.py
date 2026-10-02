SUSPICIOUS_APIS = {
    # Process Injection
    "VirtualAllocEx": "Process Injection",
    "WriteProcessMemory": "Process Injection",
    "CreateRemoteThread": "Process Injection",
    "NtMapViewOfSection": "Process Injection",

    # Persistence
    "RegCreateKeyExA": "Persistence",
    "RegCreateKeyExW": "Persistence",
    "RegSetValueExA": "Persistence",
    "RegSetValueExW": "Persistence",

    # Networking
    "InternetOpenA": "Networking",
    "InternetOpenW": "Networking",
    "InternetConnectA": "Networking",
    "InternetConnectW": "Networking",
    "WinHttpSendRequest": "Networking",

    # Encryption
    "CryptEncrypt": "Encryption",
    "CryptDecrypt": "Encryption",

    # Process Creation
    "CreateProcessA": "Process Creation",
    "CreateProcessW": "Process Creation",

    # Shell Execution
    "ShellExecuteA": "Shell Execution",
    "ShellExecuteW": "Shell Execution"
}