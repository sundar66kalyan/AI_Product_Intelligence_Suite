import re


def _section(markdown: str, start: str, end: str | None = None):

    if end:
        pattern = rf"{re.escape(start)}(.*?){re.escape(end)}"
    else:
        pattern = rf"{re.escape(start)}(.*)"

    m = re.search(pattern, markdown, re.S)

    if m:
        return m.group(1).strip()

    return ""


def _bullets(text):

    items = []

    for line in text.splitlines():

        line = line.strip()

        if line.startswith("-"):

            items.append(line[1:].strip())

    return items


def markdown_to_json(markdown):

    summary = _section(
        markdown,
        "1. Product Summary",
        "2. Key Features",
    )

    strengths = _bullets(
        _section(
            markdown,
            "5. Strengths",
            "6. Weaknesses",
        )
    )

    weaknesses = _bullets(
        _section(
            markdown,
            "6. Weaknesses",
            "7. Opportunities",
        )
    )

    opportunities = _bullets(
        _section(
            markdown,
            "7. Opportunities",
            "8. Threats",
        )
    )

    threats = _bullets(
        _section(
            markdown,
            "8. Threats",
            "9. Market Demand",
        )
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