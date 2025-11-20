# CLAUDE.md - AI Assistant Guide

## Repository Overview

This repository contains the complete configuration and deployment documentation for **Mr. Jace**, an AI-powered executive assistant voice agent built on the Retell AI platform. Mr. Jace serves as the executive assistant to Sara Casey, VP of Foreman AI, managing calendar scheduling, email triage, task management, contact management, and web research through natural voice interactions.

**Technology Stack:**
- **Retell AI**: Voice agent platform with GPT-4o realtime model
- **ElevenLabs**: Text-to-speech (Antoni voice)
- **n8n**: Workflow automation backend (15 webhook-based workflows)
- **Google Workspace**: Calendar, Gmail, Contacts, Tasks integration

---

## Repository Structure

```
retell-ai-jace/
├── README.md                       # Repository overview and quick start
├── mr-jace-retell-config.json      # Complete Retell AI agent configuration
├── mr-jace-deployment-guide.md     # Step-by-step deployment instructions
└── CLAUDE.md                       # This file - AI assistant guide
```

### File Descriptions

#### `mr-jace-retell-config.json`
Complete Retell AI agent configuration file containing:
- Agent name and identification
- Voice settings (ElevenLabs Antoni voice)
- LLM configuration (GPT-4o realtime, temperature, tokens)
- System prompt defining agent personality and behavior
- Response settings (responsiveness, interruption sensitivity, backchannel)
- Pronunciation dictionary
- Boosted keywords for speech recognition
- Post-call analysis categories

**Key Configuration Values:**
- Voice: Antoni (ID: `ErXwobaYiN019PkySvjV`)
- Model: `gpt-4o-realtime-preview-2024-12-17`
- Temperature: `0.3` (professional, consistent responses)
- Timezone: `America/Chicago`
- Max tokens: `500` (concise responses)

#### `mr-jace-deployment-guide.md`
Comprehensive deployment guide (950+ lines) including:
- Prerequisites checklist
- Step-by-step Retell AI configuration
- All 15 custom function definitions with JSON schemas
- n8n webhook URLs and configurations
- Advanced settings (pronunciation, keywords, analytics)
- Testing procedures
- Troubleshooting guide

#### `README.md`
High-level repository overview for general users.

---

## Architecture

### System Architecture

```
┌─────────────┐
│   User      │ (Voice call)
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│      Retell AI Platform         │
│  ┌───────────────────────────┐  │
│  │   GPT-4o Realtime Model   │  │
│  │   (gpt-4o-realtime-...)   │  │
│  └───────────────────────────┘  │
│  ┌───────────────────────────┐  │
│  │  ElevenLabs TTS           │  │
│  │  (Antoni Voice)           │  │
│  └───────────────────────────┘  │
└────────┬────────────────────────┘
         │ (Webhook calls)
         ▼
┌─────────────────────────────────┐
│       n8n Workflows (15)        │
│  ┌───────────────────────────┐  │
│  │ - Calendar Management (3) │  │
│  │ - Email Management (5)    │  │
│  │ - Contacts Management (3) │  │
│  │ - Tasks Management (3)    │  │
│  │ - Web Research (1)        │  │
│  └───────────────────────────┘  │
└────────┬────────────────────────┘
         │ (API calls)
         ▼
┌─────────────────────────────────┐
│     Google Workspace APIs       │
│  - Google Calendar API          │
│  - Gmail API                    │
│  - Google Contacts API          │
│  - Google Tasks API             │
└─────────────────────────────────┘
```

### Custom Functions (15 Total)

**Calendar Management:**
1. `get_calendar_events` - Retrieve calendar events for date range
2. `create_calendar_event` - Create new appointments
3. `update_calendar_event` - Modify existing appointments

**Email Management:**
4. `get_mini_emails` - Retrieve condensed inbox list
5. `read_email` - Get full email content by message ID
6. `draft_email` - Create email draft (not sent)
7. `send_email` - Compose and send email immediately
8. `triage_emails` - Categorize emails into Hot/Warm/Cold/Bills

