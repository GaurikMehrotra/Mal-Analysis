from analyzers.risk_scorer import calculate_risk
from analyzers.mitre_mapper import map_to_mitre
from analyzers.pe_analyzer import analyze_pe
from analyzers.import_analyzer import get_imports
from analyzers.capability_analyzer import detect_capabilities
from analyzers.string_analyzer import (
    extract_strings,
    find_interesting_strings
)
from analyzers.entropy_analyzer import analyze_entropy


def run_analysis(sample_path):

    pe_info = analyze_pe(sample_path)

    imports = get_imports(sample_path)

    capabilities = detect_capabilities(imports)

    mitre_attack = map_to_mitre(capabilities)

    strings = extract_strings(sample_path)

    interesting_strings = find_interesting_strings(strings)

    entropy = analyze_entropy(sample_path)
    risk_score = calculate_risk(
    {
        "capabilities": capabilities,
        "entropy": entropy,
        "mitre_attack": mitre_attack
    } )

    return {
        "file": sample_path,
        "risk_score": risk_score,
        "pe_info": pe_info,
        "imports_count": len(imports),
        "capabilities": capabilities,
        "mitre_attack": mitre_attack,
        "interesting_strings": interesting_strings[:50],
        "entropy": entropy
    }