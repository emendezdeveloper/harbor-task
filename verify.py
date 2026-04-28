import json
import sys

with open("oracle.json") as f:
    oracle = json.load(f)

with open("output.json") as f:
    output = json.load(f)

score = 0
expected = len(oracle["vulnerabilities"])
found = len(output.get("vulnerabilities", []))

for vuln in oracle["vulnerabilities"]:
    for out in output.get("vulnerabilities", []):
        if vuln["file"] == out.get("file"):
            score += 1

percentage = (score / expected * 100) if expected > 0 else 0
passed = percentage >= 80

print("=" * 50 + " SECURITY AUDIT RESULTS " + "=" * 50)
print(f"Expected vulnerabilities: {expected}")
print(f"Found vulnerabilities: {found}")
print(f"Score: {score}/{expected} ({percentage:.1f}%)")
print(f"Required: 80% or higher")
print("=" * 124)
if passed:
    print("\u2705 AUDIT PASSED")
else:
    print("\u274c AUDIT FAILED")

sys.exit(0 if passed else 1)