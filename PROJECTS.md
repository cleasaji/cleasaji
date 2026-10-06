<div align="center">

<img src="./assets/sec-catalog.svg" width="82%" alt="All Projects"/>

<i>68 repositories, grouped by theme. Each description is taken from the project's own README.</i>

<br>

<a href="#ai"><img src="https://img.shields.io/badge/AI%20and%20ML%20Security-10-E85A9B?style=for-the-badge" alt="AI and ML Security"/></a>
<a href="#threat"><img src="https://img.shields.io/badge/Threat%20Detection%20and%20Security%20Tooling-19-F27FBC?style=for-the-badge" alt="Threat Detection and Security Tooling"/></a>
<a href="#resilient"><img src="https://img.shields.io/badge/Self-Defending%20and%20Explainable%20Systems-12-B98BE8?style=for-the-badge" alt="Self-Defending and Explainable Systems"/></a>
<a href="#infra"><img src="https://img.shields.io/badge/Distributed%20Systems%20and%20Infrastructure-10-D63F85?style=for-the-badge" alt="Distributed Systems and Infrastructure"/></a>
<a href="#fintech"><img src="https://img.shields.io/badge/Fintech%20and%20Blockchain-7-FCAFDB?style=for-the-badge" alt="Fintech and Blockchain"/></a>
<a href="#ts"><img src="https://img.shields.io/badge/TypeScript%20Libraries-5-C94C93?style=for-the-badge" alt="TypeScript Libraries"/></a>
<a href="#devops"><img src="https://img.shields.io/badge/DevOps%20and%20Applications-3-F06BAE?style=for-the-badge" alt="DevOps and Applications"/></a>
<a href="#sih"><img src="https://img.shields.io/badge/Smart%20India%20Hackathon%202026-2-A874E0?style=for-the-badge" alt="Smart India Hackathon 2026"/></a>

</div>

<a id="ai"></a>

## 🤖 AI and ML Security

*Detectors and guards built on machine learning*

