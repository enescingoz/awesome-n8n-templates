# Contributing to Awesome n8n Templates

Thank you for your interest in contributing! This repository contains 280+ n8n automation templates and is growing thanks to contributors like you.

## How to Contribute a Template

1. **Fork** this repository
2. **Add your JSON template** to the correct category folder (e.g., `Gmail_and_Email_Automation/`, `Telegram/`, `OpenAI_and_LLMs/`)
3. **Update README.md** by adding a new row to the appropriate category table:
   ```
   | Template Title | Brief description of what it does. | Department | [Link to Template](Category_Folder/Template%20Name.json) |
   ```
4. **Submit a Pull Request** with a clear title and description of the template

## Template Requirements

- Must be a valid n8n workflow JSON file (exported from n8n)
- Must include a meaningful name and description
- Should be tested and working on a recent version of n8n
- Must **not** contain credentials, API keys, or any sensitive data
- File name should match the template title (spaces are fine)

## Suggesting a New Category

If your template doesn't fit into an existing category:

1. Open an [Issue](https://github.com/enescingoz/awesome-n8n-templates/issues) with the subject "New Category: [Category Name]"
2. Explain what types of templates would belong in this category
3. Include at least one template to start the category

## Reporting Issues

- If a template is broken or contains errors, open an issue with the template name and a description of the problem
- If a template contains credentials or sensitive data, please report it immediately

## Style Guide

| Column | Format |
|--------|--------|
| Title | Full template name as it appears in n8n |
| Description | 1-2 sentences explaining what the template does |
| Department | The business function (e.g., Marketing, Support, Engineering, HR, Ops) |
| Link | Relative path to the JSON file in the repository |

## Code of Conduct

- Be respectful and constructive in all interactions
- Give credit to original template authors where applicable
- Focus on quality over quantity — one well-documented template is better than many untested ones

## Questions?

Open an [Issue](https://github.com/enescingoz/awesome-n8n-templates/issues) and we'll be happy to help.
