<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-brightgreen?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/license-Educational-orange?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/modules-36+-red?style=for-the-badge" alt="Modules">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-purple?style=for-the-badge" alt="Platform">
</p>

<h1 align="center">⚡ CXploit — Exploit Development Framework</h1>

<p align="center">
  <em>A Metasploit-beating exploit development and penetration testing framework built in Python.</em><br>
  <em>36+ modules • Auto-Exploitation • Encrypted C2 • WAF Bypass • Real-Time Dashboard</em>
</p>

---

## ⚠️ Legal Disclaimer

> **This framework is designed for authorized security testing and educational purposes ONLY.**
>
> Unauthorized access to computer systems is illegal. Always obtain written permission before testing any system you do not own. The developers assume no liability for misuse of this software. By using this tool, you agree to comply with all applicable local, state, national, and international laws.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [CLI Reference](#-cli-reference)
- [Module Categories](#-module-categories)
  - [Reconnaissance](#-reconnaissance)
  - [Exploits](#-exploits)
  - [Payloads](#-payloads)
  - [Post-Exploitation](#-post-exploitation)
  - [Evasion](#-evasion)
  - [Auxiliary](#-auxiliary)
- [REST API](#-rest-api)
- [Configuration](#%EF%B8%8F-configuration)
- [Report Generation](#-report-generation)
- [Session Management](#-session-management)
- [Plugin System](#-plugin-system)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

**CXploit** is a comprehensive, modular exploit development framework that goes beyond Metasploit, written entirely in Python. It provides security professionals with an integrated environment for:

- **Reconnaissance** — Port scanning, host discovery, service enumeration, OS fingerprinting, web scanning, vulnerability scanning, and **offline CVE database matching**
- **Auto-Exploitation** — **AI-powered pipeline**: scan -> service detection -> CVE matching -> automated exploitation
- **Exploitation** — SQL injection, XSS, LFI/RFI, SSH brute-forcing, buffer overflow toolkits, and **multi-protocol credential spraying**
- **Payload Generation** — Reverse shells, bind shells, meterpreter-style stagers, and **polymorphic payloads** with multi-layer encryption
- **Post-Exploitation** — System enumeration, persistence mechanisms, credential harvesting
- **Evasion** — AES/XOR encryption, traffic obfuscation, timing randomization, **WAF detection & bypass** (20+ WAFs)
- **C2 Infrastructure** — **Encrypted C2 server** with AES-256 TCP/HTTP channels and deployable agent stubs
- **Reporting** — Professional HTML, JSON, and PDF reports with vulnerability severity ratings
- **Real-Time Dashboard** — **Live web dashboard** with vulnerability heatmaps, session monitoring, and event logs

The framework features a **Metasploit-like interactive CLI** with tab-completion, module search, session management, background jobs, **attack chain automation**, and an optional **REST API** for remote control.

---

## ✨ Features

### Core Engine
| Feature | Description |
|---------|-------------|
| **36+ Built-in Modules** | Ready-to-use modules across 8 categories |
| **Dynamic Module Loader** | Auto-discovers all modules at startup using Python package introspection |
| **Thread-Safe Singleton** | Framework core uses a locked singleton pattern for safe concurrent access |
| **SQLite Database** | Persistent storage for targets, services, vulnerabilities, credentials, sessions, and events |
| **Context-Managed Sessions** | All database operations use proper session scoping to prevent detached instance errors |
| **Event System** | Centralized logging with file output and event listeners |
| **Configuration Manager** | JSON-based config with dot-notation access and auto-merge with defaults |
| **Safety System** | Target authorization, emergency stop, rate limiting |
| **Plugin Architecture** | Extensible plugin system for custom functionality |

### Metasploit-Beating Features
| Feature | Description |
|---------|-------------|
| **Auto-Exploitation (AutoPwn)** | Automated scan -> CVE match -> exploit pipeline with one command |
| **Offline CVE Database** | 50+ CVEs across 14 services with version-range CVSS matching |
| **WAF Detection & Bypass** | Fingerprint 20+ WAFs and auto-generate mutated SQLi/XSS bypass payloads |
| **Multi-Protocol Credential Sprayer** | Single module for 11 protocols (SSH, FTP, HTTP, SMB, MySQL, RDP, etc.) |
| **Polymorphic Payload Engine** | Self-modifying payloads with 5 mutation types and multi-layer encryption |
| **Encrypted C2 Infrastructure** | AES-256 encrypted TCP/HTTP C2 server with deployable beacon agents |
| **Real-Time Web Dashboard** | Live vulnerability heatmap, session monitor, and event log |
| **Attack Chain Automation** | Create, save, and replay multi-step attack sequences |

### CLI
| Feature | Description |
|---------|-------------|
| **Interactive Console** | Metasploit-style prompt with `prompt_toolkit` |
| **Tab Completion** | Context-aware auto-completion for commands, modules, and options |
| **Module Search** | Full-text search across module names and descriptions |
| **Session Management** | Create, interact, background, and kill exploitation sessions |
| **Background Jobs** | Run modules in background threads with job tracking |
| **Resource Scripts** | Execute batch commands from `.rc` files |
| **Report Generation** | One-command report generation in multiple formats |
| **Emergency Stop** | Instantly halt all module execution |

### Networking
| Feature | Description |
|---------|-------------|
| **CIDR Support** | Scan entire subnets (e.g., `192.168.1.0/24`) |
| **Rate Limiting** | Configurable delay between connections to avoid detection |
| **Banner Grabbing** | Protocol-aware banner capture (HTTP, SSH, FTP, SMTP, etc.) |
| **Dynamic Service Detection** | Uses `socket.getservbyport()` with fallback dictionary |
| **TCP and UDP Scanning** | Full support for both protocols |

---

## 🏗 Architecture

```
+------------------------------------------------------------------+
|                          main.py                                  |
|                      (Entry Point)                                |
+-----------+-----------+-----------+-----------+-------------------+
|    CLI    | REST API  | Dashboard |  Plugins  |    Reporting      |
| console   | server    | dashboard | manager   |   report_gen     |
| commands  |           |           |           |                   |
| completer |           |           |           |                   |
+-----------+-----------+-----------+-----------+-------------------+
|                        Core Engine                                |
|  framework | database | events | module_loader | autopwn          |
|  session   | config   | safety_checker                           |
+------------------------------------------------------------------+
|                          Modules                                  |
|  Recon(7) | Exploits(5) | Payloads(6) | Post(2) | Evasion(2)     |
|  Auxiliary(2) | C2(2) | API/Dashboard(2)                         |
+------------------------------------------------------------------+
|                         Utilities                                 |
|  network | constants | validators | crypto                       |
+------------------------------------------------------------------+
```

---

## 📦 Installation

### Prerequisites

- **Python 3.10+** (tested on 3.10, 3.11, 3.12)
- **pip** (Python package manager)
- **Nmap** (optional, for enhanced service detection via `python-nmap`)

### Step 1: Clone or Download

```bash
git clone https://github.com/yourusername/cxploit-framework.git
cd cxploit-framework
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `scapy` | 2.5.0 | Raw packet crafting and network analysis |
| `paramiko` | 3.4.0 | SSH protocol implementation |
| `requests` | 2.31.0 | HTTP client for web exploits |
| `beautifulsoup4` | 4.12.2 | HTML parsing for web scanning |
| `colorama` | 0.4.6 | Cross-platform terminal colors |
| `prompt-toolkit` | 3.0.43 | Interactive CLI with tab-completion |
| `pycryptodome` | 3.20.0 | AES, XOR, and other encryption |
| `jinja2` | 3.1.3 | HTML report templating |
| `reportlab` | 4.1.0 | PDF report generation |
| `flask` | 3.0.2 | REST API server |
| `python-nmap` | 0.7.1 | Nmap integration for scanning |
| `rich` | 13.7.0 | Rich terminal formatting and tables |
| `aiohttp` | 3.9.3 | Async HTTP operations |
| `sqlalchemy` | 2.0.25 | Database ORM and session management |

### Step 4: Verify Installation

```bash
python main.py --no-banner -q
```

You should see `Ready! 36 modules loaded.` (or more) — the framework is good to go.

---

## 🚀 Quick Start

### Launch the Framework

```bash
python main.py
```

### Basic Workflow

```
cxploit > search scan
  recon/port_scanner    — TCP/UDP port scanner with service detection
  recon/vuln_scanner    — Vulnerability scanner
  recon/web_scanner     — Web application scanner

cxploit > use recon/port_scanner
cxploit (recon/port_scanner) > show options
cxploit (recon/port_scanner) > set RHOST 192.168.1.1
cxploit (recon/port_scanner) > set PORTS 1-1024
cxploit (recon/port_scanner) > set THREADS 100
cxploit (recon/port_scanner) > run

  [+] 22/tcp OPEN  (ssh)
  [+] 80/tcp OPEN  (http) | Apache/2.4.52
  [+] 443/tcp OPEN (https)

cxploit (recon/port_scanner) > back
cxploit > show targets
cxploit > show vulns
cxploit > report html
```

### Run with Resource Script

```bash
python main.py -r scripts/my_scan.rc
```

Resource script example (`my_scan.rc`):
```
authorize 192.168.1.0/24
use recon/port_scanner
set RHOST 192.168.1.0/24
set PORTS 21,22,80,443,3306,8080
set THREADS 50
run
back
report html
```

### Launch with REST API

```bash
python main.py --api --api-port 8080
```

---

## 💻 CLI Reference

### Navigation Commands

| Command | Description |
|---------|-------------|
| `help` / `?` | Show all available commands |
| `banner` | Display the framework banner |
| `clear` | Clear the screen |
| `exit` / `quit` | Shutdown and exit the framework |
| `stats` / `sysinfo` | Show framework statistics |

### Module Commands

| Command | Description |
|---------|-------------|
| `use <module>` | Select a module (supports partial names) |
| `back` | Deselect the current module |
| `info` | Show detailed module information |
| `show modules` | List all loaded modules |
| `show options` | Show current module's configurable options |
| `search <query>` | Search modules by name or description |
| `reload` | Reload the current module from disk |

### Execution Commands

| Command | Description |
|---------|-------------|
| `set <OPT> <VALUE>` | Set a module option |
| `setg <OPT> <VALUE>` | Set a global option (persists across modules) |
| `unset <OPT>` | Clear a module option |
| `run` / `exploit` | Execute the current module |
| `bg` / `run -j` | Run module in a background thread |
| `check` | Check if target is vulnerable (without exploiting) |
| `jobs` | List background jobs |
| `jobs -k <id>` | Kill a background job |

### Session Commands

| Command | Description |
|---------|-------------|
| `sessions -l` | List all sessions |
| `sessions -i <id>` | Interact with a session (enter shell) |
| `sessions -k <id>` | Kill a specific session |
| `sessions -K` | Kill all sessions |

### Data Commands

| Command | Description |
|---------|-------------|
| `show targets` | Show all targets in the database |
| `show vulns` | Show discovered vulnerabilities |
| `show creds` | Show harvested credentials |
| `show sessions` | Show exploitation sessions |
| `show events` | Show recent event logs |
| `show stats` | Show framework statistics |

### Safety & Reporting

| Command | Description |
|---------|-------------|
| `authorize <target>` | Authorize a target for testing |
| `emergency_stop` | Halt all module execution (toggle) |
| `scan <target>` | Quick port scan shortcut |
| `report <format>` | Generate report (html/json/pdf) |

### Advanced Commands (Metasploit-Beating)

| Command | Description |
|---------|-------------|
| `autopwn <target/CIDR>` | Run the full auto-exploitation pipeline |
| `dashboard [port]` | Launch the real-time web dashboard |
| `cve_search <service> [version]` | Search the offline CVE database |
| `cve <service> [version]` | Alias for `cve_search` |
| `chain create <name>` | Create a named attack chain |
| `chain add <command>` | Add a step to the current chain |
| `chain run [name]` | Execute an attack chain |
| `chain list` | List all defined chains |
| `chain save <file>` | Save chains to JSON file |
| `chain load <file>` | Load chains from JSON file |

---

## 📂 Module Categories

### 🔎 Reconnaissance

#### `recon/port_scanner` — TCP/UDP Port Scanner
Multi-threaded port scanner with CIDR support, rate limiting, and dynamic service detection.

```
set RHOST 192.168.1.0/24    # Single IP or CIDR range
set PORTS 1-65535           # Port range, comma-separated, or ranges
set THREADS 200             # Concurrent scan threads
set PROTOCOL tcp            # tcp or udp
set BANNER true             # Enable banner grabbing
set RATE_LIMIT 0            # Delay between connections (ms)
set TIMEOUT 5               # Connection timeout (seconds)
```

**Features:**
- CIDR subnet expansion (scans all hosts in range)
- Configurable rate limiting to avoid IDS detection
- Protocol-aware banner grabbing (HTTP HEAD, SSH, FTP, SMTP)
- Dynamic service identification via `socket.getservbyport()` + fallback table
- Auto-stores discovered services in the database

---

#### `recon/host_discovery` — Network Host Discovery
Discovers live hosts on a network using multiple techniques.

#### `recon/service_enum` — Service Enumeration
Deep service fingerprinting with version detection.

#### `recon/os_fingerprint` — OS Fingerprinting
Identifies target operating system using TCP/IP stack analysis.

#### `recon/web_scanner` — Web Application Scanner
Scans web applications for common directories, files, and misconfigurations.

#### `recon/vuln_scanner` — Vulnerability Scanner
Automated vulnerability detection against known CVEs and common weaknesses.

#### `recon/cve_db` — CVE Database & Auto-Matcher
Offline CVE database with 50+ CVEs across 14 services. Supports version-range matching with CVSS scoring.

```
set SERVICE openssh
set VERSION 8.9
set MIN_SEVERITY HIGH
run
```

**Supported Services:** OpenSSH, Apache, Nginx, MySQL, PostgreSQL, Redis, vsftpd, ProFTPD, SMB, RDP, Elasticsearch, MongoDB, IIS

**Example Output:**
```
[!!!] CVE-2023-38408  CVSS 9.8  (CRITICAL)  PKCS#11 remote code execution
[!! ] CVE-2024-6387   CVSS 8.1  (HIGH)      RegreSSHion: Race condition RCE
```

---

### 💥 Exploits

#### `exploit/web/sqli` — SQL Injection
Automated SQL injection scanner and exploiter with multi-DBMS support.

```
set RHOST http://target.com/page.php
set PARAM id                            # Vulnerable parameter
set METHOD GET                          # GET or POST
set TECHNIQUE all                       # error/blind/time/union/all
set DBMS auto                           # mysql/mssql/oracle/sqlite/pgsql/auto
set COOKIE PHPSESSID=abc123            # Session cookie
set HEADERS X-Custom:value             # Extra headers
set DATA key=val&key2=val2             # POST body data
```

**Techniques:**
- **Error-based** — Regex matching for MySQL, MSSQL, Oracle, PostgreSQL, SQLite error signatures
- **Blind Boolean** — Response length and status code differential analysis with multiple quoting styles
- **Time-based** — SLEEP/WAITFOR/pg_sleep inference with baseline comparison
- **UNION-based** — Auto column count detection via ORDER BY, NULL injection

**Features:**
- Multi-DBMS fingerprinting (MySQL, MSSQL, Oracle, PostgreSQL, SQLite)
- Auto column count detection
- Data extraction via UNION SELECT (version, user, database)
- Cookie and custom header injection support
- Auto-stores findings in vulnerability database

---

#### `exploit/web/xss` — Cross-Site Scripting
Reflected and stored XSS detection with payload encoding and WAF bypass.

#### `exploit/web/lfi_rfi` — Local/Remote File Inclusion
LFI/RFI scanner with path traversal, PHP filter wrappers, and log poisoning payloads.

#### `exploit/network/ssh_brute` — SSH Brute Force
Multi-threaded SSH credential brute-forcer using `paramiko`.

```
set RHOST 192.168.1.1
set RPORT 22
set USERNAME admin              # Single user or file path
set PASSWORD /path/to/wordlist  # Single password or file path
set THREADS 10
set STOP_ON_SUCCESS true
```

---

#### `exploit/bof/stack_overflow` — Buffer Overflow Toolkit
Complete 5-stage buffer overflow exploitation workflow.

```
set RHOST 192.168.1.100
set RPORT 9999
set MODE fuzz               # fuzz / pattern / offset / badchars / exploit
set BUFFER_SIZE 2000
set STEP 200
set OFFSET 524              # Set after calculating
set EIP 0x625011AF          # JMP ESP address
set SHELLCODE <hex>         # Your shellcode in hex
set NOP_SIZE 16
set PREFIX TRUN .           # Data prefix
```

**Stages:**
1. **`fuzz`** — Send incrementally larger buffers to find the crash point
2. **`pattern`** — Send a cyclic pattern to capture the EIP value in debugger
3. **`offset`** — Calculate exact EIP offset from the captured value
4. **`badchars`** — Send all 256 bytes to identify bad characters
5. **`exploit`** — Build final payload: padding + EIP + NOP sled + shellcode

---

### 🎯 Payloads

#### `payload/reverse_shell` — Reverse Shell Listener
Multi-handler listener with real bidirectional I/O.

```
set LHOST 0.0.0.0
set LPORT 4444
set TIMEOUT 0              # 0 = infinite wait
set MULTI_HANDLER false    # Accept multiple connections
```

**Features:**
- Threaded stdin reader for true interactive shell
- Multi-handler mode for accepting multiple simultaneous connections
- Automatic session creation in the framework
- Clean socket shutdown and resource cleanup

---

#### `payload/meterpreter` — Meterpreter Stager
Advanced post-exploitation Python stager with length-prefixed protocol.

```
set LHOST 192.168.1.100
set LPORT 4444
set RECONNECT true
set RECONNECT_DELAY 5
```

**Generated stager capabilities:**
- `sysinfo` — OS, user, hostname, PID, Python version
- `execute <cmd>` — Run shell commands with timeout
- `ls [path]` — List directory contents
- `cd <path>` — Change working directory
- `pwd` — Print working directory
- `getuid` — Current username
- `ps` — Process listing
- `upload <path>` — Upload file to target
- `download <path>` — Download file from target
- `hashdump` — Extract password hashes (platform-aware)
- Auto-reconnect on connection loss

---

#### `payload/bind_shell` — Bind Shell Connector
Connects to a bind shell on a target.

#### `payload/encoder` — Payload Encoder
Encode payloads with XOR, Base64, and custom schemes.

#### `payload/generator` — Payload Generator
Generate platform-specific payloads for various architectures.

#### `payload/polymorphic` — Polymorphic Payload Engine
Generates self-modifying payloads that produce a unique hash on every generation.

```
set LHOST 192.168.1.100
set LPORT 4444
set PLATFORM python             # python / powershell / bash
set MUTATIONS all               # vars,junk,strings,encrypt,flow,all
set LAYERS 2                    # Encryption layers (1-5)
run
```

**Mutation Types:**
- **Variable Randomization** — All variable names replaced with random strings
- **Junk Code Insertion** — Dead code injected between real statements
- **String Splitting** — String literals split into concatenated parts
- **Control Flow Flattening** — Adds obfuscation wrappers
- **Multi-Layer Encryption** — XOR encryption with random keys, nested N layers deep

---

### 🔧 Post-Exploitation

#### `post/sys_enum` — System Enumeration
Comprehensive system information gathering.
- **SystemEnumerator** — OS info, users, installed software, environment variables
- **NetworkEnumerator** — Network interfaces, routing tables, ARP cache, connections

#### `post/persistence` — Persistence Mechanisms
Establish persistence on compromised hosts using platform-appropriate techniques.

---

### 🛡 Evasion

#### `evasion/encryption` — Payload Encryption
- **PayloadEncryptor** — AES-256 and XOR encryption for payloads
- **TrafficObfuscator** — Encode C2 traffic to evade network inspection
- **TimingRandomizer** — Random delays between operations to avoid timing-based detection

#### `evasion/waf_bypass` — WAF Detection & Bypass Engine
Fingerprints 20+ WAFs and generates mutated payloads to bypass them.

```
set RHOST https://target.com
set MODE full                  # detect / bypass / full
set PAYLOAD_TYPE sqli          # sqli / xss
set ITERATIONS 15              # Number of mutations
run
```

**Detected WAFs:** Cloudflare, AWS WAF, ModSecurity, Imperva, Akamai, F5 BIG-IP, Sucuri, Barracuda, Fortinet, Citrix NetScaler, Wordfence, SonicWall, Comodo, StackPath, Alibaba WAF, DDoS-Guard, WatchGuard, Palo Alto, NSFOCUS, Radware

**Bypass Techniques:** Case variation, comment injection, double encoding, HPP, inline comments, hex encoding, tab substitution, scientific notation, keyword splitting, Unicode, NULL bytes, newline injection

---

### 🔨 Auxiliary

#### `auxiliary/tools` — Utility Tools
- **HTTPFileServer** — Spin up a quick HTTP file server for payload delivery
- **HashCracker** — Offline hash cracking (MD5, SHA1, SHA256, NTLM)
- **WordlistGenerator** — Generate targeted wordlists from gathered intelligence

#### `auxiliary/cred_sprayer` — Multi-Protocol Credential Sprayer
One module to spray credentials across 11 protocols.

```
set RHOST 192.168.1.10
set PROTOCOL ssh               # ssh/ftp/http/smb/mysql/mssql/rdp/telnet/pop3/imap/postgresql
set USERNAME /path/to/users.txt
set PASSWORD /path/to/passwords.txt
set MODE spray                 # bruteforce / spray / stuffing
set THREADS 10
set JITTER 0.5                 # Random delay between attempts
run
```

---

### 📡 C2 Infrastructure

#### `c2/c2_server` — Encrypted C2 Server
AES-256 encrypted Command & Control server with multi-agent management.

```
set LHOST 0.0.0.0
set LPORT 4443
set PROTOCOL tcp               # tcp / http
set BEACON_INTERVAL 5
run
```

**Features:**
- AES-256-CBC encrypted channels with auto-generated keys
- Multi-agent concurrent management (up to 50 agents)
- TCP and HTTP transport protocols
- File exfiltration endpoint
- Framework session integration
- Agent listing and command queuing

#### `c2/c2_agent` — C2 Agent Generator
Generates deployable Python beacon agents.

```
set LHOST 192.168.1.100
set LPORT 4443
set KEY <key-from-server>
set PROTOCOL tcp
set BEACON_INTERVAL 5
set JITTER 20
set ENCODE true
set SELF_DESTRUCT false
run
```

**Agent Built-in Commands:** `sysinfo`, `shell`, `pwd`, `cd`, `ls`, `getuid`, `ps`, `download`, `upload`, `screenshot`, `selfdestruct`, `exit`

---

### 📊 Real-Time Dashboard

#### `api/dashboard` — Web Dashboard
Live web dashboard with dark glassmorphism theme.

```
cxploit > dashboard 5001
```

**Dashboard Panels:**
- **Stats Cards** — Targets, services, vulnerabilities, credentials
- **Vulnerability Heatmap** — Critical/High/Medium/Low severity breakdown
- **Active Sessions** — Live session monitoring
- **Target List** — All discovered targets with status
- **Recent Vulnerabilities** — Latest findings with severity
- **Live Event Log** — Real-time framework events

Auto-refreshes every 3 seconds via AJAX polling.

---

### 🔗 Attack Chain Automation

Create, save, and replay multi-step attack sequences:

```
cxploit > chain create recon_attack
cxploit > chain add scan 192.168.1.1
cxploit > chain add cve_search openssh 8.9
cxploit > chain add use exploit/network/ssh_brute
cxploit > chain add set RHOST 192.168.1.1
cxploit > chain add run
cxploit > chain save chains.json
cxploit > chain run recon_attack
```

---

## 🌐 REST API

The framework includes a Flask-based REST API for remote control and integration.

### Start the API

```bash
python main.py --api --api-host 0.0.0.0 --api-port 5000
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/status` | Framework status and version |
| `GET` | `/api/v1/modules` | List all loaded modules |
| `GET` | `/api/v1/modules/<name>` | Get module details and options |
| `POST` | `/api/v1/modules/<name>/run` | Execute a module with options |
| `GET` | `/api/v1/targets` | List all targets in database |
| `GET` | `/api/v1/vulnerabilities` | List all discovered vulnerabilities |
| `GET` | `/api/v1/sessions` | List active sessions |
| `POST` | `/api/v1/report` | Generate a report |

### Example: Run a Port Scan via API

```bash
curl -X POST http://localhost:5000/api/v1/modules/recon/port_scanner/run \
  -H "Content-Type: application/json" \
  -d '{"rhost": "192.168.1.1", "ports": "1-1024", "threads": "50"}'
```

### Example: Get Vulnerabilities

```bash
curl http://localhost:5000/api/v1/vulnerabilities
```

---

## ⚙️ Configuration

Configuration is stored in `data/config.json` and auto-created on first launch.

```json
{
    "framework": {
        "max_threads": 10,
        "default_timeout": 5,
        "loglevel": "INFO"
    },
    "scanner": {
        "scan_timeout": 3,
        "max_concurrent_scans": 50,
        "default_ports": "1-1024",
        "service_detection": true
    },
    "payload": {
        "default_lhost": "0.0.0.0",
        "default_lport": 4444,
        "encoder": "xor",
        "iterations": 1
    },
    "reporting": {
        "output_dir": "data/reports",
        "default_format": "html",
        "include_evidence": true
    },
    "safety": {
        "require_authorization": false,
        "rate_limit_rps": 100,
        "auto_backup": true
    }
}
```

### Key Configuration Options

| Setting | Default | Description |
|---------|---------|-------------|
| `framework.max_threads` | 10 | Default thread count for modules |
| `framework.default_timeout` | 5 | Default socket timeout in seconds |
| `framework.loglevel` | INFO | Logging level (DEBUG/INFO/WARNING/ERROR) |
| `scanner.default_ports` | 1-1024 | Default port range for quick scans |
| `safety.require_authorization` | false | Require explicit target authorization |
| `safety.rate_limit_rps` | 100 | Max requests per second |

---

## 📊 Report Generation

Generate professional penetration testing reports directly from the console.

### Usage

```
cxploit > report html    # HTML report with dark theme
cxploit > report json    # Machine-readable JSON
cxploit > report pdf     # PDF document with ReportLab
```

### Report Contents

- **Executive Summary** — Target count, vulnerability count, credential count
- **Targets** — IP, hostname, OS, status
- **Vulnerabilities** — Name, severity (Critical/High/Medium/Low), description, CVE, proof
- **Credentials** — Service, username, password/hash

Reports are saved to `data/reports/report_YYYYMMDD_HHMMSS.<format>`.

### HTML Report Features
- Dark theme with glassmorphism design
- Severity-colored vulnerability cards
- Statistics dashboard with counters
- Responsive layout

---

## 🔗 Session Management

Sessions represent active connections to compromised hosts.

### Lifecycle

```
# After a successful exploit with a reverse shell:
[+] Session created: a1b2c3d4

# List sessions
cxploit > sessions -l

# Interact with a session (enters interactive shell)
cxploit > sessions -i a1b2c3d4
[*] Interactive session a1b2c3d4. Press Ctrl+C to background.

$ whoami
root
$ ^C
[*] Session a1b2c3d4 backgrounded

# Kill a session
cxploit > sessions -k a1b2c3d4
```

### Session Features
- **Socket health check** — `is_alive()` probes the connection
- **Command execution** — `execute()` sends commands with recv timeout
- **Interactive mode** — `interact()` provides bidirectional I/O with Ctrl+C backgrounding
- **History tracking** — All executed commands and outputs are logged
- **Database persistence** — Sessions are stored in the framework database

---

## 🔌 Plugin System

Extend the framework with custom plugins.

### Plugin Structure

Create a new file in `exploit_framework/plugins/custom/`:

```python
class MyPlugin:
    """My custom plugin."""
    
    MODULE_INFO = {
        "name": "My Plugin",
        "description": "Does something useful",
        "author": "You",
        "rank": "normal",
    }
    
    def __init__(self):
        self.framework = None
        self.options = {
            "TARGET": {"value": None, "required": True, "description": "Target host"},
        }
    
    def run(self):
        target = self.options["TARGET"]["value"]
        # Your logic here
        print(f"[+] Running against {target}")
        return {"status": "complete"}
```

The module loader will auto-discover it on next startup.

---

## 📁 Project Structure

```
exploit_framework/
├── __init__.py                  # Package init, BANNER
├── api/
│   ├── __init__.py
│   ├── server.py                # Flask REST API server
│   └── dashboard.py             # [NEW] Real-time web dashboard
├── auxiliary/
│   ├── __init__.py
│   ├── tools.py                 # HTTP server, hash cracker, wordlist gen
│   └── cred_sprayer.py          # [NEW] Multi-protocol credential sprayer
├── c2/                          # [NEW] C2 Infrastructure
│   ├── __init__.py
│   ├── c2_server.py             # [NEW] Encrypted C2 server (AES-256)
│   └── c2_agent.py              # [NEW] Deployable agent generator
├── cli/
│   ├── __init__.py
│   ├── commands.py              # Command handlers (help, show, use, run, etc.)
│   ├── completer.py             # Tab-completion engine
│   └── console.py               # Interactive console (+ autopwn, dashboard, chain)
├── core/
│   ├── __init__.py
│   ├── autopwn.py               # [NEW] Auto-exploitation engine
│   ├── config.py                # Configuration manager (JSON persistence)
│   ├── database.py              # SQLAlchemy ORM (targets, vulns, creds, etc.)
│   ├── events.py                # Event system and logging
│   ├── framework.py             # Central engine (singleton, module mgmt, jobs)
│   ├── module_loader.py         # Dynamic module discovery and registration
│   └── session.py               # Session management with interactive I/O
├── evasion/
│   ├── __init__.py
│   ├── encryption.py            # AES/XOR encryption, traffic obfuscation
│   └── waf_bypass.py            # [NEW] WAF detection & bypass engine
├── exploits/
│   ├── __init__.py
│   ├── base.py                  # Abstract base class for all exploits
│   ├── bof/
│   │   ├── __init__.py
│   │   └── stack_overflow.py    # 5-mode buffer overflow toolkit
│   ├── network/
│   │   ├── __init__.py
│   │   └── ssh_brute.py         # SSH brute-force with paramiko
│   └── web/
│       ├── __init__.py
│       ├── lfi_rfi.py           # Local/Remote file inclusion
│       ├── sqli.py              # SQL injection (error/blind/time/union)
│       └── xss.py               # Cross-site scripting
├── payloads/
│   ├── __init__.py
│   ├── bind_shell.py            # Bind shell connector
│   ├── encoder.py               # Payload encoder (XOR, Base64)
│   ├── generator.py             # Payload generator
│   ├── meterpreter.py           # Meterpreter-style stager
│   ├── polymorphic.py           # [NEW] Polymorphic payload engine
│   └── reverse_shell.py         # Reverse shell multi-handler
├── plugins/
│   ├── __init__.py
│   ├── custom/
│   │   ├── __init__.py
│   │   └── example_plugin.py
│   └── plugin_manager.py        # Plugin lifecycle management
├── post/
│   ├── __init__.py
│   ├── persistence.py           # Persistence mechanisms
│   └── sys_enum.py              # System and network enumeration
├── recon/
│   ├── __init__.py
│   ├── cve_db.py                # [NEW] Offline CVE database (50+ CVEs)
│   ├── host_discovery.py        # Network host discovery
│   ├── os_fingerprint.py        # OS fingerprinting
│   ├── port_scanner.py          # TCP/UDP port scanner with CIDR
│   ├── service_enum.py          # Service enumeration
│   ├── vuln_scanner.py          # Vulnerability scanner
│   └── web_scanner.py           # Web application scanner
├── reporting/
│   ├── __init__.py
│   └── report_gen.py            # HTML, JSON, PDF report generator
└── utils/
    ├── __init__.py
    ├── constants.py             # Framework constants and payload lists
    ├── crypto.py                # Cryptographic utilities
    ├── network.py               # Network helpers (CIDR, ports, DNS, etc.)
    └── validators.py            # Input validation and SafetyChecker

main.py                          # Entry point
memory.md                        # Project context for future sessions
requirements.txt                 # Python dependencies
README.md                        # This file
```

---

## 🛠 Development

### Adding a New Module

1. Create a new Python file in the appropriate category directory
2. Define a class with `MODULE_INFO` dict and a `run()` method
3. Add `options` dict for configurable parameters
4. The module loader auto-discovers it on next startup

```python
# exploit_framework/recon/my_scanner.py

class MyScanner:
    MODULE_INFO = {
        "name": "My Scanner",
        "description": "Scans for something specific",
        "author": "Your Name",
        "rank": "good",
    }

    def __init__(self):
        self.framework = None
        self.options = {
            "RHOST": {"value": None, "required": True, "description": "Target host"},
            "RPORT": {"value": "80", "required": False, "description": "Target port"},
        }

    def run(self):
        host = self.options["RHOST"]["value"]
        port = int(self.options["RPORT"]["value"])
        # Scanning logic here
        print(f"[+] Scanning {host}:{port}")
        
        # Store results in database
        if self.framework and hasattr(self.framework, "db"):
            self.framework.db.add_target(host, status="up")
        
        return {"host": host, "port": port, "status": "complete"}
    
    def check(self):
        """Optional: quick vulnerability check."""
        return True
```

### Extending an Exploit Module

Inherit from `BaseExploit` for database storage helpers:

```python
from exploit_framework.exploits.base import BaseExploit

class MyExploit(BaseExploit):
    MODULE_INFO = { ... }
    
    def __init__(self):
        super().__init__()
        self.options = { ... }
    
    def run(self):
        # Use built-in helpers
        self.store_vuln("192.168.1.1", "My Vuln", severity="high")
        self.store_cred("192.168.1.1", "admin", password="pass123", service="ssh")
        self.store_service("192.168.1.1", 22, service_name="ssh")
        
        self.print_good("Exploit successful!")
        return {"success": True}
```

### Running Tests

```bash
python -c "
from exploit_framework.core.framework import Framework
fw = Framework()
fw.initialize()
print(f'Modules: {fw.modules.count()}')
print(f'Stats: {fw.get_stats()}')
fw.shutdown()
"
```

---

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and `requirements.txt` is installed |
| `TripleDES deprecation warning` | Cosmetic warning from paramiko — safe to ignore |
| `Port already in use` | Another process is using the port. Use `netstat -tlnp` to find it |
| `Permission denied` (scanning) | Some scans require root/admin privileges (especially UDP, ICMP) |
| `Emergency stop active` | Run `emergency_stop` again to toggle it off |
| `Target not authorized` | Run `authorize <target>` before testing |
| `0 modules loaded` | Check that `exploit_framework/__init__.py` exists and `sys.path` is correct |

### Enable Debug Logging

Edit `data/config.json`:
```json
{
    "framework": {
        "loglevel": "DEBUG"
    }
}
```

Logs are stored in `data/logs/`.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-module`)
3. Add your module following the structure above
4. Ensure the framework loads with `36+` modules
5. Submit a pull request

### Coding Standards
- PEP 8 compliance
- Docstrings on all public methods
- Error handling for all network operations
- No hardcoded values — use `self.options` for configurable parameters
- Store results in the database when possible

---

## 📄 License

This project is provided for **educational and authorized security testing purposes only**.

Unauthorized use of this software against systems you do not own or have explicit permission to test is **illegal** and **unethical**. The authors take no responsibility for the misuse of this tool.

---

<p align="center">
  <strong>Built with ❤️ for the security community</strong><br>
  <em>Stay ethical. Stay curious. Stay sharp. 🔐</em>
</p>
