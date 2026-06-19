<div align="center">

# AI Agent Portfolio

### Built by Aravind Kumar Nalukurthi

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aravind-kumar-nalukurthi-45b2a41b2/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-7C3AED?style=for-the-badge&logo=github&logoColor=white)](https://data-geek-astronomy.github.io/-portfolio-website/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/data-geek-astronomy)
[![Email](https://img.shields.io/badge/Email-Contact-06B6D4?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aravind.kumar.nalukurthi@gmail.com)
[![Location](https://img.shields.io/badge/San_Francisco-California-22C55E?style=for-the-badge&logo=googlemaps&logoColor=white)]()

![status](https://img.shields.io/badge/status-live%20on%20n8n%20cloud-brightgreen)
![agents](https://img.shields.io/badge/agents-9-6366F1)
![powered by](https://img.shields.io/badge/powered%20by-GPT--4o-blueviolet)
![built with](https://img.shields.io/badge/built%20with-n8n-orange)

</div>

---

## What This Is

I build AI agents that do the work humans shouldn't have to.

This portfolio shows 9 production-grade workflow agents built on **n8n** and **GPT-4o**, each one solving a real operational problem in an industry where AI still feels new. These are not demos or tutorials. Every agent runs live in the cloud, handles real data, and replaces hours of manual work every week.

The industries I focused on — healthcare, transportation, and construction — are exactly the places where AI has the most room to make a difference and where most teams are still doing things by hand.

---

## The Agents

### Healthcare

| Agent | What It Does | Trigger | Live Link |
|-------|-------------|---------|-----------|
| **HC-1** Patient Discharge & Care Continuity | Fires when a patient is discharged from hospital. GPT-4o scores their readmission risk and routes high-risk cases to the physician with a Slack alert — before the patient reaches home. | Webhook | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/sTOHb8MdKbJ1w8tS) |
| **HC-2** Insurance Prior Authorization | Takes an incoming auth request, checks insurance eligibility, evaluates medical necessity with GPT-4o, and submits to the payer automatically. Eligible requests go from submission to confirmation in under 30 seconds. | Webhook | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/PcioiEXandyi4DhB) |
| **HC-3** Clinical Trial Recruitment | Runs every morning and screens every active patient against clinical trial criteria using GPT-4o. Eligible patients get a personalized outreach email the same day. What used to take weeks of manual chart review now happens overnight. | Daily Schedule | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/jnaNp7WZAlQw6v8o) |

### Transportation

| Agent | What It Does | Trigger | Live Link |
|-------|-------------|---------|-----------|
| **TR-4** Fleet Predictive Maintenance | Pulls live telematics data every hour for every vehicle in the fleet. GPT-4o reads the sensor readings and fault codes, flags anything that looks like an upcoming failure, and schedules service automatically before the truck breaks down on the road. | Hourly Schedule | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/WXXRgxylUgXEykTx) |
| **TR-5** Dynamic Route Optimization | Monitors every active delivery every 15 minutes against live traffic and weather. When GPT-4o detects a significant delay, it suggests the best alternate route, updates the driver, and notifies the customer before they start calling in. | 15-Min Schedule | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/Z1WNtgrFm3DesCmj) |
| **TR-6** Freight Exception Management | Checks every in-transit shipment with an exception every hour. GPT-4o classifies the severity as critical, standard, or low. Critical cases get a case opened and the account manager alerted within the same hour. High-value shipments never sit in an unread queue. | Hourly Schedule | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/trGcBqL5lylqqmjF) |

### Construction

| Agent | What It Does | Trigger | Live Link |
|-------|-------------|---------|-----------|
| **C-7** Site Safety & OSHA Reporting | Reads each day's site inspection reports and checks every violation against OSHA's 29 CFR 1926 Construction Standards using GPT-4o. Files the right incident form automatically and sends the project manager a corrective action plan. Missed OSHA deadlines cost up to $15,625 per violation. | Daily Schedule | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/yV1moFLC09gC4g6C) |
| **C-8** Subcontractor Invoice Reconciliation | Pulls every pending invoice, fetches the matching contract Schedule of Values, and asks GPT-4o to verify every line item, retainage calculation, and compliance document. Overbilling gets caught before payment goes out. The process goes from days to hours. | Weekly Schedule | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/lQhFarz4A38f2flj) |
| **C-9** Material Procurement & Supply Forecasting | Runs every morning, cross-references upcoming material needs against current inventory and supplier lead times with GPT-4o, and creates purchase orders automatically when a shortage is detected. Material gaps get caught 5 to 10 days before they stop work on site. | Daily Schedule | [Open in n8n](https://aravind5.app.n8n.cloud/workflow/aby1Dzm36hwcWkHM) |

---

## How Each Agent Works

Every agent follows the same general pattern:

```
Trigger (Webhook or Schedule)
        |
  Fetch Data from Source System
        |
  Split into Batches (for bulk processing)
        |
  GPT-4o Makes the Decision
        |
  Route Based on Result
  /               \
Critical         Routine
  |                 |
Alert Team       Log and Continue
```

The key step is the GPT-4o node. Instead of writing hundreds of rules and if/else conditions, I give the AI the context it needs (the data, the business rules, the desired output format) and let it make the call. The structured output parser then converts the AI response into clean fields that downstream nodes can act on.

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Workflow Orchestration | n8n Cloud |
| AI Decision Engine | OpenAI GPT-4o via LangChain Agent node |
| Structured Output | n8n Structured Output Parser |
| Notifications | Gmail v2.2, Slack v2.5 |
| API Integrations | HTTP Request node v4.4 with placeholder endpoints |
| Portfolio UI | Streamlit + custom CSS |
| Hosting | n8n Cloud + Streamlit Community Cloud |

---

## Domain Repositories

Each domain has its own repo with the workflow JSON files and a domain-specific README:

- [n8n-healthcare](https://github.com/data-geek-astronomy/n8n-healthcare) — HC-1, HC-2, HC-3
- [n8n-transportation](https://github.com/data-geek-astronomy/n8n-transportation) — TR-4, TR-5, TR-6
- [n8n-construction](https://github.com/data-geek-astronomy/n8n-construction) — C-7, C-8, C-9
- [n8n-ai-agents](https://github.com/data-geek-astronomy/n8n-ai-agents) — all 9 agents combined

---

## Run This Portfolio App Locally

```bash
git clone https://github.com/data-geek-astronomy/ai-agent-portfolio.git
cd ai-agent-portfolio
pip install streamlit
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## Deploy Your Own Copy

This app deploys in under 2 minutes on Streamlit Community Cloud:

1. Fork this repo to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **New app** and select your fork
4. Set **Main file path** to `app.py`
5. Click **Deploy**

---

## About Me

I'm an AI Engineer based in San Francisco focused on building workflow automation that works in the real world. I specialize in industries where AI adoption is still early — healthcare, logistics, construction — because that's where the manual work is heaviest and the wins from automation are the biggest.

If you're a company with a repetitive operational process that your team is doing by hand, I build the agent that takes it off their plate.

**Get in touch:**
- Email: [aravind.kumar.nalukurthi@gmail.com](mailto:aravind.kumar.nalukurthi@gmail.com)
- LinkedIn: [linkedin.com/in/aravind-kumar-nalukurthi-45b2a41b2](https://www.linkedin.com/in/aravind-kumar-nalukurthi-45b2a41b2/)
- Phone: 480.931.1899
- Portfolio: [data-geek-astronomy.github.io/-portfolio-website](https://data-geek-astronomy.github.io/-portfolio-website/)

---

<div align="center">
Built with n8n + GPT-4o &nbsp;·&nbsp; San Francisco, California
</div>