**Contacts Management:**
9. `get_contacts` - Search and retrieve contacts
10. `create_contact` - Add new contact
11. `update_contact` - Modify existing contact

**Tasks Management:**
12. `create_task` - Add task to Google Tasks
13. `get_tasks` - Retrieve task list
14. `update_task` - Modify or complete tasks

**Research:**
15. `web_research` - Conduct web research and provide summary

---

## Agent Behavior & Personality

### Core Identity
- **Name**: Mr. Jace
- **Role**: Executive assistant to Sara Casey
- **Personality**: Professional, educated, articulate, efficient
- **Address**: Always addresses Sara as "Miss Casey"

### Greeting Protocols
- **For Sara Casey**: "Good morning/afternoon/evening, Miss Casey. This is Jace. How may I assist you today?"
- **For Demo Callers**: "Hello, my name is Jace, Miss Casey's assistant. I manage her calendar, email, contacts, tasks, and can conduct research. How may I help you today?"

### Execution Philosophy
- **Immediate execution**: No confirmation needed when Sara gives directives
- **Clarification only**: Ask only if information is missing or ambiguous
- **Proactive**: Suggest next steps when appropriate
- **24/7 availability**: No time-based restrictions

### Email Triage Logic

**Priority Categories:**
- **HOT**:
  - VIP senders: `kel@foreman.ai`, `kel@4manai.io`, `maxstrongperformance@gmail.com`
  - Keywords: "urgent", "asap", "immediate", "critical"
- **WARM**: Requires response but not time-sensitive
- **COLD**: FYI, newsletters, promotions
- **BILLS**: Keywords ("invoice", "bill", "payment due") + sender patterns

**Bill Handling**: Automatically extract due dates from email body and organize chronologically.

### Calendar Conventions
- Default meeting length: 1 hour
- Always ask for meeting location
- Auto-suggest next slot on conflicts
- Timezone: America/Chicago (CST/CDT)

### Email Signature
```
Sara Casey
VP Foreman AI
```

---

## Development Workflows

### Making Configuration Changes

1. **Edit JSON Configuration**
   - Modify `mr-jace-retell-config.json`
   - Validate JSON syntax
   - Test configuration locally if possible

2. **Update Deployment Guide**
   - Update corresponding sections in `mr-jace-deployment-guide.md`
   - Ensure consistency between JSON and documentation
   - Update verification checklist if needed

3. **Update README**
   - Update high-level overview if major changes
   - Keep README concise and user-friendly

### Common Modification Scenarios

#### Changing Voice Settings
**Files to modify:**
- `mr-jace-retell-config.json`: Update `voice_id`, `voice_model`, `voice_temperature`, `voice_speed`
- `mr-jace-deployment-guide.md`: Update Step 2 voice configuration section

#### Modifying System Prompt
**Files to modify:**
- `mr-jace-retell-config.json`: Update `general_prompt` field
- `mr-jace-deployment-guide.md`: Update Step 4 system prompt section

**Important**: Keep both files synchronized. The JSON is the source of truth for Retell AI, but the deployment guide must match for accurate documentation.

#### Adding New Custom Functions
**Files to modify:**
- `mr-jace-deployment-guide.md`: Add new function in Step 5
- Update function count (currently 15)
- Add webhook URL template
- Include JSON schema for parameters
- Add "Speak During Execution" message

**Template for new function:**
```markdown
#### **N. Function Name**

**Function Name:** `function_name`

**Description:**
```
Clear description of what this function does and when to use it.
```

**URL:** `https://your-n8n-instance.com/webhook/jace-function-name`

**HTTP Method:** POST

**Speak During Execution:** ✅ Enabled
**Message:** `Brief status message spoken to user.`

