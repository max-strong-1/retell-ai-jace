# Manual Setup Guide for Mr. Jace

Since we're experiencing API authentication issues, here's a streamlined manual setup process:

## Step 1: Verify Your Retell.AI API Key

1. Log into https://app.retellai.com
2. Go to **Settings** → **API Keys**
3. Create a new API key with **Read & Write** permissions
4. Copy the key (format: `key_xxxxxxxxxxxxx`)

## Step 2: Create Agent via Dashboard

1. In Retell.AI dashboard, click **"Create Agent"**
2. Select **"Custom LLM"** (GPT-4o)

### Basic Configuration

**Agent Name:**
```
Mr. Jace - Sara Casey's Executive Assistant
```

**Voice Settings:**
- Provider: **ElevenLabs**
- Voice: **Antoni**
- Voice ID: `ErXwobaYiN019PkySvjV`
- Voice Model: `eleven_turbo_v2_5`
- Temperature: `0.7`
- Speed: `1.0`

### LLM Configuration

- Model: `gpt-4o-realtime-preview-2024-12-17`
- Temperature: `0.3`
- Max Tokens: `500`

### Response Settings

- Responsiveness: `0.8`
- Interruption Sensitivity: `0.7`
- Enable Backchannel: **Yes**
- Backchannel Words: `I see`, `Understood`, `Mm-hmm`, `Noted`, `Yes`
- Backchannel Frequency: `0.6`

### System Prompt

Copy the complete system prompt from `mr-jace-retell-config.json` line 20, or use the deployment guide Step 4.

## Step 3: Test Without Custom Functions First

Before adding the 15 custom functions, test basic functionality:
- Save the agent
- Test in Playground with simple prompts
- Verify voice and personality work correctly

## Step 4: Prepare n8n Workflows

You'll need an n8n instance to handle the 15 custom functions. Options:

### Option A: n8n Cloud
1. Sign up at https://n8n.io
2. Create a new workflow
3. Use webhook trigger nodes

### Option B: Self-Hosted n8n
```bash
# Using Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

## Step 5: Add Custom Functions Incrementally

Instead of adding all 15 at once, start with the most important:

### Priority 1 - Calendar (3 functions)
1. `get_calendar_events`
2. `create_calendar_event`
3. `update_calendar_event`

### Priority 2 - Email (5 functions)
4. `get_mini_emails`
5. `read_email`
6. `send_email`
7. `draft_email`
8. `triage_emails`

### Priority 3 - Tasks (3 functions)
9. `create_task`
10. `get_tasks`
11. `update_task`

### Priority 4 - Contacts (3 functions)
12. `get_contacts`
13. `create_contact`
14. `update_contact`

### Priority 5 - Research (1 function)
15. `web_research`

See `mr-jace-deployment-guide.md` for complete JSON schemas for each function.

## Troubleshooting API Issues

If you want to retry the automated setup:

1. **Get a fresh API key** from Retell.AI dashboard
2. **Verify permissions** - ensure "Read & Write" access
3. **Check account status** - ensure billing is active
4. **Try the API test**:

```bash
curl -X GET "https://api.retellai.com/list-agents" \
  -H "Authorization: Bearer YOUR_NEW_KEY_HERE" \
  -H "Content-Type: application/json"
```

If this returns agent data instead of "Access denied", the key is valid.

## Need Help?

- Retell.AI Documentation: https://docs.retellai.com
- Retell.AI Support: support@retellai.com
- Check the deployment guide: `mr-jace-deployment-guide.md`

---

**Quick Win:** You can create a functional agent in ~15 minutes using just Steps 1-3 above. Custom functions can be added incrementally as you build out the n8n workflows.
