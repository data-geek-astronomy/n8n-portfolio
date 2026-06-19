import streamlit as st

# ─── PAGE CONFIG ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="n8n AI Agent Portfolio | Aravind Kumar",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── GLOBAL CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
    background-color: #0A0F1E !important;
    font-family: 'Inter', -apple-system, sans-serif;
    color: #E2E8F0;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }
.stDecoration { display: none; }
[data-testid="stToolbar"] { display: none; }

/* Remove Streamlit default padding */
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

section[data-testid="stSidebar"] { display: none; }

/* ── Animated hero background ── */
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-8px); }
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.3); }
    50%       { box-shadow: 0 0 0 8px rgba(99, 102, 241, 0); }
}

/* ── Hero ── */
.hero-wrap {
    background: linear-gradient(135deg, #0A0F1E 0%, #0D1B3E 35%, #0F172A 65%, #0A0F1E 100%);
    background-size: 300% 300%;
    animation: gradientShift 12s ease infinite;
    padding: 72px 40px 56px;
    text-align: center;
    position: relative;
    overflow: hidden;
    border-bottom: 1px solid rgba(99,102,241,0.12);
}

.hero-wrap::before {
    content: '';
    position: absolute; inset: 0;
    background:
        radial-gradient(ellipse 60% 40% at 20% 20%, rgba(99,102,241,0.10) 0%, transparent 70%),
        radial-gradient(ellipse 50% 35% at 80% 80%, rgba(6,182,212,0.07) 0%, transparent 70%),
        radial-gradient(ellipse 40% 30% at 60% 10%, rgba(139,92,246,0.06) 0%, transparent 70%);
    pointer-events: none;
}

.hero-badge {
    display: inline-block;
    background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.35);
    color: #A5B4FC;
    padding: 5px 16px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 24px;
    animation: fadeInUp 0.6s ease both;
}

.hero-title {
    font-size: clamp(32px, 5vw, 68px);
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: 20px;
    background: linear-gradient(135deg, #FFFFFF 0%, #C7D2FE 40%, #67E8F9 75%, #A5F3FC 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: fadeInUp 0.6s ease 0.1s both;
    letter-spacing: -1px;
}

.hero-subtitle {
    font-size: 17px;
    color: #94A3B8;
    max-width: 560px;
    margin: 0 auto 48px;
    line-height: 1.75;
    font-weight: 400;
    animation: fadeInUp 0.6s ease 0.2s both;
}

.tech-badges {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 48px;
    animation: fadeInUp 0.6s ease 0.3s both;
}

.tech-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    color: #94A3B8;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 500;
    font-family: 'JetBrains Mono', monospace;
}

.tech-badge .dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #6366F1;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 0;
    animation: fadeInUp 0.6s ease 0.4s both;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    overflow: hidden;
    max-width: 540px;
    margin: 0 auto;
    background: rgba(255,255,255,0.02);
}

.stat-box {
    flex: 1;
    padding: 20px 16px;
    text-align: center;
    border-right: 1px solid rgba(255,255,255,0.07);
}

.stat-box:last-child { border-right: none; }

.stat-num {
    font-size: 32px;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 6px;
    display: block;
}

.stat-lbl {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #475569;
    display: block;
}

/* ── Streamlit Tabs Override ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid rgba(255,255,255,0.07) !important;
    padding: 0 40px !important;
    gap: 4px !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #64748B !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 16px 24px !important;
    border-radius: 0 !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    margin-bottom: -1px !important;
    transition: color 0.2s, border-color 0.2s !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #CBD5E1 !important;
    background: rgba(255,255,255,0.02) !important;
}

.stTabs [aria-selected="true"] {
    color: #E2E8F0 !important;
    border-bottom: 2px solid #6366F1 !important;
    background: transparent !important;
}

.stTabs [data-baseweb="tab-panel"] {
    background: transparent !important;
    padding: 0 !important;
}

.stTabs [data-baseweb="tab-highlight"] { display: none !important; }
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ── Domain Section Header ── */
.domain-header {
    padding: 48px 40px 0;
    animation: fadeInUp 0.4s ease both;
}

