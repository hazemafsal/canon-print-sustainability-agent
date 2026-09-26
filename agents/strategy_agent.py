import json

from agents.prompts import STRATEGY_PROMPT
from services.llm import llm
from rag.retriever import retrieve_relevant_context


def strategy_agent(
    waste_findings,
    root_cause
):

    knowledge = retrieve_relevant_context(
        "sustainability duplex color printing "
        "digital workflow reprints"
    )

    waste_text = json.dumps(
        waste_findings,
        indent=2
    )

    chain = STRATEGY_PROMPT | llm

    response = chain.invoke(
        {
            "waste_findings": waste_text,

            "root_cause":
                root_cause["analysis"],

            "knowledge":
                knowledge
        }
    )

    return {
        "recommendations":
            response.content,

        "knowledge":
            knowledge
    }