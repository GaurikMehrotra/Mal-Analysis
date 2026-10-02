import pefile


def get_imports(path):
    pe = pefile.PE(path)

    imports = []

    if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
        for dll in pe.DIRECTORY_ENTRY_IMPORT:

            dll_name = dll.dll.decode(errors="ignore")

            for imp in dll.imports:

                if imp.name:
                    imports.append(
                        {
                            "dll": dll_name,
                            "api": imp.name.decode(errors="ignore")
                        }
                    )

    return imports