.domain-tag {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 4px;
    margin-bottom: 12px;
}

.domain-title {
    font-size: 28px;
    font-weight: 800;
    color: #F1F5F9;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}

.domain-desc {
    font-size: 14px;
    color: #64748B;
    line-height: 1.7;
    max-width: 680px;
    margin-bottom: 32px;
}

/* ── Agent Cards Grid ── */
.agents-row {
    padding: 0 40px 64px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    animation: fadeInUp 0.5s ease 0.1s both;
}

/* ── Agent Card ── */
.agent-card {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    display: flex;
    flex-direction: column;
}

.agent-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255,255,255,0.14);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

/* Card header per domain */
.card-header {
    padding: 22px 22px 20px;
    position: relative;
    overflow: hidden;
}

.card-header::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 1px;
    background: rgba(0,0,0,0.25);
}

/* Subtle grid pattern on card header */
.card-header::before {
    content: '';
    position: absolute; inset: 0;
    background-image: linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
    background-size: 20px 20px;
    pointer-events: none;
}

.card-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: 0.65;
    margin-bottom: 8px;
    position: relative;
}

.card-name {
    font-size: 17px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.3;
    margin-bottom: 14px;
    position: relative;
}

.trigger-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 11px;
    font-weight: 500;
    color: rgba(255,255,255,0.6);
    position: relative;
}

.trigger-dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #22C55E;
    animation: pulseGlow 2s ease infinite;
}

/* Card body */
.card-body {
    padding: 20px 22px;
    flex: 1;
    display: flex;
    flex-direction: column;
}

/* XYZ section */
.xyz-item {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 10px;
}

.xyz-label {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 3px 8px;
    border-radius: 4px;
    min-width: 64px;
    text-align: center;
    flex-shrink: 0;
    margin-top: 2px;
    font-family: 'JetBrains Mono', monospace;
}

