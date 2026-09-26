from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from agents.data_quality_agent import (
    data_quality_agent
)

from agents.waste_detection_agent import (
    waste_detection_agent
)

from agents.root_cause_agent import (
    root_cause_agent
)

from agents.strategy_agent import (
    strategy_agent
)

from agents.decision_agent import (
    decision_agent
)

from agents.monitoring_agent import (
    monitoring_agent
)


class SustainabilityState(TypedDict, total=False):

    df: object

    data_quality: dict

    waste_findings: list

    root_cause: dict

    strategy: dict

    decision: dict

    monitoring: dict


# --------------------------------------------------
# DATA QUALITY
# --------------------------------------------------

def quality_node(state):

    result = data_quality_agent(
        state["df"]
    )

    return {
        "data_quality": result
    }


# --------------------------------------------------
# WASTE DETECTION
# --------------------------------------------------

def waste_node(state):

    result = waste_detection_agent(
        state["df"]
    )

    return {
        "waste_findings": result
    }


# --------------------------------------------------
# ROOT CAUSE
# --------------------------------------------------

def root_cause_node(state):

    result = root_cause_agent(
        state["waste_findings"]
    )

    return {
        "root_cause": result
    }


# --------------------------------------------------
# STRATEGY
# --------------------------------------------------

def strategy_node(state):

    result = strategy_agent(
        state["waste_findings"],
        state["root_cause"]
    )

    return {
        "strategy": result
    }


# --------------------------------------------------
# DECISION
# --------------------------------------------------

def decision_node(state):

    result = decision_agent(
        state["strategy"]
    )

    return {
        "decision": result
    }


# --------------------------------------------------
# MONITORING
# --------------------------------------------------

def monitoring_node(state):

    result = monitoring_agent(
        state["df"]
    )

    return {
        "monitoring": result
    }


# --------------------------------------------------
# BUILD LANGGRAPH
# --------------------------------------------------

def build_graph():

    workflow = StateGraph(
        SustainabilityState
    )

    workflow.add_node(
        "data_quality",
        quality_node
    )

    workflow.add_node(
        "waste_detection",
        waste_node
    )

    workflow.add_node(
        "root_cause",
        root_cause_node
    )

    workflow.add_node(
        "strategy",
        strategy_node
    )

    workflow.add_node(
        "decision",
        decision_node
    )

    workflow.add_node(
        "monitoring",
        monitoring_node
    )

    workflow.set_entry_point(
        "data_quality"
    )

    workflow.add_edge(
        "data_quality",
        "waste_detection"
    )

    workflow.add_edge(
        "waste_detection",
        "root_cause"
    )

    workflow.add_edge(
        "root_cause",
        "strategy"
    )

    workflow.add_edge(
        "strategy",
        "decision"
    )

    workflow.add_edge(
        "decision",
        "monitoring"
    )

    workflow.add_edge(
        "monitoring",
        END
    )

    return workflow.compile()