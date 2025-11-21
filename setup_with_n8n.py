#!/usr/bin/env python3
"""
Complete setup script for Mr. Jace with n8n integration
This script creates the Retell.AI agent and adds all 15 custom functions
with real webhook URLs from your n8n instance.
"""
import json
import subprocess

# Configuration
API_KEY = "YOUR_RETELL_API_KEY_HERE"  # Replace with your actual API key
N8N_BASE_URL = "https://maxstrong.app.n8n.cloud"

# Load Retell agent configuration
with open('/home/user/retell-ai-jace/mr-jace-retell-config.json', 'r') as f:
    config = json.load(f)

# Define all 15 custom functions with n8n webhook URLs
CUSTOM_FUNCTIONS = [
    {
        "name": "get_calendar_events",
        "description": "Retrieve calendar events for Miss Casey within a specified date range. Use this to check availability or review scheduled appointments.",
        "url": f"{N8N_BASE_URL}/webhook/jace-get-calendar-events",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {
                    "type": "string",
                    "description": "Start date in ISO format (YYYY-MM-DD). Default to today if not specified."
                },
                "end_date": {
                    "type": "string",
                    "description": "End date in ISO format (YYYY-MM-DD). Default to 7 days from start_date if not specified."
                },
                "calendar_id": {
                    "type": "string",
                    "description": "Calendar ID. Use 'primary' for Miss Casey's main calendar.",
                    "default": "primary"
                }
            },
            "required": ["start_date"]
        },
        "speak_during_execution": True,
        "speak_message": "Let me check Miss Casey's calendar."
    },
    {
        "name": "create_calendar_event",
        "description": "Create a new calendar event for Miss Casey. Always ask for location. Default meeting length is 1 hour unless specified otherwise.",
        "url": f"{N8N_BASE_URL}/webhook/jace-create-calendar-event",
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": "Meeting title or subject"
                },
                "location": {
                    "type": "string",
                    "description": "Meeting location. ALWAYS ask if not provided."
                },
                "description": {
                    "type": "string",
                    "description": "Additional meeting details or notes"
                },
                "start_time": {
                    "type": "string",
                    "description": "Start time in ISO 8601 format (YYYY-MM-DDTHH:MM:SS-06:00 for Chicago time)"
                },
                "end_time": {
                    "type": "string",
                    "description": "End time in ISO 8601 format. Default to 1 hour after start_time if not specified."
                },
                "attendees": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of attendee email addresses"
                }
            },
            "required": ["summary", "location", "start_time"]
        },
        "speak_during_execution": True,
        "speak_message": "Creating that appointment for Miss Casey."
    },
    {
        "name": "update_calendar_event",
        "description": "Update an existing calendar event. Can modify time, location, attendees, or other details.",
        "url": f"{N8N_BASE_URL}/webhook/jace-update-calendar-event",
        "parameters": {
            "type": "object",
            "properties": {
                "event_id": {
                    "type": "string",
                    "description": "The calendar event ID to update"
                },
                "summary": {"type": "string", "description": "New meeting title"},
                "location": {"type": "string", "description": "New meeting location"},
                "start_time": {"type": "string", "description": "New start time in ISO 8601 format"},
                "end_time": {"type": "string", "description": "New end time in ISO 8601 format"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Updated list of attendee email addresses"
                }
            },
            "required": ["event_id"]
        },
        "speak_during_execution": True,
        "speak_message": "Updating that appointment now."
    },
    {
        "name": "get_mini_emails",
        "description": "Retrieve a condensed list of recent emails from Miss Casey's inbox. Returns sender, subject, and timestamp.",
        "url": f"{N8N_BASE_URL}/webhook/jace-get-mini-emails",
        "parameters": {
            "type": "object",
            "properties": {
                "max_results": {
                    "type": "number",
                    "description": "Number of emails to retrieve. Default is 10.",
                    "default": 10
                },
                "query": {
                    "type": "string",
                    "description": "Gmail search query to filter emails (e.g., 'is:unread', 'from:john@example.com')"
                }
            },
            "required": []
        },
        "speak_during_execution": True,
        "speak_message": "Retrieving Miss Casey's recent emails."
    },
    {
        "name": "read_email",
        "description": "Retrieve the full content of a specific email by message ID.",
        "url": f"{N8N_BASE_URL}/webhook/jace-read-email",
        "parameters": {
            "type": "object",
            "properties": {
                "message_id": {
                    "type": "string",
                    "description": "The Gmail message ID to retrieve"
                }
            },
            "required": ["message_id"]
        },
        "speak_during_execution": True,
        "speak_message": "Let me pull up that email."
    },
    {
        "name": "draft_email",
        "description": "Create a draft email in Miss Casey's Gmail account. Does not send - saves as draft.",
        "url": f"{N8N_BASE_URL}/webhook/jace-draft-email",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Recipient email addresses"
                },
                "subject": {"type": "string", "description": "Email subject line"},
                "body": {
                    "type": "string",
                    "description": "Email body content. Automatically includes Sara Casey's signature."
                },
                "cc": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "CC recipients"
                },
                "bcc": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "BCC recipients"
                }
            },
            "required": ["to", "subject", "body"]
        },
        "speak_during_execution": True,
        "speak_message": "Drafting that email now."
    },
    {
        "name": "send_email",
        "description": "Compose and send an email immediately from Miss Casey's Gmail account.",
        "url": f"{N8N_BASE_URL}/webhook/jace-send-email",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Recipient email addresses"
                },
                "subject": {"type": "string", "description": "Email subject line"},
                "body": {
                    "type": "string",
                    "description": "Email body content. Automatically includes Sara Casey's signature."
                },
                "cc": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "CC recipients"
                },
                "bcc": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "BCC recipients"
                }
            },
            "required": ["to", "subject", "body"]
        },
        "speak_during_execution": True,
        "speak_message": "Sending that email for Miss Casey."
    },
    {
        "name": "triage_emails",
        "description": "Scan Miss Casey's inbox and categorize emails into Hot, Warm, Cold, and Bills. VIP senders (Kel and Max) are always Hot priority. Bills are identified and organized by due date.",
        "url": f"{N8N_BASE_URL}/webhook/jace-triage-emails",
        "parameters": {
            "type": "object",
            "properties": {
                "max_emails": {
                    "type": "number",
                    "description": "Maximum number of emails to triage. Default is 50.",
                    "default": 50
                }
            },
            "required": []
        },
        "speak_during_execution": True,
        "speak_message": "Beginning email triage now. Prioritizing messages from Kel and Max, and organizing all bills by due date."
    },
    {
        "name": "get_contacts",
        "description": "Retrieve contacts from Miss Casey's Google Contacts. Can search by name, email, or phone number.",
        "url": f"{N8N_BASE_URL}/webhook/jace-get-contacts",
        "parameters": {
            "type": "object",
            "properties": {
                "search_query": {
                    "type": "string",
                    "description": "Search term (name, email, or phone number)"
                },
                "max_results": {
                    "type": "number",
                    "description": "Number of contacts to return. Default is 10.",
                    "default": 10
                }
            },
            "required": []
        },
        "speak_during_execution": True,
        "speak_message": "Looking up that contact."
    },
    {
        "name": "create_contact",
        "description": "Create a new contact in Miss Casey's Google Contacts.",
        "url": f"{N8N_BASE_URL}/webhook/jace-create-contact",
        "parameters": {
            "type": "object",
            "properties": {
                "first_name": {"type": "string", "description": "Contact's first name"},
                "last_name": {"type": "string", "description": "Contact's last name"},
                "email": {"type": "string", "description": "Contact's email address"},
                "phone": {"type": "string", "description": "Contact's phone number"},
                "company": {"type": "string", "description": "Contact's company name"},
                "title": {"type": "string", "description": "Contact's job title"},
                "notes": {"type": "string", "description": "Additional notes about the contact"}
            },
            "required": ["first_name"]
        },
        "speak_during_execution": True,
        "speak_message": "Creating that contact."
    },
    {
        "name": "update_contact",
        "description": "Update an existing contact in Miss Casey's Google Contacts.",
        "url": f"{N8N_BASE_URL}/webhook/jace-update-contact",
        "parameters": {
            "type": "object",
            "properties": {
                "contact_id": {
                    "type": "string",
                    "description": "Google Contacts resource name/ID to update"
                },
                "first_name": {"type": "string", "description": "Updated first name"},
                "last_name": {"type": "string", "description": "Updated last name"},
                "email": {"type": "string", "description": "Updated email address"},
                "phone": {"type": "string", "description": "Updated phone number"},
                "company": {"type": "string", "description": "Updated company name"},
                "title": {"type": "string", "description": "Updated job title"}
            },
            "required": ["contact_id"]
        },
        "speak_during_execution": True,
        "speak_message": "Updating that contact now."
    },
    {
        "name": "create_task",
        "description": "Create a new task in Miss Casey's Google Tasks. Use this when she asks to add something to her task list or to-do list.",
        "url": f"{N8N_BASE_URL}/webhook/jace-create-task",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The task title or description"
                },
                "notes": {
                    "type": "string",
                    "description": "Additional details or notes about the task"
                },
                "due_date": {
                    "type": "string",
                    "description": "Due date in ISO 8601 format (YYYY-MM-DD). Only include if Miss Casey specifies a due date."
                },
                "task_list": {
                    "type": "string",
                    "description": "Task list ID. Use '@default' for the main task list unless Miss Casey specifies otherwise.",
                    "default": "@default"
                }
            },
            "required": ["title"]
        },
        "speak_during_execution": True,
        "speak_message": "Creating that task for you now."
    },
    {
        "name": "get_tasks",
        "description": "Retrieve Miss Casey's tasks from Google Tasks. Use this when she asks what's on her to-do list, what tasks she has, or to check her tasks.",
        "url": f"{N8N_BASE_URL}/webhook/jace-get-tasks",
        "parameters": {
            "type": "object",
            "properties": {
                "max_results": {
                    "type": "number",
                    "description": "Maximum number of tasks to retrieve. Default is 20.",
                    "default": 20
                },
                "task_list": {
                    "type": "string",
                    "description": "Task list ID. Use '@default' for the main task list.",
                    "default": "@default"
                },
                "show_completed": {
                    "type": "boolean",
                    "description": "Include completed tasks in results. Default is false.",
                    "default": False
                },
                "due_max": {
                    "type": "string",
                    "description": "Only return tasks due before this date (ISO 8601 format)"
                },
                "due_min": {
                    "type": "string",
                    "description": "Only return tasks due after this date (ISO 8601 format)"
                }
            },
            "required": []
        },
        "speak_during_execution": True,
        "speak_message": "Let me check your tasks."
    },
    {
        "name": "update_task",
        "description": "Update an existing task in Miss Casey's Google Tasks. Use this to mark tasks as complete, change due dates, update titles, or modify notes.",
        "url": f"{N8N_BASE_URL}/webhook/jace-update-task",
        "parameters": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "string",
                    "description": "The ID of the task to update. Get this from the get_tasks function first."
                },
                "task_list": {
                    "type": "string",
                    "description": "Task list ID. Use '@default' for the main task list.",
                    "default": "@default"
                },
                "title": {"type": "string", "description": "New task title"},
                "notes": {"type": "string", "description": "New task notes or details"},
                "due_date": {
                    "type": "string",
                    "description": "New due date in ISO 8601 format (YYYY-MM-DD)"
                },
                "status": {
                    "type": "string",
                    "description": "Task status. Use 'completed' to mark as done, or 'needsAction' to mark as incomplete.",
                    "enum": ["needsAction", "completed"]
                }
            },
            "required": ["task_id"]
        },
        "speak_during_execution": True,
        "speak_message": "Updating that task."
    },
    {
        "name": "web_research",
        "description": "Conduct web research on a specific topic and provide Miss Casey with a verbal summary. Can optionally email detailed results.",
        "url": f"{N8N_BASE_URL}/webhook/jace-web-research",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The research query or topic to investigate"
                },
                "email_results": {
                    "type": "boolean",
                    "description": "Whether to email detailed results to Miss Casey after the call",
                    "default": False
                }
            },
            "required": ["query"]
        },
        "speak_during_execution": True,
        "speak_message": "Researching that now."
    }
]

