import json

from agents.prompts import ROOT_CAUSE_PROMPT
from services.llm import llm
from rag.retriever import retrieve_relevant_context


def root_cause_agent(waste_findings):

    if not waste_findings:

        return {
            "analysis":
                "No significant print-waste pattern was detected."
        }

    knowledge = retrieve_relevant_context(
        "reprint failed printing color sustainability workflow"
    )

    waste_text = json.dumps(
        waste_findings,
        indent=2
    )

    chain = ROOT_CAUSE_PROMPT | llm

    response = chain.invoke(
        {
            "waste_findings": waste_text,
            "knowledge": knowledge
        }
    )

    return {
        "analysis": response.content,
        "knowledge": knowledge
    }