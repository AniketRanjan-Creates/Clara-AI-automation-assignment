# Clara AI Automation Assignment

## Overview

This project builds a zero-cost automation pipeline that converts demo call transcripts into Retell AI agent configurations and updates them after onboarding calls.

The system extracts structured account data, generates agent prompts, versions configurations, and logs changes.

## Architecture

Demo Transcript
↓
Extraction Script
↓
Account Memo JSON
↓
Agent Spec Generator
↓
Stored in Versioned Account Folder

Onboarding Transcript
↓
Update Script
↓
Memo v2
↓
Agent Spec v2
↓
Changelog

## Project Structure

scripts/
Core automation scripts

transcripts/
Demo and onboarding call transcripts

outputs/
Generated account memos and agent configurations

workflows/
Automation workflow documentation

run_pipeline.py
Main pipeline runner

## Setup

1. Clone repository
2. Ensure Python 3 installed

No paid APIs or services are used.

## Running the Pipeline

Run:

python run_pipeline.py

This will:

1. Process all demo transcripts
2. Generate v1 agent configurations
3. Apply onboarding updates
4. Generate v2 agent configurations
5. Produce changelog files

## Output Example

outputs/accounts/account_1/

v1/
memo.json
agent_spec.json

v2/
memo.json
agent_spec.json
changes.md

## Limitations

Extraction uses rule-based parsing and assumes structured transcripts.

In production, an LLM-based extraction system would improve accuracy.

## Future Improvements

- Integrate speech-to-text for audio files
- Add UI dashboard for monitoring
- Automate agent deployment to Retell