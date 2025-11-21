#!/usr/bin/env python3
"""
Script to create Mr. Jace agent in Retell.AI using the API
"""
import json
import sys

try:
    from retell import Retell
except ImportError:
    print("Installing retell-sdk...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "retell-sdk"])
    from retell import Retell

# Load configuration
with open('/home/user/retell-ai-jace/mr-jace-retell-config.json', 'r') as f:
    config = json.load(f)

# Initialize Retell client
API_KEY = "key_c4f96188afaa930aa943e8bd890b"
client = Retell(api_key=API_KEY)

try:
    # First, let's test the connection by listing existing agents
    print("Testing API connection...")
    agents = client.agent.list()
    print(f"✓ API connection successful! Found {len(agents)} existing agents.")

    # Create the agent
    print("\nCreating Mr. Jace agent...")

    agent_response = client.agent.create(
        agent_name=config["agent_name"],
        voice_id=config["voice_id"],
        voice_model=config["voice_model"],
        voice_temperature=config["voice_temperature"],
        voice_speed=config["voice_speed"],
        responsiveness=config["responsiveness"],
        interruption_sensitivity=config["interruption_sensitivity"],
        enable_backchannel=config["enable_backchannel"],
        backchannel_frequency=config["backchannel_frequency"],
        backchannel_words=config["backchannel_words"],
        language=config["language"],
        ambient_sound=config["ambient_sound"],
        ambient_sound_volume=config["ambient_sound_volume"],
        llm_websocket_url=config["llm_websocket_url"],
        model=config["model"],
        temperature=config["temperature"],
        max_tokens=config["max_tokens"],
        begin_message=config["begin_message"],
        general_prompt=config["general_prompt"],
        general_tools=config["general_tools"],
        enable_transcription_formatting=config["enable_transcription_formatting"],
        opt_out_sensitive_data_storage=config["opt_out_sensitive_data_storage"],
        pronunciation_dictionary=config["pronunciation_dictionary"],
        normalize_for_speech=config["normalize_for_speech"],
        boosted_keywords=config["boosted_keywords"],
        reminder_trigger_ms=config["reminder_trigger_ms"],
        reminder_max_count=config["reminder_max_count"],
    )

    print(f"\n✓ Agent created successfully!")
    print(f"Agent ID: {agent_response.agent_id}")
    print(f"Agent Name: {agent_response.agent_name}")

    # Save agent ID for reference
    with open('/home/user/retell-ai-jace/agent_info.json', 'w') as f:
        json.dump({
            "agent_id": agent_response.agent_id,
            "agent_name": agent_response.agent_name,
            "created_at": str(agent_response)
        }, f, indent=2)

    print(f"\nAgent info saved to: agent_info.json")
    print(f"\nNote: Custom functions need to be added separately via the Retell.AI dashboard")
    print(f"See mr-jace-deployment-guide.md for the 15 custom function definitions.")

except Exception as e:
    print(f"\n✗ Error: {e}")
    print(f"\nTroubleshooting:")
    print(f"1. Verify API key is valid in Retell.AI dashboard")
    print(f"2. Check if you have sufficient API permissions")
    print(f"3. Review error message above for specific issues")
    sys.exit(1)
