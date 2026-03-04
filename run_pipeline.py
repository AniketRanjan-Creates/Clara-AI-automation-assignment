import os

print("Starting Clara automation pipeline...\n")

print("Step 1: Extracting account memos from demo transcripts...")
os.system("python scripts/extract_memo.py")

print("\nStep 2: Generating agent specifications...")
os.system("python scripts/generate_agent.py")

print("\nStep 3: Applying onboarding updates...")
os.system("python scripts/update_agent.py")

print("\nPipeline completed successfully.")