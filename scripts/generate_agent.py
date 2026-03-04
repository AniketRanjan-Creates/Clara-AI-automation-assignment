import json
import os

ACCOUNTS_DIR = "outputs/accounts"

accounts = os.listdir(ACCOUNTS_DIR)

for account in accounts:

    memo_path = os.path.join(ACCOUNTS_DIR, account, "v1", "memo.json")

    if not os.path.exists(memo_path):
        continue

    with open(memo_path, "r") as f:
        memo = json.load(f)

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
5. If transfer fails, inform the caller and promise callback

AFTER HOURS FLOW
1. Greet caller
2. Ask if the issue is an emergency
3. If emergency, collect name, number, and address
4. Attempt technician transfer
5. If transfer fails, assure quick follow-up
6. Ask if anything else is needed before ending
""",
        "call_transfer_protocol": "Attempt technician transfer. Retry once if failed.",
        "fallback_protocol": "Collect caller name and phone number and promise callback.",
        "version": "v1"
    }

    agent_path = os.path.join(ACCOUNTS_DIR, account, "v1", "agent_spec.json")

    with open(agent_path, "w") as f:
        json.dump(agent, f, indent=2)

    print(f"Agent generated for {account}")