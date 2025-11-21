# Custom Functions to Add Manually

After importing the base agent, add these 15 custom functions one by one through the Retell AI dashboard.

**Your n8n base URL:** `https://maxstrong.app.n8n.cloud`

---

## 1. get_calendar_events

**Name:** `get_calendar_events`

**Description:**
```
Retrieve calendar events for Miss Casey within a specified date range. Use this to check availability or review scheduled appointments.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-get-calendar-events`

**Speak During Execution:** ✅ Yes
**Message:** `Let me check Miss Casey's calendar.`

**Parameters:**
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

## 2. create_calendar_event

**Name:** `create_calendar_event`

**Description:**
```
Create a new calendar event for Miss Casey. Always ask for location. Default meeting length is 1 hour unless specified otherwise.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-create-calendar-event`

**Speak During Execution:** ✅ Yes
**Message:** `Creating that appointment for Miss Casey.`

**Parameters:**
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

## 3. update_calendar_event

**Name:** `update_calendar_event`

**Description:**
```
Update an existing calendar event. Can modify time, location, attendees, or other details.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-update-calendar-event`

**Speak During Execution:** ✅ Yes
**Message:** `Updating that appointment now.`

**Parameters:**
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

## 4. get_mini_emails

**Name:** `get_mini_emails`

**Description:**
```
Retrieve a condensed list of recent emails from Miss Casey's inbox. Returns sender, subject, and timestamp.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-get-mini-emails`

**Speak During Execution:** ✅ Yes
**Message:** `Retrieving Miss Casey's recent emails.`

**Parameters:**
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

## 5. read_email

**Name:** `read_email`

**Description:**
```
Retrieve the full content of a specific email by message ID.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-read-email`

**Speak During Execution:** ✅ Yes
**Message:** `Let me pull up that email.`

**Parameters:**
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

## 6. draft_email

**Name:** `draft_email`

**Description:**
```
Create a draft email in Miss Casey's Gmail account. Does not send - saves as draft.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-draft-email`

**Speak During Execution:** ✅ Yes
**Message:** `Drafting that email now.`

**Parameters:**
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

## 7. send_email

**Name:** `send_email`

**Description:**
```
Compose and send an email immediately from Miss Casey's Gmail account.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-send-email`

**Speak During Execution:** ✅ Yes
**Message:** `Sending that email for Miss Casey.`

**Parameters:**
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

## 8. triage_emails

**Name:** `triage_emails`

**Description:**
```
Scan Miss Casey's inbox and categorize emails into Hot, Warm, Cold, and Bills. VIP senders (Kel and Max) are always Hot priority. Bills are identified and organized by due date.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-triage-emails`

**Speak During Execution:** ✅ Yes
**Message:** `Beginning email triage now. Prioritizing messages from Kel and Max, and organizing all bills by due date.`

**Parameters:**
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

## 9. get_contacts

**Name:** `get_contacts`

**Description:**
```
Retrieve contacts from Miss Casey's Google Contacts. Can search by name, email, or phone number.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-get-contacts`

**Speak During Execution:** ✅ Yes
**Message:** `Looking up that contact.`

**Parameters:**
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

## 10. create_contact

**Name:** `create_contact`

**Description:**
```
Create a new contact in Miss Casey's Google Contacts.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-create-contact`

**Speak During Execution:** ✅ Yes
**Message:** `Creating that contact.`

**Parameters:**
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

## 11. update_contact

**Name:** `update_contact`

**Description:**
```
Update an existing contact in Miss Casey's Google Contacts.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-update-contact`

**Speak During Execution:** ✅ Yes
**Message:** `Updating that contact now.`

**Parameters:**
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

## 12. create_task

**Name:** `create_task`

**Description:**
```
Create a new task in Miss Casey's Google Tasks. Use this when she asks to add something to her task list or to-do list.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-create-task`

**Speak During Execution:** ✅ Yes
**Message:** `Creating that task for you now.`

**Parameters:**
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

## 13. get_tasks

**Name:** `get_tasks`

**Description:**
```
Retrieve Miss Casey's tasks from Google Tasks. Use this when she asks what's on her to-do list, what tasks she has, or to check her tasks.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-get-tasks`

**Speak During Execution:** ✅ Yes
**Message:** `Let me check your tasks.`

**Parameters:**
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

## 14. update_task

**Name:** `update_task`

**Description:**
```
Update an existing task in Miss Casey's Google Tasks. Use this to mark tasks as complete, change due dates, update titles, or modify notes.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-update-task`

**Speak During Execution:** ✅ Yes
**Message:** `Updating that task.`

**Parameters:**
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

## 15. web_research

**Name:** `web_research`

**Description:**
```
Conduct web research on a specific topic and provide Miss Casey with a verbal summary. Can optionally email detailed results.
```

**URL:** `https://maxstrong.app.n8n.cloud/webhook/jace-web-research`

**Speak During Execution:** ✅ Yes
**Message:** `Researching that now.`

**Parameters:**
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

## ✅ All Done!

After adding all 15 functions, Mr. Jace will be fully functional with all capabilities connected to your n8n workflows.
