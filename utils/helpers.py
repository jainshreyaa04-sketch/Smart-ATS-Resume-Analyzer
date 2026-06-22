def generate_ai_suggestions(score, missing):
    suggestions = []

    if score >= 80:
        suggestions.append("Excellent ATS score. Your resume is well optimized.")
    elif score >= 60:
        suggestions.append("Your resume is good, but adding a few missing skills will improve it.")
    else:
        suggestions.append("Your resume needs improvement to increase ATS compatibility.")

    if missing:
        suggestions.append("Add the following important skills if you have experience:")
        for skill in missing:
            suggestions.append(f"• {skill}")

    suggestions.extend([
        "Use strong action verbs such as Developed, Built, Designed, Implemented.",
        "Quantify achievements using numbers wherever possible.",
        "Keep your resume to one page for campus placements.",
        "Add your GitHub and LinkedIn profile links.",
        "Highlight your best academic or personal projects."
    ])

    return suggestions