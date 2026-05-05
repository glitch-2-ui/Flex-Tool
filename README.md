# 🛠️ Network Recon & Web Testing Toolkit

A lightweight Python-based command-line toolkit for basic network reconnaissance and simple web security testing.

> ⚠️ **Disclaimer:** For educational purposes and authorized testing only. Do not scan or attack systems without permission.

---
### This is tool were only tested on Windows 11 for Kali linux is coming soon

# 📦 Features

## 🌐 Network Utilities

* **Ping Scan** – Check if a host is reachable
* **Port Scanner** – Scan common ports for open services
* **DNS Lookup** – Resolve domain to IP
* **Reverse DNS Lookup** – Get hostname from IP
* **IP Geolocation** – Get location data of an IP
* **Whois Lookup** – Retrieve domain registration info

## 🔍 Web Reconnaissance

* **Dirb (Directory Bruteforce)** – Discover hidden paths using a wordlist
* **Subdomain Finder** – Identify common subdomains
* **Robots.txt Finder** – Check for robots.txt

## ⚙️ Testing Tools

* **Rate Limit Tester** – Detect rate limiting behavior
* **Simple Fuzzing** – Test for basic vulnerabilities (XSS, LFI, etc.)

---

# 🚀 Installation
### Open Cmd/Terminal and enter: 

    cd Desktop
    git clone https://github.com/glitch-2-ui/Flex-Tool
    cd Flex-Tool
    pip install -r requirements.txt
    python main.py

Menu:

```
1) Ping scan
2) Port scan
3) DNS Lookup
4) Reverse DNS Lookup
5) Dirb
6) IP geolocate
7) Whois Lookup
8) Subdomain finder
9) Rate Limit tester
10) Robots file search
11) Simple fuzzing

99) Exit
```

---

# 📁 Module Overview

## 🔓 Port Scanner

Scans common ports (22, 80, 443, etc.) to detect open services.

## 📂 Dirb

Uses a wordlist (e.g. `dirb.txt`) to brute-force directories.

## 🌍 IP Geolocation

Uses `ip-api.com` to fetch IP location data.

## 🧪 Simple Fuzzing

Sends payloads to test:

* Reflections
* XSS indicators
* Server errors (5xx)

---

# ⚠️ Limitations

* No multithreading (can be slow)
* Basic error handling
* Not suitable for large-scale scanning
* Fuzzing is very basic

---

# 🔐 Legal Notice

Use only on systems you own or have permission to test.

---

# 🧠 Purpose

Great for:

* Learning cybersecurity basics
* Understanding recon techniques
* Practicing Python scripting

---

# 👨‍💻 Author

Made by **Glitch**

TikTok: glitch_blackhat


