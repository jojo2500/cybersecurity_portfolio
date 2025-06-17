# Incident Handler's Journal

## Date: 12/6/2025
### Entry: #1
**Description:**  
A small U.S. healthcare clinic was targeted by a phishing email containing a malicious attachment. Upon execution, ransomware encrypted the organization’s files, disrupting operations. A ransom note demanded payment for decryption.

**Tool(s) used:** None.

#### The 5 W's
- **Who caused the incident?** An organized group of unethical hackers.
- **What happened?** Phishing email delivered ransomware, encrypting files and demanding payment.
- **When did the incident occur?** On Tuesday at 9:00 a.m.
- **Where did the incident happen?** U.S. healthcare clinic.
- **Why did the incident happen?** Financial gain (primary motive via ransom payment).  
  Potential weak security posture (e.g., lack of employee training, outdated defenses).  
  Healthcare clinics are often targeted due to their reliance on immediate data access.

**Additional notes:**  
Attack Vector: The malicious attachment (e.g., disguised as an invoice, PDF, or Word doc) likely exploited macros or embedded malware.  
Impact:  
- Operational disruption (patient care delays, financial losses).
- Compliance risks (HIPAA violations if patient data was exfiltrated).

Mitigation Steps:
- Isolate infected systems to prevent lateral movement.
- Restore from clean backups (if available).
- Report to authorities (FBI, HHS OCR for HIPAA breaches).

**Questions:**
- Were employees trained to recognize phishing attempts?
- Was multi-factor authentication (MFA) enabled to limit attacker access?
- How long was the dwell time between infection and detection?

---

## Date: 12/6/2025
### Entry: #2
**Description:**  
First-time analysis of network traffic using Wireshark.

**Tool(s) used:** Wireshark (GUI-based protocol analyzer).

#### The 5 W's
- **Who:** N/A (Training exercise).
- **What:** Analyzed packet capture (.pcap) file for anomalies.
- **When:** N/A.
- **Where:** N/A.
- **Why:** Learn network traffic investigation techniques.

**Additional notes:**  
Challenges: Overwhelming interface initially.  
Key Takeaway: Wireshark is powerful for detecting malicious traffic (e.g., unusual ports, payloads).

**Questions:**
- How to filter traffic for specific threats (e.g., DNS exfiltration)?

---

## Date: 13/6/2025
### Entry: #2
**Description:**  
HR received phishing email with bfsvc.exe (confirmed backdoor).

**Tool(s) used:** VirusTotal (hash analysis), EDR (endpoint isolation).

#### The 5 W's
- **Who:** Spoofed sender "Clyde West" (76tguyhh6tgftrt7tg.su).
- **What:** bfsvc.exe (SHA256: 54e6ea47eb...) executed.
- **When:** Email sent July 20, 2022, 09:30 AM.
- **Where:** HR endpoint (hr@inergy.com, IP 176.157.125.93).
- **Why:** Credential theft/persistence (FlagPro variant).

**Additional notes:**  
Red Flags: Suspicious TLD (.su), password-protected lure (paradise10789).  
Mitigation: Isolated endpoint, reset HR credentials, scanned for lateral movement.  
Improvements Needed: Block executable email attachments, train HR on job-themed phishing.

---

## Date: 13/6/2025
### Entry: #3
**Description:**  
Command-line network traffic capture using tcpdump.

**Tool(s) used:** tcpdump (CLI protocol analyzer).

#### The 5 W's
- **Who:** N/A
- **What:** Captured and filtered live traffic.
- **When:** N/A
- **Where:** N/A
- **Why:** Practice CLI-based analysis for environments without GUI.

**Additional notes:**  
Challenges: Syntax errors due to inexperience with CLI.  
Key Takeaway: tcpdump is lightweight but requires precise commands.

**Questions:**
- How to automate tcpdump captures for SOC monitoring?

---

## Date: 13/6/2025
### Entry: #4
**Description:**  
Investigated malicious file hash (54e6ea47eb...) linked to phishing.

**Tool(s) used:** VirusTotal (multi-engine malware scanner).

#### The 5 W's
- **Who:** Unknown attacker (likely APT).
- **What:** Malicious bfsvc.exe (FlagPro trojan) via email.
- **When:** Detected at 1:20 PM by IDS.
- **Where:** Financial services company.
- **Why:** Initial access for data theft/lateral movement.

**Additional notes:**  
VirusTotal Findings: 60/70 vendors flagged as malicious.  
Labels: Backdoor.Win32.Flagpro (Kaspersky), Trojan:Win32/Kryptik!MSR (Microsoft).  
Action Taken: Blocked hash enterprise-wide.

**Questions:**
- Was the email reported by the user or automated systems?

---
