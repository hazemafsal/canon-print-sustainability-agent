import streamlit as st
import pandas as pd

from utils.data_loader import (
    load_printer_data,
    validate_columns
)

from services.calculations import (
    calculate_metrics,
    department_metrics
)

from workflow.graph import build_graph


# ==================================================
# CLEAN AI OUTPUT
# ==================================================

def clean_ai_output(value):

    if value is None:
        return ""

    if isinstance(value, str):
        return value.strip()

    if isinstance(value, list):

        text_parts = []

        for item in value:

            if isinstance(item, dict):

                if item.get("type") == "text":

                    text_parts.append(
                        item.get("text", "")
                    )

                elif "text" in item:

                    text_parts.append(
                        str(item["text"])
                    )

            elif isinstance(item, str):

                text_parts.append(item)

        return "\n".join(
            text_parts
        ).strip()

    return str(value)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Print Sustainability Agent",
    page_icon="🖨️",
    layout="wide"
)


# ==================================================
# HEADER
# ==================================================

st.title(
    "🖨️ AI Print Waste & Sustainability Decision Agent"
)

st.write(
    """
    Multi-agent AI prototype for identifying print waste,
    investigating possible causes, generating sustainability
    strategies and monitoring operational impact.
    """
)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("Data Source")

uploaded_file = st.sidebar.file_uploader(
    "Upload printer CSV",
    type=["csv"]
)


# ==================================================
# LOAD DATA
# ==================================================

try:

    df = load_printer_data(
        uploaded_file
    )

except Exception as error:

    st.error(
        f"Unable to load data: {error}"
    )

    st.stop()


# ==================================================
# VALIDATE DATA
# ==================================================

missing_columns = validate_columns(df)

if missing_columns:

    st.error(
        "Missing columns: "
        + ", ".join(missing_columns)
    )

    st.stop()


# ==================================================
# CALCULATE METRICS
# ==================================================

metrics = calculate_metrics(df)


# ==================================================
# KPI DASHBOARD
# ==================================================

st.subheader(
    "Executive Sustainability Dashboard"
)

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "Total Pages",
        f"{metrics['total_pages']:,.0f}"
    )


with col2:

    st.metric(
        "Reprints",
        f"{metrics['total_reprints']:,.0f}"
    )


with col3:

    st.metric(
        "Reprint Rate",
        f"{metrics['reprint_rate']:.2f}%"
    )


with col4:

    st.metric(
        "Color Rate",
        f"{metrics['color_rate']:.2f}%"
    )


with col5:

    st.metric(
        "Energy",
        f"{metrics['total_energy']:,.1f} kWh"
    )


# ==================================================
# DATA PREVIEW
# ==================================================

st.subheader(
    "Printer Data"
)

st.dataframe(
    df,
    use_container_width=True
)


# ==================================================
# DEPARTMENT ANALYSIS
# ==================================================

st.subheader(
    "Department Analysis"
)

dept = department_metrics(df)

st.dataframe(
    dept,
    use_container_width=True
)


# ==================================================
# RUN AI AGENTS
# ==================================================

st.subheader(
    "🤖 AI Agentic Analysis"
)


if st.button(
    "🚀 Run LangGraph Sustainability Agents",
    type="primary"
):

    with st.spinner(
        "LangGraph is running the AI agents..."
    ):

        try:

            # --------------------------------------
            # BUILD GRAPH
            # --------------------------------------

            graph = build_graph()


            # --------------------------------------
            # INITIAL STATE
            # --------------------------------------

            initial_state = {
                "df": df
            }


            # --------------------------------------
            # RUN LANGGRAPH
            # --------------------------------------

            result = graph.invoke(
                initial_state
            )


            # --------------------------------------
            # SAVE RESULT
            # --------------------------------------

            st.session_state[
                "agent_result"
            ] = result


            st.success(
                "✅ LangGraph workflow completed successfully."
            )


        except Exception as error:

            st.error(
                f"Agent workflow error: {error}"
            )


# ==================================================
# DISPLAY AGENT RESULTS
# ==================================================

if "agent_result" not in st.session_state:

    st.info(
        "Click '🚀 Run LangGraph Sustainability Agents' "
        "to start the AI analysis."
    )

