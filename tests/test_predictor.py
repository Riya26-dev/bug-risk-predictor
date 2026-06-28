import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Change working directory to root so model paths work
os.chdir(os.path.join(os.path.dirname(__file__), '..'))

from predictor import predict_risk
from comment_generator import generate_comment

def test_high_risk():
    risk, prob = predict_risk(8, 500, 100, 600, 10, 1)
    assert risk in ["HIGH RISK", "LOW RISK"]
    print(f"✅ High risk test: {risk} ({prob*100:.1f}%)")

def test_low_risk():
    risk, prob = predict_risk(1, 10, 2, 12, 30, 1)
    assert risk in ["HIGH RISK", "LOW RISK"]
    print(f"✅ Low risk test: {risk} ({prob*100:.1f}%)")

def test_comment():
    comment = generate_comment("HIGH RISK", 0.91)
    assert comment is not None
    print("✅ Comment generator test passed")

if __name__ == "__main__":
    test_high_risk()
    test_low_risk()
    test_comment()
    print("\n🎉 All tests passed!")