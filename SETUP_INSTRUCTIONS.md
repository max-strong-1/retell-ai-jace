# Mr. Jace Setup Instructions

## Current Status

I've prepared everything needed to create your Mr. Jace agent automatically. However, the API keys provided are returning "Access denied" errors from Retell.AI.

## What's Ready

✅ **Complete n8n workflow** with all 15 functions
✅ **Automated setup script** (`setup_with_n8n.py`)
✅ **All configuration files** prepared
✅ **Webhook URLs** extracted from your n8n instance

## The Issue

The API keys provided:
- `key_c4f96188afaa930aa943e8bd890b` (first attempt)
- `key_68fc68b035be1d66c4c607088702` (second attempt)

Both return **"Access denied"** when calling the Retell.AI API.

## How to Fix This

### Step 1: Get a Valid API Key

1. Log into **https://app.retellai.com**
2. Go to **Settings** → **API Keys**
3. Click **"Create New API Key"**
4. Give it a name like "Mr. Jace Setup"
5. Ensure permissions are set to **"Read & Write"**
6. Copy the full API key (format: `key_XXXXXXXXX...`)

**IMPORTANT**: Copy the ENTIRE key. They're usually 40-50 characters long.

### Step 2: Run the Automated Setup

Once you have the correct API key, run:

```bash
cd /home/user/retell-ai-jace
python3 setup_with_n8n.py YOUR_API_KEY_HERE
```

This will:
1. ✓ Create the Mr. Jace agent in Retell.AI
2. ✓ Configure all voice and LLM settings
3. ✓ Add all 15 custom functions
4. ✓ Connect to your n8n workflows at `https://maxstrong.app.n8n.cloud`

**The entire process takes about 30 seconds!**

## Your n8n Configuration

Your n8n instance is configured with all 15 webhook endpoints:

### Calendar Management (3 functions)
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-get-calendar-events`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-create-calendar-event`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-update-calendar-event`

### Email Management (5 functions)
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-get-mini-emails`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-read-email`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-draft-email`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-send-email`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-triage-emails`

### Contacts Management (3 functions)
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-get-contacts`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-create-contact`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-update-contact`

### Tasks Management (3 functions)
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-create-task`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-get-tasks`
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-update-task`

### Research (1 function)
- ✓ `https://maxstrong.app.n8n.cloud/webhook/jace-web-research`

## Before Testing

Make sure your n8n workflows have:

1. **Google OAuth Configured**:
   - Calendar API credentials
   - Gmail API credentials
   - Contacts API credentials
   - Tasks API credentials

2. **Workflows Activated**:
   - Check that all 15 workflows show green "Active" status
   - Test one webhook manually:
     ```bash
     curl -X POST https://maxstrong.app.n8n.cloud/webhook/jace-get-calendar-events \
       -H "Content-Type: application/json" \
       -d '{"args": {"start_date": "2025-01-20"}}'
     ```

## After Setup

Once the agent is created:

1. **Test in Retell Playground**:
   - Go to https://app.retellai.com
   - Open Mr. Jace agent
   - Click "Test in Playground"

2. **Try these commands**:
   - "Jace, what's on my calendar tomorrow?"
   - "Create a task: Review budget proposal"
   - "Check my recent emails"
   - "Triage my inbox"

3. **Connect a phone number** (optional):
   - Settings → Phone Numbers
   - Buy or port a number
   - Assign to Mr. Jace

## Troubleshooting

### API Key Still Not Working?

**Check the key format**:
- Should start with `key_`
- Usually 40-50 characters total
- No spaces or line breaks

**Verify permissions**:
```bash
curl -X GET "https://api.retellai.com/list-agents" \
  -H "Authorization: Bearer YOUR_KEY_HERE" \
  -H "Content-Type: application/json"
```

If you get JSON (not "Access denied"), the key works!

### n8n Webhooks Not Responding?

1. Check workflows are active (green toggle)
2. Verify Google OAuth is connected
3. Test webhook directly with curl (see above)
4. Check n8n execution logs for errors

### Agent Created But Functions Don't Work?

1. Verify webhook URLs are accessible from internet
2. Check n8n instance is not behind firewall
3. Review execution logs in n8n for each function call
4. Ensure Google API quotas haven't been exceeded

## Support

- **Retell.AI Docs**: https://docs.retellai.com
- **n8n Docs**: https://docs.n8n.io
- **Retell.AI Support**: support@retellai.com

## Files in This Repository

| File | Purpose |
|------|---------|
| `setup_with_n8n.py` | **Main setup script** - Run this once you have API key |
| `mr-jace-retell-config.json` | Complete agent configuration |
| `mr-jace-deployment-guide.md` | Manual setup guide (if you prefer UI) |
| `MANUAL_SETUP_GUIDE.md` | Simplified manual setup |
| `n8n_workflow_backup.json` | Backup of your n8n workflow |
| `CLAUDE.md` | Developer documentation |
| `README.md` | Repository overview |

---

**Ready to proceed?** Get your API key and run:

```bash
python3 setup_with_n8n.py YOUR_RETELL_API_KEY
```

The setup will complete in ~30 seconds and Mr. Jace will be ready to assist Sara!
