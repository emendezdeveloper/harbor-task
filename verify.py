import json
import sys

with open("oracle.json") as f:
    oracle = json.load(f)

with open("output.json") as f:
    output = json.load(f)

score = 0

for vuln in oracle["vulnerabilities"]:
    for out in output.get("vulnerabilities", []):
        if vuln["file"] == out.get("file"):
            score += 1

print(f"Score: {score}/{len(oracle['vulnerabilities'])}")

if score == len(oracle["vulnerabilities"]):
    sys.exit(0)
else:
    sys.exit(1)