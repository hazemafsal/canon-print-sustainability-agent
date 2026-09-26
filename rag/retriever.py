import os


DOCUMENT_PATH = r"C:\Users\hp\canon_print_sustainability_agent\rag\document\sustainability_policy.txt"


def load_documents():

    if not os.path.exists(DOCUMENT_PATH):
        return ""

    with open(
        DOCUMENT_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def retrieve_relevant_context(query):

    document = load_documents()

    if not document:
        return ""

    query_words = set(
        query.lower().split()
    )

    paragraphs = document.split("\n\n")

    scored = []

    for paragraph in paragraphs:

        words = set(
            paragraph.lower().split()
        )

        score = len(
            query_words.intersection(words)
        )

        scored.append(
            (score, paragraph)
        )

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    top_results = [
        paragraph
        for score, paragraph in scored[:3]
        if score > 0
    ]

    return "\n\n".join(top_results)