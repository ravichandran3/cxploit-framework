<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-brightgreen?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/license-Educational-orange?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/modules-105-red?style=for-the-badge" alt="Modules">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-purple?style=for-the-badge" alt="Platform">
</p>

<h1 align="center">⚡ CXploit — Custom Exploit Development Framework v2.0</h1>

<p align="center">
  <em>A comprehensive, Metasploit-class exploit development and penetration testing framework built entirely in Python.</em><br>
  <em>105 modules • 7 categories • Auto-Exploitation • Encrypted C2 • WAF Bypass • Real-Time Dashboard</em>
</p>

---

## ⚠️ Legal Disclaimer

> **This framework is designed for authorized security testing and educational purposes ONLY.**
>
> Unauthorized access to computer systems is illegal. Always obtain written permission before testing any system you do not own. The developers assume no liability for misuse of this software. By using this tool, you agree to comply with all applicable local, state, national, and international laws.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [What's New in v2.0](#-whats-new-in-v20)
- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [CLI Reference](#-cli-reference)
- [Complete Module Catalog (105 Modules)](#-complete-module-catalog-105-modules)
  - [Reconnaissance (17)](#-reconnaissance-17-modules)
  - [Exploits (20)](#-exploits-20-modules)
  - [Payloads (9)](#-payloads-9-modules)
  - [Post-Exploitation (10)](#-post-exploitation-10-modules)
  - [Evasion (7)](#-evasion-7-modules)
  - [Auxiliary (23)](#-auxiliary-23-modules)
  - [Other (19)](#-other-19-modules)
- [REST API](#-rest-api)
- [Configuration](#%EF%B8%8F-configuration)
- [Report Generation](#-report-generation)
- [Session Management](#-session-management)
- [Plugin System](#-plugin-system)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Changelog](#-changelog)
- [License](#-license)

---

## 🔍 Overview

**CXploit** is a comprehensive, modular exploit development framework written entirely in Python. With **105 loaded modules** across 7 categories, it provides security professionals with a Metasploit-class integrated environment for:

- **Reconnaissance** — Port scanning, host discovery, service enumeration, OS fingerprinting, web scanning, vulnerability scanning, OSINT, DNS enumeration, SCADA/ICS scanning, WiFi analysis, blockchain auditing, firmware analysis, supply chain auditing, and **offline CVE database matching**
- **Auto-Exploitation** — **AI-powered pipeline**: scan → service detection → CVE matching → automated exploitation
- **Exploitation** — SQL injection, XSS, LFI/RFI, SSH brute-forcing, buffer overflow toolkits, FTP/Telnet/RDP/VNC/SMTP exploits, database exploits (MySQL, MSSQL, PostgreSQL, Oracle, Redis), browser exploits, WebApp deserialization/SSRF/SSTI, IoT/MQTT/UPnP, and **multi-protocol credential spraying**
- **Payload Generation** — Reverse shells, bind shells, meterpreter-style stagers, **polymorphic payloads** with multi-layer encryption, shellcode generators, multi-handlers, and macro builders
- **Post-Exploitation** — System enumeration, persistence, credential harvesting, lateral movement, container escape, memory forensics, loot management, anti-forensics, ransomware simulation, Windows/Linux privilege escalation
- **Evasion** — AES/XOR encryption, traffic obfuscation, timing randomization, **WAF detection & bypass** (20+ WAFs), AV/AMSI bypass, DNS tunneling, JA3 fingerprint randomization
- **C2 Infrastructure** — **Encrypted C2 server** with AES-256 TCP/HTTP channels and deployable agent stubs
- **Auxiliary** — Credential sprayers, email testers, HTTP tunnels, SCADA scanners, hash crackers, multi-protocol scanners (FTP, HTTP, SSH, SSL, SNMP, NetBIOS, RDP, IPMI)
- **Reporting** — Professional HTML, JSON, PDF, and compliance reports with vulnerability severity ratings

The framework features a **Metasploit-like interactive CLI** with 72 commands, tab-completion, module search, session management, background jobs, **attack chain automation**, and an optional **REST API** for remote control.

---

## 🆕 What's New in v2.0

### Expansion: 36 → 105 Modules

| Category | v1.0 | v2.0 | New |
|----------|------|------|-----|
| Reconnaissance | 7 | 17 | WiFi, SCADA, OSINT, Blockchain, Firmware, Supply Chain, Wireless Protocol, Active Directory, Cloud, Threat Intel |
| Exploits | 5 | 20 | FTP, Telnet, RDP, VNC, SMTP, SNMP, LDAP, NFS, AD, Wireless, Cloud, MySQL, MSSQL, PostgreSQL, Oracle, Redis, Browser, WebApp, IoT |
| Payloads | 6 | 9 | Multi-Handler, Shellcode Generator, Macro Builder |
| Post-Exploitation | 2 | 10 | Lateral Movement, Container Escape, Memory Forensics, Loot Manager, Anti-Forensics, Ransomware Sim, Windows Privesc, Linux Privesc |
| Evasion | 2 | 7 | AV Evasion (AMSI), Traffic Evasion (DNS tunnel/JA3), additional encryption modules |
| Auxiliary | 2 | 23 | Email Tester, HTTP Tunnel, FTP/HTTP/SSH/SSL/SNMP/NetBIOS/RDP/IPMI Scanners, Credential Store, Report Generator |
| **Total** | **36** | **105** | **+69 new modules** |

### Quality Improvements
- ✅ Fixed 88+ bare `except:` clauses → `except Exception:` across 20+ files
- ✅ Added `check()` method to all module classes
- ✅ Suppressed paramiko TripleDES deprecation warning
- ✅ Fixed duplicate banner display
- ✅ Improved mobile tester tool detection output
- ✅ All 153 Python files pass syntax verification with 0 errors
- ✅ All 105 modules load, instantiate, and dispatch cleanly
- ✅ 72 CLI commands verified (19 base + 53 extended)

---

## ✨ Features

### Core Engine
| Feature | Description |
|---------|-------------|
| **105 Built-in Modules** | Ready-to-use modules across 7 categories |
| **Dynamic Module Loader** | Auto-discovers all modules at startup using Python package introspection |
| **Thread-Safe Singleton** | Framework core uses a locked singleton pattern for safe concurrent access |
| **SQLite Database** | Persistent storage for targets, services, vulnerabilities, credentials, sessions, and events |
| **Context-Managed Sessions** | All database operations use proper session scoping to prevent detached instance errors |
| **Event System** | Centralized logging with file output and event listeners |
| **Configuration Manager** | JSON-based config with dot-notation access and auto-merge with defaults |
| **Safety System** | Target authorization, emergency stop, rate limiting |
| **Plugin Architecture** | Extensible plugin system for custom functionality |

### Metasploit-Class Features
| Feature | Description |
|---------|-------------|
| **Auto-Exploitation (AutoPwn)** | Automated scan → CVE match → exploit pipeline with one command |
| **Offline CVE Database** | 50+ CVEs across 14 services with version-range CVSS matching |
| **WAF Detection & Bypass** | Fingerprint 20+ WAFs and auto-generate mutated SQLi/XSS bypass payloads |
| **Multi-Protocol Credential Sprayer** | Single module for 11 protocols (SSH, FTP, HTTP, SMB, MySQL, RDP, etc.) |
| **Polymorphic Payload Engine** | Self-modifying payloads with 5 mutation types and multi-layer encryption |
| **Encrypted C2 Infrastructure** | AES-256 encrypted TCP/HTTP C2 server with deployable beacon agents |
| **Real-Time Web Dashboard** | Live vulnerability heatmap, session monitor, and event log |
| **Attack Chain Automation** | Create, save, and replay multi-step attack sequences |
| **SCADA/ICS Scanning** | Modbus, DNP3, BACnet, S7comm protocol scanning |
| **IoT Exploitation** | MQTT, UPnP, CoAP protocol attacks |
| **Blockchain Auditing** | Smart contract analysis and DeFi vulnerability detection |

### CLI (72 Commands)
| Feature | Description |
|---------|-------------|
| **Interactive Console** | Metasploit-style prompt with `prompt_toolkit` |
| **Tab Completion** | Context-aware auto-completion for commands, modules, and options |
| **53 Extended Commands** | Mobile testing, SCADA scan, WiFi scan, threat intel, compliance, and more |
| **Session Management** | Create, interact, background, and kill exploitation sessions |
| **Background Jobs** | Run modules in background threads with job tracking |
| **Resource Scripts** | Execute batch commands from `.rc` files |
| **Emergency Stop** | Instantly halt all module execution |

---

## 🏗 Architecture

```
+------------------------------------------------------------------+
|                          main.py                                  |
|                      (Entry Point)                                |
+-----------+-----------+-----------+-----------+-------------------+
|    CLI    | REST API  | Dashboard |  Plugins  |    Reporting      |
| console   | server    | dashboard | manager   |   report_gen     |
| commands  |           |           |           |   compliance     |
| completer |           |           |           |                   |
+-----------+-----------+-----------+-----------+-------------------+
|                        Core Engine                                |
|  framework | database | events | module_loader | autopwn          |
|  session   | config   | safety_checker | credential_store         |
|  report_generator | zeroday_detector                              |
+------------------------------------------------------------------+
|                     Modules (105 total)                            |
|  Recon(17) | Exploits(20) | Payloads(9) | Post(10) | Evasion(7) |
|  Auxiliary(23) | C2(2) | API/Dashboard(2)                        |
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
- **Git** (for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/ravichandran3/cxploit-framework.git
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
| `flask` | 3.0.2 | REST API server and dashboard |
| `python-nmap` | 0.7.1 | Nmap integration for scanning |
| `rich` | 13.7.0 | Rich terminal formatting and tables |
| `aiohttp` | 3.9.3 | Async HTTP operations |
| `sqlalchemy` | 2.0.25 | Database ORM and session management |

### Optional External Tools

These are NOT required but enhance mobile testing capabilities:

| Tool | Purpose | Install |
|------|---------|---------|
| `adb` | Android Debug Bridge | `developer.android.com/studio` |
| `apktool` | APK reverse engineering | `github.com/iBotPeaches/Apktool` |
| `jadx` | DEX to Java decompiler | `github.com/skylot/jadx` |
| `frida` | Dynamic instrumentation | `pip install frida-tools` |
| `objection` | Mobile exploration toolkit | `pip install objection` |
| `mitmproxy` | SSL/TLS interception | `pip install mitmproxy` |

### Step 4: Verify Installation

```bash
python main.py
```

You should see the CXploit banner and `Ready! 105 modules loaded.`

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
  recon/scada_scanner   — SCADA/ICS scanner
  recon/wifi_scanner    — WiFi scanner

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

### Auto-Exploitation

```
cxploit > autopwn 192.168.1.0/24
```

This runs the full pipeline: scan → service detection → CVE matching → automated exploitation.

### Run with Resource Script

```bash
python main.py -r scripts/my_scan.rc
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
| `show modules` | List all 105 loaded modules |
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
| `compliance <framework>` | Generate compliance report (pci/hipaa/nist/gdpr) |

### Advanced Commands

| Command | Description |
|---------|-------------|
| `autopwn <target/CIDR>` | Run the full auto-exploitation pipeline |
| `dashboard [port]` | Launch the real-time web dashboard |
| `cve_search <service> [version]` | Search the offline CVE database |
| `chain create <name>` | Create a named attack chain |
| `chain add <command>` | Add a step to the current chain |
| `chain run [name]` | Execute an attack chain |
| `chain list` | List all defined chains |
| `chain save <file>` | Save chains to JSON file |
| `mobile_test [mode]` | Mobile application security testing |
| `scada_scan <target>` | SCADA/ICS protocol scanning |
| `wifi_scan [interface]` | WiFi network scanning |
| `threat_intel <target>` | Threat intelligence gathering |
| `supply_chain <project_dir>` | Supply chain security audit |
| `firmware <file>` | Firmware analysis |
| `blockchain <address>` | Blockchain/smart contract auditing |
| `osint <domain>` | OSINT intelligence gathering |

---

## 📂 Complete Module Catalog (105 Modules)

### 🔎 Reconnaissance (17 Modules)

| Module | Description |
|--------|-------------|
| `recon/port_scanner` | TCP/UDP port scanner with CIDR support, 5 timing profiles, OS fingerprinting |
| `recon/host_discovery` | Network host discovery using ARP, ICMP, TCP SYN |
| `recon/service_enum` | Deep service fingerprinting with version detection |
| `recon/os_fingerprint` | OS identification via TCP/IP stack analysis |
| `recon/web_scanner` | Web application scanner with directory brute-forcing and tech detection |
| `recon/vuln_scanner` | Automated vulnerability detection with CVE matching |
| `recon/cve_db` | Offline CVE database — 50+ CVEs across 14 services |
| `recon/dns_enum` | DNS enumeration — zone transfers, subdomain brute, wildcard detection |
| `recon/osint` | OSINT intelligence — WHOIS, DNS, subdomains, emails, certificate transparency |
| `recon/network_mapper` | Network mapping — ARP discovery, OS detection, topology visualization |
| `recon/wifi_scanner` | WiFi scanning — SSID discovery, encryption analysis, rogue AP detection |
| `recon/scada_scanner` | SCADA/ICS scanning — Modbus, DNP3, BACnet, S7comm, EtherNet/IP |
| `recon/threat_intel` | Threat intelligence — IOC analysis, STIX/TAXII, feed aggregation |
| `recon/supply_chain_auditor` | Supply chain audit — dependency CVE scanning, typosquat detection |
| `recon/firmware_analyzer` | Firmware analysis — binary extraction, string analysis, crypto detection |
| `recon/blockchain_auditor` | Blockchain audit — smart contract analysis, DeFi vulnerability detection |
| `recon/wireless_protocol` | Wireless protocol analyzer — Bluetooth, Zigbee, LoRa, NFC, Z-Wave |

### 💥 Exploits (20 Modules)

| Module | Description |
|--------|-------------|
| `exploit/web/sqli` | SQL injection — error/blind/time/union techniques, multi-DBMS |
| `exploit/web/xss` | Cross-site scripting — reflected, stored, DOM-based with WAF bypass |
| `exploit/web/lfi_rfi` | Local/Remote file inclusion with PHP wrappers and log poisoning |
| `exploit/web/advanced_web_exploit` | Advanced web — deserialization, SSRF, SSTI attacks |
| `exploit/network/ssh_brute` | SSH brute-force with wordlist support and multi-threading |
| `exploit/network/ftp_exploit` | FTP exploitation — anonymous login, path traversal, command injection |
| `exploit/network/telnet_exploit` | Telnet exploitation — default credentials, command injection |
| `exploit/network/rdp_exploit` | RDP exploitation — BlueKeep detection, brute-force, NLA bypass |
| `exploit/network/vnc_exploit` | VNC exploitation — auth bypass, brute-force, screenshot capture |
| `exploit/network/smtp_exploit` | SMTP exploitation — open relay, user enumeration, header injection |
| `exploit/network/snmp_exploit` | SNMP exploitation — community string brute-force, MIB walking |
| `exploit/network/ldap_exploit` | LDAP exploitation — anonymous bind, injection, password spraying |
| `exploit/network/nfs_exploit` | NFS exploitation — share enumeration, mount access, UID spoofing |
| `exploit/network/ad_exploit` | Active Directory — Kerberoasting, AS-REP roasting, DCSync |
| `exploit/network/wireless_exploit` | Wireless — WEP/WPA cracking, evil twin, deauth attacks |
| `exploit/network/cloud_exploit` | Cloud — S3 bucket enum, metadata service, IAM misconfiguration |
| `exploit/database/mysql_exploit` | MySQL — UDF injection, file read/write, privilege escalation |
| `exploit/database/mssql_exploit` | MSSQL — xp_cmdshell, linked servers, privilege escalation |
| `exploit/database/postgresql_exploit` | PostgreSQL — COPY command RCE, large object abuse |
| `exploit/database/oracle_exploit` | Oracle — TNS poisoning, Java stored procedure RCE |
| `exploit/database/redis_exploit` | Redis — unauthorized access, Lua sandbox escape, module loading |
| `exploit/bof/stack_overflow` | Buffer overflow — 5-stage exploitation workflow (fuzz/pattern/offset/badchars/exploit) |
| `exploit/browser/browser_exploit` | Browser exploitation — JS injection, WebRTC leak, credential stealing |
| `exploit/specialized/webapp_exploit` | WebApp advanced — deserialization chains, SSRF, SSTI |
| `exploit/specialized/iot_exploit` | IoT — MQTT exploitation, UPnP attacks, CoAP manipulation |

### 🎯 Payloads (9 Modules)

| Module | Description |
|--------|-------------|
| `payload/reverse_shell` | Reverse shell multi-handler with interactive I/O |
| `payload/bind_shell` | Bind shell connector |
| `payload/meterpreter` | Meterpreter-style stager with 12+ built-in commands |
| `payload/encoder` | Payload encoder — XOR, Base64, custom schemes |
| `payload/generator` | Platform-specific payload generator |
| `payload/polymorphic` | Polymorphic payload engine — 5 mutation types, multi-layer encryption |
| `payload/multi_handler` | Multi-handler — manages multiple simultaneous payload connections |
| `payload/shellcode_generator` | Shellcode generator — x86/x64 shellcode for Windows/Linux |
| `payload/macro_builder` | Macro builder — Office VBA/HTA/JS payload generation |

### 🔧 Post-Exploitation (10 Modules)

| Module | Description |
|--------|-------------|
| `post/sys_enum` | System enumeration — OS, users, software, network, processes |
| `post/persistence` | Persistence — registry, cron, services, scheduled tasks |
| `post/lateral_move` | Lateral movement — WMI, PsExec, SSH pivoting, pass-the-hash |
| `post/container_escape` | Container escape — Docker socket, privileged mode, kernel exploits |
| `post/memory_forensics` | Memory forensics — process dumping, credential extraction, DLL analysis |
| `post/loot_manager` | Loot manager — file search, credential harvesting, data exfiltration |
| `post/antiforensics` | Anti-forensics — log cleaning, timestamp modification, trace removal |
| `post/ransom_sim` | Ransomware simulation — safe encryption/decryption demo for training |
| `post/windows_post` | Windows post-exploitation — Mimikatz integration, UAC bypass, token manipulation |
| `post/linux_post` | Linux post-exploitation — privilege escalation, container detection, persistence |

### 🛡 Evasion (7 Modules)

| Module | Description |
|--------|-------------|
| `evasion/encryption` | Payload encryption — AES-256 and XOR with self-decrypting stubs |
| `evasion/encryption/TrafficObfuscator` | Traffic obfuscation — user-agent rotation, domain fronting, jitter |
| `evasion/encryption/AntiForensics` | Anti-forensics — log cleaning, timestomping scripts |
| `evasion/encryption/TimingRandomizer` | Timing randomization — evade behavior-based detection |
| `evasion/waf_bypass` | WAF bypass — fingerprints 20+ WAFs, generates mutated payloads |
| `evasion/av_evasion` | AV evasion — AMSI bypass, obfuscation, process hollowing |
| `evasion/traffic_evasion` | Traffic evasion — DNS tunneling, JA3 fingerprint randomization |

### 🔨 Auxiliary (23 Modules)

| Module | Description |
|--------|-------------|
| `auxiliary/tools/HTTPFileServer` | HTTP file server for payload delivery |
| `auxiliary/tools/DNSLookup` | DNS lookup and enumeration |
| `auxiliary/tools/HashCracker` | Hash cracker — MD5, SHA1, SHA256, brute-force |
| `auxiliary/tools/WordlistGenerator` | Wordlist generator with mutations and leet speak |
| `auxiliary/cred_sprayer` | Multi-protocol credential sprayer (11 protocols) |
| `auxiliary/email_tester` | Email security tester — SPF, DKIM, DMARC, open relay |
| `auxiliary/http_tunnel` | HTTP tunneling for firewall evasion |
| `auxiliary/hash_cracker` | Advanced hash cracker with rainbow tables |
| `auxiliary/ftp_scanner` | FTP vulnerability scanner — anonymous login, version detection |
| `auxiliary/http_scanner` | HTTP vulnerability scanner — headers, methods, misconfigurations |
| `auxiliary/ssh_scanner` | SSH scanner — algorithm enumeration, version detection |
| `auxiliary/ssl_scanner` | SSL/TLS scanner — certificate validation, cipher analysis, HSTS |
| `auxiliary/snmp_scanner` | SNMP scanner — community strings, MIB walking |
| `auxiliary/netbios_scanner` | NetBIOS scanner — name resolution, share enumeration |
| `auxiliary/rdp_scanner` | RDP scanner — NLA detection, version fingerprinting |
| `auxiliary/ipmi_scanner` | IPMI scanner — cipher 0 detection, hash extraction |
| `auxiliary/credential_store` | Credential store — centralized credential management |
| `auxiliary/report_generator` | Report generator — HTML/JSON/PDF output |

### 📡 Other Modules (19)

| Category | Modules |
|----------|---------|
| **C2 Infrastructure** | `c2/c2_server` (Encrypted C2 with AES-256), `c2/c2_agent` (Deployable beacon generator) |
| **API & Dashboard** | `api/server` (Flask REST API), `api/dashboard` (Real-time web dashboard) |
| **Core** | `core/autopwn`, `core/credential_store`, `core/report_generator`, `core/zeroday_detector` |
| **Reporting** | `reporting/report_gen`, `reporting/compliance_report` |
| **Recon (additional)** | `recon/mobile_tester`, `recon/ad_enum`, `recon/bluetooth_scanner`, `recon/cert_analyzer`, `recon/cloud_scanner` |

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

---

## 📊 Report Generation

Generate professional penetration testing reports directly from the console.

```
cxploit > report html       # HTML report with dark theme
cxploit > report json       # Machine-readable JSON
cxploit > report pdf        # PDF document
cxploit > compliance pci    # PCI-DSS compliance report
cxploit > compliance hipaa  # HIPAA compliance report
cxploit > compliance nist   # NIST compliance report
cxploit > compliance gdpr   # GDPR compliance report
```

### Report Contents

- **Executive Summary** — Target count, vulnerability count, credential count
- **Targets** — IP, hostname, OS, status
- **Vulnerabilities** — Name, severity (Critical/High/Medium/Low), description, CVE, proof
- **Credentials** — Service, username, password/hash
- **Compliance Mapping** — Framework-specific requirement coverage

Reports are saved to `data/reports/report_YYYYMMDD_HHMMSS.<format>`.

---

## 🔗 Session Management

Sessions represent active connections to compromised hosts.

```
# After a successful exploit with a reverse shell:
[+] Session created: a1b2c3d4

# List sessions
cxploit > sessions -l

# Interact with a session
cxploit > sessions -i a1b2c3d4
[*] Interactive session a1b2c3d4. Press Ctrl+C to background.

$ whoami
root
$ ^C
[*] Session a1b2c3d4 backgrounded

# Kill a session
cxploit > sessions -k a1b2c3d4
```

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
        print(f"[+] Running against {target}")
        return {"status": "complete"}
    
    def check(self):
        return True
```

The module loader will auto-discover it on next startup.

---

## 📁 Project Structure

```
cxploit-framework/
├── main.py                              # Entry point
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
├── exploit_framework/
│   ├── __init__.py                      # Package init + BANNER
│   ├── api/
│   │   ├── server.py                    # Flask REST API
│   │   └── dashboard.py                 # Real-time web dashboard
│   ├── auxiliary/                        # 23 modules
│   │   ├── tools.py                     # HTTP server, hash cracker, wordlist gen, DNS
│   │   ├── cred_sprayer.py              # Multi-protocol credential sprayer
│   │   ├── email_tester.py              # Email security tester
│   │   ├── http_tunnel.py               # HTTP tunneling
│   │   ├── ftp_scanner.py               # FTP scanner
│   │   ├── http_scanner.py              # HTTP scanner
│   │   ├── ssh_scanner.py               # SSH scanner
│   │   ├── ssl_scanner.py               # SSL/TLS scanner
│   │   ├── snmp_scanner.py              # SNMP scanner
│   │   ├── netbios_scanner.py           # NetBIOS scanner
│   │   ├── rdp_scanner.py               # RDP scanner
│   │   ├── ipmi_scanner.py              # IPMI scanner
│   │   ├── credential_store.py          # Credential management
│   │   └── report_generator.py          # Report generator
│   ├── c2/
│   │   ├── c2_server.py                 # Encrypted C2 server (AES-256)
│   │   └── c2_agent.py                  # Deployable agent generator
│   ├── cli/
│   │   ├── commands.py                  # Command handlers
│   │   ├── completer.py                 # Tab-completion engine
│   │   └── console.py                   # Interactive console (72 commands)
│   ├── core/
│   │   ├── autopwn.py                   # Auto-exploitation engine
│   │   ├── config.py                    # Configuration manager
│   │   ├── database.py                  # SQLAlchemy ORM
│   │   ├── events.py                    # Event system
│   │   ├── framework.py                 # Central engine (singleton)
│   │   ├── module_loader.py             # Dynamic module discovery
│   │   ├── session.py                   # Session management
│   │   ├── credential_store.py          # Credential store
│   │   ├── report_generator.py          # Report generator
│   │   └── zeroday_detector.py          # Zero-day detection engine
│   ├── evasion/                          # 7 modules
│   │   ├── encryption.py                # AES/XOR encryption + 4 classes
│   │   ├── waf_bypass.py                # WAF detection & bypass
│   │   ├── av_evasion.py                # AV/AMSI bypass
│   │   └── traffic_evasion.py           # DNS tunnel, JA3 randomization
│   ├── exploits/                         # 20 modules
│   │   ├── base.py                      # Abstract base class
│   │   ├── bof/stack_overflow.py        # Buffer overflow toolkit
│   │   ├── browser/browser_exploit.py   # Browser exploitation
│   │   ├── database/                    # MySQL, MSSQL, PostgreSQL, Oracle, Redis
│   │   ├── network/                     # SSH, FTP, Telnet, RDP, VNC, SMTP, SNMP, LDAP, NFS, AD, Wireless, Cloud
│   │   ├── specialized/                 # WebApp, IoT
│   │   └── web/                         # SQLi, XSS, LFI/RFI
│   ├── payloads/                         # 9 modules
│   │   ├── reverse_shell.py             # Reverse shell
│   │   ├── bind_shell.py                # Bind shell
│   │   ├── meterpreter.py               # Meterpreter stager
│   │   ├── polymorphic.py               # Polymorphic engine
│   │   ├── multi_handler.py             # Multi-handler
│   │   ├── shellcode_generator.py       # Shellcode generator
│   │   └── macro_builder.py             # Office macro builder
│   ├── post/                             # 10 modules
│   │   ├── sys_enum.py                  # System enumeration
│   │   ├── persistence.py               # Persistence mechanisms
│   │   ├── lateral_move.py              # Lateral movement
│   │   ├── container_escape.py          # Container escape
│   │   ├── memory_forensics.py          # Memory forensics
│   │   ├── loot_manager.py              # Loot management
│   │   ├── antiforensics.py             # Anti-forensics
│   │   ├── ransom_sim.py                # Ransomware simulation
│   │   ├── windows_post.py              # Windows post-exploitation
│   │   └── linux_post.py                # Linux post-exploitation
│   ├── recon/                            # 17 modules
│   │   ├── port_scanner.py              # Port scanner
│   │   ├── host_discovery.py            # Host discovery
│   │   ├── service_enum.py              # Service enumeration
│   │   ├── os_fingerprint.py            # OS fingerprinting
│   │   ├── web_scanner.py               # Web scanner
│   │   ├── vuln_scanner.py              # Vulnerability scanner
│   │   ├── cve_db.py                    # CVE database
│   │   ├── dns_enum.py                  # DNS enumeration
│   │   ├── osint.py                     # OSINT intelligence
│   │   ├── network_mapper.py            # Network mapping
│   │   ├── wifi_scanner.py              # WiFi scanning
│   │   ├── scada_scanner.py             # SCADA/ICS scanning
│   │   ├── threat_intel.py              # Threat intelligence
│   │   ├── supply_chain_auditor.py      # Supply chain audit
│   │   ├── firmware_analyzer.py         # Firmware analysis
│   │   ├── blockchain_auditor.py        # Blockchain auditing
│   │   └── wireless_protocol.py         # Wireless protocol analysis
│   ├── reporting/
│   │   ├── report_gen.py                # HTML/JSON/PDF reports
│   │   └── compliance_report.py         # Compliance reports
│   └── utils/
│       ├── constants.py                 # Framework constants
│       ├── crypto.py                    # Crypto utilities
│       ├── network.py                   # Network helpers
│       └── validators.py               # Input validation
├── data/                                # Runtime data
│   ├── config.json                      # Configuration
│   ├── logs/                            # Log files
│   └── reports/                         # Generated reports
└── plugins/                             # Custom plugins
```

---

## 🛠 Development

### Adding a New Module

1. Create a new Python file in the appropriate category directory
2. Define a class with `MODULE_INFO` dict, a `run()` method, and a `check()` method
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
        print(f"[+] Scanning {host}:{port}")
        
        if self.framework and hasattr(self.framework, "db"):
            self.framework.db.add_target(host, status="up")
        
        return {"host": host, "port": port, "status": "complete"}
    
    def check(self):
        """Quick vulnerability check."""
        return True
```

### Running Verification

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

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure venv is activated and `pip install -r requirements.txt` complete |
| `0 modules loaded` | Check that `exploit_framework/__init__.py` exists and `sys.path` is correct |
| `Port already in use` | Another process is using the port. Use `netstat -tlnp` to find it |
| `Permission denied` (scanning) | Some scans require root/admin privileges (especially UDP, ICMP) |
| `Emergency stop active` | Run `emergency_stop` again to toggle it off |
| `Target not authorized` | Run `authorize <target>` before testing |
| Mobile tools "Not installed" | These are optional external tools — see Installation for install instructions |

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
4. Ensure all modules have `MODULE_INFO`, `run()`, and `check()` methods
5. Verify syntax: `python -c "import py_compile; py_compile.compile('your_file.py', doraise=True)"`
6. Submit a pull request

### Coding Standards
- PEP 8 compliance
- Docstrings on all public methods
- Use `except Exception:` (never bare `except:`)
- No hardcoded values — use `self.options` for configurable parameters
- Store results in the database when possible

---

## 📋 Changelog

### v2.0.0 (2025-02-25)
- **+69 new modules** — expanded from 36 to 105 modules
- Added database exploits: MySQL, MSSQL, PostgreSQL, Oracle, Redis
- Added network exploits: FTP, Telnet, RDP, VNC, SMTP, SNMP, LDAP, NFS, AD, Wireless, Cloud
- Added advanced recon: OSINT, SCADA, WiFi, Blockchain, Firmware, Supply Chain, Threat Intel
- Added post-exploitation: Lateral movement, container escape, memory forensics, anti-forensics
- Added evasion: AV/AMSI bypass, DNS tunneling, JA3 randomization
- Added payloads: Multi-handler, shellcode generator, macro builder
- Added auxiliary scanners: FTP, HTTP, SSH, SSL, SNMP, NetBIOS, RDP, IPMI
- Fixed 88+ bare `except:` clauses for proper error handling
- Added `check()` method to all module classes
- Suppressed paramiko deprecation warnings
- Fixed duplicate banner display
- Updated CLI to 72 commands (19 base + 53 extended)

### v1.0.0
- Initial release with 36 modules
- Core framework with dynamic module loader
- Interactive CLI with tab-completion
- REST API and web dashboard
- Auto-exploitation engine
- Encrypted C2 infrastructure

---

## 📄 License

This project is provided for **educational and authorized security testing purposes only**.

Unauthorized use of this software against systems you do not own or have explicit permission to test is **illegal** and **unethical**. The authors take no responsibility for the misuse of this tool.

---

<p align="center">
  <strong>Built with ❤️ for the security community</strong><br>
  <em>Stay ethical. Stay curious. Stay sharp. 🔐</em>
</p>