.label-p { background: rgba(239,68,68,0.12);  color: #FCA5A5; border: 1px solid rgba(239,68,68,0.2); }
.label-b { background: rgba(99,102,241,0.12); color: #A5B4FC; border: 1px solid rgba(99,102,241,0.2); }
.label-s { background: rgba(34,197,94,0.12);  color: #86EFAC; border: 1px solid rgba(34,197,94,0.2); }

.xyz-text {
    font-size: 12.5px;
    color: #CBD5E1;
    line-height: 1.65;
    font-weight: 400;
}

/* Divider */
.card-divider {
    height: 1px;
    background: rgba(255,255,255,0.05);
    margin: 16px 0;
}

/* Workflow diagram */
.workflow-box {
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #64748B;
    line-height: 1.9;
    overflow-x: auto;
    white-space: pre;
}

/* Use cases */
.uc-title {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 10px;
    font-family: 'JetBrains Mono', monospace;
}

.uc-item {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin-bottom: 7px;
}

.uc-dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    margin-top: 6px;
    flex-shrink: 0;
}

.uc-text {
    font-size: 12px;
    color: #94A3B8;
    line-height: 1.55;
}

.uc-co { font-weight: 600; color: #CBD5E1; }

/* Metrics row */
.metrics-row {
    display: flex;
    gap: 8px;
    margin-top: auto;
    padding-top: 16px;
}

.metric-chip {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 11px;
    color: #64748B;
    font-family: 'JetBrains Mono', monospace;
    flex: 1;
    text-align: center;
}

.metric-chip span { display: block; }
.metric-val { color: #CBD5E1; font-weight: 600; font-size: 13px; }

/* n8n Link Button */
.n8n-btn {
    display: block;
    text-align: center;
    padding: 11px 20px;
    border-radius: 9px;
    font-size: 13px;
    font-weight: 600;
    text-decoration: none;
    margin-top: 14px;
    color: white;
    transition: opacity 0.2s, transform 0.15s;
    letter-spacing: 0.2px;
}

.n8n-btn:hover { opacity: 0.87; transform: translateY(-1px); }

/* ──── Domain Color Themes ──── */

/* Healthcare: Cyan + Teal */
.hc-header  { background: linear-gradient(135deg, #0C4A6E 0%, #134E4A 100%); }
.hc-id      { color: #67E8F9; }
.hc-tag     { background: rgba(6,182,212,0.12); color: #67E8F9; border: 1px solid rgba(6,182,212,0.25); }
.hc-title   { color: #67E8F9; }
.hc-dot     { background: #06B6D4; }
.hc-btn     { background: linear-gradient(135deg, #0369A1, #0F766E); }
.hc-stat    { color: #67E8F9; }

/* Transportation: Orange + Amber */
.tr-header  { background: linear-gradient(135deg, #7C2D12 0%, #78350F 100%); }
.tr-id      { color: #FDBA74; }
.tr-tag     { background: rgba(249,115,22,0.12); color: #FDBA74; border: 1px solid rgba(249,115,22,0.25); }
.tr-title   { color: #FDBA74; }
.tr-dot     { background: #F97316; }
.tr-btn     { background: linear-gradient(135deg, #C2410C, #B45309); }
.tr-stat    { color: #FDBA74; }

/* Construction: Yellow + Violet */
.cn-header  { background: linear-gradient(135deg, #3B1702 0%, #2E1065 100%); }
.cn-id      { color: #FDE68A; }
.cn-tag     { background: rgba(234,179,8,0.12); color: #FDE68A; border: 1px solid rgba(234,179,8,0.25); }
.cn-title   { color: #FDE68A; }
.cn-dot     { background: #EAB308; }
.cn-btn     { background: linear-gradient(135deg, #92400E, #5B21B6); }
.cn-stat    { color: #FDE68A; }

/* ── Footer ── */
.portfolio-footer {
    background: rgba(0,0,0,0.25);
    border-top: 1px solid rgba(255,255,255,0.05);
    padding: 40px;
    text-align: center;
}

.footer-repos {
    display: flex;
    justify-content: center;
    gap: 16px;
    margin-bottom: 24px;
    flex-wrap: wrap;
}

.repo-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 9px;
    padding: 9px 18px;
    font-size: 13px;
    font-weight: 500;
    color: #94A3B8;
    text-decoration: none;
    transition: all 0.2s;
}

.repo-link:hover {
    background: rgba(255,255,255,0.07);
    color: #E2E8F0;
    border-color: rgba(255,255,255,0.15);
}

.footer-credit {
    font-size: 13px;
    color: #475569;
}

.footer-credit a {
    color: #6366F1;
    text-decoration: none;
    font-weight: 500;
}

/* Responsive */
@media (max-width: 900px) {
    .agents-row { grid-template-columns: 1fr !important; }
    .hero-wrap { padding: 48px 20px 40px; }
    .domain-header { padding: 32px 20px 0; }
    .agents-row { padding: 0 20px 48px; }
    .stTabs [data-baseweb="tab-list"] { padding: 0 20px !important; }
}
</style>
""", unsafe_allow_html=True)


# ─── DATA ────────────────────────────────────────────────────────────────────

AGENTS = {
    "healthcare": [
        {
            "id": "HC-1",
            "name": "Patient Discharge & Care Continuity",
            "trigger": "Webhook",
            "trigger_label": "Live EHR Events",
            "nodes": 8,
            "saves": "14 hrs/week",
            "problem": "Hospitals have nurses manually reviewing hundreds of discharged patients every day. High risk patients slip through and end up back in the ER within 30 days.",
            "built": "An agent that fires the moment a patient is discharged, scores their readmission risk with GPT-4o, and routes the right alert to the right person immediately.",
            "solved": "High risk patients now get a physician callback within hours. The care team gets a Slack message with everything they need before the patient even reaches home.",
            "workflow": (
                "EHR Discharge Event\n"
                "       |\n"
                "  Normalize Payload\n"
                "       |\n"
                " GPT-4o Risk Scoring\n"
                "       |\n"
                "   Risk Router\n"
                "  /    |    \\\n"
                "High  Med   Low\n"
                " |           |\n"
                "Alert      Log\n"
                "MD+Slack  Care Plan"
            ),
            "companies": [
                ("Kaiser Permanente", "post-discharge cardiac patient follow ups"),
                ("HCA Healthcare", "CHF and COPD nurse callbacks on the same day"),
                ("Teladoc", "virtual follow up scheduling right at discharge"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/sTOHb8MdKbJ1w8tS",
        },
        {
            "id": "HC-2",
            "name": "Insurance Prior Authorization Automation",
            "trigger": "Webhook",
            "trigger_label": "Auth Requests",
            "nodes": 7,
            "saves": "18 hrs/week",
            "problem": "Doctors and admin staff spend over two hours daily filling out prior auth forms by hand. A patient needing surgery can wait two to three days just for paperwork.",
            "built": "An agent that checks insurance eligibility, evaluates medical necessity with GPT-4o against payer criteria, and submits approved requests automatically.",
            "solved": "Eligible prior auth requests go from submission to confirmation in under 30 seconds. If something is missing, the provider gets an email with exactly what to fix.",
            "workflow": (
                "Auth Request Webhook\n"
                "       |\n"
                " Check Eligibility\n"
                "       |\n"
                "GPT-4o Assessment\n"
                "       |\n"
                "  Criteria Met?\n"
                "  Yes        No\n"
                "   |          |\n"
                "Submit   Notify\n"
                "to Payer  Provider"
            ),
            "companies": [
                ("UnitedHealth Group", "millions of ortho and imaging prior auths yearly"),
                ("Aetna / CVS Health", "routine outpatient procedure review automation"),
                ("Epic Clinics", "trigger directly from Epic SmartForms"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/PcioiEXandyi4DhB",
        },
        {
            "id": "HC-3",
            "name": "Clinical Trial Recruitment & Screening",
            "trigger": "Schedule",
            "trigger_label": "Daily at 8am",
            "nodes": 9,
            "saves": "22 hrs/week",
            "problem": "Research teams at pharma companies spend weeks going through patient charts by hand. By the time they find candidates, enrollment windows have often already closed.",
            "built": "An agent that wakes up every morning, runs every patient through inclusion and exclusion criteria with GPT-4o, and sends personalized outreach emails the same day.",
            "solved": "Weeks of manual chart review now happens overnight. Research coordinators arrive each morning to a ready list of screened candidates with outreach already sent.",
            "workflow": (
                "  Daily 8am Trigger\n"
                "        |\n"
                " Fetch Active Patients\n"
                "        |\n"
                "  Split into Batches\n"
                "        |\n"
                "GPT-4o Trial Screening\n"
                "        |\n"
                " Eligible?  No\n"
                "     |       |\n"
                "  Email    Log\n"
                "Outreach   CRM"
            ),
            "companies": [
                ("Pfizer", "Phase III trial screening across partner clinics at scale"),
                ("Medidata / Veeva", "pipe screening results into CTMS platforms"),
                ("Johns Hopkins", "screen same patients across multiple concurrent trials"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/jnaNp7WZAlQw6v8o",
        },
    ],
    "transportation": [
        {
            "id": "TR-4",
            "name": "Fleet Predictive Maintenance",
            "trigger": "Schedule",
            "trigger_label": "Every Hour",
            "nodes": 8,
            "saves": "26 hrs/week",
            "problem": "Fleet operators find out about a truck problem when it breaks down on the side of the road. At that point a tow is needed and deliveries are already missed.",
            "built": "An agent that pulls live telematics data every hour for every vehicle, feeds sensor readings and fault codes into GPT-4o, and schedules service before a failure happens.",
            "solved": "Maintenance teams know about problems days before a breakdown. Service appointments get booked automatically and the fleet manager gets a Slack alert with repair details.",
            "workflow": (
                "  Hourly Trigger\n"
                "       |\n"
                " Fetch Fleet Telemetry\n"
                "       |\n"
                " Split into Batches\n"
                "       |\n"
                "GPT-4o DTC Analysis\n"
                "       |\n"
                " Maintenance Needed?\n"
                "  Yes          No\n"
                "   |            |\n"
                "Schedule    Log\n"
                "Service   Healthy\n"
                "+ Slack"
            ),
            "companies": [
                ("Ryder System", "235,000+ commercial vehicles monitored continuously"),
                ("Amazon Logistics", "last mile van health checks for same-day SLAs"),
                ("Werner Enterprises", "catch DTC codes early on long haul OTR routes"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/WXXRgxylUgXEykTx",
        },
        {
            "id": "TR-5",
            "name": "Dynamic Route Optimization & Exception",
            "trigger": "Schedule",
            "trigger_label": "Every 15 Min",
            "nodes": 9,
            "saves": "30 hrs/week",
            "problem": "When a storm hits, dispatchers at major carriers manually reroute drivers one by one. Customers have no idea a delivery is late until it just does not show up.",
            "built": "An agent that checks every active delivery every 15 minutes against live traffic and weather. GPT-4o suggests the best alternate route and notifies driver and customer.",
            "solved": "Drivers get new instructions before they hit congestion. Customers get a heads up with a revised arrival time before they start calling in. No manual dispatch needed.",
            "workflow": (
                "Every 15 Minutes\n"
                "       |\n"
                "Fetch Active Deliveries\n"
                "       |\n"
                "Split into Batches\n"
                "       |\n"
                "Fetch Traffic + Weather\n"
                "       |\n"
                "GPT-4o Delay Assessment\n"
                "       |\n"
                "Significant Delay?\n"
                " Yes          No\n"
                "  |            |\n"
                "Reroute    Log\n"
                "Driver + Customer OK"
            ),
            "companies": [
                ("UPS", "automated rerouting during peak season weather on I-95"),
                ("DoorDash / Instacart", "real-time ETA corrections for same-day delivery"),
                ("XPO Logistics", "proactive shipper notifications during LTL delays"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/Z1WNtgrFm3DesCmj",
        },
        {
            "id": "TR-6",
            "name": "Freight Exception & Carrier Resolution",
            "trigger": "Schedule",
            "trigger_label": "Every Hour",
            "nodes": 8,
            "saves": "20 hrs/week",
            "problem": "Freight brokers get dozens of shipment exception notifications every hour. By the time a high value shipment gets escalated, it is often too late to avoid a penalty.",
            "built": "An agent that checks every in-transit shipment with an exception, classifies severity with GPT-4o, opens a case, and alerts the account manager within the hour.",
            "solved": "High value shipments never sit in an unread queue. Account managers are looped in the same hour an exception is detected. Customers get updates before they have to ask.",
            "workflow": (
                "  Hourly Trigger\n"
                "        |\n"
                "Fetch Exceptions\n"
                "        |\n"
                " Split into Batches\n"
                "        |\n"
                "GPT-4o Severity Class\n"
                "        |\n"
                "    Severity\n"
                " /     |     \\\n"
                "Crit  Std   Low\n"
                " |     |     |\n"
                "Case  Case  Log\n"
                "Alert  Notify\n"
                "AM   Customer"
            ),
            "companies": [
                ("C.H. Robinson", "20M+ shipments per year, triage exceptions at scale"),
                ("FedEx Freight", "same-hour alerts on high-value LTL exceptions"),
                ("Amazon Freight", "B2B shipping exception updates before customers ask"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/trGcBqL5lylqqmjF",
        },
    ],
    "construction": [
        {
            "id": "C-7",
            "name": "Site Safety Compliance & OSHA Reporting",
            "trigger": "Schedule",
            "trigger_label": "Daily",
            "nodes": 8,
            "saves": "16 hrs/week",
            "problem": "Safety managers fill out OSHA forms by hand, often missing deadlines or filing the wrong form. A single missed serious violation can result in a fine up to $15,625.",
            "built": "An agent that reads each day's inspection reports, checks violations against 29 CFR 1926 with GPT-4o, files the right form, and sends the PM a corrective action plan.",
            "solved": "OSHA forms get filed on time every time. Project managers start each morning knowing which sites have violations, what the citations are, and what to fix by when.",
            "workflow": (
                "  Daily Trigger\n"
                "       |\n"
                "Fetch Inspections\n"
                "       |\n"
                "Split into Batches\n"
                "       |\n"
                "GPT-4o 29 CFR 1926\n"
                "       |\n"
                "OSHA Reportable?\n"
                " Yes         No\n"
                "  |           |\n"
                "File OSHA  Log\n"
                "Form + Alert Minor\n"
                "PM        Violation"
            ),
            "companies": [
                ("Turner Construction", "1,500+ active sites, OSHA 300 logs kept current"),
                ("Bechtel", "fall protection and PPE violations for same-day action"),
                ("Procore Contractors", "pull inspections from Procore, push to OSHA system"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/yV1moFLC09gC4g6C",
        },
        {
            "id": "C-8",
            "name": "Subcontractor Invoice Reconciliation",
            "trigger": "Schedule",
            "trigger_label": "Weekly",
            "nodes": 10,
            "saves": "28 hrs/week",
            "problem": "Finance teams manually check subcontractor invoices line by line against Schedule of Values. It takes days, errors still happen, and overpayments are common.",
            "built": "An agent that pulls every pending invoice, fetches the matching contract SOV, and asks GPT-4o to verify every line item, retainage calculation, and compliance doc.",
            "solved": "Overbilling gets caught before payment. Subs with missing lien waivers get a clear email explaining what is needed. The whole process goes from days to hours.",
            "workflow": (
                "Weekly Trigger\n"
                "      |\n"
                "Fetch Pending Invoices\n"
                "      |\n"
                "Split into Batches\n"
                "      |\n"
                "Fetch Contract SOV\n"
                "      |\n"
                "GPT-4o Reconciliation\n"
                "      |\n"
                " Approved?\n"
                " Yes      No\n"
                "  |        |\n"
                "Create  Flag +\n"
                "Payment Notify\n"
                "Voucher   Sub"
            ),
            "companies": [
                ("Skanska USA", "billions in subcontractor payments verified consistently"),
                ("Hensel Phelps", "Davis-Bacon certified payroll compliance on federal projects"),
                ("Procore + Sage 300", "pull SOV from Procore, push vouchers into Sage ERP"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/lQhFarz4A38f2flj",
        },
        {
            "id": "C-9",
            "name": "Material Procurement & Supply Forecasting",
            "trigger": "Schedule",
            "trigger_label": "Daily",
            "nodes": 9,
            "saves": "24 hrs/week",
            "problem": "Project managers find out about material shortages when the crew shows up and there is nothing to work with. An idle trade crew costs between $1,800 and $3,000 per hour.",
            "built": "An agent that runs every morning, checks upcoming material needs against current inventory, and asks GPT-4o to find gaps given supplier lead times. POs are created automatically.",
            "solved": "Material gaps get caught 5 to 10 days before they become a site problem. Procurement teams have time to source and deliver without ever stopping work.",
            "workflow": (
                " Daily Trigger\n"
                "      |\n"
                "Fetch Schedules\n"
                "+ Inventory\n"
                "      |\n"
                "Split by Project\n"
                "      |\n"
                "GPT-4o Cross-Ref\n"
                "Needs vs Stock\n"
                "      |\n"
                "Critical Shortage?\n"
                " Yes         No\n"
                "  |           |\n"
                "Create     Daily\n"
                "Bulk POs  Summary\n"
                "+ Alert PM to PM"
            ),
            "companies": [
                ("Whiting Turner", "prevent steel and concrete shortages on high-rise builds"),
                ("DPR Construction", "MEP material tracking for fast-track data center projects"),
                ("Procore + NetSuite", "pull schedules from Procore, push POs into NetSuite"),
            ],
            "n8n_url": "https://aravind5.app.n8n.cloud/workflow/aby1Dzm36hwcWkHM",
        },
    ],
}

DOMAIN_META = {
    "healthcare": {
        "label": "Healthcare",
        "tag_class": "hc-tag",
        "title_class": "hc-title",
        "header_class": "hc-header",
        "id_class": "hc-id",
        "dot_class": "hc-dot",
        "btn_class": "hc-btn",
        "stat_class": "hc-stat",
        "desc": "Three agents that automate patient discharge triage, insurance prior authorization, and clinical trial recruitment using GPT-4o and live EHR data.",
    },
    "transportation": {
        "label": "Transportation",
        "tag_class": "tr-tag",
        "title_class": "tr-title",
        "header_class": "tr-header",
        "id_class": "tr-id",
        "dot_class": "tr-dot",
        "btn_class": "tr-btn",
        "stat_class": "tr-stat",
        "desc": "Three agents that predict fleet breakdowns, reroute deliveries in real time, and escalate freight exceptions by severity before account managers have to ask.",
    },
    "construction": {
        "label": "Construction",
        "tag_class": "cn-tag",
        "title_class": "cn-title",
        "header_class": "cn-header",
        "id_class": "cn-id",
        "dot_class": "cn-dot",
        "btn_class": "cn-btn",
        "stat_class": "cn-stat",
        "desc": "Three agents that file OSHA reports automatically, reconcile subcontractor invoices against Schedule of Values, and forecast material shortages before they stop work on site.",
    },
}


# ─── RENDER HELPERS ──────────────────────────────────────────────────────────

def agent_card_html(agent: dict, meta: dict) -> str:
    companies_html = "".join(
        f"""<div class="uc-item">
              <div class="uc-dot {meta['dot_class']}"></div>
              <div class="uc-text"><span class="uc-co">{co}</span> — {desc}</div>
            </div>"""
        for co, desc in agent["companies"]
    )

    workflow_escaped = (
        agent["workflow"]
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

    return f"""
<div class="agent-card">
  <!-- Header -->
  <div class="card-header {meta['header_class']}">
    <div class="card-id {meta['id_class']}">{agent['id']}</div>
    <div class="card-name">{agent['name']}</div>
    <span class="trigger-pill">
      <span class="trigger-dot"></span>
      {agent['trigger']} · {agent['trigger_label']}
    </span>
  </div>

  <!-- Body -->
  <div class="card-body">

    <!-- Google XYZ -->
    <div class="xyz-item">
      <span class="xyz-label label-p">Problem</span>
      <span class="xyz-text">{agent['problem']}</span>
    </div>
    <div class="xyz-item">
      <span class="xyz-label label-b">Built</span>
      <span class="xyz-text">{agent['built']}</span>
    </div>
    <div class="xyz-item">
      <span class="xyz-label label-s">Solved</span>
      <span class="xyz-text">{agent['solved']}</span>
    </div>

    <div class="card-divider"></div>

    <!-- Workflow Diagram -->
    <div class="workflow-box">{workflow_escaped}</div>

    <!-- Use Cases -->
    <div class="uc-title">Real World Use Cases</div>
    {companies_html}

    <!-- Metrics -->
    <div class="metrics-row">
      <div class="metric-chip">
        <span class="metric-val">{agent['nodes']}</span>
        <span>nodes</span>
      </div>
      <div class="metric-chip">
        <span class="metric-val {meta['stat_class']}">{agent['saves']}</span>
        <span>saved</span>
      </div>
    </div>

    <!-- n8n Link -->
    <a class="n8n-btn {meta['btn_class']}" href="{agent['n8n_url']}" target="_blank">
      View Live in n8n Cloud →
    </a>

  </div>
</div>
"""


def render_domain_section(domain_key: str):
    meta = DOMAIN_META[domain_key]
    agents = AGENTS[domain_key]

    # Domain header
    st.markdown(f"""
    <div class="domain-header">
      <div class="domain-tag {meta['tag_class']}">{meta['label']}</div>
      <div class="domain-title">{meta['label']} AI Agents</div>
      <div class="domain-desc">{meta['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

    # 3 cards in columns
    cols = st.columns(3, gap="medium")
    for col, agent in zip(cols, agents):
        with col:
            st.markdown(agent_card_html(agent, meta), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


# ─── HERO ────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="hero-wrap">
  <div class="hero-badge">n8n · GPT-4o · Production Ready</div>
  <div class="hero-title">AI Agent Portfolio</div>
  <div class="hero-subtitle">
    9 production-grade workflow agents built on n8n and GPT-4o.
    Each agent solves a real business problem across three industries —
    fully automated, running live in the cloud.
  </div>
  <div class="tech-badges">
    <span class="tech-badge"><span class="dot"></span>n8n Cloud</span>
    <span class="tech-badge"><span class="dot" style="background:#10B981"></span>GPT-4o</span>
    <span class="tech-badge"><span class="dot" style="background:#F97316"></span>Gmail + Slack</span>
    <span class="tech-badge"><span class="dot" style="background:#8B5CF6"></span>Webhook + Schedule</span>
  </div>
  <div class="hero-stats">
    <div class="stat-box">
      <span class="stat-num" style="background:linear-gradient(135deg,#fff,#A5B4FC);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">9</span>
      <span class="stat-lbl">AI Agents</span>
    </div>
    <div class="stat-box">
      <span class="stat-num" style="background:linear-gradient(135deg,#fff,#67E8F9);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">3</span>
      <span class="stat-lbl">Industries</span>
    </div>
    <div class="stat-box">
      <span class="stat-num" style="background:linear-gradient(135deg,#fff,#86EFAC);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">GPT-4o</span>
      <span class="stat-lbl">Powered</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─── TABS ────────────────────────────────────────────────────────────────────

tab_hc, tab_tr, tab_cn = st.tabs([
    "  Healthcare  ",
    "  Transportation  ",
    "  Construction  ",
])

with tab_hc:
    render_domain_section("healthcare")

with tab_tr:
    render_domain_section("transportation")

with tab_cn:
    render_domain_section("construction")


# ─── FOOTER ──────────────────────────────────────────────────────────────────

st.markdown("""
<div class="portfolio-footer">
  <div class="footer-repos">
    <a class="repo-link" href="https://github.com/data-geek-astronomy/n8n-healthcare" target="_blank">
      github / n8n-healthcare
    </a>
    <a class="repo-link" href="https://github.com/data-geek-astronomy/n8n-transportation" target="_blank">
      github / n8n-transportation
    </a>
    <a class="repo-link" href="https://github.com/data-geek-astronomy/n8n-construction" target="_blank">
      github / n8n-construction
    </a>
    <a class="repo-link" href="https://github.com/data-geek-astronomy/n8n-ai-agents" target="_blank">
      github / n8n-ai-agents (combined)
    </a>
  </div>
  <div class="footer-credit">
    Built by <a href="https://github.com/data-geek-astronomy" target="_blank">Aravind Kumar</a>
    &nbsp;·&nbsp; n8n + GPT-4o &nbsp;·&nbsp; 9 agents live on
    <a href="https://aravind5.app.n8n.cloud" target="_blank">n8n Cloud</a>
  </div>
</div>
""", unsafe_allow_html=True)
