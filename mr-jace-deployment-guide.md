# Mr. Jace Deployment Guide
## Complete Setup Instructions for Retell AI

---

## 📋 Prerequisites

Before you begin, ensure you have:
- [ ] Retell AI account (https://app.retellai.com)
- [ ] n8n instance running with all 15 workflows imported
- [ ] Google OAuth credentials configured (Calendar, Gmail, Contacts, Tasks)
- [ ] All webhook URLs from n8n active and accessible

---

## 🚀 Step-by-Step Deployment

### **Step 1: Create New Agent in Retell**

1. Log into Retell AI dashboard: https://app.retellai.com
2. Click **"Create Agent"** button
3. Select **"Custom LLM"** (GPT-4o)

---

### **Step 2: Configure Basic Settings**

**Agent Name:**
```
Mr. Jace - Sara Casey's Executive Assistant
```

**Voice Settings:**
- Voice Provider: **ElevenLabs**
- Voice: **Antoni** (Voice ID: `ErXwobaYiN019PkySvjV`)
- Voice Model: **eleven_turbo_v2_5**
- Voice Temperature: **0.7**
- Voice Speed: **1.0**

**Response Settings:**
- Responsiveness: **0.8** (fast but not interrupting)
- Interruption Sensitivity: **0.7** (allows Sara to interrupt naturally)
- Enable Backchannel: **Yes**
- Backchannel Words: `I see`, `Understood`, `Mm-hmm`, `Noted`, `Yes`
- Backchannel Frequency: **0.6**

**Language:**
- Primary Language: **English (US)**
- Timezone: **America/Chicago**

**Ambient Sound:**
- Sound: **Office**
- Volume: **0.3**

---

### **Step 3: Configure LLM Settings**

**Model Configuration:**
- Model: **gpt-4o-realtime-preview-2024-12-17**
- Temperature: **0.3** (consistent, professional responses)
- Max Tokens: **500** (concise responses)

**Begin Message:**
```
Good morning, Miss Casey. This is Jace. How may I assist you today?
```

---

### **Step 4: Add System Prompt**

Copy and paste this complete system prompt into the **"General Prompt"** field:

```
You are Mr. Jace, the executive assistant to Sara Casey, Vice President of Foreman AI. You are professional, educated, articulate, and efficient. You address Sara as "Miss Casey" at all times.

## YOUR ROLE
You manage Miss Casey's calendar, email, contacts, tasks, and conduct web research on her behalf. You execute tasks immediately when instructed by Miss Casey without asking for confirmation unless clarification is needed.

## GREETING & IDENTIFICATION
When answering calls:
- For Sara: "Good morning/afternoon/evening, Miss Casey. This is Jace. How may I assist you today?"
- For others (demo purposes): "Hello, my name is Jace, Miss Casey's assistant. I manage her calendar, email, contacts, tasks, and can conduct research. How may I help you today?"

For demo callers, provide a brief overview of your capabilities but do NOT execute tasks unless explicitly told to do so for demonstration purposes.

## CALENDAR MANAGEMENT
- Default meeting length: 1 hour
- Always ask for meeting location
- If video call is needed, Miss Casey will specify
- When conflicts arise, automatically suggest the next available time slot
- Timezone: America/Chicago

## EMAIL MANAGEMENT
When Miss Casey requests email triage:
1. Scan her inbox and categorize emails by priority:
   - **HOT**: Urgent deadlines, VIPs (kel@foreman.ai, kel@4manai.io, maxstrongperformance@gmail.com), contains keywords: "urgent", "asap", "immediate", "critical"
   - **WARM**: Requires response but not time-sensitive
   - **COLD**: FYI, newsletters, promotions, updates
   - **BILLS**: Identified by keywords ("invoice", "bill", "payment due", "statement") AND sender patterns (utility companies, banks, services)

2. For bills: Extract due dates from email body automatically and organize chronologically (most urgent due date first)

3. Apply Gmail labels: "Hot", "Warm", "Cold", "Bills"

When drafting or sending emails, use this signature:
Sara Casey
VP Foreman AI

## CONTACTS
- Create, update, or retrieve contacts immediately when instructed
- No confirmation needed - execute on command

## TASK MANAGEMENT
- Create tasks when Miss Casey says "add to my to-do list" or "create a task"
- Retrieve tasks when she asks "what's on my to-do list" or "what tasks do I have"
- Update tasks to mark complete or modify details
- Default task list is the primary list unless specified otherwise

## WEB RESEARCH
- Summarize findings verbally during the call
- If Miss Casey requests an email with results, send a formatted summary after the call

## EXECUTION PHILOSOPHY
- Execute immediately when Miss Casey gives a directive
- Only ask for clarification if information is missing or ambiguous
- Be proactive: suggest next steps when appropriate
- Maintain professional composure at all times
- Work 24/7 - no time-based restrictions
```

---

### **Step 5: Add All 15 Custom Functions**

Click **"Add Tool"** → **"Custom Function"** for each function below:

#### **1. Get Calendar Events**

**Function Name:** `get_calendar_events`

**Description:**
```
Retrieve calendar events for Miss Casey within a specified date range. Use this to check availability or review scheduled appointments.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-get-calendar-events`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Let me check Miss Casey's calendar.`

**Parameters (JSON Schema):**
```json
{
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
}
```

---

#### **2. Create Calendar Event**

**Function Name:** `create_calendar_event`

**Description:**
```
Create a new calendar event for Miss Casey. Always ask for location. Default meeting length is 1 hour unless specified otherwise.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-create-calendar-event`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Creating that appointment for Miss Casey.`

**Parameters (JSON Schema):**
```json
{
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
      "items": {
        "type": "string"
      },
      "description": "List of attendee email addresses"
    }
  },
  "required": ["summary", "location", "start_time"]
}
```

---

#### **3. Update Calendar Event**

**Function Name:** `update_calendar_event`

**Description:**
```
Update an existing calendar event. Can modify time, location, attendees, or other details.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-update-calendar-event`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Updating that appointment now.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "event_id": {
      "type": "string",
      "description": "The calendar event ID to update"
    },
    "summary": {
      "type": "string",
      "description": "New meeting title"
    },
    "location": {
      "type": "string",
      "description": "New meeting location"
    },
    "start_time": {
      "type": "string",
      "description": "New start time in ISO 8601 format"
    },
    "end_time": {
      "type": "string",
      "description": "New end time in ISO 8601 format"
    },
    "attendees": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Updated list of attendee email addresses"
    }
  },
  "required": ["event_id"]
}
```

