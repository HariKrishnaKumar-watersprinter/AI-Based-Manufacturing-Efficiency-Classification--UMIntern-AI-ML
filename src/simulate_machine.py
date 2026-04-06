def simulate_machine(temp, vibration, latency):

    efficiency_score = (
        0.5 * temp +
        0.3 * vibration +
        0.2 * latency
    )

    if efficiency_score < 50:
        return "High"
    elif efficiency_score < 100:
        return "Medium"
    else:
        return "Low"