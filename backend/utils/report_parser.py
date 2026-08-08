import re

def extract_section(text, start, end=None):
    pattern = rf"##\s*{re.escape(start)}(.*)"
    if end:
        pattern = rf"##\s*{re.escape(start)}(.*?)##\s*{re.escape(end)}"

    m = re.search(pattern, text, re.S)
    return m.group(1).strip() if m else ""


def extract_bullets(section):
    return [
        line.replace("-", "").strip()
        for line in section.splitlines()
        if line.strip().startswith("-")
    ]


def markdown_to_analysis(markdown):

    strengths = extract_bullets(
        extract_section(markdown, "5. Strengths", "6. Weaknesses")
    )

    weaknesses = extract_bullets(
        extract_section(markdown, "6. Weaknesses", "7. Opportunities")
    )

    opportunities = extract_bullets(
        extract_section(markdown, "7. Opportunities", "8. Threats")
    )

    threats = extract_bullets(
        extract_section(markdown, "8. Threats", "9. Market Demand")
    )

    summary = extract_section(
        markdown,
        "1. Product Summary",
        "2. Key Features",
    )

    return {
        "executive_summary": summary,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "opportunities": opportunities,
        "threats": threats,
        "opportunity_score": len(opportunities) * 20,
        "risk_score": len(threats) * 15,
        "markdown": markdown,
    }