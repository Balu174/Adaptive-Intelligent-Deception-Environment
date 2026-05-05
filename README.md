# Adaptive intelligent Deception Environment
# Aureon Bank OS

A creative cybersecurity and deception-based Flask web application designed for hackathon demonstration.  
This project simulates a **banking operating system interface** with an immersive UI, monitored login flow, fake internal workspace, event logging, chatbot interactions, and a visual analytics dashboard.[file:1]

## Overview

Aureon Bank OS is built as a **single-file Flask application** that combines backend logic and frontend templates into one executable Python file.[file:1]  
The project demonstrates how deceptive environments, activity monitoring, and dashboard analytics can be combined into an engaging security-themed product experience.[file:1]

The application has two major modes:

- **Authorized admin flow** that opens the real monitoring dashboard.[file:1]
- **Suspicious user flow** that redirects potential attackers into a controlled fake banking workspace.[file:1]

This creates a strong hackathon concept by blending:

- Cybersecurity
- Honeypot-style deception
- UI/UX storytelling
- Session tracking
- Data visualization
- Flask web development.[file:1]

## Key Idea

The main idea behind this project is to detect suspicious login behavior and redirect such users into a **fake internal banking environment** instead of giving direct system feedback.[file:1]  
Inside that controlled environment, user actions are tracked, interactions are logged, file previews are simulated, and chatbot activity is recorded for analysis.[file:1]

This gives the project a hackathon-friendly angle:

- It looks like a premium banking OS product.[file:1]
- It behaves like a deceptive security sandbox.[file:1]
- It logs activity like a lightweight monitoring system.[file:1]
- It visualizes activity using graphs in the admin dashboard.[file:1]

## Features

### 1. Secure login interface

The application starts with a polished **Bank OS-style secure login screen**.[file:1]

Features:
- Premium dark banking UI.[file:1]
- Branded secure-access experience.[file:1]
- Admin credential check using predefined username and password.[file:1]
- Session-based authentication for dashboard access.[file:1]

### 2. Admin login support

If valid admin credentials are entered, the user is redirected to the monitoring dashboard.[file:1]

Features:
- Flask session handling.[file:1]
- Protected dashboard route.[file:1]
- Logout support.[file:1]
- Admin activity logging.[file:1]

### 3. SQL injection detection

The project includes a simple pattern-based SQL injection detection function.[file:1]

It checks entered credentials for suspicious patterns such as:
- `' or 1=1`
- `" or 1=1`
- `union select`
- `drop table`
- `--` [file:1]

If such patterns are detected, the user is redirected into the fake internal environment instead of the real dashboard.[file:1]

### 4. Fake banking workspace

Suspicious users are redirected to a **fake Bank OS workspace** that acts like a controlled internal banking system.[file:1]

Features:
- Banking-themed interface.[file:1]
- Simulated ledger and records view.[file:1]
- Dummy employee records.[file:1]
- Dummy documents and files.[file:1]
- Operational action tiles.[file:1]
- Interactive assistant/chatbot.[file:1]

This works like a mini honeypot demonstration for hackathon judging.[file:1]

### 5. Dummy file preview system

The workspace contains simulated internal files such as:
- `salary_report_q1.xlsx`
- `vendor_master.csv`
- `system_audit_notes.txt` [file:1]

Clicking on them:
- Opens a preview in the viewer panel.[file:1]
- Logs the open event.[file:1]
- Automatically closes the file after a short delay.[file:1]
- Stores file interaction duration in logs.[file:1]

### 6. Action tracking

The workspace contains buttons for internal actions such as:
- Viewing employee directory
- Viewing documents
- Viewing support tickets
- Inspecting records
- Opening operational panel simulations.[file:1]

Each action is recorded in the log system with:
- IP address
- Timestamp
- Action type
- Severity
- Threat score.[file:1]

### 7. Chatbot assistant

The fake workspace includes a simple chatbot assistant.[file:1]

Features:
- Accepts user questions.[file:1]
- Returns predefined contextual responses.[file:1]
- Handles queries about records, files, dashboard access, support items, and workspace status.[file:1]
- Logs each chatbot interaction for monitoring.[file:1]

### 8. Attack and event logging

The application stores all important activities in a JSON log file:

```text
logs/attacks.json
```

Logged events include:
- Authorized admin login.[file:1]
- Invalid login.[file:1]
- SQL injection attempt.[file:1]
- File access duration.[file:1]
- Chat interactions.[file:1]
- Workspace actions.[file:1]

Each log entry may include:
- IP address
- Time
- Attack type or event type
- Severity
- Threat score
- Message
- Chatbot response
- Duration.[file:1]

### 9. Monitoring dashboard

The project includes a premium **Bank OS monitoring dashboard** for admin users.[file:1]

Dashboard features:
- Total logs counter.[file:1]
- Current IP display.[file:1]
- Session action count.[file:1]
- Open file handle count.[file:1]
- Detailed event log table.[file:1]

