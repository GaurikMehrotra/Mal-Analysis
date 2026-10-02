import pefile

def analyze_pe(path):
    pe = pefile.PE(path)

    return {
        "entry_point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
        "image_base": hex(pe.OPTIONAL_HEADER.ImageBase),
        "sections": [
            section.Name.decode(errors="ignore").strip("\x00")
            for section in pe.sections
        ]
    }