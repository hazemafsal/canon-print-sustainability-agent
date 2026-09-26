def decision_agent(strategy):

    return {
        "status": "PENDING HUMAN APPROVAL",

        "strategy":
            strategy["recommendations"],

        "approval_required": True
    }