**Parameters (JSON Schema):**
```json
{
  "type": "object",
  "properties": {
    "param_name": {
      "type": "string",
      "description": "Parameter description"
    }
  },
  "required": ["param_name"]
}
```
```

#### Updating VIP Email Addresses
**Files to modify:**
- `mr-jace-retell-config.json`: Update email list in `general_prompt` under "EMAIL MANAGEMENT" section
- `mr-jace-deployment-guide.md`: Update Step 4 and Step 8 (triage_emails function)

### Version Control Best Practices

1. **Commit messages should be descriptive:**
   - ✅ "Update voice temperature from 0.7 to 0.8 for more natural responses"
   - ✅ "Add new VIP email: newvip@company.com"
   - ❌ "Update config"
   - ❌ "Changes"

2. **Always test changes before committing:**
   - Validate JSON syntax
   - Check for broken links in markdown
   - Verify documentation matches configuration

3. **Keep documentation in sync:**
   - When updating JSON, update deployment guide
   - When adding features, update README overview
   - When changing behavior, update this CLAUDE.md

---

## Key Conventions

### Naming Conventions
- **Function names**: Lowercase with underscores (e.g., `get_calendar_events`)
- **Webhook URLs**: Format `https://your-n8n-instance.com/webhook/jace-{function-name}`
- **File names**: Kebab-case (e.g., `mr-jace-deployment-guide.md`)

### JSON Schema Patterns
- Always use `"type": "object"` for root schema
- Include clear `description` fields
- Use `default` values where appropriate
- Mark truly required fields in `required` array
- Use enums for fixed value sets

### Documentation Style
- Use emoji headers (📋, 🚀, ✅) for visual hierarchy in deployment guide
- Include code blocks with syntax highlighting
- Provide examples where helpful
- Keep troubleshooting sections practical

### Configuration Standards
- **Temperature**: 0.3 for consistent, professional responses
- **Max tokens**: 500 for concise voice responses
- **Responsiveness**: 0.8 (fast but not interrupting)
- **Interruption sensitivity**: 0.7 (allows natural interruptions)

---

## Testing & Validation

### Before Deployment Testing
1. **JSON Validation**: Ensure `mr-jace-retell-config.json` is valid JSON
2. **Documentation Review**: Check all webhook URLs are placeholder templates
3. **Consistency Check**: Verify JSON config matches deployment guide

### Post-Deployment Testing
According to deployment guide Step 7, test these scenarios:
- "Jace, what's on my calendar tomorrow?"
- "Create a task: Review budget proposal"
- "Check my recent emails"

### Full Verification Checklist
See `mr-jace-deployment-guide.md` line 893-905 for complete checklist.

---

## Important Context for AI Assistants

### When Assisting with This Repository

1. **Understand the separation of concerns:**
   - `mr-jace-retell-config.json` is the Retell AI configuration (source of truth)
   - `mr-jace-deployment-guide.md` is the human-readable deployment instructions
   - Changes often need to be made in both files

2. **Webhook URLs are templates:**
   - URLs like `https://your-n8n-instance.com/webhook/...` are placeholders
   - Actual deployment requires real n8n instance URLs
   - Never commit real production webhook URLs to public repos

3. **VIP email addresses are hardcoded:**
   - Kel's emails: `kel@foreman.ai`, `kel@4manai.io`
   - Max's email: `maxstrongperformance@gmail.com`
   - These are intentionally hardcoded in the triage logic

4. **The agent has specific personality constraints:**
   - Must address Sara as "Miss Casey" (not Sara, Ms. Casey, etc.)
   - Professional but efficient (no small talk)
   - Executes immediately without confirmation
   - Works 24/7 with no time restrictions

5. **Email signature is minimal:**
   - Only 2 lines: name and title
   - No phone, address, or other contact info
   - Intentionally concise for professional emails

### Common Questions & Answers

**Q: Can I add more backchannel words?**
A: Yes, modify `backchannel_words` array in JSON config. Keep them short and natural.

**Q: How do I change the timezone?**
A: Update references to `America/Chicago` in the system prompt. Note: This is Central Time.

**Q: Can I add more post-call analysis categories?**
A: Yes, add to `post_call_analysis_data.categories` array in JSON config.

**Q: What if I want to add a 16th custom function?**
A: Add function definition to deployment guide Step 5, update count from 15 to 16, ensure n8n workflow is created.

**Q: Why is temperature set to 0.3?**
A: Low temperature (0.3) ensures consistent, professional responses. Voice agents need predictability.

---

## Security Considerations