def create_agent_with_curl():
    """Create agent using curl command"""
    print("=" * 80)
    print("CREATING MR. JACE AGENT")
    print("=" * 80)

    # Prepare agent payload
    agent_payload = {
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
        "enable_transcription_formatting": config["enable_transcription_formatting"],
        "opt_out_sensitive_data_storage": config["opt_out_sensitive_data_storage"],
        "pronunciation_dictionary": config["pronunciation_dictionary"],
        "normalize_for_speech": config["normalize_for_speech"],
        "boosted_keywords": config["boosted_keywords"],
        "reminder_trigger_ms": config["reminder_trigger_ms"],
        "reminder_max_count": config["reminder_max_count"]
    }

    # Save payload to temp file
    with open('/tmp/agent_payload.json', 'w') as f:
        json.dump(agent_payload, f, indent=2)

    # Create agent with curl
    print("\n1. Creating base agent...")
    result = subprocess.run([
        'curl', '-X', 'POST',
        'https://api.retellai.com/create-agent',
        '-H', f'Authorization: Bearer {API_KEY}',
        '-H', 'Content-Type: application/json',
        '-d', f'@/tmp/agent_payload.json'
    ], capture_output=True, text=True)

    if result.returncode != 0 or 'error' in result.stdout.lower() or 'denied' in result.stdout.lower():
        print(f"\n✗ Agent creation failed!")
        print(f"Response: {result.stdout}")
        print(f"\nPlease check:")
        print(f"1. API key is correct: {API_KEY[:20]}...")
        print(f"2. API key has 'Read & Write' permissions")
        print(f"3. Account is active and in good standing")
        return None

    try:
        agent_data = json.loads(result.stdout)
        agent_id = agent_data.get('agent_id')

        if not agent_id:
            print(f"\n✗ No agent ID in response: {result.stdout}")
            return None

        print(f"✓ Base agent created successfully!")
        print(f"  Agent ID: {agent_id}")

        # Save agent info
        with open('/home/user/retell-ai-jace/agent_info.json', 'w') as f:
            json.dump(agent_data, f, indent=2)

        return agent_id

    except json.JSONDecodeError:
        print(f"\n✗ Invalid JSON response: {result.stdout}")
        return None

