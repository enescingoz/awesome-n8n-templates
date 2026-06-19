# Awesome n8n Templates

> The largest open-source collection of n8n automation templates on GitHub. Browse 280+ free, ready-to-import workflow templates covering Gmail, Telegram, OpenAI, WhatsApp, Slack, Discord, WordPress, Google Sheets, and dozens more platforms. Continuously updated as of March 2026.

<p align="center">
  <a href="https://trendshift.io/repositories/14621" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/14621" alt="enescingoz%2Fawesome-n8n-templates | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/enescingoz/awesome-n8n-templates?style=social" alt="GitHub Stars" /> <img src="https://img.shields.io/github/forks/enescingoz/awesome-n8n-templates?style=social" alt="GitHub Forks" /> <img src="https://img.shields.io/badge/templates-280+-blue" alt="Templates" /> <img src="https://img.shields.io/badge/license-CC--BY--4.0-blue" alt="License" /> <img src="https://img.shields.io/github/last-commit/enescingoz/awesome-n8n-templates" alt="Last Commit" /> <img src="https://awesome.re/badge.svg" alt="Awesome" />
</p>

---

<p align="center">
  <a href="README-tr.md"><img src="https://img.shields.io/badge/Türkçe-Tıkla-crimson" alt="Türkçe" /></a> | <a href="README.md"><img src="https://img.shields.io/badge/English-Click-yellow" alt="English" /></a> | <a href="README-zh.md"><img src="https://img.shields.io/badge/中文-点击查看-orange" alt="中文" /></a> | <a href="README-de.md"><img src="https://img.shields.io/badge/Deutsch-Klicken-blue" alt="Deutsch" /></a> | <a href="README-fr.md"><img src="https://img.shields.io/badge/Français-Cliquer-green" alt="Français" /></a> | <a href="README-es.md"><img src="https://img.shields.io/badge/Español-Clic-red" alt="Español" /></a> | <a href="README-pt.md"><img src="https://img.shields.io/badge/Português-Clique-brightgreen" alt="Português" /></a> | <a href="README-ja.md"><img src="https://img.shields.io/badge/日本語-クリック-blueviolet" alt="日本語" /></a> | <a href="README-ko.md"><img src="https://img.shields.io/badge/한국어-클릭-ff69b4" alt="한국어" /></a> | <a href="README-hi.md"><img src="https://img.shields.io/badge/हिन्दी-क्लिक-orange" alt="हिन्दी" /></a> | <a href="README-ar.md"><img src="https://img.shields.io/badge/العربية-انقر-green" alt="العربية" /></a> | <a href="README-id.md"><img src="https://img.shields.io/badge/Bahasa_Indonesia-Klik-red" alt="Bahasa Indonesia" /></a> | <a href="README-ru.md"><img src="https://img.shields.io/badge/Русский-Нажмите-blue" alt="Русский" /></a> | <a href="README-it.md"><img src="https://img.shields.io/badge/Italiano-Clicca-brightgreen" alt="Italiano" /></a>
</p>

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="https://img.shields.io/badge/Try_n8n_Free-Start_Automating-orange?style=for-the-badge" alt="Try n8n Free" />
  </a>
</p>

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="/img/n8n.png" alt="n8n automation platform" style="max-height: 300px;" />
  </a>
</p>

---

## Table of Contents

