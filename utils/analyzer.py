ROLE_KEYWORDS = {
    "AI Engineer": [
        "python", "machine learning", "deep learning", "tensorflow",
        "pytorch", "nlp", "sql", "git"
    ],
    "Cybersecurity": [
        "network security", "linux", "python", "wireshark",
        "penetration testing", "firewall", "nmap", "siem"
    ],
    "Software Engineer": [
        "java", "python", "c++", "sql", "git",
        "oop", "data structures", "algorithms"
    ]
}

def analyze_resume(resume_text, role):
    resume = resume_text.lower()

    keywords = ROLE_KEYWORDS.get(role, [])

    matched = []
    missing = []

    for word in keywords:
        if word.lower() in resume:
            matched.append(word)
        else:
            missing.append(word)

    if len(keywords) == 0:
        score = 0
    else:
        score = int((len(matched) / len(keywords)) * 100)

    return score, missing