### Sensitive Data
- **Never commit**: Real webhook URLs, API keys, OAuth tokens
- **Use placeholders**: `https://your-n8n-instance.com/...`
- **Environment variables**: Keep secrets in n8n environment config

### Google OAuth Scopes Required
- Google Calendar API (read/write)
- Gmail API (read/write/send)
- Google Contacts API (read/write)
- Google Tasks API (read/write)

### Access Control
- Agent has full access to Sara Casey's Google Workspace
- Execute-on-command behavior means no confirmation prompts
- Designed for single-user (Sara) with demo mode for others

---

## Troubleshooting Guide

### Common Issues

**Issue: Functions not being called**
- Check webhook URLs are correct and accessible
- Verify n8n workflows are active
- Test webhooks individually with curl/Postman
- Review function descriptions for clarity

**Issue: Voice sounds wrong**
- Verify Voice ID: `ErXwobaYiN019PkySvjV`
- Check voice model: `eleven_turbo_v2_5`
- Adjust voice temperature (range: 0.5-1.0)

**Issue: Responses too slow**
- Increase responsiveness to 0.9
- Reduce max_tokens to 300
- Check n8n workflow execution times

**Issue: Too many confirmation requests**
- Review system prompt execution philosophy
- Reduce LLM temperature to 0.2
- Emphasize "execute immediately" in prompt

### Debug Process
1. Check n8n execution logs for errors
2. Review Retell AI call logs in dashboard
3. Test individual functions in Retell Playground
4. Verify Google OAuth credentials are active

---

## Integration Requirements

### n8n Setup
This agent requires 15 active n8n workflows corresponding to the 15 custom functions. Each workflow must:
- Have a Webhook Trigger node (POST method)
- Implement Google API authentication
- Process the incoming JSON parameters
- Return appropriate JSON response
- Handle errors gracefully

### Google Workspace Setup
- OAuth 2.0 credentials configured
- Appropriate API scopes enabled
- Calendar, Gmail, Contacts, Tasks APIs enabled
- Service account or user OAuth depending on n8n config

### Retell AI Account
- Active Retell AI account
- GPT-4o realtime API access
- ElevenLabs integration enabled
- Phone number (optional, for inbound calls)

---

## Roadmap & Future Enhancements

Potential improvements (not yet implemented):
- Multi-calendar support (currently only "primary")
- Email templates for common responses
- Calendar conflict resolution preferences
- Task prioritization and smart scheduling
- Voice biometrics for caller identification
- Integration with additional tools (Slack, CRM, etc.)

---

## Support & Resources

### Official Documentation
- **Retell AI Docs**: https://docs.retellai.com
- **n8n Documentation**: https://docs.n8n.io
- **Google Workspace APIs**: https://developers.google.com/workspace

### Repository Files Reference
- Configuration: `mr-jace-retell-config.json:1-45`
- System Prompt: `mr-jace-retell-config.json:20` (general_prompt field)
- Deployment Guide: `mr-jace-deployment-guide.md:1-952`
- Function Definitions: `mr-jace-deployment-guide.md:135-839`

---

## Quick Reference

### Key Configuration Values
```json
{
  "voice_id": "ErXwobaYiN019PkySvjV",
  "model": "gpt-4o-realtime-preview-2024-12-17",
  "temperature": 0.3,
  "max_tokens": 500,
  "responsiveness": 0.8,
  "interruption_sensitivity": 0.7,
  "timezone": "America/Chicago"
}
```

### VIP Email Addresses (Auto-Hot Priority)
- kel@foreman.ai
- kel@4manai.io
- maxstrongperformance@gmail.com

### Default Behaviors
- Meeting length: 1 hour
- Task list: @default
- Calendar: primary
- Email signature: "Sara Casey\nVP Foreman AI"

---

## Changelog

When making changes to this repository, document them here:

### [Current] - 2025-11-20
- Initial CLAUDE.md creation
- Complete documentation of repository structure
- Architecture diagrams and workflow documentation

---

*This CLAUDE.md file is maintained to help AI assistants understand and work with this repository effectively. Keep it updated when making significant changes to the codebase.*
