# Complete Google API Setup Guide for Mr. Jace n8n Workflows

This guide walks you through setting up ALL Google API credentials from scratch for the 15 Mr. Jace custom functions.

**Services You'll Configure:**
- ✅ Google Calendar API
- ✅ Gmail API
- ✅ Google Contacts API (People API)
- ✅ Google Tasks API

**Time Required:** 30-45 minutes

---

## Prerequisites

- [ ] Google account (Gmail) - the account Mr. Jace will manage
- [ ] Access to Google Cloud Console
- [ ] n8n account (https://maxstrong.app.n8n.cloud)

**IMPORTANT:** Use Sara Casey's Google account that Mr. Jace will manage (her calendar, emails, contacts, tasks).

---

## Part 1: Create Google Cloud Project (10 minutes)

### Step 1: Go to Google Cloud Console

1. Open your browser
2. Go to: **https://console.cloud.google.com/**
3. Sign in with Sara Casey's Google account

### Step 2: Create a New Project

1. Click the **project dropdown** at the top (next to "Google Cloud")
2. Click **"New Project"**
3. Fill in:
   - **Project name:** `Mr Jace Assistant`
   - **Organization:** Leave as "No organization" (or select if you have one)
4. Click **"Create"**
5. Wait 10-20 seconds for project creation
6. Click **"Select Project"** when it appears

**✓ Checkpoint:** You should see "Mr Jace Assistant" at the top of the page.

---

## Part 2: Enable Required APIs (5 minutes)

You need to enable 4 different Google APIs.

### Step 3: Enable Google Calendar API

1. In Google Cloud Console, click the **☰ menu** (top-left)
2. Go to: **APIs & Services** → **Library**
3. In the search box, type: `Google Calendar API`
4. Click on **"Google Calendar API"**
5. Click **"Enable"**
6. Wait for it to enable (10-15 seconds)

### Step 4: Enable Gmail API

1. Click **"< Go to Library"** (back arrow at top)
2. Search for: `Gmail API`
3. Click on **"Gmail API"**
4. Click **"Enable"**
5. Wait for it to enable

### Step 5: Enable Google People API (for Contacts)

1. Go back to API Library
2. Search for: `People API` or `Google People API`
3. Click on **"Google People API"**
4. Click **"Enable"**
5. Wait for it to enable

**Note:** Google Contacts uses the "People API" - this is correct!

### Step 6: Enable Google Tasks API

1. Go back to API Library
2. Search for: `Tasks API` or `Google Tasks API`
3. Click on **"Tasks API"**
4. Click **"Enable"**
5. Wait for it to enable

**✓ Checkpoint:** You should now have 4 APIs enabled. To verify:
- Go to **APIs & Services** → **Dashboard**
- You should see all 4 APIs listed

---

## Part 3: Configure OAuth Consent Screen (10 minutes)

Before creating credentials, you must configure the OAuth consent screen.

### Step 7: Set Up OAuth Consent Screen

1. In the ☰ menu, go to: **APIs & Services** → **OAuth consent screen**
2. Select **User type:**
   - Choose **"External"** (unless you have Google Workspace)
   - Click **"Create"**

### Step 8: Fill Out App Information

**Page 1: OAuth consent screen**

1. **App name:** `Mr Jace Assistant`
2. **User support email:** Select Sara Casey's email from dropdown
3. **App logo:** (Optional - skip for now)
4. **App domain:** Leave blank for now
5. **Authorized domains:** Leave blank
6. **Developer contact information:** Enter Sara Casey's email
7. Click **"Save and Continue"**

**Page 2: Scopes**

1. Click **"Add or Remove Scopes"**
2. In the filter box, search and add these scopes one by one:

   **For Gmail:**
   - `https://www.googleapis.com/auth/gmail.readonly`
   - `https://www.googleapis.com/auth/gmail.send`
   - `https://www.googleapis.com/auth/gmail.compose`
   - `https://www.googleapis.com/auth/gmail.modify`

   **For Calendar:**
   - `https://www.googleapis.com/auth/calendar`
   - `https://www.googleapis.com/auth/calendar.events`

   **For Contacts (People API):**
   - `https://www.googleapis.com/auth/contacts`

   **For Tasks:**
   - `https://www.googleapis.com/auth/tasks`

3. Click **"Update"** at the bottom
4. Click **"Save and Continue"**

**Page 3: Test users**

1. Click **"Add Users"**
2. Add Sara Casey's Gmail address
3. Click **"Add"**
4. Click **"Save and Continue"**

**Page 4: Summary**

1. Review everything
2. Click **"Back to Dashboard"**

**✓ Checkpoint:** OAuth consent screen is now configured!

---

## Part 4: Create OAuth 2.0 Credentials (5 minutes)

### Step 9: Create OAuth Client ID

1. Go to: **APIs & Services** → **Credentials**
2. Click **"+ Create Credentials"** at the top
3. Select **"OAuth client ID"**

### Step 10: Configure OAuth Client

1. **Application type:** Select **"Web application"**
2. **Name:** `Mr Jace n8n Integration`
3. **Authorized JavaScript origins:**
   - Click **"+ Add URI"**
   - Enter: `https://maxstrong.app.n8n.cloud`

4. **Authorized redirect URIs:**
   - Click **"+ Add URI"**
   - Enter: `https://maxstrong.app.n8n.cloud/rest/oauth2-credential/callback`

5. Click **"Create"**

### Step 11: Save Your Credentials

A popup will appear with your credentials:

1. **Copy and save these in a safe place:**
   - **Client ID:** (starts with something like `123456789-abc...apps.googleusercontent.com`)
   - **Client Secret:** (looks like `GOCSPX-abc123...`)

2. Click **"Download JSON"** (optional - for backup)
3. Click **"OK"**

**⚠️ IMPORTANT:** Keep these credentials private and secure!

**✓ Checkpoint:** You now have OAuth Client ID and Secret!

---

## Part 5: Connect Google APIs to n8n (10 minutes)

Now you'll add these credentials to n8n for each Google service.

### Step 12: Log into n8n

1. Go to: **https://maxstrong.app.n8n.cloud**
2. Log in to your n8n account

### Step 13: Add Google Calendar Credentials

1. Click your **profile icon** (top-right)
2. Go to: **Settings** → **Credentials**
3. Click **"+ Add Credential"**
4. Search for and select: **"Google Calendar OAuth2 API"**
5. Fill in:
   - **Credential Name:** `Sara Casey - Google Calendar`
   - **Client ID:** Paste the Client ID from Step 11
   - **Client Secret:** Paste the Client Secret from Step 11
6. Click **"Connect my account"** or **"Authorize"**
7. You'll be redirected to Google:
   - Sign in with Sara Casey's account
   - Click **"Allow"** to grant permissions
   - You'll be redirected back to n8n
8. Click **"Save"**

**✓ Success:** Google Calendar is now connected!

### Step 14: Add Gmail Credentials

1. Still in **Credentials**, click **"+ Add Credential"**
2. Search for and select: **"Gmail OAuth2 API"**
3. Fill in:
   - **Credential Name:** `Sara Casey - Gmail`
   - **Client ID:** Same Client ID from Step 11
   - **Client Secret:** Same Client Secret from Step 11
4. Click **"Connect my account"**
5. Sign in and authorize (same as Step 13)
6. Click **"Save"**

**✓ Success:** Gmail is now connected!

### Step 15: Add Google Contacts Credentials

1. Click **"+ Add Credential"**
2. Search for and select: **"Google Contacts OAuth2 API"** or **"Google People OAuth2 API"**
3. Fill in:
   - **Credential Name:** `Sara Casey - Google Contacts`
   - **Client ID:** Same Client ID
   - **Client Secret:** Same Client Secret
4. Click **"Connect my account"**
5. Sign in and authorize
6. Click **"Save"**

**✓ Success:** Google Contacts is now connected!

### Step 16: Add Google Tasks Credentials

1. Click **"+ Add Credential"**
2. Search for and select: **"Google Tasks OAuth2 API"**
3. Fill in:
   - **Credential Name:** `Sara Casey - Google Tasks`
   - **Client ID:** Same Client ID
   - **Client Secret:** Same Client Secret
4. Click **"Connect my account"**
5. Sign in and authorize
6. Click **"Save"**

**✓ Success:** Google Tasks is now connected!

---

## Part 6: Update n8n Workflows with Credentials (5 minutes)

Now you need to assign these credentials to your 15 workflows.

### Step 17: Update Calendar Workflows

1. In n8n, go to **Workflows**
2. Open workflow: **"Jace - Get Calendar Events"** (or similar name)
3. Find the **Google Calendar** node
4. Click on the node
5. In the **Credential** dropdown, select: `Sara Casey - Google Calendar`
6. Click **"Save"** (top-right)
7. Repeat for:
   - **"Jace - Create Calendar Event"**
   - **"Jace - Update Calendar Event"**

### Step 18: Update Gmail Workflows

1. Open each Gmail workflow:
   - Get Mini Emails
   - Read Email
   - Draft Email
   - Send Email
   - Triage Emails

2. For each **Gmail** node:
   - Select credential: `Sara Casey - Gmail`
   - Save the workflow

### Step 19: Update Contacts Workflows

1. Open each Contacts workflow:
   - Get Contacts
   - Create Contact
   - Update Contact

2. For each **Google Contacts** node:
   - Select credential: `Sara Casey - Google Contacts`
   - Save the workflow

### Step 20: Update Tasks Workflows

1. Open each Tasks workflow:
   - Create Task
   - Get Tasks
   - Update Task

2. For each **Google Tasks** node:
   - Select credential: `Sara Casey - Google Tasks`
   - Save the workflow

---

## Part 7: Test Everything (5 minutes)

Test each integration to make sure it works!

### Step 21: Test Google Calendar

1. Open the **"Jace - Get Calendar Events"** workflow
2. Click **"Execute Workflow"** (play button at bottom)
3. You should see calendar events returned (or empty array if no events)

**✓ If successful:** Calendar API is working!
**✗ If error:** Check credential is selected and authorized

### Step 22: Test Gmail

1. Open the **"Jace - Get Mini Emails"** workflow
2. Execute the workflow
3. You should see emails from Sara's inbox

**✓ If successful:** Gmail API is working!

### Step 23: Test Google Contacts

1. Open the **"Jace - Get Contacts"** workflow
2. Execute the workflow
3. You should see contacts list

**✓ If successful:** Contacts API is working!

### Step 24: Test Google Tasks

1. Open the **"Jace - Get Tasks"** workflow
2. Execute the workflow
3. You should see tasks (or empty if no tasks exist)

**✓ If successful:** Tasks API is working!

---

## Part 8: Activate All Workflows

### Step 25: Turn on Workflows

1. Go to your **Workflows** list in n8n
2. For each of the 15 Mr. Jace workflows:
   - Find the **Active** toggle (usually top-right of workflow)
   - Turn it **ON** (should show green)

**You should activate:**
- get-calendar-events
- create-calendar-event
- update-calendar-event
- get-mini-emails
- read-email
- draft-email
- send-email
- triage-emails
- get-contacts
- create-contact
- update-contact
- create-task
- get-tasks
- update-task
- web-research

**✓ All workflows should show as ACTIVE (green)**

---

## 🎉 You're Done!

All Google APIs are now:
- ✅ Enabled in Google Cloud
- ✅ OAuth configured
- ✅ Connected to n8n
- ✅ Assigned to workflows
- ✅ Tested and working
- ✅ Activated

---

## 🆘 Troubleshooting

### Error: "Access Not Configured"

**Solution:**
- Go back to Google Cloud Console
- Verify the API is enabled (Part 2)
- Wait 2-3 minutes for changes to propagate

### Error: "Invalid Grant" or "Redirect URI Mismatch"

**Solution:**
- Go to Google Cloud Console → Credentials
- Click on your OAuth Client ID
- Verify redirect URI is exactly: `https://maxstrong.app.n8n.cloud/rest/oauth2-credential/callback`
- Make sure there are no extra spaces or characters

### Error: "Insufficient Permissions"

**Solution:**
- Go to OAuth consent screen
- Verify all scopes are added (see Step 8)
- Re-authorize the connection in n8n

### Workflows Show "Credential Invalid"

**Solution:**
- Go to n8n Settings → Credentials
- Find the credential that's invalid
- Click **"Reconnect"** or **"Reauthorize"**
- Sign in and approve again

### Can't Find OAuth Client ID

**Solution:**
- Go to Google Cloud Console
- APIs & Services → Credentials
- Your Client ID should be listed under "OAuth 2.0 Client IDs"

---

## 📋 Credentials Summary

After completing this guide, you have:

**Google Cloud Project:**
- Name: Mr Jace Assistant
- 4 APIs enabled

**OAuth Client:**
- Client ID: `123456789-...apps.googleusercontent.com`
- Client Secret: `GOCSPX-...`
- Redirect URI: `https://maxstrong.app.n8n.cloud/rest/oauth2-credential/callback`

**n8n Credentials:**
- Sara Casey - Google Calendar
- Sara Casey - Gmail
- Sara Casey - Google Contacts
- Sara Casey - Google Tasks

**All credentials use the SAME Client ID and Secret.**

---

## 🔒 Security Best Practices

1. **Never share** your Client Secret publicly
2. **Don't commit** credentials to GitHub or public repos
3. **Use OAuth consent screen** in "External" mode for testing
4. **For production:** Consider publishing your OAuth app or using internal mode with Google Workspace
5. **Regularly review** authorized apps in Sara's Google account: https://myaccount.google.com/permissions

---

## 📞 Need Help?

- **Google Cloud Issues:** https://support.google.com/cloud
- **n8n Issues:** https://community.n8n.io
- **API Documentation:**
  - Calendar: https://developers.google.com/calendar
  - Gmail: https://developers.google.com/gmail
  - People (Contacts): https://developers.google.com/people
  - Tasks: https://developers.google.com/tasks

---

**Congratulations! Mr. Jace is now fully connected to all Google services!** 🎉
