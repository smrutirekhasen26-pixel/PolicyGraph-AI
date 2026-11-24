import re


def extract_policy_details(text: str) -> dict:
    """Extract key information from policy text."""

    details = {
        "eligibility": None,
        "minimum_age": None,
        "scholarship_amount": None,
        "application_deadline": None
    }

    eligibility = re.search(
        r"Eligibility:\s*(.*)",
        text,
        re.IGNORECASE
    )

    age = re.search(
        r"at least (\d+) years old",
        text,
        re.IGNORECASE
    )

    amount = re.search(
        r"Rs\.?\s*([\d,]+)\s*per year",
        text,
        re.IGNORECASE
    )

    deadline = re.search(
        r"before\s+(\d{1,2}\s+\w+\s+\d{4})",
        text,
        re.IGNORECASE
    )

    if eligibility:
        details["eligibility"] = eligibility.group(1).strip()

    if age:
        details["minimum_age"] = int(age.group(1))

    if amount:
        details["scholarship_amount"] = int(
            amount.group(1).replace(",", "")
        )

    if deadline:
        details["application_deadline"] = deadline.group(1)

    return details