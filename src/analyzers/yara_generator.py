def generate_yara(capabilities):

    rule = """
rule Malware_Agent_Detection
{
    meta:
        author = "Gaurik Malware Agent"
        description = "Auto-generated rule"

    strings:
"""

    count = 1

    for item in capabilities:

        api = item["api"]

        rule += f'        $api{count} = "{api}"\n'

        count += 1

    rule += """

    condition:
        2 of them
}
"""

    return rule