def add_custom_functions(agent_id):
    """Add all 15 custom functions to the agent"""
    print(f"\n2. Adding all 15 custom functions...")

    for idx, func in enumerate(CUSTOM_FUNCTIONS, 1):
        print(f"\n   [{idx}/15] Adding {func['name']}...")

        function_payload = {
            "agent_id": agent_id,
            "function_name": func["name"],
            "description": func["description"],
            "url": func["url"],
            "parameters": func["parameters"],
            "speak_during_execution": func.get("speak_during_execution", True),
            "speak_during_execution_message": func.get("speak_message", "")
        }

        # Save to temp file
        with open('/tmp/function_payload.json', 'w') as f:
            json.dump(function_payload, f, indent=2)

        # Add function with curl
        result = subprocess.run([
            'curl', '-X', 'POST',
            f'https://api.retellai.com/agent/{agent_id}/add-function',
            '-H', f'Authorization: Bearer {API_KEY}',
            '-H', 'Content-Type: application/json',
            '-d', '@/tmp/function_payload.json'
        ], capture_output=True, text=True)

        if result.returncode == 0 and 'error' not in result.stdout.lower():
            print(f"       ✓ {func['name']} added")
        else:
            print(f"       ✗ Failed: {result.stdout[:100]}")

    print(f"\n✓ All custom functions configured!")