else:

    # Get saved result
    result = st.session_state[
        "agent_result"
    ]


    # ==================================================
    # 1. DATA QUALITY AGENT
    # ==================================================

    st.header(
        "1️⃣ Data Quality Agent"
    )

    quality = result.get(
        "data_quality",
        {}
    )


    quality_status = quality.get(
        "status",
        "UNKNOWN"
    )


    if quality_status == "PASS":

        st.success(
            quality.get(
                "message",
                "Data quality checks passed."
            )
        )

    else:

        st.warning(
            quality.get(
                "message",
                "Data quality requires attention."
            )
        )


        issues = quality.get(
            "issues",
            []
        )


        for issue in issues:

            st.write(
                f"• {issue}"
            )


    # ==================================================
    # 2. WASTE DETECTION AGENT
    # ==================================================

    st.header(
        "2️⃣ Waste Detection Agent"
    )


    findings = result.get(
        "waste_findings",
        []
    )


    if findings:

        findings_df = pd.DataFrame(
            findings
        )


        st.dataframe(
            findings_df,
            use_container_width=True
        )

    else:

        st.success(
            "No significant waste pattern detected."
        )


    # ==================================================
    # 3. ROOT CAUSE AGENT
    # ==================================================

    st.header(
        "3️⃣ 🤖 AI Root Cause Agent"
    )


    root_cause = result.get(
        "root_cause",
        {}
    )


    root_cause_text = clean_ai_output(
        root_cause.get(
            "analysis",
            "No root cause analysis available."
        )
    )


    st.markdown(
        root_cause_text
    )


    # RAG CONTEXT

    with st.expander(
        "📚 RAG Knowledge Used"
    ):

        knowledge = root_cause.get(
            "knowledge",
            "No context available."
        )


        st.write(
            knowledge
        )


    # ==================================================
    # 4. STRATEGY AGENT
    # ==================================================

    st.header(
        "4️⃣ 💡 AI Sustainability Strategy Agent"
    )


    strategy = result.get(
        "strategy",
        {}
    )


    strategy_text = clean_ai_output(
        strategy.get(
            "recommendations",
            "No sustainability recommendations available."
        )
    )


    st.markdown(
        strategy_text
    )


    # RAG CONTEXT

    with st.expander(
        "📚 Sustainability Knowledge Retrieved"
    ):

        strategy_knowledge = strategy.get(
            "knowledge",
            "No context available."
        )


        st.write(
            strategy_knowledge
        )


    # ==================================================
    # 5. HUMAN DECISION
    # ==================================================

    st.header(
        "5️⃣ 👤 Human Decision"
    )


    decision = result.get(
        "decision",
        {}
    )


    decision_status = decision.get(
        "status",
        "PENDING HUMAN APPROVAL"
    )


    st.warning(
        decision_status
    )


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "✅ Approve Recommendation",
            key="approve_recommendation"
        ):

            st.session_state[
                "approval"
            ] = "APPROVED"

            st.success(
                "Recommendation approved by user."
            )


    with col2:

        if st.button(
            "❌ Reject Recommendation",
            key="reject_recommendation"
        ):

            st.session_state[
                "approval"
            ] = "REJECTED"

            st.error(
                "Recommendation rejected by user."
            )


    # ==================================================
    # APPROVAL STATUS
    # ==================================================

    if "approval" in st.session_state:

        approval = st.session_state[
            "approval"
        ]


        if approval == "APPROVED":

            st.success(
                "🟢 Human approval recorded."
            )

        elif approval == "REJECTED":

            st.error(
                "🔴 Recommendation rejected."
            )


    # ==================================================
    # 6. MONITORING AGENT
    # ==================================================

    st.header(
        "6️⃣ 📈 Monitoring Agent"
    )


    monitoring = result.get(
        "monitoring",
        {}
    )


    percentage_change = monitoring.get(
        "percentage_change",
        0
    )


    message = monitoring.get(
        "message",
        "No monitoring information available."
    )


    st.metric(
        "Reprint Change",
        f"{percentage_change:.2f}%"
    )


    st.info(
        message
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "AI Print Waste & Sustainability Decision Agent | "
    "LangChain + LangGraph + Gemini + RAG"
)