---

#### **4. Get Mini Emails**

**Function Name:** `get_mini_emails`

**Description:**
```
Retrieve a condensed list of recent emails from Miss Casey's inbox. Returns sender, subject, and timestamp.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-get-mini-emails`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Retrieving Miss Casey's recent emails.`

**Parameters (JSON Schema):**
```json
{
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
}
```

---

#### **5. Read Email**

**Function Name:** `read_email`

**Description:**
```
Retrieve the full content of a specific email by message ID.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-read-email`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Let me pull up that email.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "message_id": {
      "type": "string",
      "description": "The Gmail message ID to retrieve"
    }
  },
  "required": ["message_id"]
}
```

---

#### **6. Draft Email**

**Function Name:** `draft_email`

**Description:**
```
Create a draft email in Miss Casey's Gmail account. Does not send - saves as draft.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-draft-email`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Drafting that email now.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "to": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Recipient email addresses"
    },
    "subject": {
      "type": "string",
      "description": "Email subject line"
    },
    "body": {
      "type": "string",
      "description": "Email body content. Automatically includes Sara Casey's signature."
    },
    "cc": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "CC recipients"
    },
    "bcc": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "BCC recipients"
    }
  },
  "required": ["to", "subject", "body"]
}
```

---

#### **7. Send Email**

**Function Name:** `send_email`

**Description:**
```
Compose and send an email immediately from Miss Casey's Gmail account.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-send-email`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Sending that email for Miss Casey.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "to": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Recipient email addresses"
    },
    "subject": {
      "type": "string",
      "description": "Email subject line"
    },
    "body": {
      "type": "string",
      "description": "Email body content. Automatically includes Sara Casey's signature."
    },
    "cc": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "CC recipients"
    },
    "bcc": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "BCC recipients"
    }
  },
  "required": ["to", "subject", "body"]
}
```

---

#### **8. Triage Emails**

**Function Name:** `triage_emails`

**Description:**
```
Scan Miss Casey's inbox and categorize emails into Hot, Warm, Cold, and Bills. VIP senders (Kel and Max) are always Hot priority. Bills are identified and organized by due date.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-triage-emails`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Beginning email triage now. Prioritizing messages from Kel and Max, and organizing all bills by due date.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "max_emails": {
      "type": "number",
      "description": "Maximum number of emails to triage. Default is 50.",
      "default": 50
    }
  },
  "required": []
}
```

---

#### **9. Get Contacts**

**Function Name:** `get_contacts`

**Description:**
```
Retrieve contacts from Miss Casey's Google Contacts. Can search by name, email, or phone number.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-get-contacts`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Looking up that contact.`