### 10. Data visualization graphs

The dashboard also includes analytics graphs to improve presentation and make the project more hackathon-ready.[file:1]

Current graph ideas implemented / planned:
- **Login vs Time bar graph** to show login-related activity over time.[file:1]
- **Threat score pie chart** to show how logs are distributed across score ranges.[file:1]

These charts make the system feel more like a real monitoring product instead of a basic Flask demo.[file:1]

## Tech Stack

- **Python** for backend logic.[file:1]
- **Flask** for routing, session handling, API endpoints, and template rendering.[file:1]
- **HTML/CSS/JavaScript** for frontend UI and interactions.[file:1]
- **Jinja templating** through `render_template_string()` for embedded templates.[file:1]
- **JSON** for log storage.[file:1]
- **Chart.js** for dashboard graphs.[file:1]

## Architecture

This project is designed as a **single-file Flask application**.[file:1]

### Main architectural idea

Instead of storing separate HTML files in a templates folder, all major UI pages are embedded directly as Python multiline strings such as:

- `LOGIN_HTML`
- `FAKE_ENV_HTML`
- `DASHBOARD_HTML` [file:1]

These are rendered using:

```python
render_template_string(...)
```

This makes the project easy to:
- Run
- Demo
- Package

## Main Routes

| Route | Method | Purpose |
|------|--------|---------|
| `/` | GET, POST | Login page and credential handling.[file:1] |
| `/fake_system` | GET | Fake banking workspace for suspicious users.[file:1] |
| `/dashboard` | GET | Protected admin monitoring dashboard.[file:1] |
| `/track` | POST | Logs user actions from the fake workspace.[file:1] |
| `/open` | POST | Starts file interaction tracking.[file:1] |
| `/close` | POST | Ends file interaction and logs duration.[file:1] |
| `/chatbot` | POST | Handles chatbot requests and logs interactions.[file:1] |
| `/logout` | GET | Clears session and returns to login.[file:1] |

## Security Concepts Demonstrated

This project is not a production banking application.  
It is a **hackathon demonstration project** that showcases core cybersecurity ideas in a creative way.[file:1]

Concepts demonstrated:
- Honeypot-style redirection.[file:1]
- Suspicious input detection.[file:1]
- Behavior logging.[file:1]
- Session-based admin protection.[file:1]
- Event monitoring dashboard.[file:1]
- Deceptive UI design for attacker engagement.[file:1]

## UI/UX Design Idea

The UI was intentionally designed as a **Bank OS** instead of a plain admin panel.[file:1]

Design ideas used:
- Dark premium visual identity.[file:1]
- Gold and cyan accent colors for fintech feel.[file:1]
- Glassmorphism-inspired panels.[file:1]
- Executive dashboard aesthetics.[file:1]
- Banking terminology such as vault, ledger, treasury, settlement rail, and telemetry.[file:1]
- A product-style interface rather than a plain academic prototype.[file:1]

This helps the project stand out in hackathons because the presentation feels more polished and story-driven.[file:1]

## How It Works

1. User opens the login page.[file:1]
2. If correct admin credentials are entered, admin session starts and dashboard opens.[file:1]
3. If suspicious SQL-like input is detected, the user is redirected to the fake banking workspace.[file:1]
4. If invalid normal credentials are entered, the user is redirected away from the app.[file:1]
5. Inside the fake workspace, all actions, file previews, and chatbot interactions are logged.[file:1]
6. Admin can later review those events from the monitoring dashboard and graphs.[file:1]

## Project Highlights for Hackathon

Why this project is strong for the realworld:

- Combines **cybersecurity + UI/UX + analytics** in one demo.[file:1]
- Has a strong visual identity instead of a basic security dashboard.[file:1]
- Demonstrates deception technology ideas in a simple and understandable way.[file:1]
- Uses realistic internal banking terminology and workspace simulation.[file:1]
- Includes logging, charting, chatbot, and interactive modules.[file:1]

## Future Improvements

Possible future upgrades:
- Add severity-wise chart visualizations.[file:1]
- Add login heatmaps and timeline analytics.[file:1]
- Add export of logs as CSV or PDF.[file:1]
- Add role-based admin accounts.[file:1]
- Add real database storage instead of JSON.[file:1]
- Add machine learning-based anomaly detection.[file:1]
- Add animated fraud indicators and live alert widgets.[file:1]
- Add multi-page dashboard navigation with sidebar modules.[file:1]

## Installation

```bash
pip install flask
python app.py
```

Then open the local Flask URL in your browser.[file:1]

## Demo Credentials

```text
Username: mohith
Password: 12345
```

## Folder Structure

```text
project/
│
├── app.py
└── logs/
    └── attacks.json
```

## Disclaimer

This project is created for **educational and hackathon demonstration purposes only**.[file:1]  
It is not intended to be used as a real banking system or production-grade security platform.[file:1]

## License

This project can be released under the MIT License for hackathon/GitHub submission if desired.[file:1]
