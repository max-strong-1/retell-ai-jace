#!/usr/bin/env python3
"""
Script to create Mr. Jace agent in Retell.AI using direct REST API
"""
import json
import requests

# Load configuration
with open('/home/user/retell-ai-jace/mr-jace-retell-config.json', 'r') as f:
    config = json.load(f)

# API configuration
API_KEY = "key_c4f96188afaa930aa943e8bd890b"
BASE_URL = "https://api.retellai.com"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def test_connection():
    """Test API connection by listing agents"""
    print("Testing API connection...")
    response = requests.get(f"{BASE_URL}/list-agents", headers=HEADERS)

    if response.status_code == 200:
        agents = response.json()
        print(f"✓ API connection successful!")
        return True
    else:
        print(f"✗ API connection failed: {response.status_code}")
        print(f"Response: {response.text}")
        return False

def create_agent():
    """Create Mr. Jace agent"""
    print("\nCreating Mr. Jace agent...")

    # Prepare agent data according to Retell.AI API spec
    agent_data = {
        "agent_name": config["agent_name"],
        "voice_id": config["voice_id"],
        "voice_model": config["voice_model"],
        "voice_temperature": config["voice_temperature"],
        "voice_speed": config["voice_speed"],
        "responsiveness": config["responsiveness"],
        "interruption_sensitivity": config["interruption_sensitivity"],
        "enable_backchannel": config["enable_backchannel"],
        "backchannel_frequency": config["backchannel_frequency"],
        "backchannel_words": config["backchannel_words"],
        "language": config["language"],
        "ambient_sound": config["ambient_sound"],
        "ambient_sound_volume": config["ambient_sound_volume"],
        "llm_websocket_url": config["llm_websocket_url"],
        "model": config["model"],
        "temperature": config["temperature"],
        "max_tokens": config["max_tokens"],
        "begin_message": config["begin_message"],
        "general_prompt": config["general_prompt"],
        "general_tools": config["general_tools"],
        "enable_transcription_formatting": config["enable_transcription_formatting"],
        "opt_out_sensitive_data_storage": config["opt_out_sensitive_data_storage"],
        "pronunciation_dictionary": config["pronunciation_dictionary"],
        "normalize_for_speech": config["normalize_for_speech"],
        "boosted_keywords": config["boosted_keywords"],
        "reminder_trigger_ms": config["reminder_trigger_ms"],
        "reminder_max_count": config["reminder_max_count"],
    }

    response = requests.post(
        f"{BASE_URL}/create-agent",
        headers=HEADERS,
        json=agent_data
    )

    if response.status_code in [200, 201]:
        agent_info = response.json()
        print(f"\n✓ Agent created successfully!")
        print(f"Agent ID: {agent_info.get('agent_id', 'N/A')}")
        print(f"Agent Name: {agent_info.get('agent_name', config['agent_name'])}")

        # Save agent info
        with open('/home/user/retell-ai-jace/agent_info.json', 'w') as f:
            json.dump(agent_info, f, indent=2)

        print(f"\nAgent info saved to: agent_info.json")
        return agent_info
    else:
        print(f"\n✗ Agent creation failed: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def main():
    print("=" * 60)
    print("Creating Mr. Jace - Retell.AI Agent")
    print("=" * 60)

    if not test_connection():
        print("\nTroubleshooting:")
        print("1. Verify API key is valid in Retell.AI dashboard")
        print("2. Check if you have sufficient API permissions")
        print("3. Ensure your account is active")
        return

    agent = create_agent()

    if agent:
        print("\n" + "=" * 60)
        print("NEXT STEPS:")
        print("=" * 60)
        print("\n1. Add Custom Functions:")
        print("   - Log into Retell.AI dashboard")
        print("   - Navigate to your agent settings")
        print("   - Add all 15 custom functions from mr-jace-deployment-guide.md")
        print("\n2. Set up n8n workflows:")
        print("   - Create 15 webhook workflows in n8n")
        print("   - Update webhook URLs in Retell.AI custom functions")
        print("\n3. Test the agent:")
        print("   - Use Retell.AI playground to test")
        print("   - Try: 'Jace, what's on my calendar tomorrow?'")
        print("\nSee mr-jace-deployment-guide.md for detailed instructions.")
        print("=" * 60)

if __name__ == "__main__":
    main()
