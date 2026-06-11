# Free Google Sheets Invoice Reminder Workflow

A lightweight n8n workflow that checks invoice rows in Google Sheets and prepares reminder emails for overdue or upcoming invoices.

## What it does

- Reads invoice/customer rows from Google Sheets.
- Filters invoices by due date and payment status.
- Builds reminder email content for the relevant invoices.
- Keeps credentials and sheet IDs as placeholders so importers can configure their own accounts.

## Good fit for

Freelancers, consultants, and small-business operators who track invoices in a spreadsheet and want a simple reminder automation before moving to a heavier accounting stack.

## Setup

1. Import `workflow.json` into n8n.
2. Connect your Google Sheets and email credentials.
3. Replace the placeholder sheet ID/range with your invoice sheet.
4. Test with a copy of your sheet before enabling any scheduled trigger.

Source/free setup guide: https://cleo-ai-ops.github.io/client-intake-autopilot-pack/free-n8n-invoice-reminder-workflow/
