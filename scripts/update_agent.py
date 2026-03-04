import json
import os
import re

ACCOUNT_DIR = "outputs/accounts/account_1"
ONBOARDING_FILE = "transcripts/onboarding/onboarding_call_1.txt"

with open(ONBOARDING_FILE, "r") as f:
    text = f.read()

company = re.search(r"Company name[:\-]\s*(.*)", text)
hours = re.search(r"hours updated to (.*)", text)
address = re.search(r"address remains (.*)", text)

v1_path = os.path.join(ACCOUNT_DIR, "v1", "memo.json")

with open(v1_path, "r") as f:
    memo = json.load(f)

old_hours = memo["business_hours"]

if hours:
    memo["business_hours"] = hours.group(1)

if address:
    memo["office_address"] = address.group(1)

v2_folder = os.path.join(ACCOUNT_DIR, "v2")
os.makedirs(v2_folder, exist_ok=True)

v2_memo_path = os.path.join(v2_folder, "memo.json")

with open(v2_memo_path, "w") as f:
    json.dump(memo, f, indent=2)

changes = f"""
Business hours changed:
OLD: {old_hours}
NEW: {memo['business_hours']}
"""

change_path = os.path.join(v2_folder, "changes.md")

with open(change_path, "w") as f:
    f.write(changes)

print("v2 memo created and changes logged")

agent = {
    "agent_name": memo["company_name"] + " Assistant",
    "voice_style": "professional and friendly",
    "system_prompt": f"""
You are the phone assistant for {memo['company_name']}.

Business hours:
{memo['business_hours']}

Office address:
{memo['office_address']}

OFFICE HOURS FLOW
1. Greet the caller politely
2. Ask the purpose of the call
3. Collect caller name and phone number
4. Route or transfer the call
5. If transfer fails, inform caller and promise callback

AFTER HOURS FLOW
1. Greet caller
2. Ask if the issue is an emergency
3. Collect name, phone, and address
4. Attempt technician transfer
5. If transfer fails, assure quick follow-up
6. Ask if anything else is needed
""",
    "call_transfer_protocol": "Attempt technician transfer, retry once if failed",
    "fallback_protocol": "Collect caller info and promise callback",
    "version": "v2"
}

agent_path = os.path.join(v2_folder, "agent_spec.json")

with open(agent_path, "w") as f:
    json.dump(agent, f, indent=2)

print("v2 agent generated")