- [Quick Start: How to Use These Templates](#quick-start-how-to-use-these-templates)
- [Why n8n?](#why-n8n)
- [Repository Statistics](#repository-statistics)
- [Disclaimer](#disclaimer)
- [Categories & Template List](#categories--template-list)
  - [Gmail & Email Automation](#what-n8n-templates-are-available-for-gmail-and-email-automation)
  - [Telegram](#how-can-i-automate-telegram-bots-with-n8n)
  - [Google Drive & Google Sheets](#what-are-the-best-n8n-templates-for-google-drive-and-google-sheets)
  - [WordPress](#how-do-i-automate-wordpress-with-n8n)
  - [PDF & Document Processing](#what-n8n-templates-exist-for-pdf-and-document-processing)
  - [Discord](#how-can-i-automate-discord-with-n8n)
  - [Database & Storage](#what-are-the-best-n8n-database-and-storage-automation-templates)
  - [DevOps / Server Automation](#what-n8n-templates-are-available-for-devops-and-server-automation)
  - [Airtable](#how-do-i-automate-airtable-with-n8n)
  - [Notion](#what-are-the-best-n8n-templates-for-notion)
  - [Slack](#how-can-i-automate-slack-with-n8n)
  - [OpenAI & LLMs](#what-n8n-templates-are-available-for-openai-llms-and-ai-agents)
  - [WhatsApp](#how-do-i-build-whatsapp-chatbots-with-n8n)
  - [Instagram, Twitter, Social Media](#what-are-the-best-n8n-templates-for-social-media-automation)
  - [Other Integrations & Use Cases](#what-other-n8n-integration-templates-are-available)
  - [Forms & Surveys](#how-do-i-automate-forms-and-surveys-with-n8n)
  - [AI Research, RAG, and Data Analysis](#what-n8n-templates-exist-for-ai-research-rag-and-data-analysis)
  - [Other](#other)
- [FAQ](#faq)
- [Contributing](#contributing)
- [Star History](#star-history)
- [Contributors](#contributors)
- [Sponsors](#sponsors)

---

## Quick Start: How to Use These Templates

1. **[Sign up for n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe)** (free & open-source)
2. Download any `.json` template file from this repository
3. In n8n, go to **Workflows → Import from File** and select the JSON
4. Configure your credentials for each connected service
5. Activate the workflow and start automating!

---

## Why n8n?

[n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) is an open-source workflow automation platform that lets you connect anything to everything. Unlike closed-source alternatives, n8n gives you full control over your data and infrastructure. Key advantages include:

- **Open-source and self-hostable** -- run it on your own server with no vendor lock-in
- **400+ built-in integrations** -- connect to virtually any service or API
- **Visual workflow editor** -- build automations by dragging and dropping nodes, no coding required
- **AI-native capabilities** -- built-in support for OpenAI, Claude, Gemini, LangChain, and vector databases
- **Free to start** -- generous free tier on n8n Cloud, or self-host at no cost

Whether you are automating email workflows, building AI chatbots, processing documents, or orchestrating DevOps pipelines, n8n provides the foundation these templates run on.

---

## Repository Statistics

- **280+ automation templates** across 18 categories
- **19,000+ GitHub stars** from the automation community
- **Platforms covered**: Gmail, Telegram, Google Drive, Google Sheets, WordPress, Discord, Slack, Notion, Airtable, WhatsApp, Instagram, Twitter/X, LinkedIn, Spotify, Pinterest, Todoist, Obsidian, and more
- **AI integrations**: OpenAI GPT-4, Anthropic Claude, Google Gemini, DeepSeek R1, Mistral AI, LangChain, Perplexity, Hugging Face, and more
- **Use cases**: Email automation, AI chatbots, RAG pipelines, document processing, social media management, HR workflows, DevOps automation, lead qualification, sentiment analysis, data extraction, and more
- **Database support**: PostgreSQL, MongoDB, SQLite, Supabase, Pinecone, Qdrant, Elasticsearch, Airtable, NocoDB, Baserow

---

## Disclaimer

All automation templates in this repository were found online and are uploaded here solely for easy access and sharing. None of the templates are created or owned by the repository author. If you encounter any issues, errors, or damages resulting from the use of these templates, the repository author assumes no responsibility or liability. All rights to the original templates belong to their respective creators.

---

## Categories & Template List

### What n8n templates are available for Gmail and email automation?

This collection includes 9 email automation templates for n8n covering Gmail, Outlook, and IMAP. Templates range from AI-powered email labeling and categorization with OpenAI to phishing detection, auto-reply drafting, and daily financial news delivery. Ideal for operations, security, and executive teams looking to streamline email management.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Auto-label incoming Gmail messages with AI nodes | Automatically labels incoming Gmail messages using AI. The workflow retrieves message content, suggests labels like Partnership or Inquiry, and assigns them for better organization. | Ops | [Link to Template](Gmail_and_Email_Automation/Auto-label%20incoming%20Gmail%20messages%20with%20AI%20nodes.json) |
| Basic Automatic Gmail Email Labelling with OpenAI and Gmail API | Uses OpenAI and Gmail API to trigger on new emails, analyze content, and assign or create labels automatically. Helps categorize emails efficiently using AI. | Ops | [Link to Template](Gmail_and_Email_Automation/Basic%20Automatic%20Gmail%20Email%20Labelling%20with%20OpenAI%20and%20Gmail%20API.json) |
| Compose reply draft in Gmail with OpenAI Assistant | Generates draft replies in Gmail using OpenAI. Triggers on new emails, extracts content, and creates a suggested reply draft to streamline responses. | Executive | [Link to Template](Gmail_and_Email_Automation/Compose%20reply%20draft%20in%20Gmail%20with%20OpenAI%20Assistant.json) |
| Analyze & Sort Suspicious Email Contents with ChatGPT | Analyzes suspicious emails using ChatGPT, classifies them, and can generate screenshots for review. Helps identify and sort potentially dangerous emails. | Security | [Link to Template](Gmail_and_Email_Automation/Analyze%20&%20Sort%20Suspicious%20Email%20Contents%20with%20ChatGPT.json) |
| Analyze Suspicious Email Contents with ChatGPT Vision | Uses both text and image analysis (ChatGPT Vision) to evaluate suspicious emails. Extracts screenshots, analyzes headers and content, and flags phishing attempts. | Security | [Link to Template](Gmail_and_Email_Automation/Analyze%20Suspicious%20Email%20Contents%20with%20ChatGPT%20Vision.json) |
| A Very Simple "Human in the Loop" Email Response System Using AI and IMAP | Implements a simple workflow for human-in-the-loop email responses. Uses IMAP to fetch emails, summarizes content with AI, and drafts professional replies for review before sending. | Support | [Link to Template](Gmail_and_Email_Automation/A%20Very%20Simple%20_Human%20in%20the%20Loop_%20Email%20Response%20System%20Using%20AI%20and%20IMAP.json) |
| Auto Categorise Outlook Emails with AI | Automatically categorizes Outlook emails using AI models. Moves messages to folders and assigns categories based on content, reducing manual sorting. | Ops | [Link to Template](Gmail_and_Email_Automation/Auto%20Categorise%20Outlook%20Emails%20with%20AI.json) |
| Microsoft Outlook AI Email Assistant with contact support from Monday and Airtable | An AI-powered assistant for Outlook that processes emails, sanitizes content, and assigns categories using rules from Airtable. Integrates with Monday.com for contact support. | Ops | [Link to Template](Gmail_and_Email_Automation/Microsoft%20Outlook%20AI%20Email%20Assistant%20with%20contact%20support%20from%20Monday%20and%20Airtable.json) |
| 📈 Receive Daily Market News from FT.com to your Microsoft outlook inbox | Extracts financial news from FT.com and delivers daily updates to your Outlook inbox. Automates content extraction and email delivery for timely market insights. | Executive | [Link to Template](Gmail_and_Email_Automation/📈%20Receive%20Daily%20Market%20News%20from%20FT.com%20to%20your%20Microsoft%20outlook%20inbox.json) |
| AI Email Auto-Responder with Ollama | Classifies incoming emails, filters spam, and drafts context-aware replies using Ollama local AI. No external API keys required. | Support | [Link to Template](Gmail_and_Email_Automation/AI%20Email%20Auto-Responder%20with%20Ollama.json) |
| InboxZero Lite - AI Email Classifier | AI classifies Gmail emails as urgent, important, info, or spam using OpenAI gpt-4o-mini. Lightweight single-workflow setup with Google Sheets logging. | Ops | [Link to Template](Gmail_and_Email_Automation/InboxZero%20Lite%20-%20AI%20Email%20Classifier.json) |
| LeadPilot Lite - AI Cold Email Writer | AI writes personalized cold emails from a Google Sheets lead list using OpenAI. Generates subject lines and body text tailored to each prospect. | Sales | [Link to Template](Gmail_and_Email_Automation/LeadPilot%20Lite%20-%20AI%20Cold%20Email%20Writer.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### How can I automate Telegram bots with n8n?

Explore 18 Telegram automation templates for n8n, including AI chatbots with LangChain and OpenAI, voice-to-text translation across 55 languages, PDF chat functionality, image analysis bots, and Spotify integration. These templates cover support, marketing, and content moderation use cases for Telegram.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Agentic Telegram AI bot with LangChain nodes and new tools | An advanced Telegram bot leveraging LangChain and OpenAI for conversational AI. Supports memory, dynamic tool use, and handles incoming events for rich, context-aware chat interactions. | Support | [Link to Template](Telegram/Agentic%20Telegram%20AI%20bot%20with%20with%20LangChain%20nodes%20and%20new%20tools.json) |
| AI-Powered Children's Arabic Storytelling on Telegram | A Telegram bot that uses OpenAI to generate and narrate children's stories in Arabic, making storytelling interactive and educational for young users. | Support | [Link to Template](Telegram/AI-Powered%20Children_s%20Arabic%20Storytelling%20on%20Telegram.json) |
| AI-Powered Children's English Storytelling on Telegram with OpenAI | Creates and tells children's stories in English using OpenAI to engage young audiences in an interactive way. | Support | [Link to Template](Telegram/AI-Powered%20Children_s%20English%20Storytelling%20on%20Telegram%20with%20OpenAI.json) |
| Automated AI image analysis and response via Telegram | Lets users send images to Telegram and receive AI-based analysis and feedback automatically. | Ops | [Link to Template](Telegram/Automated%20AI%20image%20analysis%20and%20response%20via%20Telegram.json) |
| Angie, Personal AI Assistant with Telegram Voice and Text | Personal voice & text assistant bot that answers queries, manages tasks, and interacts naturally using AI. | Support | [Link to Template](Telegram/Angie,%20Personal%20AI%20Assistant%20with%20Telegram%20Voice%20and%20Text.json) |
| Chat with OpenAI's GPT via a simple Telegram Bot | A minimal Telegram bot that forwards user messages to GPT and returns AI-generated replies. Ideal starting point for AI chat. | Support | [Link to Template](Telegram/Chat%20with%20OpenAIs%20GPT%20via%20a%20simple%20Telegram%20Bot.json) |
| Telegram AI bot assistant: ready-made template for voice & text messages | Ready-made assistant bot handling both voice and text input, leveraging AI for smart conversational responses in Telegram. | Support | [Link to Template](Telegram/Telegram%20AI%20bot%20assistant_%20ready-made%20template%20for%20voice%20&%20text%20messages.json) |
| Telegram AI Bot: NeurochainAI Text & Image | Integrates NeurochainAI API for text and image generation inside Telegram, enabling creative media interactions. | Marketing | [Link to Template](Telegram/Telegram%20AI%20Bot_%20NeurochainAI%20Text%20&%20Image%20-%20NeurochainAI%20Basic%20API%20Integration.json) |
| Telegram AI bot with LangChain nodes | Uses LangChain nodes for advanced AI conversations and tool use in Telegram. | Support | [Link to Template](Telegram/Telegram%20AI%20bot%20with%20LangChain%20nodes.json) |
| Telegram AI Chatbot | A general-purpose AI chatbot template for Telegram that can be customized for various use cases. | Support | [Link to Template](Telegram/Telegram%20AI%20Chatbot.json) |
| Telegram Bot with Supabase memory and OpenAI assistant integration | Adds long-term memory with Supabase to a Telegram bot, coupled with OpenAI for rich, context-aware conversations. | Support | [Link to Template](Telegram/Telegram%20Bot%20with%20Supabase%20memory%20and%20OpenAI%20assistant%20integration.json) |
| Telegram chat with PDF | Allows users to upload a PDF to Telegram and chat with its contents using AI-powered summarization and Q&A. | Ops | [Link to Template](Telegram/Telegram%20chat%20with%20PDF.json) |
| 🤖 Telegram Messaging Agent for Text_Audio_Images | Multi-modal agent that processes text, audio, and images in Telegram chats using AI for responses. | Support | [Link to Template](Telegram/%F0%9F%A4%96%20Telegram%20Messaging%20Agent%20for%20Text_Audio_Images.json) |
| Telegram to Spotify with OpenAI | Lets users request songs or playlists in Telegram and automatically create them in Spotify via OpenAI. | Marketing | [Link to Template](Telegram/Telegram%20to%20Spotify%20with%20OpenAI.json) |
| Send a random recipe once a day to Telegram | Scheduled workflow that fetches a random recipe daily and posts it to a Telegram chat. | Marketing | [Link to Template](Telegram/Send%20a%20random%20recipe%20once%20a%20day%20to%20Telegram.json) |
| Detect toxic language in Telegram messages | Monitors Telegram chats and flags messages containing toxic language using AI moderation. | Security | [Link to Template](Telegram/Detect%20toxic%20language%20in%20Telegram%20messages.json) |
| Translate Telegram audio messages with AI (55 supported languages) | Receives voice messages, transcribes them, and sends back translations in over 50 languages. | Support | [Link to Template](Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json) |
| Empower Your AI Chatbot with Long-Term Memory and Dynamic Tool Routing | External workflow enhancing an AI chatbot with long-term memory and dynamic tool routing capabilities. | Support | [Link to Template](https://n8n.io/workflows/3025-empower-your-ai-chatbot-with-long-term-memory-and-dynamic-tool-routing/) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What are the best n8n templates for Google Drive and Google Sheets?

Browse 13 Google Drive and Google Sheets automation templates for n8n. Includes RAG chatbots for company documents, OpenAI model fine-tuning pipelines, automated background removal, lead qualification with GPT-4, applicant screening for HR, and document summarization workflows. Perfect for operations, sales, marketing, and engineering teams.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Automated End-to-End Fine-Tuning of OpenAI Models with Google Drive Integration | Automates the fine-tuning of OpenAI models by integrating with Google Drive for data input and output, streamlining custom AI model training. | Engineering | [Link to Template](Google_Drive_and_Google_Sheets/Automated%20End-to-End%20Fine-Tuning%20of%20OpenAI%20Models%20with%20Google%20Drive%20Integration.json) |
| Automatic Background Removal for Images in Google Drive | Automatically removes backgrounds from images stored in Google Drive, preparing them for various uses like product catalogs or marketing materials. | Marketing | [Link to Template](Google_Drive_and_Google_Sheets/Automatic%20Background%20Removal%20for%20Images%20in%20Google%20Drive.json) |
| Build an OpenAI Assistant with Google Drive Integration | Demonstrates building an OpenAI Assistant that accesses and utilizes files in Google Drive, enabling it to answer questions or perform tasks based on document content. | Support | [Link to Template](Google_Drive_and_Google_Sheets/Build%20an%20OpenAI%20Assistant%20with%20Google%20Drive%20Integration.json) |
| RAG Chatbot for Company Documents using Google Drive and Gemini | Creates a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on company documents stored in Google Drive, leveraging Google Gemini. | Support | [Link to Template](Google_Drive_and_Google_Sheets/RAG%20Chatbot%20for%20Company%20Documents%20using%20Google%20Drive%20and%20Gemini.json) |
| RAG_Context-Aware Chunking: Google Drive to Pinecone via OpenRouter & Gemini | Implements context-aware chunking for Google Drive documents, sending them to Pinecone for vector storage and using OpenRouter & Gemini for advanced RAG. | Engineering | [Link to Template](Google_Drive_and_Google_Sheets/RAG_Context-Aware%20Chunking%20_%20Google%20Drive%20to%20Pinecone%20via%20OpenRouter%20&%20Gemini.json) |
| Summarize the New Documents from Google Drive and Save Summary in Google Sheet | Monitors Google Drive for new documents, summarizes their content using AI, and saves these summaries into a Google Sheet for quick overview and analysis. | Ops | [Link to Template](Google_Drive_and_Google_Sheets/Summarize%20the%20New%20Documents%20from%20Google%20Drive%20and%20Save%20Summary%20in%20Google%20Sheet.json) |
| Upload to Instagram and Tiktok from Google Drive | Automates uploading media from Google Drive directly to Instagram and TikTok, streamlining social media content publishing. | Marketing | [Link to Template](Google_Drive_and_Google_Sheets/Upload%20to%20Instagram%20and%20Tiktok%20from%20Google%20Drive.json) |
| Author and Publish Blog Posts From Google Sheets | Enables authoring blog posts in Google Sheets and automatically publishing them to a content management system, simplifying content creation and publishing. | Marketing | [Link to Template](Google_Drive_and_Google_Sheets/Author%20and%20Publish%20Blog%20Posts%20From%20Google%20Sheets.json) |
| Chat with a Google Sheet using AI | Allows users to interact with and query data within a Google Sheet using natural language via an AI model, making data analysis more accessible. | Ops | [Link to Template](Google_Drive_and_Google_Sheets/Chat%20with%20a%20Google%20Sheet%20using%20AI.json) |
| Chat with your event schedule from Google Sheets in Telegram | Connects a Google Sheet containing an event schedule to Telegram, allowing users to query their schedule through a Telegram bot. | Ops | [Link to Template](Google_Drive_and_Google_Sheets/Chat%20with%20your%20event%20schedule%20from%20Google%20Sheets%20in%20Telegram.json) |
| Qualify new leads in Google Sheets via OpenAI's GPT-4 | Uses OpenAI's GPT-4 to analyze and qualify new leads entered into a Google Sheet, helping sales teams prioritize their outreach. | Sales | [Link to Template](Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20Sheets%20via%20OpenAI_s%20GPT-4.json) |
| Screen Applicants With AI, notify HR and save them in a Google Sheet | Automates the screening of job applicants using AI, notifies HR of qualified candidates, and saves applicant data into a Google Sheet. | HR | [Link to Template](Google_Drive_and_Google_Sheets/Screen%20Applicants%20With%20AI,%20notify%20HR%20and%20save%20them%20in%20a%20Google%20Sheet.json) |
| Summarize Google Sheets form feedback via OpenAI's GPT-4 | Summarizes feedback collected through Google Forms and stored in Google Sheets using OpenAI's GPT-4, providing quick insights from survey responses. | Marketing | [Link to Template](Google_Drive_and_Google_Sheets/Summarize%20Google%20Sheets%20form%20feedback%20via%20OpenAI_s%20GPT-4.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### How do I automate WordPress with n8n?

This section features 6 WordPress automation templates for n8n. Automate blog post categorization and tagging with AI, generate content in your brand voice, use DeepSeek R1 for rapid content creation, embed an AI chatbot with Supabase and OpenAI, or write full blog posts from just a few keywords.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Auto-Categorize blog posts in wordpress using A.I. | This workflow automates the categorization of WordPress blog posts using AI, streamlining content organization and management. | Marketing/Content | [Link to Template](WordPress/Auto-Categorize%20blog%20posts%20in%20wordpress%20using%20A.I..json) |
| Auto-Tag Blog Posts in WordPress with AI | This workflow automatically tags WordPress blog posts using AI, improving SEO and content discoverability. | Marketing/Content | [Link to Template](WordPress/Auto-Tag%20Blog%20Posts%20in%20WordPress%20with%20AI.json) |
| Automate Blog Creation in Brand Voice with AI | This workflow automates the creation of blog posts, ensuring they adhere to a specific brand voice using AI. | Marketing/Content | [Link to Template](WordPress/Automate%20Blog%20Creation%20in%20Brand%20Voice%20with%20AI.json) |
| Automate Content Generator for WordPress with DeepSeek R1 | This workflow automates content generation for WordPress using the DeepSeek R1 AI model, enabling rapid content creation. | Marketing/Content | [Link to Template](WordPress/Automate%20Content%20Generator%20for%20WordPress%20with%20DeepSeek%20R1.json) |
| WordPress - AI Chatbot to enhance user experience - with Supabase and OpenAI | This workflow integrates an AI chatbot into WordPress using Supabase and OpenAI to enhance user experience by providing intelligent interactions. | Customer Support/Marketing | [Link to Template](WordPress/WordPress%20-%20AI%20Chatbot%20to%20enhance%20user%20experience%20-%20with%20Supabase%20and%20OpenAI.json) |
| Write a WordPress post with AI (starting from a few keywords) | This workflow uses AI to write WordPress posts based on a few keywords, simplifying the content creation process. | Marketing/Content | [Link to Template](WordPress/Write%20a%20WordPress%20post%20with%20AI%20(starting%20from%20a%20few%20keywords).json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What n8n templates exist for PDF and document processing?

Find 11 PDF and document processing templates for n8n. These workflows handle AI-powered PDF Q&A with source quoting, resume parsing with multimodal vision AI, invoice data extraction via LlamaParse, document-to-study-notes conversion, ETL text pipelines, HTML-to-Markdown conversion, and more. Supports Claude, Gemini, MistralAI, and OpenAI models.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Ask questions about a PDF using AI | This workflow fetches a PDF from Google Drive, splits it into chunks, embeds the chunks using OpenAI embeddings, and enables chat interactions with the document content. | Customer Support/Knowledge Management | [Link to Template](PDF_and_Document_Processing/Ask%20questions%20about%20a%20PDF%20using%20AI.json) |
| Breakdown Documents into Study Notes using Templating MistralAI and Qdrant | This workflow triggers on new files, processes documents with MistralAI embeddings, and stores data in Qdrant vector store for study note generation. | Education/Knowledge Management | [Link to Template](PDF_and_Document_Processing/Breakdown%20Documents%20into%20Study%20Notes%20using%20Templating%20MistralAI%20and%20Qdrant.json) |
| CV Resume PDF Parsing with Multimodal Vision AI | This workflow converts candidate resume PDFs to images, uses a Vision Language Model to assess candidate fit, and includes logic to bypass hidden AI prompts in resumes. | HR | [Link to Template](PDF_and_Document_Processing/CV%20Resume%20PDF%20Parsing%20with%20Multimodal%20Vision%20AI.json) |
| Chat with PDF docs using AI (quoting sources) | This workflow enables chat interactions with PDF documents, allowing users to ask questions and receive answers with quoted sources from the document. | Customer Support/Knowledge Management | [Link to Template](PDF_and_Document_Processing/Chat%20with%20PDF%20docs%20using%20AI%20(quoting%20sources).json) |
| Convert URL HTML to Markdown Format and Get Page Links | This workflow converts HTML content from a given URL into Markdown format and extracts all page links, useful for content scraping and analysis. | Marketing/Content | [Link to Template](PDF_and_Document_Processing/Convert%20URL%20HTML%20to%20Markdown%20Format%20and%20Get%20Page%20Links.json) |
| ETL pipeline for text processing | This workflow implements an ETL pipeline for text processing, extracting data from Twitter, storing it in MongoDB and PostgreSQL, and sending alerts to Slack based on sentiment analysis. | Data Analytics/IT | [Link to Template](PDF_and_Document_Processing/ETL%20pipeline%20for%20text%20processing.json) |
| Extract and process information directly from PDF using Claude and Gemini | This workflow extracts and processes information directly from PDFs using advanced AI models like Claude and Gemini, enabling intelligent document analysis. | Data Extraction/IT | [Link to Template](PDF_and_Document_Processing/Extract%20and%20process%20information%20directly%20from%20PDF%20using%20Claude%20and%20Gemini.json) |
| Extract data from resume and create PDF with Gotenberg | This workflow extracts structured data from resumes using AI, converts it into HTML, and then generates a well-formatted PDF using Gotenberg. | HR | [Link to Template](PDF_and_Document_Processing/Extract%20data%20from%20resume%20and%20create%20PDF%20with%20Gotenberg.json) |
| Extract license plate number from image uploaded via an n8n form | This workflow extracts license plate numbers from images uploaded via an n8n form using a Vision Language Model, then displays the extracted information. | Operations/Logistics | [Link to Template](PDF_and_Document_Processing/Extract%20license%20plate%20number%20from%20image%20uploaded%20via%20an%20n8n%20form.json) |
| Extract text from PDF and image using Vertex AI (Gemini) into CSV | This workflow extracts text from PDFs and images using Vertex AI (Gemini), routes based on file type, and converts the extracted data into a CSV format. | Data Extraction/IT | [Link to Template](PDF_and_Document_Processing/Extract%20text%20from%20PDF%20and%20image%20using%20Vertex%20AI%20(Gemini)%20into%20CSV.json) |
| Invoice data extraction with LlamaParse and OpenAI | This workflow extracts structured data from invoices using LlamaParse and OpenAI, then processes it with a structured output parser for detailed invoice data extraction. | Finance/Admin | [Link to Template](PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20LlamaParse%20and%20OpenAI.json) |
| Extract data from PDFs with human-in-the-loop validation and auto-training using Cradl AI | Extracts structured data from invoices and similar documents using Cradl AI. Flags low-confidence predictions for human review before they enter your system, automatically retrains the model on approved corrections, and applies built-in LLM guardrails to detect and reject hallucinations. | Finance/Logistics/Operations| [Link to Template](PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20human-in-the-loop%20validation%20and%20auto-training%20using%20Cradl%20AI.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### How can I automate Discord with n8n?

This section contains 3 Discord automation templates for n8n. Build an AI-powered Discord bot that routes messages to the right department, automate daily comic translations and posts, or share YouTube videos with AI-generated summaries directly to your Discord server.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Discord AI-powered bot | This workflow creates an AI-powered Discord bot that categorizes user messages (success story, urgent issue, ticket) and routes them to the appropriate department (customer success, IT, customer support). | Customer Support | [Link to Template](Discord/Discord%20AI-powered%20bot.json) |
| Send daily translated Calvin and Hobbes Comics to Discord | This workflow automates the daily retrieval of Calvin and Hobbes comics, translates the dialogues into English and Korean (or other languages), and posts them to Discord. | Marketing/Content | [Link to Template](Discord/Send%20daily%20translated%20Calvin%20and%20Hobbes%20Comics%20to%20Discord.json) |
| Share YouTube Videos with AI Summaries on Discord | This workflow automatically shares new YouTube videos on Discord along with AI-generated summaries of their content, leveraging caption data. | Marketing | [Link to Template](Discord/Share%20YouTube%20Videos%20with%20AI%20Summaries%20on%20Discord.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What are the best n8n database and storage automation templates?

Find 5 database and storage automation templates for n8n. Chat with PostgreSQL using natural language, generate SQL queries from schema with AI, get intelligent movie recommendations from MongoDB, manage Supabase vector embeddings, or query SQLite databases through a LangChain AI agent.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Chat with Postgresql Database | This workflow enables an AI assistant to chat with a PostgreSQL database, allowing users to query and retrieve data using natural language. It supports custom SQL queries and schema introspection. | Data Analytics | [Link to Template](Database_and_Storage/Chat%20with%20Postgresql%20Database.json) |
| Generate SQL queries from schema only - AI-powered | This workflow uses AI to generate SQL queries based on a given database schema, making it easier to interact with databases without manual query writing. | Engineering | [Link to Template](Database_and_Storage/Generate%20SQL%20queries%20from%20schema%20only%20-%20AI-powered.json) |
| MongoDB AI Agent - Intelligent Movie Recommendations | This workflow creates an AI agent that provides intelligent movie recommendations by interacting with a MongoDB database, using aggregation pipelines to fetch relevant movie data. | Data Analytics | [Link to Template](Database_and_Storage/MongoDB%20AI%20Agent%20-%20Intelligent%20Movie%20Recommendations.json) |
| Supabase Insertion & Upsertion & Retrieval | This workflow demonstrates how to perform insertion, upsertion, and retrieval operations with Supabase, specifically for handling vector embeddings and associated metadata. | Engineering | [Link to Template](Database_and_Storage/Supabase%20Insertion%20&%20Upsertion%20&%20Retrieval.json) |
| Talk to your SQLite database with a LangChain AI Agent | This workflow allows users to interact with a SQLite database using a LangChain AI agent, enabling natural language queries and data retrieval from the database. | Data Analytics | [Link to Template](Database_and_Storage/Talk%20to%20your%20SQLite%20database%20with%20a%20LangChain%20AI%20Agent.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What n8n templates are available for DevOps and server automation?

This section includes 2 DevOps and server automation templates for n8n. Trigger Linux system updates via authenticated webhooks over SSH, or control Docker Compose services remotely through HTTP POST requests. Both templates use SSH for secure server management.

| Title | Description | Link |
|-------|-------------|------|
| Linux System Update via Webhook | Trigger update & upgrade of your Debian-based server via an authenticated POST request and SSH. | SSH Tools | [Link to Template](devops/linux-update-via-webhook.json)
| Docker Compose Controller via Webhook | Start or stop Docker Compose services on your server via authenticated HTTP POST request with n8n + SSH. | SSH Tools | [Link to Template](devops/docker-compose-controller.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### How do I automate Airtable with n8n?

Browse 5 Airtable automation templates for n8n. Automate project management and meeting follow-ups with Fireflies transcripts, chat with Airtable data using AI agents, integrate with Obsidian Notes, process job applications with AI-powered resume parsing, or connect HubSpot Chat with OpenAI and Airtable for customer support.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| AI Agent for project management and meetings with Airtable and Fireflies | This workflow uses an AI agent to automate project management tasks and meeting follow-ups by analyzing call transcripts from Fireflies. It creates tasks in Airtable and notifies clients about their tasks. | Operations | [Link to Template](Airtable/AI%20Agent%20for%20project%20management%20and%20meetings%20with%20Airtable%20and%20Fireflies.json) |
| AI Agent to chat with Airtable and analyze data | This workflow creates an AI agent that can chat with Airtable, analyze data, and perform queries based on user requests. It can handle aggregation functions and generate graphs/images. | Data Analytics | [Link to Template](Airtable/AI%20Agent%20to%20chat%20with%20Airtable%20and%20analyze%20data.json) |
| Get Airtable data via AI and Obsidian Notes | This workflow retrieves data from Airtable using an AI agent and integrates it with Obsidian Notes, allowing for seamless data access and organization within Obsidian. | Productivity | [Link to Template](Airtable/Get%20Airtable%20data%20via%20AI%20and%20Obsidian%20Notes.json) |
| Handling Job Application Submissions with AI and n8n Forms | This workflow automates the handling of job application submissions by extracting information from resumes (PDFs) using AI, parsing it into a structured format, and potentially storing it in Airtable. | HR | [Link to Template](Airtable/Handling%20Job%20Application%20Submissions%20with%20AI%20and%20n8n%20Forms.json) |
| vAssistant for Hubspot Chat using OpenAi and Airtable | This workflow integrates an OpenAI assistant with HubSpot Chat and Airtable to provide automated responses and manage customer interactions. It fetches chat messages, processes them with AI, and can store relevant information in Airtable. | Sales | [Link to Template](Airtable/vAssistant%20for%20Hubspot%20Chat%20using%20OpenAi%20and%20Airtable.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What are the best n8n templates for Notion?

Discover 10 Notion automation templates for n8n. Store positive feedback from Typeform with sentiment analysis, analyze Hugging Face research papers, run competitor research with AI agents, automate LinkedIn outreach, build custom AI assistants for your Notion databases, create knowledge base chatbots, and integrate with Pinecone and Supabase vector stores.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Add positive feedback messages to a table in Notion | Captures positive feedback from Typeform, analyzes sentiment with Google Cloud Natural Language, and adds it to a Notion table, with Slack notifications for high-scoring feedback. | Support | [Link to Template](Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20Notion.json) |
| Analyse papers from Hugging Face with AI and store them in Notion | Automatically fetches and analyzes papers from Hugging Face, extracts key information using AI, and stores the structured data in a Notion database. | Engineering | [Link to Template](Notion/Analyse%20papers%20from%20Hugging%20Face%20with%20AI%20and%20store%20them%20in%20Notion.json) |
| Automate Competitor Research with Exa.ai, Notion and AI Agents | Builds a competitor research agent using Exa.ai to find similar companies. AI agents then scour the internet for company overviews, product offerings, and customer reviews, compiling a report into a Notion table. | Marketing | [Link to Template](Notion/Automate%20Competitor%20Research%20with%20Exa.ai,%20Notion%20and%20AI%20Agents.json) |
| Automate LinkedIn Outreach with Notion and OpenAI | Automates LinkedIn outreach by fetching daily posts from a Notion database, formatting them with OpenAI for LinkedIn engagement, and then posting them to LinkedIn. | Marketing | [Link to Template](Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json) |
| Notion AI Assistant Generator | Generates a custom AI Assistant chatbot workflow for a specific Notion database schema, allowing users to chat with their Notion data. | Engineering | [Link to Template](Notion/Notion%20AI%20Assistant%20Generator.json) |
| Notion knowledge base AI assistant | Creates an AI assistant that can search and retrieve information from a Notion knowledge base, providing answers to user queries. | Support | [Link to Template](Notion/Notion%20knowledge%20base%20AI%20assistant.json) |
| Notion to Pinecone Vector Store Integration | Integrates Notion with Pinecone, allowing Notion pages to be converted into vector embeddings and stored in Pinecone for advanced search and retrieval. | Engineering | [Link to Template](Notion/Notion%20to%20Pinecone%20Vector%20Store%20Integration.json) |
| Store Notion's Pages as Vector Documents into Supabase with OpenAI | Automates storing Notion pages as vector documents in a Supabase database, using OpenAI to generate embeddings for the content. | Engineering | [Link to Template](Notion/Store%20Notion_s%20Pages%20as%20Vector%20Documents%20into%20Supabase%20with%20OpenAI.json) |
| Turn Emails into AI-Enhanced Tasks in Notion (Multi-User Support) with Gmail, Airtable and Softr | Transforms emails into AI-enhanced tasks in Notion, supporting multiple users. It integrates with Gmail for email triggers, Airtable for routing, and Softr for a user interface. | Ops | [Link to Template](Notion/Turn%20Emails%20into%20AI-Enhanced%20Tasks%20in%20Notion%20(Multi-User%20Support)%20with%20Gmail,%20Airtable%20and%20Softr.json) |
| Upsert huge documents in a vector store with Supabase and Notion | Manages large documents by splitting them into chunks, generating embeddings, and upserting them into a Supabase vector store, with Notion serving as the document source. | Engineering | [Link to Template](Notion/Upsert%20huge%20documents%20in%20a%20vector%20store%20with%20Supabase%20and%20Notion.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### How can I automate Slack with n8n?

Explore 9 Slack automation templates for n8n. Monitor RSS feeds with AI-powered summaries, build Slack bots using Google Gemini, automate customer support ticketing with Linear, enhance security operations with Qualys integration, enrich Pipedrive CRM data, create IT knowledge base chatbots, track sentiment on support issues, and manage certificates via Venafi Cloud.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI and Slack | Monitors RSS feeds, summarizes articles with OpenAI and Jina AI, classifies them, and sends formatted notifications to Slack, enabling AI-powered information monitoring. | Marketing | [Link to Template](Slack/AI-Powered%20Information%20Monitoring%20with%20OpenAI,%20Google%20Sheets,%20Jina%20AI%20and%20Slack.json) |
| Creating a AI Slack Bot with Google Gemini | Builds an AI Slack bot using Google Gemini, handling webhooks, integrating an AI agent, managing memory, and responding to Slack messages. | Engineering | [Link to Template](Slack/Creating%20a%20AI%20Slack%20Bot%20with%20Google%20Gemini.json) |
| Customer Support Channel and Ticketing System with Slack and Linear | Automates customer support by querying Slack for messages with a ticket emoji, deciding if a new Linear ticket is needed, creating or updating tickets, and notifying Slack. | Support | [Link to Template](Slack/Customer%20Support%20Channel%20and%20Ticketing%20System%20with%20Slack%20and%20Linear.json) |
| Enhance Security Operations with the Qualys Slack Shortcut Bot! | Creates a Slack shortcut bot for Qualys to enhance security operations, allowing users to trigger actions like creating reports or starting vulnerability scans directly from Slack. | Security | [Link to Template](Slack/Enhance%20Security%20Operations%20with%20the%20Qualys%20Slack%20Shortcut%20Bot!.json) |
| Enrich Pipedrive's Organization Data with OpenAI GPT-4o & Notify it in Slack | Enriches Pipedrive organization data by scraping website content, using OpenAI GPT-4o to generate a summary, and adding it as a note in Pipedrive, then notifying a Slack channel. | Sales | [Link to Template](Slack/Enrich%20Pipedrive_s%20Organization%20Data%20with%20OpenAI%20GPT-4o%20&%20Notify%20it%20in%20Slack.json) |
| IT Ops AI SlackBot Workflow - Chat with your knowledge base | Creates an AI Slackbot for IT Operations, enabling users to chat with a knowledge base to retrieve information and get answers directly within Slack. | IT | [Link to Template](Slack/IT%20Ops%20AI%20SlackBot%20Workflow%20-%20Chat%20with%20your%20knowledge%20base.json) |
| Sentiment Analysis Tracking on Support Issues with Linear and Slack | Tracks sentiment on support issues by integrating with Linear and Slack, performing sentiment analysis using OpenAI on Linear comments, and notifying relevant Slack channels. | Support | [Link to Template](Slack/Sentiment%20Analysis%20Tracking%20on%20Support%20Issues%20with%20Linear%20and%20Slack.json) |
| Slack slash commands AI Chat Bot | Implements an AI chatbot accessible via Slack slash commands, processing user commands, interacting with an AI model, and responding within Slack. | IT | [Link to Template](Slack/Slack%20slash%20commands%20AI%20Chat%20Bot.json) |
| Venafi Cloud Slack Cert Bot | Provides a Slack bot that interacts with Venafi Cloud for certificate management, allowing users to check certificate status, receive alerts, or request certificate actions via Slack. | Security | [Link to Template](Slack/Venafi%20Cloud%20Slack%20Cert%20Bot.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What n8n templates are available for OpenAI, LLMs, and AI agents?

This is the largest category with 17 AI and LLM templates for n8n. Templates include advanced AI agent demos, web scraping agents, stock analysis crews, customer feedback sentiment analysis, AI-powered lead management with ERPNext, fitness coaching via Strava, candidate shortlisting for HR, RAG pipelines for email and stock reports, social media amplification, WooCommerce support agents, YouTube summarization, and podcast enhancement with Wikipedia.

| Title | Description | Department | Link |
|---|---|---|---|
| Advanced AI Demo (Presented at AI Developers #14 meetup) | Advanced AI capabilities demo. | AI/Development | [Link to Template](OpenAI_and_LLMs/Advanced%20AI%20Demo%20(Presented%20at%20AI%20Developers%20%2314%20meetup).json) |
| AI agent chat | Basic AI chat agent. | AI/Customer Service | [Link to Template](OpenAI_and_LLMs/AI%20agent%20chat.json) |
| AI agent that can scrape webpages | AI agent for web scraping. | AI/Data Extraction | [Link to Template](OpenAI_and_LLMs/AI%20agent%20that%20can%20scrape%20webpages.json) |
| AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow | Stock analysis automation. | Finance/AI/Data Analysis | [Link to Template](OpenAI_and_LLMs/AI%20Crew%20to%20Automate%20Fundamental%20Stock%20Analysis%20-%20Q&A%20Workflow.json) |
| AI Customer feedback sentiment analysis | Sentiment analysis on customer feedback. | Customer Service/Marketing/Data Analysis | [Link to Template](OpenAI_and_LLMs/AI%20Customer%20feedback%20sentiment%20analysis.json) |
| AI Data Extraction with Dynamic Prompts and Airtable | AI-driven data extraction with Airtable integration. | AI/Data Extraction/Database | [Link to Template](OpenAI_and_LLMs/AI%20Data%20Extraction%20with%20Dynamic%20Prompts%20and%20Airtable.json) |
| AI Data Extraction with Dynamic Prompts and Baserow | AI-driven data extraction with Baserow integration. | AI/Data Extraction/Database | [Link to Template](OpenAI_and_LLMs/AI%20Data%20Extraction%20with%20Dynamic%20Prompts%20and%20Baserow.json) |
| AI-Driven Lead Management and Inquiry Automation with ERPNext & n8n | Lead management automation. | Sales/CRM/AI | [Link to Template](OpenAI_and_LLMs/AI-Driven%20Lead%20Management%20and%20Inquiry%20Automation%20with%20ERPNext%20&%20n8n.json) |
| AI Fitness Coach Strava Data Analysis and Personalized Training Insights | Fitness coaching via Strava data analysis. | Fitness/AI/Data Analysis | [Link to Template](OpenAI_and_LLMs/AI%20Fitness%20Coach%20Strava%20Data%20Analysis%20and%20Personalized%20Training%20Insights.json) |
| AI-Powered Candidate Shortlisting Automation for ERPNext | Candidate shortlisting automation. | HR/AI/Recruitment | [Link to Template](OpenAI_and_LLMs/AI-Powered%20Candidate%20Shortlisting%20Automation%20for%20ERPNext.json) |
| AI-Powered Email Automation for Business: Summarize & Respond with RAG | Email automation with summarization and response. | Business Automation/AI/Communication | [Link to Template](OpenAI_and_LLMs/AI-Powered%20Email%20Automation%20for%20Business_%20Summarize%20&%20Respond%20with%20RAG.json) |
| AI-Powered RAG Workflow For Stock Earnings Report Analysis | Stock earnings report analysis with RAG. | Finance/AI/Data Analysis | [Link to Template](OpenAI_and_LLMs/AI-Powered%20RAG%20Workflow%20For%20Stock%20Earnings%20Report%20Analysis.json) |
| AI-Powered Social Media Amplifier | Amplifies social media presence using AI. | Marketing/AI/Social Media | [Link to Template](OpenAI_and_LLMs/AI-Powered%20Social%20Media%20Amplifier.json) |
| AI-powered WooCommerce Support-Agent | Creates an AI-powered support agent for WooCommerce stores. | E-commerce/AI/Customer Service | [Link to Template](OpenAI_and_LLMs/AI-powered%20WooCommerce%20Support-Agent.json) |
| AI-Powered YouTube Video Summarization & Analysis | Summarizes and analyzes YouTube videos using AI. | Content Creation/AI/Data Analysis | [Link to Template](OpenAI_and_LLMs/%E2%9A%A1AI-Powered%20YouTube%20Video%20Summarization%20&%20Analysis.json) |
| AI: Ask questions about any data source (using the n8n workflow retriever) | Allows users to ask questions about various data sources using an n8n workflow retriever. | AI/Data Analysis/Workflow Automation | [Link to Template](OpenAI_and_LLMs/AI_%20Ask%20questions%20about%20any%20data%20source%20(using%20the%20n8n%20workflow%20retriever).json) |
| AI: Summarize podcast episode and enhance using Wikipedia | Summarizes podcast episodes and enhances the summary with information from Wikipedia using AI. | Content Creation/AI/Data Analysis | [Link to Template](OpenAI_and_LLMs/AI_%20Summarize%20podcast%20episode%20and%20enhance%20using%20Wikipedia.json) |
| AI Blog Writer Pipeline with Ollama | Uses Ollama local AI to research topics, create outlines, draft full blog posts, and edit them. Runs entirely locally with no API keys needed. | Content Creation/AI | [Link to Template](OpenAI_and_LLMs/AI%20Blog%20Writer%20Pipeline%20with%20Ollama.json) |
| SupportFlow Lite - Simple AI Customer Support Chatbot | A lightweight AI chatbot that answers customer questions using company info and OpenAI gpt-4o-mini. Easy single-workflow setup with Google Sheets knowledge base. | Customer Support/AI | [Link to Template](OpenAI_and_LLMs/SupportFlow%20Lite%20-%20Simple%20AI%20Customer%20Support%20Chatbot.json) |
| n8n + Local LLM (Ollama) Basic Setup | Connect n8n with local LLMs (Llama 3, Mistral, Phi-3) for 100% free AI automation. No API keys required. | AI/Automation | [Link to Template](./OpenAI_and_LLMs/Ollama_Basic_Workflow.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### How do I build WhatsApp chatbots with n8n?

This section includes 4 WhatsApp automation templates for n8n. Automate sales meeting preparation with AI and Apify, build your first WhatsApp chatbot, create a full business RAG chatbot powered by OpenAI, or set up professional AI-powered message responses. Ideal for customer service, sales, and business communication workflows.

| Title | Description | Department | Link |
|---|---|---|---|
| Automate Sales Meeting Prep with AI & APIFY Sent To WhatsApp | This workflow automates sales meeting preparation using AI and Apify, sending relevant information to WhatsApp. | Sales/AI/Automation | [Link to Template](./WhatsApp/Automate%20Sales%20Meeting%20Prep%20with%20AI%20&%20APIFY%20Sent%20To%20WhatsApp.json) |
| Building Your First WhatsApp Chatbot | This workflow guides you through building your first WhatsApp chatbot. | Customer Service/Development | [Link to Template](./WhatsApp/Building%20Your%20First%20WhatsApp%20Chatbot.json) |
| Complete business WhatsApp AI-Powered RAG Chatbot using OpenAI | This workflow builds a complete business WhatsApp AI-powered RAG chatbot using OpenAI. | Customer Service/AI/Development | [Link to Template](./WhatsApp/Complete%20business%20WhatsApp%20AI-Powered%20RAG%20Chatbot%20using%20OpenAI.json) |
| Respond to WhatsApp Messages with AI Like a Pro! | This workflow enables professional AI-powered responses to WhatsApp messages. | Customer Service/AI/Communication | [Link to Template](./WhatsApp/Respond%20to%20WhatsApp%20Messages%20with%20AI%20Like%20a%20Pro!.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What are the best n8n templates for social media automation?

Explore 10 social media automation templates for n8n covering Instagram, Twitter/X, Reddit, YouTube, LinkedIn, and more. Templates include AI-powered Instagram DM management with Manychat, dynamic Twitter banners, trend-based content generation with AI image creation, tweet generators, YouTube-to-X posting, Reddit digest creation, social media analytics, and virtual AI influencer management.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| AI agent for Instagram DM_inbox. Manychat + Open AI integration | Integrates Manychat with OpenAI to create an AI agent for managing Instagram direct messages. | Marketing/Customer Service/AI | [Link to Template](Instagram_Twitter_Social_Media/AI%20agent%20for%20Instagram%20DM_inbox.%20Manychat%20%2B%20Open%20AI%20integration.json) |
| Create dynamic Twitter profile banner | Automates the creation of dynamic Twitter profile banners. | Marketing/Social Media | [Link to Template](Instagram_Twitter_Social_Media/Create%20dynamic%20Twitter%20profile%20banner.json) |
| Generate Instagram Content from Top Trends with AI Image Generation | Creates Instagram content by analyzing top trends and generating relevant images using AI. | Marketing/AI/Content | [Link to Template](Instagram_Twitter_Social_Media/Generate%20Instagram%20Content%20from%20Top%20Trends%20with%20AI%20Image%20Generation.json) |
| OpenAI-powered tweet generator | Generates tweets using OpenAI's language models. | Marketing/Social Media/AI | [Link to Template](Instagram_Twitter_Social_Media/OpenAI-powered%20tweet%20generator.json) |
| Post New YouTube Videos to X | Automatically posts new YouTube videos to X (formerly Twitter). | Marketing/Social Media | [Link to Template](Instagram_Twitter_Social_Media/Post%20New%20YouTube%20Videos%20to%20X.json) |
| Reddit AI digest | Creates an AI-generated digest of Reddit content. | Marketing/Content/AI | [Link to Template](Instagram_Twitter_Social_Media/Reddit%20AI%20digest.json) |
| Social Media Analysis and Automated Email Generation | Analyzes social media data and generates automated email reports. | Marketing/Analytics | [Link to Template](Instagram_Twitter_Social_Media/Social%20Media%20Analysis%20and%20Automated%20Email%20Generation.json) |
| Speed Up Social Media Banners With BannerBear.com | Automates the creation of social media banners using BannerBear.com. | Marketing/Design | [Link to Template](Instagram_Twitter_Social_Media/Speed%20Up%20Social%20Media%20Banners%20With%20BannerBear.com.json) |
| Twitter Virtual AI Influencer | Manages a virtual AI influencer's Twitter account. | Marketing/AI | [Link to Template](Instagram_Twitter_Social_Media/Twitter%20Virtual%20AI%20Influencer.json) |
| Update Twitter banner using HTTP request | Updates a Twitter banner using HTTP requests. | Marketing/Development | [Link to Template](Instagram_Twitter_Social_Media/Update%20Twitter%20banner%20using%20HTTP%20request.json) |
| AI Social Media Content Generator with Ollama | Generates optimized posts for Twitter, LinkedIn, Reddit, and Instagram from a single topic using Ollama local AI with built-in quality review. | Marketing/AI/Content | [Link to Template](Instagram_Twitter_Social_Media/AI%20Social%20Media%20Content%20Generator%20with%20Ollama.json) |
| FlowScribe Lite - AI Content Repurposing (4 Platforms) | Converts one blog post into four optimized social media posts for Twitter, LinkedIn, Instagram, and Facebook using OpenAI. | Marketing/Content | [Link to Template](Instagram_Twitter_Social_Media/FlowScribe%20Lite%20-%20AI%20Content%20Repurposing%204%20Platforms.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What other n8n integration templates are available?

This section includes 28 additional n8n integration templates covering a wide range of platforms and use cases. Highlights include API schema extraction, Pinterest analysis with AI, SIEM alert enrichment with MITRE ATT&CK, Bitrix24 chatbots, GitLab code review with ChatGPT, LINE assistant integration, Spotify playlist archiving, Zoom meeting AI assistants, Siri AI agents via Apple Shortcuts, and Todoist inbox organization.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| API Schema Extractor | Extracts API schemas from web services for documentation or integration purposes. | Development/Integration | [Link to Template](Other_Integrations_and_Use_Cases/API%20Schema%20Extractor.json) |
| Analyze feedback and send a message on Mattermost | Analyzes user feedback and sends notifications to Mattermost channels. | Support/Communication | [Link to Template](Other_Integrations_and_Use_Cases/Analyze%20feedback%20and%20send%20a%20message%20on%20Mattermost.json) |
| Analyze feedback using AWS Comprehend | Performs sentiment analysis on feedback using AWS Comprehend and sends results to Mattermost. | Support/AI | [Link to Template](Other_Integrations_and_Use_Cases/Analyze%20feedback%20using%20AWS%20Comprehend%20and%20send%20it%20to%20a%20Mattermost%20channel.json) |
| Automate Pinterest Analysis & AI-Powered Content Suggestions | Analyzes Pinterest data and provides AI-powered content suggestions. | Marketing/AI | [Link to Template](Other_Integrations_and_Use_Cases/Automate%20Pinterest%20Analysis%20%26%20AI-Powered%20Content%20Suggestions%20With%20Pinterest%20API.json) |
| Automate SIEM Alert Enrichment | Enriches SIEM alerts with MITRE ATT&CK data and integrates with Zendesk. | Security/IT | [Link to Template](Other_Integrations_and_Use_Cases/Automate%20SIEM%20Alert%20Enrichment%20with%20MITRE%20ATT%26CK,%20Qdrant%20%26%20Zendesk%20in%20n8n.json) |
| Automate Screenshots with URLbox & Analyze with AI | Takes screenshots of webpages and analyzes them using AI. | Development/Marketing | [Link to Template](Other_Integrations_and_Use_Cases/Automate%20Screenshots%20with%20URLbox%20%26%20Analyze%20them%20with%20AI.json) |
| Automate testimonials in Strapi | Automates the process of collecting and managing testimonials in Strapi. | Marketing/Content | [Link to Template](Other_Integrations_and_Use_Cases/Automate%20testimonials%20in%20Strapi%20with%20n8n.json) |
| Bitrix24 Chatbot Application | Example workflow for creating a Bitrix24 chatbot with webhook integration. | Business/Communication | [Link to Template](Other_Integrations_and_Use_Cases/Bitrix24%20Chatbot%20Application%20Workflow%20example%20with%20Webhook%20Integration.json) |
| ChatGPT Automatic Code Review in Gitlab MR | Automates code reviews in GitLab merge requests using ChatGPT. | Development/DevOps | [Link to Template](Other_Integrations_and_Use_Cases/ChatGPT%20Automatic%20Code%20Review%20in%20Gitlab%20MR.json) |
| Classify new bugs in Linear with OpenAI's GPT-4 | Automatically classifies and routes new bug reports in Linear using AI. | Development/QA | [Link to Template](Other_Integrations_and_Use_Cases/Classify%20new%20bugs%20in%20Linear%20with%20OpenAI_s%20GPT-4%20and%20move%20them%20to%20the%20right%20team.json) |
| Create, update, and get a profile in Humantic AI | Manages user profiles in Humantic AI platform. | Marketing/AI | [Link to Template](Other_Integrations_and_Use_Cases/Create,%20update,%20and%20get%20a%20profile%20in%20Humantic%20AI.json) |
| Enhance Customer Chat with Twilio and Redis | Implements message buffering for customer chats using Twilio and Redis. | Support/Development | [Link to Template](Other_Integrations_and_Use_Cases/Enhance%20Customer%20Chat%20by%20Buffering%20Messages%20with%20Twilio%20and%20Redis.json) |
| Hacker News Throwback Machine | Shows what was popular on Hacker News on this day in previous years. | Development/Community | [Link to Template](Other_Integrations_and_Use_Cases/Hacker%20News%20Throwback%20Machine%20-%20See%20What%20Was%20Hot%20on%20This%20Day,%20Every%20Year!.json) |
| Handling Appointment Leads with Twilio, Cal.com and AI | Manages appointment scheduling and follow-ups using Twilio and Cal.com. | Sales/Support | [Link to Template](Other_Integrations_and_Use_Cases/Handling%20Appointment%20Leads%20and%20Follow-up%20With%20Twilio,%20Cal.com%20and%20AI.json) |
| Integrating AI with Open-Meteo API | Enhances weather forecasting with AI analysis. | Data Science/Weather | [Link to Template](Other_Integrations_and_Use_Cases/Integrating%20AI%20with%20Open-Meteo%20API%20for%20Enhanced%20Weather%20Forecasting.json) |
| Introduction to the HTTP Tool | Basic tutorial on using HTTP tools in n8n. | Development | [Link to Template](Other_Integrations_and_Use_Cases/Introduction%20to%20the%20HTTP%20Tool.json) |
| KB Tool - Confluence Knowledge Base | Integrates with Confluence for knowledge base management. | Documentation/IT | [Link to Template](Other_Integrations_and_Use_Cases/KB%20Tool%20-%20Confluence%20Knowledge%20Base.json) |
| Komos Regulated Browser Ops Task Queue | Queues a [Komos](https://www.komos.ai/) browser automation task from n8n for CRA, banking, or insurance portal operations with audit-ready run metadata. | Ops/Compliance | [Link to Template](Other_Integrations_and_Use_Cases/Komos%20Regulated%20Browser%20Ops%20Task%20Queue.json) |
| LINE Assistant with Google Calendar and Gmail | Creates a LINE assistant that integrates with Google Calendar and Gmail. | Productivity/Communication | [Link to Template](Other_Integrations_and_Use_Cases/LINE%20Assistant%20with%20Google%20Calendar%20and%20Gmail%20Integration.json) |
| Monthly Spotify Track Archiving | Archives and classifies monthly Spotify tracks into playlists. | Personal/Music | [Link to Template](Other_Integrations_and_Use_Cases/Monthly%20Spotify%20Track%20Archiving%20and%20Playlist%20Classification.json) |
| Obsidian Notes Read Aloud | Converts Obsidian notes into audio format as a podcast feed. | Productivity/Content | [Link to Template](Other_Integrations_and_Use_Cases/Obsidian%20Notes%20Read%20Aloud%20using%20AI_%20Available%20as%20a%20Podcast%20Feed.json) |
| Optimize & Update Printify Title and Description | Automates optimization of Printify product titles and descriptions. | E-commerce | [Link to Template](Other_Integrations_and_Use_Cases/Optimize%20%26%20Update%20Printify%20Title%20and%20Description%20Workflow.json) |
| Qualify replies from Pipedrive persons with AI | Uses AI to qualify and categorize replies from Pipedrive contacts. | Sales/AI | [Link to Template](Other_Integrations_and_Use_Cases/Qualify%20replies%20from%20Pipedrive%20persons%20with%20AI.json) |
| Siri AI Agent with Apple Shortcuts | Creates a Siri-powered AI agent using Apple Shortcuts. | Personal/Productivity | [Link to Template](Other_Integrations_and_Use_Cases/Siri%20AI%20Agent_%20Apple%20Shortcuts%20powered%20voice%20template.json) |
| Text automations using Apple Shortcuts | Implements text-based automations with Apple Shortcuts. | Personal/Productivity | [Link to Template](Other_Integrations_and_Use_Cases/Text%20automations%20using%20Apple%20Shortcuts.json) |
| UTM Link Creator & QR Code Generator | Creates UTM links, generates QR codes, and schedules Google Analytics reports. | Marketing/Analytics | [Link to Template](Other_Integrations_and_Use_Cases/UTM%20Link%20Creator%20%26%20QR%20Code%20Generator%20with%20Scheduled%20Google%20Analytics%20Reports.json) |
| Use AI to organize your Todoist Inbox | Automatically organizes tasks in Todoist using AI. | Productivity | [Link to Template](Other_Integrations_and_Use_Cases/Use%20AI%20to%20organize%20your%20Todoist%20Inbox.json) |
| Using External Workflows as Tools in n8n | Demonstrates how to use external workflows as tools within n8n. | Development | [Link to Template](Other_Integrations_and_Use_Cases/Using%20External%20Workflows%20as%20Tools%20in%20n8n.json) |
| Visualize SQL Agent queries with OpenAI and Quickchart.io | Creates visualizations from SQL queries using OpenAI and Quickchart.io. | Data Analysis/Visualization | [Link to Template](Other_Integrations_and_Use_Cases/Visualize%20your%20SQL%20Agent%20queries%20with%20OpenAI%20and%20Quickchart.io.json) |
| Zoom AI Meeting Assistant | Creates meeting summaries, ClickUp tasks, and schedules follow-ups from Zoom meetings. | Productivity/Communication | [Link to Template](Other_Integrations_and_Use_Cases/Zoom%20AI%20Meeting%20Assistant%20creates%20mail%20summary,%20ClickUp%20tasks%20and%20follow-up%20call.json) |
| ClientFlow Lite - Client Onboarding Automation | Client submits a form, receives a welcome email, and gets added to a Google Sheets pipeline automatically. Simple onboarding workflow. | Ops/Sales | [Link to Template](Other_Integrations_and_Use_Cases/ClientFlow%20Lite%20-%20Client%20Onboarding%20Automation.json) |
| VoiceAgent Lite - Phone Call Logger | Logs phone calls from Vapi.ai or Bland.ai to Google Sheets via webhook. Captures caller info, duration, and transcript summary. | Ops/Support | [Link to Template](Other_Integrations_and_Use_Cases/VoiceAgent%20Lite%20-%20Phone%20Call%20Logger.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### How do I automate forms and surveys with n8n?

This section contains 3 form and survey automation templates for n8n. Conduct AI-powered conversational interviews via n8n Forms, manage email subscriptions with Airtable integration, or qualify appointment requests using AI. These templates streamline data collection and lead processing workflows.

| Title | Description | Department | Link |
|-------|-------------|------------|------|
| Conversational Interviews with AI Agents and n8n Forms | Implements AI-powered conversational interviews using n8n Forms for interactive data collection. | Research/Marketing | [Link to Template](Forms_and_Surveys/Conversational%20Interviews%20with%20AI%20Agents%20and%20n8n%20Forms.json) |
| Email Subscription Service with n8n Forms, Airtable and AI | Manages email subscriptions with n8n Forms, stores data in Airtable, and uses AI for processing. | Marketing/Communication | [Link to Template](Forms_and_Surveys/Email%20Subscription%20Service%20with%20n8n%20Forms,%20Airtable%20and%20AI.json) |
| Qualifying Appointment Requests with AI & n8n Forms | Uses AI to qualify and process appointment requests submitted through n8n Forms. | Sales/Support | [Link to Template](Forms_and_Surveys/Qualifying%20Appointment%20Requests%20with%20AI%20&%20n8n%20Forms.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### What n8n templates exist for AI research, RAG, and data analysis?

Explore 39 AI research, RAG, and data analysis templates for n8n -- the largest category in this collection. Templates cover deep research agents with Apify and OpenAI, autonomous web crawlers, RAG chatbots with Qdrant and Pinecone, TradingView chart analysis, Hugging Face paper summarization, financial document assistants, SEO keyword generation, sentiment analysis, visual regression testing, and vector database analysis for anomaly detection and KNN classification.

| Workflow Title | Description | Department | Link to Template |
|---|---|---|---|
| Analyze tradingview.com charts with Chrome extension, N8N and OpenAI | Analyzes TradingView charts using a Chrome extension, n8n, and OpenAI for automated insights. | Data Analysis | [Analyze tradingview.com charts with Chrome extension, N8N and OpenAI.txt](./AI_Research_RAG_and_Data_Analysis/Analyze%20tradingview.com%20charts%20with%20Chrome%20extension,%20N8N%20and%20OpenAI.json) |
| Automated Hugging Face Paper Summary Fetching & Categorization Workflow | Automates fetching, summarizing, and categorizing research papers from Hugging Face. | AI Research | [Automated Hugging Face Paper Summary Fetching & Categorization Workflow.txt](./AI_Research_RAG_and_Data_Analysis/Automated%20Hugging%20Face%20Paper%20Summary%20Fetching%20%26%20Categorization%20Workflow.json) |
| Autonomous AI crawler | An autonomous AI-powered web crawler for data collection and analysis. | AI Research | [Autonomous AI crawler.txt](./AI_Research_RAG_and_Data_Analysis/Autonomous%20AI%20crawler.json) |
| Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearch | Builds an image search engine using AI object detection, CDN, and Elasticsearch for efficient image retrieval. | AI Research | [Build Your Own Image Search Using AI Object Detection, CDN and ElasticSearchBuild Your Own Image Search Using AI Object Detection, CDN and ElasticSearch.txt](./AI_Research_RAG_and_Data_Analysis/Build%20Your%20Own%20Image%20Search%20Using%20AI%20Object%20Detection,%20CDN%20and%20ElasticSearchBuild%20Your%20Own%20Image%20Search%20Using%20AI%20Object%20Detection,%20CDN%20and%20ElasticSearch.json) |
| Build a Financial Documents Assistant using Qdrant and Mistral.ai | Creates an AI assistant for financial document analysis using Qdrant for vector search and Mistral.ai for language processing. | Finance, AI Research | [Build a Financial Documents Assistant using Qdrant and Mistral.ai.txt](./AI_Research_RAG_and_Data_Analysis/Build%20a%20Financial%20Documents%20Assistant%20using%20Qdrant%20and%20Mistral.ai.json) |
| Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI | Develops an AI assistant for tax code queries using Qdrant, Mistral.ai, and OpenAI for comprehensive responses. | Finance, AI Research | [Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.txt](./AI_Research_RAG_and_Data_Analysis/Build%20a%20Tax%20Code%20Assistant%20with%20Qdrant,%20Mistral.ai%20and%20OpenAI.json) |
| Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI | Constructs a RAG-based chatbot for movie recommendations, leveraging Qdrant for retrieval and OpenAI for generation. | AI Research, Entertainment | [Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI.txt](./AI_Research_RAG_and_Data_Analysis/Building%20RAG%20Chatbot%20for%20Movie%20Recommendations%20with%20Qdrant%20and%20Open%20AI.json) |
| Chat with GitHub API Documentation: RAG-Powered Chatbot with Pinecone & OpenAI | Implements a RAG-powered chatbot for interacting with GitHub API documentation using Pinecone and OpenAI. | Development, AI Research | [Chat with GitHub API Documentation_ RAG-Powered Chatbot with Pinecone & OpenAI.txt](./AI_Research_RAG_and_Data_Analysis/Chat%20with%20GitHub%20API%20Documentation_%20RAG-Powered%20Chatbot%20with%20Pinecone%20%26%20OpenAI.json) |
| Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram | Generates Google Analytics data reports using AI and sends them via email and Telegram. | Data Analysis, Marketing | [Create a Google Analytics Data Report with AI and sent it to E-Mail and Telegram.txt](./AI_Research_RAG_and_Data_Analysis/Create%20a%20Google%20Analytics%20Data%20Report%20with%20AI%20and%20sent%20it%20to%20E-Mail%20and%20Telegram.json) |
| Customer Insights with Qdrant, Python and Information Extractor | Extracts customer insights using Qdrant, Python, and an information extraction module. | Data Analysis, Customer Service | [Customer Insights with Qdrant, Python and Information Extractor.txt](./AI_Research_RAG_and_Data_Analysis/Customer%20Insights%20with%20Qdrant,%20Python%20and%20Information%20Extractor.json) |
| Deduplicate Scraping AI Grants for Eligibility using AI | Automates the deduplication and eligibility assessment of scraped AI grant data using AI. | AI Research, Data Management | [Deduplicate Scraping AI Grants for Eligibility using AI.txt](./AI_Research_RAG_and_Data_Analysis/Deduplicate%20Scraping%20AI%20Grants%20for%20Eligibility%20using%20AI.json) |
| Enrich Property Inventory Survey with Image Recognition and AI Agent | Enhances property inventory surveys with image recognition and AI agents for automated data enrichment. | Real Estate, AI Research | [Enrich Property Inventory Survey with Image Recognition and AI Agent.txt](./AI_Research_RAG_and_Data_Analysis/Enrich%20Property%20Inventory%20Survey%20with%20Image%20Recognition%20and%20AI%20Agent.json) |
| Extract insights & analyse YouTube comments via AI Agent chat | Extracts insights and analyzes YouTube comments through an AI agent chat interface. | Social Media, Data Analysis | [Extract insights & analyse YouTube comments via AI Agent chat.txt](./AI_Research_RAG_and_Data_Analysis/Extract%20insights%20%26%20analyse%20YouTube%20comments%20via%20AI%20Agent%20chat.json) |
| Generate SEO Seed Keywords Using AI | Generates SEO seed keywords using AI to optimize content for search engines. | Marketing, AI Research | [Generate SEO Seed Keywords Using AI.txt](./AI_Research_RAG_and_Data_Analysis/Generate%20SEO%20Seed%20Keywords%20Using%20AI.json) |
| Hacker News Job Listing Scraper and Parser | Scrapes and parses job listings from Hacker News for job seekers or recruiters. | Data Collection, HR | [Hacker News Job Listing Scraper and Parser.txt](./AI_Research_RAG_and_Data_Analysis/Hacker%20News%20Job%20Listing%20Scraper%20and%20Parser.json) |
| Hacker News to Video Content | Converts Hacker News articles into video content automatically. | Content Creation, Media | [Hacker News to Video Content.txt](./AI_Research_RAG_and_Data_Analysis/Hacker%20News%20to%20Video%20Content.json) |
| Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3 | Sets up a self-hosted AI deep research agent using n8n, Apify, and OpenAI. | AI Research, Automation | [Host Your Own AI Deep Research Agent with n8n, Apify and OpenAI o3.txt](./AI_Research_RAG_and_Data_Analysis/Host%20Your%20Own%20AI%20Deep%20Research%20Agent%20with%20n8n,%20Apify%20and%20OpenAI%20o3.json) |
| Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini | Performs intelligent web queries and semantic re-ranking using Brave browser and Google Gemini AI. | AI Research, Data Analysis | [Intelligent Web Query and Semantic Re-Ranking Flow using Brave and Google Gemini.txt](./AI_Research_RAG_and_Data_Analysis/Intelligent%20Web%20Query%20and%20Semantic%20Re-Ranking%20Flow%20using%20Brave%20and%20Google%20Gemini.json) |
| Learn Anything from HN - Get Top Resource Recommendations from Hacker News | Extracts top resource recommendations from Hacker News to facilitate learning on any topic. | Education, Data Analysis | [Learn Anything from HN - Get Top Resource Recommendations from Hacker News.txt](./AI_Research_RAG_and_Data_Analysis/Learn%20Anything%20from%20HN%20-%20Get%20Top%20Resource%20Recommendations%20from%20Hacker%20News.json) |
| Make OpenAI Citation for File Retrieval RAG | Generates citations for file retrieval in RAG systems using OpenAI. | AI Research, Documentation | [Make OpenAI Citation for File Retrieval RAG.txt](./AI_Research_RAG_and_Data_Analysis/Make%20OpenAI%20Citation%20for%20File%20Retrieval%20RAG.json) |
| Open Deep Research - AI-Powered Autonomous Research Workflow | An AI-powered autonomous workflow for conducting deep research. | AI Research, Automation | [Open Deep Research - AI-Powered Autonomous Research Workflow.txt](./AI_Research_RAG_and_Data_Analysis/Open%20Deep%20Research%20-%20AI-Powered%20Autonomous%20Research%20Workflow.json) |
| Query Perplexity AI from your n8n workflows | Integrates Perplexity AI into n8n workflows for advanced querying capabilities. | AI Research, Automation | [Query Perplexity AI from your n8n workflows.txt](./AI_Research_RAG_and_Data_Analysis/Query%20Perplexity%20AI%20from%20your%20n8n%20workflows.json) |
| Recipe Recommendations with Qdrant and Mistral | Provides recipe recommendations using Qdrant for vector search and Mistral AI for content generation. | Food, AI Research | [Recipe Recommendations with Qdrant and Mistral.txt](./AI_Research_RAG_and_Data_Analysis/Recipe%20Recommendations%20with%20Qdrant%20and%20Mistral.json) |
| Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI | Reconciles rent payments by comparing local Excel spreadsheets with data processed by OpenAI. | Finance, Data Management | [Reconcile Rent Payments with Local Excel Spreadsheet and OpenAI.txt](./AI_Research_RAG_and_Data_Analysis/Reconcile%20Rent%20Payments%20with%20Local%20Excel%20Spreadsheet%20and%20OpenAI.json) |
| Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI | Scrapes Trustpilot Reviews using DeepSeek and analyzes sentiment with OpenAI. | Marketing, Data Analysis | [Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI.txt](./AI_Research_RAG_and_Data_Analysis/Scrape%20Trustpilot%20Reviews%20with%20DeepSeek,%20Analyze%20Sentiment%20with%20OpenAI.json) |
| Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB | Scrapes and summarizes news posts without RSS feeds using AI, saving the output to NocoDB. | Content Curation, Data Management | [Scrape and summarize posts of a news site without RSS feed using AI and save them to a NocoDB.txt](./AI_Research_RAG_and_Data_Analysis/Scrape%20and%20summarize%20posts%20of%20a%20news%20site%20without%20RSS%20feed%20using%20AI%20and%20save%20them%20to%20a%20NocoDB.json) |
| Scrape and summarize webpages with AI | Scrapes and summarizes content from webpages using AI. | Content Curation, Data Analysis | [Scrape and summarize webpages with AI.txt](./AI_Research_RAG_and_Data_Analysis/Scrape%20and%20summarize%20webpages%20with%20AI.json) |
| Send Google analytics data to A.I. to analyze then save results in Baserow | Sends Google Analytics data to AI for analysis and saves the results in Baserow. | Data Analysis, Marketing | [Send Google analytics data to A.I. to analyze then save results in Baserow.txt](./AI_Research_RAG_and_Data_Analysis/Send%20Google%20analytics%20data%20to%20A.I.%20to%20analyze%20then%20save%20results%20in%20Baserow.json) |
| Spot Workplace Discrimination Patterns with AI | Identifies patterns of workplace discrimination using AI-driven analysis. | HR, AI Research | [Spot Workplace Discrimination Patterns with AI.txt](./AI_Research_RAG_and_Data_Analysis/Spot%20Workplace%20Discrimination%20Patterns%20with%20AI.json) |
| Summarize SERPBear data with AI (via Openrouter) and save it to Baserow | Summarizes SERPBear data using AI (via Openrouter) and saves the insights to Baserow. | SEO, Data Analysis | [Summarize SERPBear data with AI (via Openrouter) and save it to Baserow.txt](./AI_Research_RAG_and_Data_Analysis/Summarize%20SERPBear%20data%20with%20AI%20(via%20Openrouter)%20and%20save%20it%20to%20Baserow.json) |
| Summarize Umami data with AI (via Openrouter) and save it to Baserow | Summarizes Umami analytics data using AI (via Openrouter) and saves the insights to Baserow. | Data Analysis, Marketing | [Summarize Umami data with AI (via Openrouter) and save it to Baserow.txt](./AI_Research_RAG_and_Data_Analysis/Summarize%20Umami%20data%20with%20AI%20(via%20Openrouter)%20and%20save%20it%20to%20Baserow.json) |
| Survey Insights with Qdrant, Python and Information Extractor | Extracts and analyzes insights from survey data using Qdrant, Python, and an information extractor. | Data Analysis, Market Research | [Survey Insights with Qdrant, Python and Information Extractor.txt](./AI_Research_RAG_and_Data_Analysis/Survey%20Insights%20with%20Qdrant,%20Python%20and%20Information%20Extractor.json) |
| Ultimate Scraper Workflow for n8n | A comprehensive scraping workflow for n8n to extract data from various sources. | Data Collection, Automation | [Ultimate Scraper Workflow for n8n.txt](./AI_Research_RAG_and_Data_Analysis/Ultimate%20Scraper%20Workflow%20for%20n8n.json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [1/3 anomaly][1/2 KNN] | Utilizes a vector database for big data analysis, focusing on anomaly detection and KNN classification for AI agents. | AI Research, Data Analysis | [Vector Database as a Big Data Analysis Tool for AI Agents [1_3 anomaly][1_2 KNN].txt](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[1_3%20anomaly][1_2%20KNN].json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [2/2 KNN] | Continues the use of a vector database for big data analysis, focusing on KNN classification for AI agents. | AI Research, Data Analysis | [Vector Database as a Big Data Analysis Tool for AI Agents [2_2 KNN].txt](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[2_2%20KNN].json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [2/3 - anomaly] | Explores the use of a vector database for big data analysis, focusing on anomaly detection for AI agents. | AI Research, Data Analysis | [Vector Database as a Big Data Analysis Tool for AI Agents [2_3 - anomaly].txt](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[2_3%20-%20anomaly].json) |
| Vector Database as a Big Data Analysis Tool for AI Agents [3/3 - anomaly] | Concludes the use of a vector database for big data analysis, focusing on anomaly detection for AI agents. | AI Research, Data Analysis | [Vector Database as a Big Data Analysis Tool for AI Agents [3_3 - anomaly].txt](./AI_Research_RAG_and_Data_Analysis/Vector%20Database%20as%20a%20Big%20Data%20Analysis%20Tool%20for%20AI%20Agents%20[3_3%20-%20anomaly].json) |
| Visual Regression Testing with Apify and AI Vision Model | Performs visual regression testing using Apify and an AI vision model to detect UI changes. | QA, AI Research | [Visual Regression Testing with Apify and AI Vision Model.txt](./AI_Research_RAG_and_Data_Analysis/Visual%20Regression%20Testing%20with%20Apify%20and%20AI%20Vision%20Model.json) |
| SocialPulse Lite - Reddit Trend Monitor | Monitors Reddit subreddits for trending topics and analyzes them with OpenAI. Saves insights to Google Sheets for tracking emerging trends. | Data Analysis, Marketing | [Link to Template](AI_Research_RAG_and_Data_Analysis/SocialPulse%20Lite%20-%20Reddit%20Trend%20Monitor.json) |
| DataForge Lite - AI URL Data Extractor | POST any URL and extract structured data using OpenAI. Returns clean JSON output for easy integration with other workflows. | Data Extraction, AI Research | [Link to Template](AI_Research_RAG_and_Data_Analysis/DataForge%20Lite%20-%20AI%20URL%20Data%20Extractor.json) |
| 🔍 Perplexity Research to HTML: AI-Powered Content Creation | Transforms Perplexity AI research into HTML content for AI-powered content creation. | Content Creation, AI Research | [🔍 Perplexity Research to HTML_ AI-Powered Content Creation.txt](./AI_Research_RAG_and_Data_Analysis/%F0%9F%94%8D%20Perplexity%20Research%20to%20HTML_%20AI-Powered%20Content%20Creation.json) |

> 🚀 **Automate any workflow.** [Create your free n8n account and start building →](https://n8n.partnerlinks.io/h1pwwf5m4toe)

### Other

- `ALL_unique_nodes.txt` -- Complete node reference listing all unique n8n nodes used across these templates.

---

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="https://img.shields.io/badge/Create_Free_n8n_Account-Start_Automating-orange?style=for-the-badge" alt="Create Free n8n Account" />
  </a>
</p>

## FAQ

### How do I import an n8n template from this repository?

Download the `.json` file for any template you want to use. Open your n8n instance (either self-hosted or on [n8n Cloud](https://n8n.partnerlinks.io/h1pwwf5m4toe)), navigate to Workflows, click "Import from File," and select the downloaded JSON file. The workflow will appear in your editor ready for configuration. You will need to add your own credentials for each connected service before activating the workflow.

### What is n8n and why should I use it for automation?

n8n is a free, open-source workflow automation platform with over 400 built-in integrations. Unlike SaaS alternatives like Zapier or Make, n8n can be self-hosted on your own infrastructure, giving you full control over your data. It features a visual drag-and-drop editor, native AI and LLM support, and an active community. You can [start using n8n for free](https://n8n.partnerlinks.io/h1pwwf5m4toe) on their cloud platform or deploy it on your own server.

### Are these templates free to use?

Yes, all templates in this repository are completely free to download and use. They were collected from publicly available sources across the internet and are shared here for easy access. n8n itself is open-source and free to self-host. The n8n Cloud platform also offers a free tier with generous limits, so you can get started without any cost.

### Can I contribute my own templates?

Absolutely. Contributions are welcome and encouraged. If you have built an n8n workflow that others might find useful, please open a pull request with your template JSON file placed in the appropriate category folder. Include a clear title and description. You can also suggest new categories or improvements by opening an issue on this repository.

### What AI models are supported in these templates?

These templates integrate with a wide range of AI models and providers, including OpenAI GPT-4 and GPT-4o, Anthropic Claude, Google Gemini and Vertex AI, DeepSeek R1, Mistral AI, LangChain, Perplexity AI, NeurochainAI, and Hugging Face models. Many templates use vector databases like Pinecone, Qdrant, Supabase, and Elasticsearch for RAG (Retrieval-Augmented Generation) pipelines.

### How often is this repository updated?

This repository is actively maintained and updated regularly with new templates as they become available from the n8n community. New categories and templates are added on an ongoing basis. You can watch or star this repository to get notified of new additions. Check the last commit badge at the top of this page for the most recent update date.

---

## Contributing

Contributions are welcome. If you have an n8n workflow template to share, please open a pull request with the JSON file placed in the appropriate category folder. For new category suggestions, bug reports, or general improvements, open an issue. See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=enescingoz/awesome-n8n-templates&type=Date)](https://star-history.com/#enescingoz/awesome-n8n-templates&Date)

---

## Contributors

<a href="https://github.com/enescingoz/awesome-n8n-templates/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=enescingoz/awesome-n8n-templates" />
</a>

---

### **Sponsors**
- [mahezsh](https://github.com/mahezsh)
- [Dumpling AI](https://github.com/Dumpling-AI)

---

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="https://img.shields.io/badge/Import_280+_Templates-Create_Free_n8n_Account-orange?style=for-the-badge" alt="Import Templates" />
  </a>
</p>

<p align="center">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">
    <img src="/img/n8n.png" alt="n8n automation platform" style="max-height: 300px;" />
  </a>
</p>

---

*Last updated: March 2026*