def main():
    if API_KEY == "YOUR_RETELL_API_KEY_HERE":
        print("\n" + "=" * 80)
        print("ERROR: Please set your Retell.AI API key")
        print("=" * 80)
        print("\nInstructions:")
        print("1. Log into https://app.retellai.com")
        print("2. Go to Settings → API Keys")
        print("3. Create a new key with 'Read & Write' permissions")
        print("4. Edit this file and replace 'YOUR_RETELL_API_KEY_HERE' with your key")
        print("5. Run this script again")
        print("\nOr run: python3 setup_with_n8n.py YOUR_API_KEY_HERE")
        return

    agent_id = create_agent_with_curl()

    if not agent_id:
        return

    add_custom_functions(agent_id)

    print("\n" + "=" * 80)
    print("✓ MR. JACE SETUP COMPLETE!")
    print("=" * 80)
    print(f"\nAgent ID: {agent_id}")
    print(f"n8n Workflows: {N8N_BASE_URL}")
    print(f"\nNext steps:")
    print(f"1. Test in Retell.AI Playground: https://app.retellai.com")
    print(f"2. Try: 'Jace, what's on my calendar tomorrow?'")
    print(f"3. Ensure all n8n workflows are active and Google OAuth is configured")
    print("=" * 80)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        API_KEY = sys.argv[1]
    main()