| Project | What it does | Language |
|---|---|---|
| [**AgentShield**](https://github.com/cleasaji/AgentShield) | Security benchmark for autonomous AI agents: a catalog of concrete attack scenarios used to test an agent. | Python |
| [**AgentSOC**](https://github.com/cleasaji/AgentSOC) | Evidence-verified AI threat hunter: a threat-hunting pipeline with a vector-based RAG layer. | Python |
| [**AIShield**](https://github.com/cleasaji/AIShield) | Enterprise AI-security gateway: a FastAPI service that inspects employee interactions with AI tools. | Python |
| [**CodeSentry**](https://github.com/cleasaji/CodeSentry) | AI-assisted static application security testing for Python: an AST rule engine in the style of Bandit and Semgrep, combined with machine learning. | Python |
| [**DeepVoice-Shield**](https://github.com/cleasaji/DeepVoice-Shield) | Voice deepfake and vishing detection: classifies a clip as genuine or synthetic from acoustic cues. | Python |
| [**LogSentinel**](https://github.com/cleasaji/LogSentinel) | SOC log anomaly detection: parses SSH and firewall logs into Drain3 template clusters, builds window features and flags anomalies. | Python |
| [**ModelGuard**](https://github.com/cleasaji/ModelGuard) | ML model security toolkit: pickle malware scanner, signed manifests, adversarial robustness testing and backdoor screening. | Python |
| [**NetGuard-IDS**](https://github.com/cleasaji/NetGuard-IDS) | Network intrusion detection: classifies flows as benign, DoS, port scan or brute-force using XGBoost. | Python |
| [**PhishGuard-AI**](https://github.com/cleasaji/PhishGuard-AI) | Explainable phishing URL detection: XGBoost on lexical and structural URL features, with SHAP explanations for every prediction. | Python |
| [**PhishIntel-X**](https://github.com/cleasaji/PhishIntel-X) | Phishing and threat-intelligence engine: a FastAPI service with a trained, SHAP-explained XGBoost classifier. | Python |

<a id="threat"></a>

## 🔎 Threat Detection and Security Tooling

*SOC, threat hunting, scanners and analyzers*

| Project | What it does | Language |
|---|---|---|
| [**APT-Tracker**](https://github.com/cleasaji/APT-Tracker) | Attack-chain reconstruction: correlates security events from multiple sources such as an email gateway. | Python |
| [**CloudHunt**](https://github.com/cleasaji/CloudHunt) | Cloud threat hunting on CloudTrail-style AWS audit logs: a FastAPI detection service. | Python |
| [**CodeGenome**](https://github.com/cleasaji/CodeGenome) | Treats a repository's commit history as an evolving genome to trace what actually produced a vulnerability. | Python |
| [**CompilerSentry**](https://github.com/cleasaji/CompilerSentry) | Security scanner: Python taint analysis, C unsafe-API rules, build-flag audit and ELF hardening checks, with SARIF output. | Python |
| [**DNSHunter**](https://github.com/cleasaji/DNSHunter) | DNS-based command-and-control detection: classifies DNS query streams per source IP. | Python |
| [**FuzzForge**](https://github.com/cleasaji/FuzzForge) | Coverage-guided fuzzer for Python: edge coverage, power scheduling, crash deduplication and minimization. | Python |
| [**MalwareScope**](https://github.com/cleasaji/MalwareScope) | Behavioral malware analysis service: FastAPI backend with real static analysis such as SHA256 and MD5 hashing. | Python |
| [**MemGuard**](https://github.com/cleasaji/MemGuard) | Memory-behavior observatory that fingerprints processes by how they use memory. | Python |
| [**NetTrace**](https://github.com/cleasaji/NetTrace) | Network threat detection and investigation: a FastAPI backend that parses real PCAP files with Scapy. | Python |
| [**oem-network-scanner**](https://github.com/cleasaji/oem-network-scanner) | Network reconnaissance and vulnerability detection tool that discovers OEM devices such as routers. | Python |
| [**phishing-detector-ext**](https://github.com/cleasaji/phishing-detector-ext) | Chrome extension that scores URLs in real time with a Naive Bayes phishing classifier. | Python |
| [**SecretScan**](https://github.com/cleasaji/SecretScan) | Source-code scanner that detects exposed credentials: API keys, passwords, tokens and private keys. | Python |
| [**SelfExplainingAccessControl**](https://github.com/cleasaji/SelfExplainingAccessControl) | Access-control decision engine where every decision explains itself. | Python |
| [**siem-log-analyser**](https://github.com/cleasaji/siem-log-analyser) | Lightweight SIEM prototype: ingests Windows Event Logs and correlates alerts. | Python |
| [**SmartContract-Auditor**](https://github.com/cleasaji/SmartContract-Auditor) | Static analyzer for Solidity smart contracts that catches reentrancy and other common vulnerability classes. | Python |
| [**ThreatHunt-X**](https://github.com/cleasaji/ThreatHunt-X) | Automated threat hunting backend that ingests Windows, auth, DNS and proxy logs. | Python |
| [**TrustFabric**](https://github.com/cleasaji/TrustFabric) | Continuous, explainable trust score for software dependencies: temporal and behavioral, not just CVE lookups. | Python |
| [**ZeroDayLab**](https://github.com/cleasaji/ZeroDayLab) | Reproducible vulnerability-discovery benchmark: intentionally vulnerable C programs with hand-verified ground truth. | Python |
| [**ZeroTrace**](https://github.com/cleasaji/ZeroTrace) | Zero-trust risk and access engine: a FastAPI policy engine evaluating identity, device and location. | Python |

<a id="resilient"></a>

## 🧬 Self-Defending and Explainable Systems

*Systems that recover, explain themselves or reason about evidence*

| Project | What it does | Language |
|---|---|---|
| [**AdaptiveComputingEnv**](https://github.com/cleasaji/AdaptiveComputingEnv) | Behavioral-security model that learns how a specific machine is normally used. | Python |
| [**AirType**](https://github.com/cleasaji/AirType) | Multimodal interaction engine that fuses gaze, gesture and voice into a single predicted intent. | Python |
| [**CausalOS**](https://github.com/cleasaji/CausalOS) | Causal digital twin for computer security: models an incident causally instead of matching signatures. | Python |
| [**Digital-Twin-of-a-Smartphone**](https://github.com/cleasaji/Digital-Twin-of-a-Smartphone) | Miniature smartphone digital twin: simulates CPU, battery, temperature, memory and network, with a risk engine. | Python |
| [**GhostProcess**](https://github.com/cleasaji/GhostProcess) | Reconstructs a vanished process's behavior from residual evidence scattered across independent logging systems. | Python |
| [**PredictiveFailureEngine**](https://github.com/cleasaji/PredictiveFailureEngine) | Predicts service failures from telemetry trends and quantifies the prediction. | Python |
| [**PrivCompute**](https://github.com/cleasaji/PrivCompute) | Local-first engine that answers questions from personal documents without sending them to the cloud. | Python |
| [**ProofTrace**](https://github.com/cleasaji/ProofTrace) | Evidence-provenance engine that refuses an AI system's conclusion unless it can show its supporting evidence. | Python |
| [**SelfForensicOS**](https://github.com/cleasaji/SelfForensicOS) | OS-level event model that reconstructs an incident timeline; every conclusion traces back to evidence. | Python |
| [**SelfHeal**](https://github.com/cleasaji/SelfHeal) | Self-healing software that proves its recovery worked before committing to it, using a two-tier verification loop. | Python |
| [**SelfHealingSoftware**](https://github.com/cleasaji/SelfHealingSoftware) | Software that detects a failing component and recovers automatically, with root-cause diagnosis and a recovery policy. | Python |
| [**SyntheticComputerLab**](https://github.com/cleasaji/SyntheticComputerLab) | Fully simulated computer ecosystem of users, files, processes and network connections, with a togglable security control. | Python |

<a id="infra"></a>

## ⚙️ Distributed Systems and Infrastructure

*Consensus, databases, gateways, tracing and streaming*

| Project | What it does | Language |
|---|---|---|
| [**ChainAudit**](https://github.com/cleasaji/ChainAudit) | Tamper-evident audit log: hash chain, RFC 6962 Merkle proofs and HMAC-signed checkpoints. | Python |
| [**CollabDocs**](https://github.com/cleasaji/CollabDocs) | Real-time collaborative text editor backed by an RGA CRDT. | Python |
| [**DistributedKV**](https://github.com/cleasaji/DistributedKV) | Raft-consensus distributed key-value store. | Python |
| [**GatewayMesh**](https://github.com/cleasaji/GatewayMesh) | Resilient API gateway: load balancing, retries with failover, circuit breakers, rate limiting and health checks. | Python |
| [**MobileVault**](https://github.com/cleasaji/MobileVault) | Encrypted credential vault core: scrypt, AES-256-GCM and RFC-verified TOTP, with a password generator. | Python |
| [**QueryOptimizer**](https://github.com/cleasaji/QueryOptimizer) | SQL query planner and cost-based optimizer with its own tokenizer and recursive-descent parser. | Python |
| [**RaftKV**](https://github.com/cleasaji/RaftKV) | Distributed key-value store implementing the Raft consensus algorithm from scratch. | Python |
| [**RateLimiter-Gateway**](https://github.com/cleasaji/RateLimiter-Gateway) | Distributed API rate limiter and gateway implementing four rate-limiting algorithms. | Python |
| [**StreamGuard**](https://github.com/cleasaji/StreamGuard) | Streaming anomaly detection on fixed-memory sketches: HyperLogLog, Count-Min and Space-Saving. | Python |
| [**TraceLens**](https://github.com/cleasaji/TraceLens) | Distributed tracing and observability: a FastAPI service that ingests OpenTelemetry-shaped spans. | Python |

<a id="fintech"></a>

## 💹 Fintech and Blockchain

*Ledgers, exchanges, wallets and chains from first principles*

| Project | What it does | Language |
|---|---|---|
| [**ArbitrageScanner**](https://github.com/cleasaji/ArbitrageScanner) | Market-neutral arbitrage detector for currency and crypto pairs. | Python |
| [**blockchain-secure-logger**](https://github.com/cleasaji/blockchain-secure-logger) | Tamper-proof security audit logging with a SHA-256 chained block structure. | Python |
| [**ChainForge**](https://github.com/cleasaji/ChainForge) | Blockchain from scratch: proof-of-work mining, Merkle trees, a UTXO model and ECDSA-signed transactions. | Python |
| [**HDWallet-Kit**](https://github.com/cleasaji/HDWallet-Kit) | BIP32, BIP39 and BIP44 hierarchical deterministic wallet implemented from the specifications. | Python |
| [**LedgerCore**](https://github.com/cleasaji/LedgerCore) | Double-entry bookkeeping core, the accounting model behind banking and payment systems. | Python |
| [**QuantRisk-Engine**](https://github.com/cleasaji/QuantRisk-Engine) | Portfolio risk analytics: Value at Risk by three methods, CVaR, Sharpe and Sortino ratios. | Python |
| [**TradeMatch-Engine**](https://github.com/cleasaji/TradeMatch-Engine) | Limit order book with price-time priority matching, the core algorithm of real exchanges. | Python |

<a id="ts"></a>

## 🧩 TypeScript Libraries

*Type-safe building blocks*

| Project | What it does | Language |
|---|---|---|
| [**PubSub-TS**](https://github.com/cleasaji/PubSub-TS) | Fully type-safe event bus: every event name and payload type is declared once in an event map. | TypeScript |
| [**QueryCraft**](https://github.com/cleasaji/QueryCraft) | Type-safe SQL query builder and mini ORM with compile-time-checked queries. | TypeScript |
| [**StateForge**](https://github.com/cleasaji/StateForge) | Lightweight type-safe state management library in the spirit of Redux and Zustand. | TypeScript |
| [**TypedRPC**](https://github.com/cleasaji/TypedRPC) | End-to-end type-safe RPC framework in the spirit of tRPC. | TypeScript |
| [**TypeGuard**](https://github.com/cleasaji/TypeGuard) | Runtime schema validation library built from scratch, in the spirit of Zod. | TypeScript |

<a id="devops"></a>

## 🚀 DevOps and Applications

*Pipelines, dashboards and small apps*

| Project | What it does | Language |
|---|---|---|
| [**demo-clea**](https://github.com/cleasaji/demo-clea) | Containerized Task API deployed through a DevSecOps Jenkins pipeline: test, SonarQube scan and Docker build. | Python |
| [**intern-management-system**](https://github.com/cleasaji/intern-management-system) | Single-file HTML, CSS and JavaScript inventory dashboard backed by a Google Apps Script. | HTML |
| [**simple_python_web_app**](https://github.com/cleasaji/simple_python_web_app) | Minimal Flask app with a Jenkins CI/CD pipeline, built as a hands-on continuous integration exercise. | Python |

<a id="sih"></a>

## 🇮🇳 Smart India Hackathon 2026

*Team Sirius entries*

| Project | What it does | Language |
|---|---|---|
| [**kaushal-vaani**](https://github.com/cleasaji/kaushal-vaani) | Smart India Hackathon 2026 (SIH26097): voice-first AI for livelihood mapping and NSQF-aligned skilling recommendations. Working prototype. | HTML |
| [**team-sirius**](https://github.com/cleasaji/team-sirius) | Smart India Hackathon 2026 (SIH26116): Courtyard Rise, a nature-integrated B+G+9 mixed-use building concept for the Autodesk Revit challenge. | HTML |

---

*Also on GitHub: `rag-soc-analyst` is an empty placeholder for an upcoming RAG-based SOC analyst, and this repository is the profile README itself.*

<div align="center">

<a href="./README.md">← Back to profile</a>

</div>
