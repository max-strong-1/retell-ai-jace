# Retell.AI API Key Troubleshooting Guide

## Current Situation

All three API keys tested return **HTTP 403 Forbidden** ("Access denied"):
1. `key_c4f96188afaa930aa943e8bd890b`
2. `key_68fc68b035be1d66c4c607088702`
3. `key_c8ec9d1920211df2eea145a56386`

The authentication format is correct (verified from official docs), which means the issue is with the API keys themselves or account permissions.

## Common Causes & Solutions

### 1. API Key is Incomplete or Truncated

**Problem**: API keys are typically 40-60 characters. Your keys are ~33 characters.

**Solution**: When copying the API key from Retell.AI dashboard:
- Click the **"Copy"** button (don't manually select)
- Paste into a text editor first to verify full length
- Look for any line breaks or spaces
- The full key should be one continuous string

**To verify**: API keys usually look like:
```
key_abcdefghijklmnopqrstuvwxyz0123456789ABCDEF123
     ↑_______________40-60 characters______________↑
```

### 2. Wrong API Key Type (Webhook-Only)

**Problem**: You might be copying the **Webhook API Key** instead of a general REST API key.

**Solution**:
1. Log into https://app.retellai.com
2. Go to **Settings** → **API Keys**
3. Look for a key that is **NOT** labeled as "Webhook Key"
4. If all keys are webhook keys, create a **new general-purpose API key**

### 3. Workspace Permissions

**Problem**: You might be in a restricted workspace or have read-only access.

**Solution**:
1. Check your workspace role: Settings → Members
2. Ensure you're an **Owner** or **Admin** (not just Member)
3. Try switching workspaces if you have multiple
4. Create API key from the correct workspace

### 4. Account Not Fully Activated

**Problem**: Account might need verification or billing setup.

**Solution**:
1. Check for verification emails
2. Verify billing information: Settings → Billing
3. Ensure credit card is valid and active
4. Check for any pending actions in dashboard

### 5. API Keys Revoked or Expired

**Problem**: Keys might have been automatically revoked.

**Solution**:
1. Go to Settings → API Keys
2. Delete all existing keys
3. Create a **brand new API key**
4. Copy it immediately (shown only once)

## Step-by-Step: Create a Working API Key

### Method 1: Via Dashboard (Recommended)

1. **Navigate to API Keys**
   ```
   https://app.retellai.com → Settings → API Keys
   ```

2. **Create New Key**
   - Click **"+ New API Key"** or **"Create API Key"**
   - Name it: "Mr. Jace Setup - REST API"
   - Ensure it's **NOT** designated as webhook-only

3. **Copy the FULL Key**
   - Use the copy button (📋)
   - Paste into text editor to verify length
   - Should be 40+ characters

4. **Test Immediately**
   ```bash
   curl -X GET "https://api.retellai.com/v2/list-agents" \
     -H "Authorization: Bearer YOUR_FULL_KEY_HERE"
   ```

   ✅ **Success**: Returns JSON (even if empty array `[]`)
   ❌ **Failed**: Returns "Access denied"

### Method 2: Via Retell Support

If you continue having issues:

1. **Email Retell Support**: support@retellai.com
2. **Include**:
   - Your account email
   - Workspace name
   - Screenshot of API Keys page
   - Error message: "403 Forbidden on /v2/list-agents"
3. **Ask**: "Why are my API keys returning 403 errors?"

## Testing Your API Key

Once you have a new key, test it with this command:

```bash
# Test authentication
curl -X GET "https://api.retellai.com/v2/list-agents" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  | python3 -m json.tool

# Expected success response:
# [] or [{"agent_id": "...", ...}]

# Expected failure response:
# Access denied
```

## Alternative: Manual Setup

If API key issues persist, you can set up Mr. Jace **manually via the dashboard**:

### Option A: Use the Retell.AI Web Dashboard

1. **Create Agent Manually**:
   - Log into https://app.retellai.com
   - Click "Create Agent"
   - Follow the manual setup guide in `MANUAL_SETUP_GUIDE.md`

2. **Add Functions One-by-One**:
   - In agent settings, add Custom Functions
   - Copy function definitions from `mr-jace-deployment-guide.md`
   - Use your n8n webhook URLs

**Estimated Time**: 30-45 minutes for manual setup

### Option B: Import Configuration

Some platforms allow importing JSON configurations. Check if Retell.AI supports:
- Importing `mr-jace-retell-config.json`
- Bulk adding custom functions

## What Happens After You Get a Working Key?

Once you have a valid API key:

```bash
# Run automated setup (30 seconds)
cd /home/user/retell-ai-jace
python3 setup_with_n8n.py YOUR_WORKING_API_KEY

# This will:
# ✓ Create Mr. Jace agent
# ✓ Add all 15 custom functions
# ✓ Connect to n8n webhooks
# ✓ Configure voice, LLM, and behavior
```

## Checklist Before Contacting Support

- [ ] Tried creating a brand new API key
- [ ] Verified account has billing set up
- [ ] Checked workspace role (Owner/Admin)
- [ ] Copied full key with copy button (not manual selection)
- [ ] Tested key with curl command
- [ ] Cleared browser cache and tried again
- [ ] Tried from a different browser/device
- [ ] Verified email address is confirmed

## Contact Information

- **Retell.AI Support**: support@retellai.com
- **Documentation**: https://docs.retellai.com
- **Status Page**: Check https://status.retellai.com for outages

---

## Current Repository Status

✅ **Everything is ready except the API key**:
- Agent configuration: `mr-jace-retell-config.json`
- Automated setup script: `setup_with_n8n.py`
- All 15 n8n webhooks: Connected at `https://maxstrong.app.n8n.cloud`
- Documentation: Complete

⏳ **Waiting for**: Valid Retell.AI REST API key

---

**Once resolved, deployment will take less than 1 minute!** 🚀