**Parameters (JSON Schema):**
```json
{
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
}
```

---

#### **10. Create Contact**

**Function Name:** `create_contact`

**Description:**
```
Create a new contact in Miss Casey's Google Contacts.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-create-contact`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Creating that contact.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "first_name": {
      "type": "string",
      "description": "Contact's first name"
    },
    "last_name": {
      "type": "string",
      "description": "Contact's last name"
    },
    "email": {
      "type": "string",
      "description": "Contact's email address"
    },
    "phone": {
      "type": "string",
      "description": "Contact's phone number"
    },
    "company": {
      "type": "string",
      "description": "Contact's company name"
    },
    "title": {
      "type": "string",
      "description": "Contact's job title"
    },
    "notes": {
      "type": "string",
      "description": "Additional notes about the contact"
    }
  },
  "required": ["first_name"]
}
```

---

#### **11. Update Contact**

**Function Name:** `update_contact`

**Description:**
```
Update an existing contact in Miss Casey's Google Contacts.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-update-contact`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Updating that contact now.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "contact_id": {
      "type": "string",
      "description": "Google Contacts resource name/ID to update"
    },
    "first_name": {
      "type": "string",
      "description": "Updated first name"
    },
    "last_name": {
      "type": "string",
      "description": "Updated last name"
    },
    "email": {
      "type": "string",
      "description": "Updated email address"
    },
    "phone": {
      "type": "string",
      "description": "Updated phone number"
    },
    "company": {
      "type": "string",
      "description": "Updated company name"
    },
    "title": {
      "type": "string",
      "description": "Updated job title"
    }
  },
  "required": ["contact_id"]
}
```

---

#### **12. Create Task**

**Function Name:** `create_task`

**Description:**
```
Create a new task in Miss Casey's Google Tasks. Use this when she asks to add something to her task list or to-do list.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-create-task`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Creating that task for you now.`

**Parameters (JSON Schema):**
```json
{
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
}
```

---

#### **13. Get Tasks**

**Function Name:** `get_tasks`

**Description:**
```
Retrieve Miss Casey's tasks from Google Tasks. Use this when she asks what's on her to-do list, what tasks she has, or to check her tasks.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-get-tasks`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Let me check your tasks.`

**Parameters (JSON Schema):**
```json
{
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
      "default": false
    },
    "due_max": {
      "type": "string",
      "description": "Only return tasks due before this date (ISO 8601 format). Example: '2025-01-31T00:00:00Z'"
    },
    "due_min": {
      "type": "string",
      "description": "Only return tasks due after this date (ISO 8601 format). Example: '2025-01-01T00:00:00Z'"
    }
  },
  "required": []
}
```

---

#### **14. Update Task**

**Function Name:** `update_task`

**Description:**
```
Update an existing task in Miss Casey's Google Tasks. Use this to mark tasks as complete, change due dates, update titles, or modify notes.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-update-task`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Updating that task.`

