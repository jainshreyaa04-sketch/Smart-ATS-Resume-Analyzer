def calculate_match(resume_text, job_description):
    if not job_description.strip():
        return 0, []

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    common = resume_words.intersection(jd_words)
    missing = jd_words - resume_words

    if len(jd_words) == 0:
        score = 0
    else:
        score = int((len(common) / len(jd_words)) * 100)

    return score, sorted(list(missing))[:20]