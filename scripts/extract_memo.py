import json
import re
import os

DEMO_DIR = "transcripts/demo"
OUTPUT_DIR = "outputs/accounts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

files = os.listdir(DEMO_DIR)

account_number = 1

for file in files:

    if not file.endswith(".txt"):
        continue

    path = os.path.join(DEMO_DIR, file)

    with open(path, "r") as f:
        text = f.read()

    company = re.search(r"Company name[:\-]\s*(.*)", text)
    hours = re.search(r"operate (.*)", text)
    address = re.search(r"address is (.*)", text)

    account_id = f"account_{account_number}"

    memo = {
        "account_id": account_id,
        "company_name": company.group(1) if company else "",
        "business_hours": hours.group(1) if hours else "",
        "office_address": address.group(1) if address else "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": [],
        "notes": "Generated from demo transcript"
    }

    account_folder = os.path.join(OUTPUT_DIR, account_id, "v1")
    os.makedirs(account_folder, exist_ok=True)

    memo_path = os.path.join(account_folder, "memo.json")

    with open(memo_path, "w") as f:
        json.dump(memo, f, indent=2)

    print(f"Generated memo for {account_id}")

    account_number += 1