**Parameters (JSON Schema):**
```json
{
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
    "title": {
      "type": "string",
      "description": "New task title"
    },
    "notes": {
      "type": "string",
      "description": "New task notes or details"
    },
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
}
```

---

#### **15. Web Research**

**Function Name:** `web_research`

**Description:**
```
Conduct web research on a specific topic and provide Miss Casey with a verbal summary. Can optionally email detailed results.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-web-research`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Researching that now.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "The research query or topic to investigate"
    },
    "email_results": {
      "type": "boolean",
      "description": "Whether to email detailed results to Miss Casey after the call",
      "default": false
    }
  },
  "required": ["query"]
}
```

---

### **Step 6: Configure Advanced Settings**

**Pronunciation Dictionary:**
Add these custom pronunciations:
- Word: `Foreman` → Pronunciation: `FOR-man` (IPA)
- Word: `Jace` → Pronunciation: `JAYSS` (IPA)

**Normalize for Speech:** ✅ Enabled

**Boosted Keywords:**
Add these keywords for better recognition:
- Foreman AI
- Sara Casey
- calendar
- email
- task
- appointment
- meeting
- Kel
- Max

**Post-Call Analysis:**
Enable and add these categories:
- meeting_scheduled
- task_created
- email_sent
- calendar_checked
- email_triaged

---

### **Step 7: Save and Test**

1. Click **"Save Agent"**
2. Copy the Agent ID (looks like: `agent_xxxxxxxxxx`)
3. Test in **Playground**:
   - "Jace, what's on my calendar tomorrow?"
   - "Create a task: Review budget proposal"
   - "Check my recent emails"

---

### **Step 8: Connect Phone Number (Optional)**

1. Go to **Phone Numbers** section
2. Click **"Buy Number"** or import from Twilio
3. Assign number to Mr. Jace agent
4. Test live call

---

## ✅ Verification Checklist

- [ ] Agent created with correct name
- [ ] Voice set to Antoni (ElevenLabs)
- [ ] System prompt added completely
- [ ] All 15 custom functions added with correct webhook URLs
- [ ] n8n webhooks are active and responding
- [ ] Test call in Playground successful
- [ ] Calendar function tested
- [ ] Email function tested
- [ ] Task function tested
- [ ] Phone number connected (if needed)

---

## 🆘 Troubleshooting

**If functions aren't being called:**
- Check webhook URLs are correct and accessible
- Verify n8n workflows are active (green checkmark)
- Test each webhook individually with Postman/curl
- Check function descriptions are clear about when to use them

**If voice sounds wrong:**
- Verify Voice ID is `ErXwobaYiN019PkySvjV`
- Check voice model is `eleven_turbo_v2_5`
- Adjust voice temperature if needed (0.5-1.0 range)

**If responses are too slow:**
- Increase responsiveness (try 0.9)
- Reduce max_tokens to 300
- Check n8n workflow execution times

**If Mr. Jace asks for confirmation too much:**
- Review system prompt - emphasize "execute immediately"
- Reduce temperature to 0.2 for more consistent behavior

---

## 📞 Support

If you encounter issues:
1. Check n8n execution logs for errors
2. Review Retell AI call logs in dashboard
3. Test individual functions in Retell Playground
4. Verify all Google OAuth credentials are active

---

## 🎉 You're Done!

Mr. Jace is now ready to serve as Sara Casey's executive assistant!

**Test Commands:**
- "Jace, what's on my calendar today?"
- "Add a task to call Kel about the summit"
- "Triage my inbox"
- "Schedule a meeting with John Smith tomorrow at 2pm"
- "What tasks do I have this week?"
