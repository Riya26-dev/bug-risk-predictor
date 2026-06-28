def generate_comment(risk, probability):
    """
    Generate AI review comment based on risk prediction.
    """

    probability = probability * 100

    if probability >= 80:
        return f"""
⚠️ AI Code Review

Prediction : {risk}
Risk Score : {probability:.2f}%

Reason:
• Large or complex code changes detected.
• Higher chance of introducing bugs.

Recommendation:
✔ Request another reviewer.
✔ Run complete test suite.
✔ Verify code coverage before merging.
"""

    elif probability >= 40:
        return f"""
🟡 AI Code Review

Prediction : {risk}
Risk Score : {probability:.2f}%

Reason:
• Moderate risk detected.

Recommendation:
✔ Review the changed files carefully.
✔ Run unit tests before merging.
"""

    else:
        return f"""
✅ AI Code Review

Prediction : {risk}
Risk Score : {probability:.2f}%

Reason:
• Low risk commit.

Recommendation:
✔ Safe to proceed with normal review.
✔ Merge after standard testing.
"""


# Test
if __name__ == "__main__":

    print(generate_comment("HIGH RISK", 0.91))
    print("------------------------------------")
    print(generate_comment("LOW RISK", 0.20))