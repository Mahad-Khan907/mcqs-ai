"""
Full artifact generator for PCAO-F & Anthropic CCAO-F Certification Exam Guide
Chapter 09: General Agents on the Web: A Crash Course
Produces:
1. questions.json (40 scenario-based questions with strict option length parity)
2. Compiles finalmcqs.md, quiz.html, print_guide.html, and PDF via compile_chapter.py
"""

import json
import os
import sys
import subprocess
import re

# Ensure UTF-8 stdout on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

QUESTIONS_CH9 = [
    # ----------------------------------------------------
    # Sub-Topic 1: Chat vs. Delegated Agent Surfaces & The Two-Axis Runtime Model (Q1 - Q5)
    # ----------------------------------------------------
    {
        "id": 1,
        "subtopic": "Chat Box vs. Agent Surface Operational Distinction",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 1: Same address, two different things (Lines 347-372)",
        "scenario": "A pricing manager at a wholesale commercial tyre chain argues that because her team uses claude.ai every morning to draft customer discount letters, they are already running autonomous agents. According to Section 1, which single operational test invalidates this assumption?",
        "options": {
            "A": "If the user stops typing, does the task continue moving toward an outcome, or does the system halt?",
            "B": "If the browser window is resized, does the text reflow automatically into responsive screen columns?",
            "C": "If multiple team members login simultaneously, does the session log out due to concurrent session limits?",
            "D": "If an API key is omitted, does the interface revert immediately to a legacy local command-line prompt?"
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 1. The defining test separating a chat box from an agent surface is: 'If I stop typing, does the work stop? Chat box: yes. Agent surface: no.' Plain chat is synchronous and requires the user to initiate every turn. An agent surface is delegated; once assigned an outcome, it plans, uses tools, and keeps working even if the user stops typing or closes the tab.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because responsive CSS text reflow is a front-end rendering behavior unrelated to agentic delegation.",
            "distractor_C": "Option C is incorrect because concurrent session token management is an authentication rule, not the test for delegated execution.",
            "distractor_D": "Option D is incorrect because web chat interfaces do not revert to command-line prompts when end-users interact without developer API keys."
        }
    },
    {
        "id": 2,
        "subtopic": "The Two-Axis Runtime Model",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 2: The remote session: the tab is a window, not the runtime (Lines 381-395)",
        "scenario": "A clinical operations analyst configures a delegated patient intake summary task in Claude Cowork. She assumes that because she opened the session in her laptop's web browser, the model execution and data processing are restricted entirely to her local hardware. Why does Section 2 reject this assumption?",
        "options": {
            "A": "Web browsers automatically redirect all encrypted data packets into decentralized public blockchain nodes.",
            "B": "The browser tab is merely a remote viewing window; the agent loop and processing run on vendor cloud servers.",
            "C": "Local machine hardware lacks the mathematical instruction set required to render web application user interfaces.",
            "D": "Desktop browser sessions are legally prohibited from executing basic string parsing without government oversight."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 2. The chapter instructs operators to separate two runtime questions: Axis 1 (where does the agent loop run?) and Axis 2 (where does each tool execute?). In a cloud session, planning, tool selection, code execution, and task state run on the vendor's servers. The browser tab is only a viewing window onto an active cloud session ID.",
            "distractor_A": "Option A is incorrect because commercial AI vendors do not transmit customer data to public decentralized blockchain nodes.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because client laptops routinely render complex browser interfaces and can run local code when configured.",
            "distractor_D": "Option D is incorrect because local text parsing requires no regulatory legal licensing or external oversight."
        }
    },
    {
        "id": 3,
        "subtopic": "Cloud Session plus Desktop Bridge Offline Failure Modes",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 2: The remote session: the tab is a window, not the runtime (Lines 414-434, 461-465)",
        "scenario": "A logistics coordinator launches a cloud Cowork task that analyzes warehouse shipment records from Google Drive and correlates them with inventory spreadsheets stored in a folder connected through Claude Desktop. Halfway through execution, the coordinator closes her laptop. How will the session behave?",
        "options": {
            "A": "The entire cloud session terminates immediately and permanently erases all processed Google Drive outputs.",
            "B": "The agent loop migrates its execution context to the warehouse local area network routers to complete the run.",
            "C": "The cloud loop continues running with cloud tools, but the bridged local folder disappears from the session.",
            "D": "The session pauses and broadcasts an emergency SMS verification code to the corporate fleet supervisor."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 2. In a hybrid pattern (cloud loop plus desktop bridge), the agent loop runs remotely on vendor infrastructure. If the laptop disconnects or sleeps, the cloud session remains active and continues using cloud-reachable tools (like Google Drive). However, tools borrowed across the desktop bridge vanish. The operational diagnosis is that a tool became unavailable, not that Cowork stopped running.",
            "distractor_A": "Option A is incorrect because closing the laptop does not terminate the remote cloud loop or wipe cloud-synced deliverables.",
            "distractor_B": "Option B is incorrect because cloud agent loops cannot dynamically transfer execution to local networking hardware.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because losing a bridged tool does not trigger automated SMS emergency dispatching."
        }
    },
    {
        "id": 4,
        "subtopic": "Desktop Bridge Data Custody Realities",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 2: Four consequences (Lines 442-450) & Concept 10 (Lines 1124-1127)",
        "scenario": "A legal ops director reviews an analyst who processed privileged corporate merger documents by connecting a local folder to a cloud Cowork session via Claude Desktop. The analyst asserts: 'Because the files sat on my MacBook hard drive, their contents never left my machine.' Why is this assertion false?",
        "options": {
            "A": "MacBook operating systems automatically duplicate local text files into public peer-to-peer torrent networks.",
            "B": "Connecting a folder permanently transfers physical hardware drive ownership rights to the software vendor.",
            "C": "Local desktop folders cannot be read by software tools unless the hard drive is completely unencrypted.",
            "D": "Local files opened across a desktop bridge are transmitted to and processed within the vendor's cloud runtime."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 2 and Section 10. The text explicitly warns: 'A local file opened this way is processed in the vendor's cloud... A bridge is a convenience, not a custody loophole. If a cloud Cowork session reads a local file through Claude Desktop, its contents are processed in Anthropic's cloud. So do not route sensitive work to \"local file\" and assume local custody. The first question is where the processing happens, not where the file was sitting five seconds earlier.'",
            "distractor_A": "Option A is incorrect because macOS does not transmit user documents to peer-to-peer file-sharing networks.",
            "distractor_B": "Option B is incorrect because software connections have no effect on physical hardware property ownership.",
            "distractor_C": "Option C is incorrect because desktop bridge connectors read local file systems without requiring full-disk decryption.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 5,
        "subtopic": "Enterprise Controls: Work Cloud vs. Work Local",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 2: Axis 1 and ChatGPT Work (Lines 436-439)",
        "scenario": "A municipal cybersecurity auditor inspects an enterprise deployment of ChatGPT Work across government workstations. The agency's data retention mandate strictly forbids government records from entering cloud task environments. How can an administrator enforce this boundary within the platform settings?",
        "options": {
            "A": "Enable Work Local controls while disabling Work Cloud, confining agent execution strictly to local machines.",
            "B": "Configure all workstation monitors to run at reduced refresh rates to prevent remote screen capture tools.",
            "C": "Mandate that employees type all prompts exclusively in capital letters to block automated cloud ingestion.",
            "D": "Uninstall web browser extensions while leaving default unauthenticated public cloud ports open on servers."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 2. The text notes that OpenAI exposes Work Cloud and Work Local as separate enterprise administrative controls: 'An administrator can enable Work Local without Work Cloud, so members work locally and cannot start cloud tasks.' This enforces strict data locality by ensuring tasks and files remain on the local device.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because monitor refresh rates have no bearing on network routing or cloud data transmission.",
            "distractor_C": "Option C is incorrect because letter capitalization does not prevent cloud language models from ingesting prompts.",
            "distractor_D": "Option D is incorrect because leaving unauthenticated cloud ports open actively breaches security boundaries."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 2: The Six-Part Harness Anatomy & Vendor Packaging (Q6 - Q10)
    # ----------------------------------------------------
    {
        "id": 6,
        "subtopic": "The Six-Part Universal Harness Anatomy",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 471-479)",
        "scenario": "An enterprise systems architect evaluates competing agent products from emerging AI startups. Rather than relying on vendor marketing jargon, the architect applies the universal six-part harness framework defined in Chapter 9. Which complete set of components represents this architectural lens?",
        "options": {
            "A": "Prompt optimizer, vector embedding cache, token serializer, gradient checkpoint, loss curve, and hyperparameter.",
            "B": "Heartbeat (trigger), Reach (tools), Run-until-done loop, State spine (persistence), Human gate, and Body (runtime).",
            "C": "Customer billing ledger, sales pipeline CRM, marketing email sequencer, web scraper, analytics tracker, and CMS.",
            "D": "Local subnet mask, default gateway router, DNS resolution table, SSL certificate, firewall rule, and proxy port."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 3. The six universal parts of every serious agent harness are: 1. Heartbeat: what starts a run. 2. Reach: what the run can read and act on. 3. Run-until-done loop: how it keeps moving toward an outcome. 4. State spine: what persists across runs. 5. Human gate: where autonomy stops or gets screened. 6. Body: where the work actually executes.",
            "distractor_A": "Option A is incorrect because token serializers and loss curves are internal model training and inference mechanics.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because CRMs, email sequencers, and CMS platforms are external enterprise business applications.",
            "distractor_D": "Option D is incorrect because subnets, DNS tables, and firewalls are standard networking infrastructure components."
        }
    },
    {
        "id": 7,
        "subtopic": "Claude Cowork vs. ChatGPT Work Packaging Alignment",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 480-547)",
        "scenario": "A technology director compares how Claude Cowork and ChatGPT Work package their respective agent capabilities. When mapping their specific product features to the universal six-part harness, which alignment accurately reflects their structural equivalence?",
        "options": {
            "A": "Cowork Scheduled Tasks represent the Gate, while ChatGPT Work Approval Prompts represent the Heartbeat component.",
            "B": "Cowork MCP Connectors represent the Body, while ChatGPT Work Cloud Sandboxes represent the Reach tool part.",
            "C": "Cowork Connectors and ChatGPT Plugins map to Reach; Cowork Sessions and ChatGPT Synced Sessions map to Spine.",
            "D": "Cowork Manual Mode represents the State Spine, while ChatGPT Work Plan Mode represents the Heartbeat component."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 3 (Figure 3 and comparison table). Connectors in Cowork and Plugins in ChatGPT Work map to Reach (what the agent can read and act on). Saved sessions, Projects, and files map to the State Spine (what persists). Scheduled tasks map to Heartbeat, approval modes map to Gate, and cloud sandboxes/execution environments map to Body.",
            "distractor_A": "Option A is incorrect because Scheduled Tasks are the Heartbeat (trigger), and Approval Prompts are the Gate.",
            "distractor_B": "Option B is incorrect because Connectors represent Reach (tools), while cloud sandboxes represent the Body (execution environment).",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because Manual Mode is a Human Gate setting, and Plan Mode is part of the Run-until-done loop.",
        }
    },
    {
        "id": 8,
        "subtopic": "Plan Mode as an Execution Loop Discipline",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 544-545)",
        "scenario": "A product manager notices that ChatGPT Work features an explicit 'Plan mode' that gathers context, asks clarifying questions, and proposes a step-by-step approach before executing actions. How does Section 3 classify this feature within the six-part harness framework?",
        "options": {
            "A": "It is an entirely new seventh architectural harness component that replaces the need for a State spine.",
            "B": "It is a hardware virtualization hypervisor that partitions remote cloud CPU cores across tenant accounts.",
            "C": "It is an autonomous network security protocol designed to block denial-of-service traffic on cloud servers.",
            "D": "It is an interactive implementation of the Run-until-done loop that surfaces intent before execution begins."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 3. The text explains: 'ChatGPT Work Plan mode is a current example. It gathers context, asks questions, creates a step-by-step plan, and lets you approve it before execution. That is not a seventh part. It is Concept 8 built into a product.' It operationalizes the Run-until-done loop by making the agent's planned trajectory inspectable before expensive or consequential actions begin.",
            "distractor_A": "Option A is incorrect because Plan mode does not create a seventh component or replace persistent context storage.",
            "distractor_B": "Option B is incorrect because planning is a software reasoning and orchestration layer, not a hardware hypervisor.",
            "distractor_C": "Option C is incorrect because Plan mode addresses task delegation rather than DDoS network traffic filtering.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 9,
        "subtopic": "Identical Shape vs. Identical Trust",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 3: Two warnings (Lines 550-555)",
        "scenario": "An IT compliance officer evaluates an agent workflow that can interact with the corporate CRM either via an authenticated Model Context Protocol (MCP) connector or by driving a web browser through screen clicks. Why does Section 3 warn that 'same shape does not mean same trust'?",
        "options": {
            "A": "Connectors offer structured, permission-scoped actions, whereas browser automation introduces wider exposure and ambiguity.",
            "B": "Browser-based screen driving is legally recognized as a certified cryptographic signature across all federal jurisdictions.",
            "C": "MCP connectors are technically incapable of transmitting text data across standard internet firewall boundaries.",
            "D": "Web browsers automatically prevent language models from interpreting malicious instructions found in website code."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 3. The text explicitly warns: 'Same shape does not mean same trust. A connector call and a browser click can reach the same business system with different permissions, visibility, and exposure to hidden instructions... Connectors come first because structure gives you clearer permissions, clearer actions, and less ambiguity than screen-driving.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because automated browser clicks do not constitute legally binding cryptographic signatures.",
            "distractor_C": "Option C is incorrect because MCP connectors operate over standard client-server network protocols (e.g., HTTP/SSE, stdio).",
            "distractor_D": "Option D is incorrect because browsers directly expose models to untrusted web content and indirect prompt injections."
        }
    },
    {
        "id": 10,
        "subtopic": "The Harness Wars Market Shift",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Appendix G: The harness war, industry-wide (Lines 1701-1725)",
        "scenario": "A venture partner evaluating artificial intelligence startups notes that frontier model intelligence benchmarks have largely converged. According to Appendix G, where has the primary competitive battleground across major frontier AI providers shifted?",
        "options": {
            "A": "Competing exclusively on reducing physical semiconductor chip manufacturing facility construction times.",
            "B": "Competing on the complete agent harness: persistent state, browser reach, tools, schedules, and governance.",
            "C": "Competing on establishing proprietary closed-source programming languages to replace modern JavaScript.",
            "D": "Competing on marketing consumer desktop monitors with higher display pixel resolutions to office workers."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Appendix G. The text emphasizes: 'The durable market signal is not a model ranking. It is that major vendors compete on the whole agent system: memory, tools, browser reach, schedules, plugins, approvals, runtime, identity, and governance. That is the harness war.' The competitive differentiator is the surrounding harness rather than marginal raw model capability.",
            "distractor_A": "Option A is incorrect because AI software vendors compete on software harnesses, not foundry chip fabrication construction.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because AI providers rely on standard languages (Python, TypeScript) rather than replacing JavaScript.",
            "distractor_D": "Option D is incorrect because display hardware manufacturing is unrelated to agent software ecosystem competition."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 3: The Persistent Context Stack & State Spine Architecture (Q11 - Q15)
    # ----------------------------------------------------
    {
        "id": 11,
        "subtopic": "The Five Layers of the Persistent Context Stack",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 578-618)",
        "scenario": "A project lead at a commercial property consultancy wants Claude to apply a specific 20-page regional building lease analysis rubric across twelve different property evaluation tasks over the next four months. In which layer of the Persistent Context Stack should this rubric reside?",
        "options": {
            "A": "A single temporary Task Filesystem scratch pad that wipes automatically after each property review runs.",
            "B": "Global user-level Semantic Memory shared indiscriminately across all personal and non-work conversations.",
            "C": "A dedicated Project workspace holding the shared files, instructions, and context for that ongoing workstream.",
            "D": "The browser cache history of the local computer terminal used to launch the first introductory property chat."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 4. The 5-layer stack partitions persistence: Session history (what happened in this task), Project (what belongs to this continuing body of work), Semantic memory (cross-session facts/preferences), Standing instructions (recurring behavioral rules), and User-owned context files. A dedicated Project workspace is the exact architectural layer engineered for an ongoing multi-task initiative with shared reference files and guidelines.",
            "distractor_A": "Option A is incorrect because the Task Filesystem is Tier 1 scratch space that gets wiped when each task ends.",
            "distractor_B": "Option B is incorrect because storing a 20-page commercial rubric in global personal memory pollutes unrelated chat contexts.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because browser cache history is a client web artifact, not an agent persistence layer."
        }
    },
    {
        "id": 12,
        "subtopic": "The Old Session Fallacy",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 620-625)",
        "scenario": "An accountant preparing corporate quarterly tax filings maintains a single 400-turn chat conversation that began eight months ago. When asked why she refuses to start a fresh session, she replies: 'If I start a new chat, the AI will forget my company's accounting rules.' Why does Section 4 label this practice an anti-pattern?",
        "options": {
            "A": "Old chat conversations automatically convert financial numbers into random negative integers after 100 turns.",
            "B": "Enterprise cloud security protocols automatically delete all active conversations at midnight every Friday.",
            "C": "Language models refuse to process tax forms unless the user re-enters their credit card details every turn.",
            "D": "An old session is not memory; massive conversation history creates context noise and increases model drift."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 4. The text cautions: 'An old session is not memory. A Project is not memory either. A global instruction is not memory. They all persist, for different reasons... Start a fresh session when the old conversation is noise. Continue when the history is part of the job. Memory does not replace deliberate context.' Long monolithic sessions degrade performance through context contamination and cost, whereas durable rules belong in Projects or instructions.",
            "distractor_A": "Option A is incorrect because language models do not deliberately invert numbers based on turn counts.",
            "distractor_B": "Option B is incorrect because platform sessions persist in account storage and are not purged weekly.",
            "distractor_C": "Option C is incorrect because models do not demand credit card re-entry during standard conversational sessions.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 13,
        "subtopic": "Semantic Memory Controls in Claude Cowork",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 620-631)",
        "scenario": "A talent recruitment coordinator uses Claude Cowork for executive candidate research. Following the August 2026 update, Claude notices that the coordinator prefers candidates with medical device experience. How is this preference managed across the Cowork ecosystem?",
        "options": {
            "A": "It enters shared cloud Semantic Memory, where the user can inspect, edit, or delete the topic at any time.",
            "B": "It is permanently etched into the underlying foundational model weights during overnight retraining runs.",
            "C": "It is broadcast automatically to public recruitment job boards via an unauthenticated webhook integration.",
            "D": "It is saved exclusively to local laptop hard drives and cannot be accessed from cloud Cowork sessions."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 4. The August 25 update integrated semantic memory across Claude chat and cloud Cowork: 'Cloud Cowork tasks now use the same memory as Claude chat, so what Claude remembers from chat can reach a cloud Cowork task, and what matters in Cowork can carry back. You can inspect memory topic by topic and edit or delete it.' It is inspectable and user-governed, not baked into base weights.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because user preferences are stored in retrieval memory, not fine-tuned into base model weights.",
            "distractor_C": "Option C is incorrect because private conversational memory is never broadcast to external public job boards.",
            "distractor_D": "Option D is incorrect because cloud Cowork memory is hosted in the vendor's cloud and synchronizes across cloud surfaces."
        }
    },
    {
        "id": 14,
        "subtopic": "The Strategic Role of Portable Context Files (`CLAUDE.md`)",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 632-635)",
        "scenario": "A software agency operations lead directs multiple client projects across Claude Cowork, Claude Code, and local command-line tools. Why does Section 4 recommend maintaining a standalone `CLAUDE.md` file rather than relying solely on vendor-managed account memory?",
        "options": {
            "A": "Vendor cloud servers refuse to execute code unless a markdown file is cryptographically signed by an auditor.",
            "B": "A markdown file provides an inspectable, version-controlled, vendor-neutral source of truth you own and export.",
            "C": "Creating a `CLAUDE.md` file grants the user unlimited free compute tokens on commercial cloud platforms.",
            "D": "Local markdown files prevent computers from experiencing physical hardware overheating during agent runs."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 4. The text explains: 'CLAUDE.md is a plain markdown file of standing instructions that some Claude tools read at the start of a task. It makes an excellent portable context file. But native memory and instructions are first-class mechanisms now. Use the file for portability... give critical state a portable source of truth you control.' It ensures instructions are readable, versioned, and independent of vendor lock-in.",
            "distractor_A": "Option A is incorrect because agent tools do not require cryptographic auditor signatures on markdown files.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because text instruction files do not bypass metered token usage or grant free compute.",
            "distractor_D": "Option D is incorrect because software configuration files have no relationship to CPU thermal thermodynamics."
        }
    },
    {
        "id": 15,
        "subtopic": "Switching Costs and Persistence Architecture",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 4: The account spine (Lines 636-639)",
        "scenario": "A financial advisory firm consolidates all of its client portfolio tracking, custom prompt instructions, and historical session logs inside a single commercial AI vendor's proprietary cloud workspace. What significant strategic risk does Section 4 highlight regarding this approach?",
        "options": {
            "A": "Proprietary cloud workspaces automatically publish confidential client portfolios to public social media platforms.",
            "B": "Commercial language models experience catastrophic syntax failure whenever portfolio balances exceed one million dollars.",
            "C": "Accumulated state creates high switching costs and vendor lock-in unless durable assets exist in portable formats.",
            "D": "Cloud vendors are legally required to confiscate client investment assets if an organization changes software providers."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 4. The text warns: 'The convenience has a price, and the price is custody and dependency. Vendor-managed memory, Projects, sessions, plugins, and files are useful because they pile up, which also makes the account sticky. So keep operational state in the vendor spine while work is active, and give critical state a portable source of truth you control.'",
            "distractor_A": "Option A is incorrect because commercial enterprise platforms maintain private tenant isolation and do not publish to social media.",
            "distractor_B": "Option B is incorrect because large numbers do not trigger model syntax compilation crashes.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because cloud software vendors hold no legal authority to seize client financial assets."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 4: The Three File Tiers & Custody Discipline (Q16 - Q20)
    # ----------------------------------------------------
    {
        "id": 16,
        "subtopic": "The Three File Tiers Defined",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 658-666)",
        "scenario": "A hospital billing administrator audits an automated claim reconciliation workflow. The workflow generates temporary math scratch files, saves monthly summary tables in the user's platform workspace, and deposits signed reimbursement PDFs into the hospital's secure AWS S3 archive. How do these three locations map to the Three File Tiers?",
        "options": {
            "A": "Scratch files are Tier 2 (Platform); monthly tables are Tier 1 (Task Filesystem); S3 PDFs are Tier 3 (Exit).",
            "B": "Scratch files are Tier 3 (Exit); monthly tables are Tier 2 (Platform); S3 PDFs are Tier 1 (Task Filesystem).",
            "C": "Scratch files are Tier 2 (Platform); monthly tables are Tier 3 (Exit); S3 PDFs are Tier 1 (Task Filesystem).",
            "D": "Scratch files are Tier 1 (Task Filesystem); monthly tables are Tier 2 (Platform); S3 PDFs are Tier 3 (Exit)."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 5. Tier 1 is the Task Filesystem (temporary scratch space on vendor servers, wiped when work finishes). Tier 2 is Platform Storage (files saved to your account in vendor custody, surviving the task and tab). Tier 3 is The Exit (files entering a system under user/firm control, such as a secure AWS S3 bucket, Google Drive, or on-prem repository).",
            "distractor_A": "Option A is incorrect because scratch files are Tier 1 and monthly workspace tables are Tier 2.",
            "distractor_B": "Option B is incorrect because temporary scratch work is never Tier 3, and S3 archives are not Tier 1.",
            "distractor_C": "Option C is incorrect because scratch work is Tier 1, and external cloud archives are Tier 3.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 17,
        "subtopic": "The Signature Custody Discipline",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 668-674)",
        "scenario": "A corporate compliance officer reviews an AI workflow that drafts formal employee disciplinary letters. The lead analyst intends to leave the finalized letters stored exclusively in the cloud workspace session history. What signature rule from Chapter 9 does this violate?",
        "options": {
            "A": "Finished work exits the platform; deliverables left in Tier 2 remain hostage to vendor custody and retention rules.",
            "B": "All disciplinary letters must be etched onto physical metallic plates before being shown to human resources.",
            "C": "Language models are legally barred from drafting letters that contain employee names or corporate job titles.",
            "D": "Cloud platform storage automatically converts confidential human resource files into publicly accessible web links."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 5. The text establishes the defining discipline: 'Finished work exits the platform. Everything else may stay... A deliverable that exists only in tier 2 is safe today and hostage tomorrow, because it survives only in someone else's custody. A deliverable in tier 3 is yours, under your retention rules, and still there if the vendor's product changes shape.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because disciplinary documentation does not require physical metal engraving.",
            "distractor_C": "Option C is incorrect because models routinely process HR drafts under appropriate authorization and human review.",
            "distractor_D": "Option D is incorrect because Tier 2 platform storage is private to the authenticated account and not automatically made public."
        }
    },
    {
        "id": 18,
        "subtopic": "Public URLs vs. True Custody (ChatGPT Sites)",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 676-677)",
        "scenario": "A marketing specialist uses ChatGPT Work to build an interactive campaign analytics dashboard, which he publishes to a live web URL using ChatGPT Sites. The specialist reports to his director: 'This dashboard is now securely preserved in Tier 3.' Why does Section 5 refute this classification?",
        "options": {
            "A": "Interactive web dashboards are technically incapable of rendering charts unless hosted on local intranet servers.",
            "B": "A platform-hosted Site is Tier 2 with a public door; it remains under vendor custody rather than firm infrastructure.",
            "C": "Publishing a website immediately revokes the enterprise's copyright ownership over all marketing campaign assets.",
            "D": "Websites generated by artificial intelligence models automatically expire after exactly twelve elapsed seconds."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 5. The text explains: 'Sites can publish a finished web app or dashboard to a shareable URL. But a Site hosted on the platform is still tier 2 with a public door, not tier 3 in your own custody.' It remains hosted on OpenAI's infrastructure, subject to vendor platform availability, format, and access policies.",
            "distractor_A": "Option A is incorrect because modern cloud web apps render complex charts seamlessly across public and private networks.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because hosting on a vendor platform does not automatically transfer copyright ownership to the public domain.",
            "distractor_D": "Option D is incorrect because hosted sites persist indefinitely according to platform account retention terms."
        }
    },
    {
        "id": 19,
        "subtopic": "Enforcing the Tier Decision in Briefs",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 5: The three file tiers (Lines 680-686)",
        "scenario": "A procurement manager drafts an autonomous agent brief to analyze vendor bids and generate a contract award recommendation memo. To prevent generated deliverables from getting lost in scratch space or locked in vendor custody, which specific instruction should terminate the brief?",
        "options": {
            "A": "Encrypt all output text using custom hexadecimal rot13 ciphers before printing to the user screen terminal.",
            "B": "Re-run the entire bid evaluation five times consecutively and take the mathematical average of the token counts.",
            "C": "List every file created and its destination tier: temporary scratch, platform storage, or a system I control.",
            "D": "Mandate that the agent delete the vendor's cloud server database upon completing the contract award analysis."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 5. Section 5 provides the exact operational instruction to enforce custody discipline: 'End by listing every file you created and where each one landed: temporary working space, platform storage, or a system I control (connector save, download, local write, or repo commit).' This turns invisible default storage into an auditable operational decision.",
            "distractor_A": "Option A is incorrect because obscuring text with rot13 ciphers prevents human review and does not resolve file custody.",
            "distractor_B": "Option B is incorrect because averaging token counts does not verify output quality or specify file storage locations.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because deleting remote databases is destructive and technically impossible for standard agent accounts."
        }
    },
    {
        "id": 20,
        "subtopic": "Legal & Operational Risks of Platform Link Sharing",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: Check yourself (Lines 700-707)",
        "scenario": "A senior associate at a commercial litigation firm drafts a critical litigation strategy memo in a web agent session and emails the vendor's platform share link directly to the corporate client. According to the analysis in Section 5, what two major governance failures occurred?",
        "options": {
            "A": "The email protocol automatically deletes text attachments, and the client's screen cannot render web fonts.",
            "B": "The law firm violated state bar rules by using modern computers, and the cloud server bandwidth was exceeded.",
            "C": "The memo was transmitted without a physical wax seal, and the vendor platform charged an unapproved export tariff.",
            "D": "The memo bypassed the firm's matter retention system, and access depends on vendor sharing rules the firm cannot govern."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 5. The check-yourself analysis notes two fundamental failures: 'First, custody. The memo exists only in tier 2, outside the firm's matter folder and retention system, so the firm's record has a hole in it. Second, access. The link's sharing rules are the platform's, not the firm's, and the firm cannot govern what it does not hold. The fix is tier 3. Save the memo into the document management system, then share from there.'",
            "distractor_A": "Option A is incorrect because email gateways support links and modern operating systems render web typography.",
            "distractor_B": "Option B is incorrect because legal ethics permits technology use, and cloud bandwidth was not the root governance issue.",
            "distractor_C": "Option C is incorrect because wax seals and fictional export tariffs are irrelevant to digital custody standards.",
            "distractor_D": "N/A (Correct Option)"
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 5: The Reach Ladder, Browser Paths & Prompt Injection Defense (Q21 - Q25)
    # ----------------------------------------------------
    {
        "id": 21,
        "subtopic": "The Four-Rung Reach Ladder",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: Connectors on the web: reach and exit door in one (Lines 754-761)",
        "scenario": "A healthcare systems administrator must configure an agent to retrieve patient appointment schedules from an internal database. The developer proposes writing a computer-use script that takes screenshots and clicks the desktop screen. Why does Section 6 mandate using a structured connector instead?",
        "options": {
            "A": "Use the most structured tool available; connectors provide bounded permissions and actions with less ambiguity.",
            "B": "Screen-driving scripts consume 100% of municipal electrical grid output and damage physical hardware displays.",
            "C": "Model Context Protocol connectors are legally required to be written exclusively in compiled assembly language.",
            "D": "Computer use scripts are technically incapable of recognizing numbers or dates on computer monitor screens."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 6. The reach ladder establishes the rule: 'Use the most structured tool that can do the job. Connector before browser. Browser before full computer use.' Structured connectors (APIs/MCP) enforce explicit OAuth scopes, clear data schemas, and auditable actions, minimizing the operational ambiguity and injection surface inherent in screen driving.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because screen-driving scripts do not consume municipal power grids or harm monitor hardware.",
            "distractor_C": "Option C is incorrect because MCP servers are commonly authored in high-level languages like TypeScript or Python.",
            "distractor_D": "Option D is incorrect because computer vision models can parse text and numbers from screen captures, albeit with higher error rates."
        }
    },
    {
        "id": 22,
        "subtopic": "Built-in Cowork Browser vs. Claude in Chrome",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 6: Reach path comparison (Lines 762-777, 1128-1133)",
        "scenario": "An investment research associate needs an AI assistant to: (1) scrape quarterly financial disclosures from a public state utility commission portal overnight, and (2) assist him in summarizing a password-protected Bloomberg terminal web tab currently open on his desktop. Which tools should be routed to each task?",
        "options": {
            "A": "Use Claude in Chrome for the overnight public scraping; use an unverified community plugin for the Bloomberg tab.",
            "B": "Use Cowork's built-in browser for the portal task; use Claude in Chrome for the actively open Bloomberg tab.",
            "C": "Use full desktop computer use for both tasks to ensure that all keystrokes are recorded in system kernel logs.",
            "D": "Use an external command-line terminal for the Bloomberg tab; use a phone SMS assistant for the utility portal."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 6 and Section 10. The text distinguishes the two browser paths: 'Use Claude in Chrome when the work is \"help me with this page\" [the user's existing Chrome session, open tabs, and active logins]. Use the built-in browser when the work is \"go handle this website task for me\" [delegated web work with its own separate browser state].'",
            "distractor_A": "Option A is incorrect because Claude in Chrome requires an active user session and is ill-suited for standalone unattended batch scraping.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because full computer use carries the highest operational risk and violates the reach ladder when browser tools exist.",
            "distractor_D": "Option D is incorrect because SMS assistants cannot navigate complex municipal utility portals or parse secure data feeds."
        }
    },
    {
        "id": 23,
        "subtopic": "Browser Trust Boundaries and Stored Credentials",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: Reach path comparison (Lines 764-765, 793-795)",
        "scenario": "A financial controller signs into the company's primary corporate banking portal using Claude Cowork's built-in browser inside Claude Desktop. Why does Section 6 highlight this action as a severe, permanent expansion of the agent's trust boundary?",
        "options": {
            "A": "Signing into a bank portal automatically transfers the corporation's liquid cash reserves into the vendor's stock.",
            "B": "The browser software deletes the user's operating system credentials and forces a complete hardware reformat.",
            "C": "Saved login state in the built-in browser becomes accessible to future unattended Cowork sessions on that machine.",
            "D": "Federal banking regulations automatically suspend commercial banking licenses whenever AI tools navigate web forms."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 6. The text explicitly warns: 'The built-in browser starts separate from your personal browser state. You can sign in as needed... That creates a new trust boundary. Anything you sign into inside Claude's browser can reach future Cowork sessions on that computer. Treat browser login state as a permission... Do not casually import or reuse logins for banking, medical, identity, or other highly sensitive systems.'",
            "distractor_A": "Option A is incorrect because browser logins do not automatically trigger unauthorized equity transfers.",
            "distractor_B": "Option B is incorrect because browser cookies and sessions do not wipe operating system installations.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because banking licenses are not revoked simply because automated tools render banking HTML pages."
        }
    },
    {
        "id": 24,
        "subtopic": "Prompt Injection Dual Condition and Defense Rules",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: The security model changes (Lines 780-792)",
        "scenario": "A real estate property manager configures an agent to read incoming tenant email inquiries and autonomously execute lease contract modifications in the property management database. According to Section 6, why is this specific architecture exceptionally dangerous?",
        "options": {
            "A": "Email servers automatically corrupt database records whenever incoming messages contain grammatical mistakes.",
            "B": "Real estate lease contracts are legally invalid unless hand-written in blue ink on sheepskin parchment paper.",
            "C": "Language models refuse to process tenant emails unless every tenant provides a notarized biometric passport copy.",
            "D": "The agent reads untrusted outside content while holding authority to take consequential, hard-to-reverse actions."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 6. Section 6 identifies the critical dual condition that creates acute risk: '1. the agent can read content outside your trusted boundary, AND 2. the agent can take a consequential action... Prompt injection means hidden instructions placed in a webpage, email, document, or connector result, written to redirect the agent... Your brief is authority. Outside content is evidence, never a new boss.' An attacker can embed instructions in an email that hijack the model into modifying database records.",
            "distractor_A": "Option A is incorrect because email typos do not cause mechanical database corruption.",
            "distractor_B": "Option B is incorrect because modern digital real estate contracts are recognized under electronic signature statutes.",
            "distractor_C": "Option C is incorrect because language models do not require biometric passports to parse incoming email text.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 25,
        "subtopic": "Permission Scopes, Blast Radius, and Plugins",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: The security model changes (Lines 799-803)",
        "scenario": "A school administrator installs a third-party 'Parent Communications' plugin in Claude Cowork. The plugin requests permissions to read incoming parent emails and send outgoing messages. The administrator reasons: 'Since it only reads emails to draft responses, granting write access is harmless.' How does Section 6 evaluate this decision?",
        "options": {
            "A": "Granting send authority widens blast radius; read is not send, and scopes must stay least-privileged.",
            "B": "Parent messaging plugins are strictly classified as military munitions under international export bans.",
            "C": "Language models automatically encrypt all outgoing messages using unbreakable quantum key distributions.",
            "D": "Software plugins cannot execute actions unless the user manually checks every token in a hex editor."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 6. The text instructs: 'A permission label is not a formality. Read is not send, draft is not publish, and view is not edit. If a mail connector can read threads, that does not mean it should send as you. Write access is a separate increase in blast radius, which means the worst damage a wrong action can do. Grant the smallest scope that completes the workflow.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because school communication plugins are not restricted under international arms export treaties.",
            "distractor_C": "Option C is incorrect because standard email delivery protocols do not utilize quantum cryptographic distribution.",
            "distractor_D": "Option D is incorrect because plugins execute automated API calls without requiring manual hex editor verification."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 6: The Human Gate, Approval Modes & Blast Radius Calibration (Q26 - Q30)
    # ----------------------------------------------------
    {
        "id": 26,
        "subtopic": "Claude Cowork Approval Modes: Manual vs. Auto vs. Skip",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: The gate in your pocket (Lines 832-858)",
        "scenario": "An operations lead directs a newly designed agent workflow that updates product inventory counts on an e-commerce platform. When selecting an approval mode in Claude Cowork, what operational trade-off distinguishes 'Auto' mode from 'Manual' and 'Skip' modes?",
        "options": {
            "A": "Auto mode forces the user to approve every single HTTP request while skipping all automated safety screening.",
            "B": "Auto mode lets the agent continue while safety classifiers check actions, consuming more allowance for checks.",
            "C": "Auto mode delegates all purchasing decisions to external public stock market automated algorithmic brokers.",
            "D": "Auto mode permanently disables user account access if any inventory number falls below zero units in stock."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 7. In Cowork: Manual pauses for actions needing approval (tightest oversight). Auto lets Claude continue while a safety classifier checks proposed actions for safety, blocking or escalating unsafe ones; these extra checks consume more usage allowance. Skip removes ordinary approval prompts and bypasses Auto's safety action checking, giving maximum autonomy and highest blast radius.",
            "distractor_A": "Option A is incorrect because Manual mode (not Auto) pauses for individual action approvals.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because Auto mode evaluates action safety and has nothing to do with stock market trading.",
            "distractor_D": "Option D is incorrect because inventory data values do not trigger account termination or lockout."
        }
    },
    {
        "id": 27,
        "subtopic": "The Default Fallacy in Side-Panel Approvals",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: The gate in your pocket (Lines 858-863)",
        "scenario": "A junior analyst launches a new workflow in the Claude Cowork Chrome side panel that interacts with a signed-in financial billing portal. The analyst leaves the approval setting on the side panel's default 'Automatically approve'. Why does Section 7 caution against this practice for initial runs?",
        "options": {
            "A": "Side panel extensions automatically bill personal credit cards ten thousand dollars upon initial activation.",
            "B": "Automatic approval modes cause computer monitors to emit high-frequency auditory tones that disrupt office staff.",
            "C": "Product defaults are not risk recommendations; new workflows and signed-in sites should start in Manual mode.",
            "D": "Chrome side panels are legally restricted from accessing internet websites between the hours of 9am and 5pm."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 7. The text cautions: 'The current Cowork side panel defaults to Automatically approve. That is a product default, not a recommendation for every first run. For unfamiliar tools, signed-in sites, new plugins, or high-consequence actions, switch to Manual while you learn the workflow. Once a bounded workflow earns trust, Auto reduces interruptions at the cost of more usage.'",
            "distractor_A": "Option A is incorrect because browser extensions do not charge arbitrary $10,000 credit card penalties.",
            "distractor_B": "Option B is incorrect because software approval modes have no physical capability to emit acoustic tones from monitors.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because browser side panels operate without arbitrary daytime time-of-day restrictions."
        }
    },
    {
        "id": 28,
        "subtopic": "Matching Gates to Blast Radius",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 871-879)",
        "scenario": "A credit union risk officer reviews four proposed automated agent tasks: (1) reading public competitor deposit rates, (2) drafting internal loan summary memos, (3) updating member phone numbers in reversible database logs, and (4) wiring escrow funds to title companies. How should the officer gate these tasks per Section 7?",
        "options": {
            "A": "Set all four tasks to Skip mode to maximize operational processing velocity across credit union systems.",
            "B": "Mandate Manual approval for reading rates, while permitting autonomous wiring of title company escrow funds.",
            "C": "Assign tasks 1 and 2 to Manual mode, and assign tasks 3 and 4 to completely unmonitored autonomous execution.",
            "D": "Permit automated execution for reading rates, require review for drafts, and enforce strict Manual gates for wiring."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 7. The autonomy ladder matches gates to consequence: 1. Read and summarize (low consequence $\\rightarrow$ automatic execution often reasonable). 2. Draft but do not send (medium consequence $\\rightarrow$ reviewable before leaving). 3. Write to reversible records (higher consequence $\\rightarrow$ stronger gate until proven). 4. Send, publish, purchase, delete, or wire funds (high consequence $\\rightarrow$ Manual or explicit human control). Wiring funds carries high blast radius and requires strict manual intervention.",
            "distractor_A": "Option A is incorrect because placing wire disbursements on Skip mode invites catastrophic financial loss.",
            "distractor_B": "Option B is incorrect because gating public reading while automating wire disbursements inverts basic risk management.",
            "distractor_C": "Option C is incorrect because low-risk reading needs less oversight than irreversible record changes or fund transfers.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 29,
        "subtopic": "Action Gate vs. Output Review Thresholds",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 880-883)",
        "scenario": "A clinical data associate builds an agent that reads public medical trial registrations and generates an executive briefing for the Chief Medical Officer. The associate claims: 'Because reading public websites is Rung 1 on the reach ladder, the finished briefing requires zero human review before distribution.' Why is this claim flawed?",
        "options": {
            "A": "Action gates govern what tools may execute; Anthropic review thresholds govern whether results need human review.",
            "B": "Public clinical trial registries are legally prohibited from being viewed on commercial laptop computer screens.",
            "C": "All medical summaries generated by language models must be approved by a unanimous vote of the United Nations.",
            "D": "Executive briefings automatically trigger hospital emergency sirens unless signed with a physical ink pen."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 7. The text emphasizes separating action gates from output review: 'Keep the two sets apart. The rung picks the gate on the action [what the tool may do]. The four thresholds [stakes, reversibility, audience, regulatory exposure] pick the review on the result. A rung-one summary can still need review if it goes to a client, or if the source data is regulated.' A briefing for the CMO carries high audience and stakes, requiring output validation regardless of how safe the input read action was.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because public clinical registries (e.g., ClinicalTrials.gov) are open access documents.",
            "distractor_C": "Option C is incorrect because medical trial summaries do not require international United Nations ratification.",
            "distractor_D": "Option D is incorrect because hospital emergency sirens are not connected to digital executive document workflows."
        }
    },
    {
        "id": 30,
        "subtopic": "Testing the Escalation Path",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 884-885)",
        "scenario": "A municipal transport planner prepares to launch an unattended scheduled agent that monitors traffic sensor feeds and posts road closure advisories. Before enabling recurring execution, the planner creates a synthetic test step that requires manual confirmation and walks away. Why does Section 7 require this test?",
        "options": {
            "A": "Walking away during an agent run is required by federal labor laws to ensure operators take ergonomic desk breaks.",
            "B": "An untested escalation path is only an assumption; operators must verify that requests reach a monitored surface.",
            "C": "Synthetic test steps force the language model to download updated road map geography files from cloud servers.",
            "D": "Testing escalation paths permanently immunizes cloud software platforms against all hardware hardware faults."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 7. The text instructs: 'Before you trust an unattended workflow, ring the gate on purpose. Create one harmless step that should need your input, start the task, walk away, and confirm the request reaches a surface you actually watch. Then deny or approve it and confirm the run responds correctly. An untested escalation path is only an assumption.' If the operator does not receive the prompt, the unattended workflow will stall silently.",
            "distractor_A": "Option A is incorrect because the escalation test is a systems verification protocol, not an ergonomic break mandate.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because testing an approval prompt does not trigger geographic map data downloads.",
            "distractor_D": "Option D is incorrect because software escalation tests cannot prevent physical hardware server component failures."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 7: The Unwatched Delegation Loop & Device-Independent Scheduling (Q31 - Q35)
    # ----------------------------------------------------
    {
        "id": 31,
        "subtopic": "Workflow Discovery Interviews",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 8: The delegation loop: brief, plan, approve, review (Lines 911-917, 978-984)",
        "scenario": "A logistics director spends two hours every Friday manually reconciling freight shipping manifests across three legacy portals, frequently missing discrepancies. She wants to delegate this to an agent but cannot clearly define the decision logic. According to Section 8, what is the best initial prompt?",
        "options": {
            "A": "Paste a single massive 500-line prompt guessing all edge cases and demanding immediate autonomous execution.",
            "B": "Command the agent to delete all discrepancies from the legacy portals to ensure the manifest balances to zero.",
            "C": "Describe the operational frustration and ask the agent to interview her until the workflow is fully understood.",
            "D": "Order the agent to rewrite the legacy portal source code into a mobile gaming application over the weekend."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 8. The text highlights workflow discovery: 'A common beginner mistake is to reach for a longer prompt. Often the better first move is workflow discovery, which means letting the agent help you find the procedure you cannot yet describe... \"Every Monday I spend an hour checking three places and still miss something. Interview me until you understand what I am trying to accomplish, what sources matter, what I never want changed, and what a good finished brief looks like. Then propose the workflow before doing it.\"'",
            "distractor_A": "Option A is incorrect because guessing complex procedures in a monolithic prompt leads to brittle, flawed automations.",
            "distractor_B": "Option B is incorrect because deleting data discrepancies conceals freight errors rather than auditing them.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because rewriting enterprise portal systems into mobile games is irrelevant and absurd."
        }
    },
    {
        "id": 32,
        "subtopic": "Plan-First Requirement in the Four-Step Delegation Loop",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 8: The delegation loop (Lines 918-933)",
        "scenario": "An investment analyst sets Claude Cowork to 'Manual' mode and assumes that because Manual mode pauses before individual tool actions, Claude will automatically generate a complete step-by-step plan for approval before starting work. Why does Section 8 warn that this assumption is incorrect?",
        "options": {
            "A": "Manual mode is technically incapable of running in web browsers without purchasing a physical hardware dongle.",
            "B": "Claude is programmed to ignore all user instructions whenever financial investment assets are mentioned in text.",
            "C": "Manual mode automatically converts all text plans into encrypted voice recordings that cannot be reviewed.",
            "D": "Manual mode pauses before individual actions; an upfront plan is an explicit prompt instruction you must brief."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 8. The text highlights a critical callout: 'Plan-first is an instruction, not a guarantee of Manual mode. In the current Cowork side panel, Manual mode does not automatically create a plan for you to approve before starting. Claude may ask clarifying questions, then begins work and asks before individual actions. If you want the Concept 8 safety intercept, put it in the brief: \"Show me your plan first and wait for my approval before taking consequential actions.\"'",
            "distractor_A": "Option A is incorrect because Manual mode is a native software setting requiring no physical hardware dongles.",
            "distractor_B": "Option B is incorrect because Claude processes financial analysis tasks compliant with standard usage guidelines.",
            "distractor_C": "Option C is incorrect because plans are rendered in plain text rather than obfuscated audio recordings.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 33,
        "subtopic": "The Anti-Hallucination Clause for Unattended Work",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 8: A brief for work you will not watch (Lines 948-953)",
        "scenario": "A clinical research associate authors a brief for an unattended agent task that scans five medical journals overnight and compiles an adverse reaction summary. According to Section 8, which critical boundary line must be explicitly included to prevent cascading hallucinations while the associate sleeps?",
        "options": {
            "A": "If the necessary evidence is missing, state what is missing and halt rather than inventing plausible data.",
            "B": "If any medical journal article is behind a paywall, charge personal credit cards up to five thousand dollars.",
            "C": "If adverse reactions are detected, immediately dispatch an automated ambulance to the journal author's home.",
            "D": "If text contains complex chemical terminology, translate all sentences into seventeenth-century Latin prose."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 8. The text emphasizes: 'Then add one line beginners routinely leave out: \"If the necessary evidence is missing, say what is missing and stop rather than inventing it.\" That line matters more in unattended work, because a confident invention can otherwise travel through several steps before you see it.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because authorizing unconstrained credit card charges exposes the researcher to severe financial loss.",
            "distractor_C": "Option C is incorrect because automated emergency medical dispatching based on literature reviews is completely inappropriate.",
            "distractor_D": "Option D is incorrect because translating medical reports into archaic Latin destroys operational clarity."
        }
    },
    {
        "id": 34,
        "subtopic": "The Device-Independence Rule for Scheduled Tasks",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 9: Scheduled tasks with no device online (Lines 995-1008, 1041-1046)",
        "scenario": "A marketing operations specialist creates a weekly recurring task scheduled to run every Monday at 6:00 AM. The task reads campaign statistics from Google Drive via a cloud connector, checks an active project tracking spreadsheet on his sleeping laptop via a desktop bridge, and emails a summary. What will happen on Monday morning?",
        "options": {
            "A": "The cloud task automatically awakens the physical laptop from across the internet by bypassing office power cords.",
            "B": "The task fails or produces an incomplete report because the bridged local file is unreachable while the laptop sleeps.",
            "C": "The scheduled task transfers its execution to the Google Drive cloud servers and re-formats the spreadsheet.",
            "D": "The cloud platform sends a physical mail courier to the specialist's residence to retrieve the laptop hard drive."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 9. The cardinal rule of scheduling states: 'A schedule is truly device-independent only if every required tool is also reachable without your device.' While the cloud agent loop fires on schedule and reads Google Drive, the bridged local spreadsheet requires the desktop app to be awake and connected. Without it, the bridged tool is unavailable and the task cannot complete normally.",
            "distractor_A": "Option A is incorrect because cloud software cannot wirelessly bypass disconnected power supplies to boot sleeping hardware.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because Google Drive storage APIs do not execute arbitrary external agent loops.",
            "distractor_D": "Option D is incorrect because cloud software platforms do not dispatch physical courier personnel."
        }
    },
    {
        "id": 35,
        "subtopic": "Runtime Evidence vs. Outcome Evidence ('Ran is Not Worked')",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 9: Ran is not the same as worked (Lines 1015-1023)",
        "scenario": "A facilities manager inspects an automated scheduled agent that checks HVAC temperature logs every morning at 5:00 AM. The cloud scheduler console displays a green checkmark indicating 'Status: Completed (Exit Code 0)'. Why does Section 9 insist that 'ran is not the same as worked'?",
        "options": {
            "A": "Green checkmarks in web consoles indicate that the cloud server was infected by a malicious computer virus.",
            "B": "Exit Code 0 is technically reserved for tasks that encountered fatal syntax crashes during loop initialization.",
            "C": "Runtime completion proves the mechanism fired; only verified Tier 3 deliverables prove the work was successful.",
            "D": "HVAC temperature sensors are legally prohibited from communicating with artificial intelligence software models."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 9. The text insists: 'Ran is not the same as worked. A scheduler can tell you that a run started or completed. That does not prove the output was correct, complete, or delivered. Give every recurring workflow an observable success signal: items processed, a dated file created, the tier-3 destination used, or an explicit \"no new items\" result.' Runtime success is not proof of substantive outcome accuracy.",
            "distractor_A": "Option A is incorrect because standard success status indicators do not denote malware infection.",
            "distractor_B": "Option B is incorrect because Exit Code 0 is the universal computing standard for clean execution without unhandled errors.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because industrial IoT sensors routinely interface with analytical and AI systems."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 8: Operational Routing, Compliance Boundaries & Rented vs. Owned Harnesses (Q36 - Q40)
    # ----------------------------------------------------
    {
        "id": 36,
        "subtopic": "The Three Routing Questions",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Web, desktop, or terminal (Lines 1057-1070)",
        "scenario": "An enterprise systems architect establishes an intake standard for internal AI automation requests. Rather than allowing employees to select tools based on recent product hype, the architect mandates evaluating three decisive questions from Section 10. Which three questions govern this operational routing?",
        "options": {
            "A": "Which model has the highest benchmark score, which vendor has the most funding, and which UI looks modern?",
            "B": "What color is the application icon, how many employees follow the vendor on Twitter, and what is token cost?",
            "C": "How fast does the user type prompts, which monitor brand is used, and what is the office Wi-Fi bandwidth?",
            "D": "What does the work touch, must it run while devices are off, and who is allowed to hold and process the data?"
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 10. The three governing routing questions are: 1. What does the work touch? (files, connectors, databases, codebases). 2. Must it run while my device is off? (cloud vs. local dependency). 3. Who is allowed to hold and process the data? (compliance, regulatory custody, BAA coverage).",
            "distractor_A": "Option A is incorrect because raw benchmark scores and vendor venture funding do not determine workflow routing.",
            "distractor_B": "Option B is incorrect because superficial UI colors and social media metrics are irrelevant to systems architecture.",
            "distractor_C": "Option C is incorrect because user typing speed and monitor brands do not dictate data custody or runtime boundaries.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 37,
        "subtopic": "HIPAA, PHI, and BAA Realities on Managed Surfaces",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Regulated or contractually restricted data (Lines 1118-1123, 1751, 1761)",
        "scenario": "A hospital clinical research administrator wants to deploy Claude Cowork to summarize electronic health records containing patient names and cancer staging diagnoses. The administrator points out that the hospital holds an Enterprise agreement with Anthropic. Why does Section 10 forbid this deployment?",
        "options": {
            "A": "Cowork is not covered under Anthropic's BAA for HIPAA use; enterprise account visibility is not legal permission.",
            "B": "Electronic health records are technically incapable of being converted into digital text format for AI review.",
            "C": "HIPAA regulations require that all cancer patient records be reviewed exclusively by veterinary medicine doctors.",
            "D": "Commercial AI models refuse to process medical terms unless approved by an act of the United States Congress."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 10. The text explicitly warns: 'Anthropic now exposes Cowork activity to Enterprise compliance tooling... That approves no regulated workload by itself. As of this fact check, Anthropic states that Cowork is not covered under its BAA for HIPAA use. OpenAI makes the same point. Event-triggered Work tasks in ChatGPT for Healthcare are not BAA-covered and must not process PHI. Product availability is not permission.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because EHR systems natively export structured digital records (e.g., HL7, FHIR, text).",
            "distractor_C": "Option C is incorrect because human oncology records are governed by medical boards, not veterinary doctors.",
            "distractor_D": "Option D is incorrect because congressional statutory acts are not required for individual healthcare data processing workflows."
        }
    },
    {
        "id": 38,
        "subtopic": "De-identification as an Operational Routing Strategy",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Regulated or contractually restricted data (Lines 1121-1123)",
        "scenario": "A healthcare insurance claims analyst wants to use Claude Cowork to identify fraudulent billing patterns across 50,000 claim line items. Because Cowork lacks BAA coverage for protected health information, how can the analyst legitimately route this task per Section 10?",
        "options": {
            "A": "Transmit the claims data during weekend hours when federal regulatory compliance officers are out of office.",
            "B": "Strip or mask direct and quasi-identifiers, routing the underlying mathematical billing patterns instead of PHI.",
            "C": "Rename the claim spreadsheet column headers into an invented foreign language to conceal patient identities.",
            "D": "Upload the records to public web forums first and then instruct the agent to scrape the data from the internet."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 10. The text explains: 'Ask what the task needs: the identifiers, or only the pattern. A spending-trend analysis rarely needs customer names. Remove them, check what is left against your organization's standard, and you may not be routing regulated data at all. Removing what the task does not need is a route, not an evasion.' Removing regulated identifiers transforms the payload into safe, non-PHI pattern data.",
            "distractor_A": "Option A is incorrect because regulatory compliance laws apply 24/7 and cannot be bypassed by weekend scheduling.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because translating column names into foreign words does not de-identify underlying patient data.",
            "distractor_D": "Option D is incorrect because publishing confidential patient records to public forums constitutes an egregious data breach."
        }
    },
    {
        "id": 39,
        "subtopic": "The Open Path Trade-Off (Spine vs. Custody)",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 11: The open path: no vendor cloud (Lines 1153-1179)",
        "scenario": "A non-governmental organization handling sensitive political refugee relocation records evaluates whether to adopt commercial web agent platforms or deploy an open-source alternative (like OpenWork with self-hosted models). What fundamental operational trade-off does Section 11 establish between these two paths?",
        "options": {
            "A": "Commercial platforms charge zero dollars for enterprise accounts, whereas open-source tools require gold payments.",
            "B": "Open-source software tools are illegal to run in democratic nations without written United Nations clearance.",
            "C": "Vendors sell a working spine but hold custody; the open path gives custody and choice but requires you to build the spine.",
            "D": "Commercial platforms delete user accounts every twenty-four hours, whereas open tools provide free lifetime hardware."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 11. The fundamental trade is defined succinctly: 'The companies sell you a spine. The open path makes you build one. On the vendor surface, everything is handed to you and working on day one: sessions, files, sync, the phone gate, the scheduler. But it lives in their custody, in their format, at their price. On the open path, each of those is yours to set up, run, and fix. In exchange you get two things no vendor sells. First, custody, meaning your data on machines you control. Second, choice, meaning which model sees your prompts.'",
            "distractor_A": "Option A is incorrect because commercial platforms charge subscription fees and open-source models do not require gold.",
            "distractor_B": "Option B is incorrect because open-source AI software is fully legal and requires no UN permits.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because vendor platforms do not wipe accounts daily, nor does open software supply free hardware.",
        }
    },
    {
        "id": 40,
        "subtopic": "Rented vs. Owned Enforcement Across the Five Harness Verbs",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Appendix D: Harness Engineering, on the web (Lines 1519-1570)",
        "scenario": "A fintech engineering director must decide whether an automated account credit-limit adjustment workflow can remain in a managed Cowork plugin or must transition to an owned harness in CI. According to Appendix D, what condition makes transitioning to an engineered harness mandatory?",
        "options": {
            "A": "When the credit limit adjustment workflow completes its mathematical execution in under fifteen elapsed seconds.",
            "B": "When the fintech firm transitions all of its corporate desktop computers from Windows to macOS laptops.",
            "C": "When the engineering director decides to publish all customer bank balances on public social media websites.",
            "D": "When enforcement rules must be guaranteed by owned infrastructure, CI gates, and code rather than model compliance."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Appendix D. The text outlines when an owned harness is necessary across the five harness verbs (Constrain, Inform, Verify, Correct, Escalate): 'When Harness Engineering becomes necessary: A rule must be enforced even if the model's instructions say otherwise. A path, network destination, branch, command, or data class must be fenced by infrastructure you control. Verification must run as code and block acceptance automatically... The boundary is who enforces the rule. Build your own harness when a control must be provable on your terms.'",
            "distractor_A": "Option A is incorrect because execution latency does not dictate compliance enforcement architecture.",
            "distractor_B": "Option B is incorrect because operating system transitions have no bearing on backend financial risk controls.",
            "distractor_C": "Option C is incorrect because publishing customer balances breaches privacy and banking confidentiality laws.",
            "distractor_D": "N/A (Correct Option)"
        }
    }
]

def validate_and_save():
    print(f"Validating and balancing 40 questions for Chapter 09...")
    assert len(QUESTIONS_CH9) == 40, f"Expected 40 questions, got {len(QUESTIONS_CH9)}"

    # Validate character length variance & key distribution
    max_var = 0
    total_var = 0
    key_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    
    for q in QUESTIONS_CH9:
        key_counts[q["correct"]] += 1
        opts = q["options"]
        lens = [len(opts[k]) for k in ["A", "B", "C", "D"]]
        variance = max(lens) - min(lens)
        total_var += variance
        if variance > max_var:
            max_var = variance
        if variance >= 15:
            print(f"[!] Warning: Question {q['id']} has length variance {variance}: {lens}")
            
    print(f"Option Length Validation:")
    print(f"  - Maximum character variance across any question: {max_var} chars")
    print(f"  - Average character variance across all 40 questions: {total_var / 40:.2f} chars")
    print(f"Answer Key Distribution: {key_counts}")
    
    # Save to questions.json
    out_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(out_dir, "questions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(QUESTIONS_CH9, f, indent=2, ensure_ascii=False)
    print(f"[+] Successfully wrote: {json_path}")

    # Trigger compiler
    workspace_root = os.path.abspath(os.path.join(out_dir, ".."))
    compiler_path = os.path.join(workspace_root, ".agents", "skills", "pcao-f-mcq-compiler", "compile_chapter.py")
    if os.path.exists(compiler_path):
        print(f"[*] Running compiler: {compiler_path}")
        cmd = [sys.executable, compiler_path, "--chapter-dir", out_dir, "--title", "General Agents on the Web"]
        res = subprocess.run(cmd, check=True)
        print(f"[+] Compilation completed with exit code {res.returncode}")
    else:
        print(f"[!] Compiler not found at: {compiler_path}")

if __name__ == "__main__":
    validate_and_save()questions = [
    {
        "id": 1,
        "subtopic": "Chat Box vs. Agent Surface Operational Distinction",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 1: Same address, two different things (Lines 347-372)",
        "scenario": "A pricing manager at a wholesale commercial tyre chain argues that because her team uses claude.ai every morning to draft customer discount letters, they are already running autonomous agents. Which single operational test invalidates this assumption?",
        "options": {
            "A": "If the user stops typing, does the task continue moving toward an outcome, or does the system halt?",
            "B": "If the browser window is resized, does the text reflow automatically into responsive screen columns?",
            "C": "If multiple team members login simultaneously, does the session log out due to concurrent session limits?",
            "D": "If an API key is omitted, does the interface revert immediately to a legacy local command-line prompt?"
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 1. The defining test separating a chat box from an agent surface is: 'If I stop typing, does the work stop? Chat box: yes. Agent surface: no.' Plain chat is synchronous and requires the user to initiate every turn. An agent surface is delegated; once assigned an outcome, it plans, uses tools, and keeps working even if the user stops typing or closes the tab.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because responsive CSS text reflow is a front-end rendering behavior unrelated to agentic delegation.",
            "distractor_C": "Option C is incorrect because concurrent session token management is an authentication rule, not the test for delegated execution.",
            "distractor_D": "Option D is incorrect because web chat interfaces do not revert to command-line prompts when end-users interact without developer API keys."
        }
    },
    {
        "id": 2,
        "subtopic": "The Two-Axis Runtime Model",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 2: The remote session: the tab is a window, not the runtime (Lines 381-395)",
        "scenario": "A clinical operations analyst configures a delegated patient intake summary task in Claude Cowork. She assumes that because she opened the session in her laptop's web browser, the model execution and data processing are restricted entirely to her local hardware. Why is this technical assumption invalid?",
        "options": {
            "A": "Web browsers automatically redirect all encrypted data packets into decentralized public blockchain nodes.",
            "B": "The browser tab is merely a remote viewing window; the agent loop and processing run on vendor cloud servers.",
            "C": "Local machine hardware lacks the mathematical instruction set required to render web application user interfaces.",
            "D": "Desktop browser sessions are legally prohibited from executing basic string parsing without government oversight."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 2. The chapter instructs operators to separate two runtime questions: Axis 1 (where does the agent loop run?) and Axis 2 (where does each tool execute?). In a cloud session, planning, tool selection, code execution, and task state run on the vendor's servers. The browser tab is only a viewing window onto an active cloud session ID.",
            "distractor_A": "Option A is incorrect because commercial AI vendors do not transmit customer data to public decentralized blockchain nodes.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because client laptops routinely render complex browser interfaces and can run local code when configured.",
            "distractor_D": "Option D is incorrect because local text parsing requires no regulatory legal licensing or external oversight."
        }
    },
    {
        "id": 3,
        "subtopic": "Cloud Session plus Desktop Bridge Offline Failure Modes",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 2: The remote session: the tab is a window, not the runtime (Lines 414-434, 461-465)",
        "scenario": "A logistics coordinator launches a cloud Cowork task that analyzes warehouse shipment records from Google Drive and correlates them with inventory spreadsheets stored in a folder connected through Claude Desktop. Halfway through execution, the coordinator closes her laptop. How will the session behave?",
        "options": {
            "A": "The entire cloud session terminates immediately and permanently erases all processed Google Drive outputs.",
            "B": "The agent loop migrates its execution context to the warehouse local area network routers to complete the run.",
            "C": "The cloud loop continues running with cloud tools, but the bridged local folder disappears from the session.",
            "D": "The session pauses and broadcasts an emergency SMS verification code to the corporate fleet supervisor."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 2. In a hybrid pattern (cloud loop plus desktop bridge), the agent loop runs remotely on vendor infrastructure. If the laptop disconnects or sleeps, the cloud session remains active and continues using cloud-reachable tools (like Google Drive). However, tools borrowed across the desktop bridge vanish. The operational diagnosis is that a tool became unavailable, not that Cowork stopped running.",
            "distractor_A": "Option A is incorrect because closing the laptop does not terminate the remote cloud loop or wipe cloud-synced deliverables.",
            "distractor_B": "Option B is incorrect because cloud agent loops cannot dynamically transfer execution to local networking hardware.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because losing a bridged tool does not trigger automated SMS emergency dispatching."
        }
    },
    {
        "id": 4,
        "subtopic": "Desktop Bridge Data Custody Realities",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 2: Four consequences (Lines 442-450) & Concept 10 (Lines 1124-1127)",
        "scenario": "A legal ops director reviews an analyst who processed privileged corporate merger documents by connecting a local folder to a cloud Cowork session via Claude Desktop. The analyst asserts: 'Because the files sat on my MacBook hard drive, their contents never left my machine.' Why is this assertion false?",
        "options": {
            "A": "MacBook operating systems automatically duplicate local text files into public peer-to-peer torrent networks.",
            "B": "Connecting a folder permanently transfers physical hardware drive ownership rights to the software vendor.",
            "C": "Local desktop folders cannot be read by software tools unless the hard drive is completely unencrypted.",
            "D": "Local files opened across a desktop bridge are transmitted to and processed within the vendor's cloud runtime."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 2 and Section 10. The text explicitly warns: 'A local file opened this way is processed in the vendor's cloud... A bridge is a convenience, not a custody loophole. If a cloud Cowork session reads a local file through Claude Desktop, its contents are processed in Anthropic's cloud. So do not route sensitive work to \"local file\" and assume local custody. The first question is where the processing happens, not where the file was sitting five seconds earlier.'",
            "distractor_A": "Option A is incorrect because macOS does not transmit user documents to peer-to-peer file-sharing networks.",
            "distractor_B": "Option B is incorrect because software connections have no effect on physical hardware property ownership.",
            "distractor_C": "Option C is incorrect because desktop bridge connectors read local file systems without requiring full-disk decryption.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 5,
        "subtopic": "Enterprise Controls: Work Cloud vs. Work Local",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 2: Axis 1 and ChatGPT Work (Lines 436-439)",
        "scenario": "A municipal cybersecurity auditor inspects an enterprise deployment of ChatGPT Work across government workstations. The agency's data retention mandate strictly forbids government records from entering cloud task environments. How can an administrator enforce this boundary within the platform settings?",
        "options": {
            "A": "Enable Work Local controls while disabling Work Cloud, confining agent execution strictly to local machines.",
            "B": "Configure all workstation monitors to run at reduced refresh rates to prevent remote screen capture tools.",
            "C": "Mandate that employees type all prompts exclusively in capital letters to block automated cloud ingestion.",
            "D": "Uninstall web browser extensions while leaving default unauthenticated public cloud ports open on servers."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 2. The text notes that OpenAI exposes Work Cloud and Work Local as separate enterprise administrative controls: 'An administrator can enable Work Local without Work Cloud, so members work locally and cannot start cloud tasks.' This enforces strict data locality by ensuring tasks and files remain on the local device.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because monitor refresh rates have no bearing on network routing or cloud data transmission.",
            "distractor_C": "Option C is incorrect because letter capitalization does not prevent cloud language models from ingesting prompts.",
            "distractor_D": "Option D is incorrect because leaving unauthenticated cloud ports open actively breaches security boundaries."
        }
    },
    {
        "id": 6,
        "subtopic": "The Six-Part Universal Harness Anatomy",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 471-479)",
        "scenario": "An enterprise systems architect evaluates competing agent products from emerging AI startups. Rather than relying on vendor marketing jargon, the architect analyzes their technical execution harness. Which complete set of components represents this universal architectural model?",
        "options": {
            "A": "Prompt optimizer, vector embedding cache, token serializer, gradient checkpoint, loss curve, and hyperparameter.",
            "B": "Heartbeat (trigger), Reach (tools), Run-until-done loop, State spine (persistence), Human gate, and Body (runtime).",
            "C": "Customer billing ledger, sales pipeline CRM, marketing email sequencer, web scraper, analytics tracker, and CMS.",
            "D": "Local subnet mask, default gateway router, DNS resolution table, SSL certificate, firewall rule, and proxy port."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 3. The six universal parts of every serious agent harness are: 1. Heartbeat: what starts a run. 2. Reach: what the run can read and act on. 3. Run-until-done loop: how it keeps moving toward an outcome. 4. State spine: what persists across runs. 5. Human gate: where autonomy stops or gets screened. 6. Body: where the work actually executes.",
            "distractor_A": "Option A is incorrect because token serializers and loss curves are internal model training and inference mechanics.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because CRMs, email sequencers, and CMS platforms are external enterprise business applications.",
            "distractor_D": "Option D is incorrect because subnets, DNS tables, and firewalls are standard networking infrastructure components."
        }
    },
    {
        "id": 7,
        "subtopic": "Claude Cowork vs. ChatGPT Work Packaging Alignment",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 480-547)",
        "scenario": "A technology director compares how Claude Cowork and ChatGPT Work package their respective agent capabilities. When mapping their specific product features to the universal six-part harness, which alignment accurately reflects their structural equivalence?",
        "options": {
            "A": "Cowork Scheduled Tasks represent the Gate, while ChatGPT Work Approval Prompts represent the Heartbeat component.",
            "B": "Cowork MCP Connectors represent the Body, while ChatGPT Work Cloud Sandboxes represent the Reach tool part.",
            "C": "Cowork Connectors and ChatGPT Plugins map to Reach; Cowork Sessions and ChatGPT Synced Sessions map to Spine.",
            "D": "Cowork Manual Mode represents the State Spine, while ChatGPT Work Plan Mode represents the Heartbeat component."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 3 (Figure 3 and comparison table). Connectors in Cowork and Plugins in ChatGPT Work map to Reach (what the agent can read and act on). Saved sessions, Projects, and files map to the State Spine (what persists). Scheduled tasks map to Heartbeat, approval modes map to Gate, and cloud sandboxes/execution environments map to Body.",
            "distractor_A": "Option A is incorrect because Scheduled Tasks are the Heartbeat (trigger), and Approval Prompts are the Gate.",
            "distractor_B": "Option B is incorrect because Connectors represent Reach (tools), while cloud sandboxes represent the Body (execution environment).",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because Manual Mode is a Human Gate setting, and Plan Mode is part of the Run-until-done loop."
        }
    },
    {
        "id": 8,
        "subtopic": "Plan Mode as an Execution Loop Discipline",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 544-545)",
        "scenario": "A product manager notices that ChatGPT Work features an explicit 'Plan mode' that gathers context, asks clarifying questions, and proposes a step-by-step approach before executing actions. How is this feature classified within a standard agent execution harness?",
        "options": {
            "A": "It is an entirely new seventh architectural harness component that replaces the need for a State spine.",
            "B": "It is a hardware virtualization hypervisor that partitions remote cloud CPU cores across tenant accounts.",
            "C": "It is an autonomous network security protocol designed to block denial-of-service traffic on cloud servers.",
            "D": "It is an interactive implementation of the Run-until-done loop that surfaces intent before execution begins."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 3. The text explains: 'ChatGPT Work Plan mode is a current example. It gathers context, asks questions, creates a step-by-step plan, and lets you approve it before execution. That is not a seventh part. It is Concept 8 built into a product.' It operationalizes the Run-until-done loop by making the agent's planned trajectory inspectable before expensive or consequential actions begin.",
            "distractor_A": "Option A is incorrect because Plan mode does not create a seventh component or replace persistent context storage.",
            "distractor_B": "Option B is incorrect because planning is a software reasoning and orchestration layer, not a hardware hypervisor.",
            "distractor_C": "Option C is incorrect because Plan mode addresses task delegation rather than DDoS network traffic filtering.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 9,
        "subtopic": "Identical Shape vs. Identical Trust",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 3: Two warnings (Lines 550-555)",
        "scenario": "An IT compliance officer evaluates an agent workflow that can interact with the corporate CRM either via an authenticated Model Context Protocol (MCP) connector or by driving a web browser through screen clicks. Why does security governance dictate that 'same visible shape does not mean same trust'?",
        "options": {
            "A": "Connectors offer structured, permission-scoped actions, whereas browser automation introduces wider exposure and ambiguity.",
            "B": "Browser-based screen driving is legally recognized as a certified cryptographic signature across all federal jurisdictions.",
            "C": "MCP connectors are technically incapable of transmitting text data across standard internet firewall boundaries.",
            "D": "Web browsers automatically prevent language models from interpreting malicious instructions found in website code."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 3. The text explicitly warns: 'Same shape does not mean same trust. A connector call and a browser click can reach the same business system with different permissions, visibility, and exposure to hidden instructions... Connectors come first because structure gives you clearer permissions, clearer actions, and less ambiguity than screen-driving.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because automated browser clicks do not constitute legally binding cryptographic signatures.",
            "distractor_C": "Option C is incorrect because MCP connectors operate over standard client-server network protocols (e.g., HTTP/SSE, stdio).",
            "distractor_D": "Option D is incorrect because browsers directly expose models to untrusted web content and indirect prompt injections."
        }
    },
    {
        "id": 10,
        "subtopic": "The Harness Wars Market Shift",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Appendix G: The harness war, industry-wide (Lines 1701-1725)",
        "scenario": "A venture partner evaluating artificial intelligence startups notes that frontier model intelligence benchmarks have largely converged. In enterprise deployments, where has the primary competitive differentiation across major frontier AI providers shifted?",
        "options": {
            "A": "Competing exclusively on reducing physical semiconductor chip manufacturing facility construction times.",
            "B": "Competing on the complete agent harness: persistent state, browser reach, tools, schedules, and governance.",
            "C": "Competing on establishing proprietary closed-source programming languages to replace modern JavaScript.",
            "D": "Competing on marketing consumer desktop monitors with higher display pixel resolutions to office workers."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Appendix G. The text emphasizes: 'The durable market signal is not a model ranking. It is that major vendors compete on the whole agent system: memory, tools, browser reach, schedules, plugins, approvals, runtime, identity, and governance. That is the harness war.' The competitive differentiator is the surrounding harness rather than marginal raw model capability.",
            "distractor_A": "Option A is incorrect because AI software vendors compete on software harnesses, not foundry chip fabrication construction.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because AI providers rely on standard languages (Python, TypeScript) rather than replacing JavaScript.",
            "distractor_D": "Option D is incorrect because display hardware manufacturing is unrelated to agent software ecosystem competition."
        }
    },
    {
        "id": 11,
        "subtopic": "The Five Layers of the Persistent Context Stack",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 578-618)",
        "scenario": "A project lead at a commercial property consultancy wants Claude to apply a specific 20-page regional building lease analysis rubric across twelve different property evaluation tasks over the next four months. In which layer of the Persistent Context Stack should this rubric reside?",
        "options": {
            "A": "A single temporary Task Filesystem scratch pad that wipes automatically after each property review runs.",
            "B": "Global user-level Semantic Memory shared indiscriminately across all personal and non-work conversations.",
            "C": "A dedicated Project workspace holding the shared files, instructions, and context for that ongoing workstream.",
            "D": "The browser cache history of the local computer terminal used to launch the first introductory property chat."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 4. The 5-layer stack partitions persistence: Session history (what happened in this task), Project (what belongs to this continuing body of work), Semantic memory (cross-session facts/preferences), Standing instructions (recurring behavioral rules), and User-owned context files. A dedicated Project workspace is the exact architectural layer engineered for an ongoing multi-task initiative with shared reference files and guidelines.",
            "distractor_A": "Option A is incorrect because the Task Filesystem is Tier 1 scratch space that gets wiped when each task ends.",
            "distractor_B": "Option B is incorrect because storing a 20-page commercial rubric in global personal memory pollutes unrelated chat contexts.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because browser cache history is a client web artifact, not an agent persistence layer."
        }
    },
    {
        "id": 12,
        "subtopic": "The Old Session Fallacy",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 620-625)",
        "scenario": "An accountant preparing corporate quarterly tax filings maintains a single 400-turn chat conversation that began eight months ago. When asked why she refuses to start a fresh session, she replies: 'If I start a new chat, the AI will forget my company's accounting rules.' Why is this practice considered an operational anti-pattern?",
        "options": {
            "A": "Old chat conversations automatically convert financial numbers into random negative integers after 100 turns.",
            "B": "Enterprise cloud security protocols automatically delete all active conversations at midnight every Friday.",
            "C": "Language models refuse to process tax forms unless the user re-enters their credit card details every turn.",
            "D": "An old session is not memory; massive conversation history creates context noise and increases model drift."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 4. The text cautions: 'An old session is not memory. A Project is not memory either. A global instruction is not memory. They all persist, for different reasons... Start a fresh session when the old conversation is noise. Continue when the history is part of the job. Memory does not replace deliberate context.' Long monolithic sessions degrade performance through context contamination and cost, whereas durable rules belong in Projects or instructions.",
            "distractor_A": "Option A is incorrect because language models do not deliberately invert numbers based on turn counts.",
            "distractor_B": "Option B is incorrect because platform sessions persist in account storage and are not purged weekly.",
            "distractor_C": "Option C is incorrect because models do not demand credit card re-entry during standard conversational sessions.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 13,
        "subtopic": "Semantic Memory Controls in Claude Cowork",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 620-631)",
        "scenario": "A talent recruitment coordinator uses Claude Cowork for executive candidate research. Following the August 2026 update, Claude notices that the coordinator prefers candidates with medical device experience. How is this preference managed across the Cowork ecosystem?",
        "options": {
            "A": "It enters shared cloud Semantic Memory, where the user can inspect, edit, or delete the topic at any time.",
            "B": "It is permanently etched into the underlying foundational model weights during overnight retraining runs.",
            "C": "It is broadcast automatically to public recruitment job boards via an unauthenticated webhook integration.",
            "D": "It is saved exclusively to local laptop hard drives and cannot be accessed from cloud Cowork sessions."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 4. The August 25 update integrated semantic memory across Claude chat and cloud Cowork: 'Cloud Cowork tasks now use the same memory as Claude chat, so what Claude remembers from chat can reach a cloud Cowork task, and what matters in Cowork can carry back. You can inspect memory topic by topic and edit or delete it.' It is inspectable and user-governed, not baked into base weights.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because user preferences are stored in retrieval memory, not fine-tuned into base model weights.",
            "distractor_C": "Option C is incorrect because private conversational memory is never broadcast to external public job boards.",
            "distractor_D": "Option D is incorrect because cloud Cowork memory is hosted in the vendor's cloud and synchronizes across cloud surfaces."
        }
    },
    {
        "id": 14,
        "subtopic": "The Strategic Role of Portable Context Files (`CLAUDE.md`)",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 632-635)",
        "scenario": "A software agency operations lead directs multiple client projects across Claude Cowork, Claude Code, and local command-line tools. Why is maintaining a standalone project instruction file (e.g., `CLAUDE.md`) operationally superior to relying solely on platform memory?",
        "options": {
            "A": "Vendor cloud servers refuse to execute code unless a markdown file is cryptographically signed by an auditor.",
            "B": "A markdown file provides an inspectable, version-controlled, vendor-neutral source of truth you own and export.",
            "C": "Creating a `CLAUDE.md` file grants the user unlimited free compute tokens on commercial cloud platforms.",
            "D": "Local markdown files prevent computers from experiencing physical hardware overheating during agent runs."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 4. The text explains: 'CLAUDE.md is a plain markdown file of standing instructions that some Claude tools read at the start of a task. It makes an excellent portable context file. But native memory and instructions are first-class mechanisms now. Use the file for portability... give critical state a portable source of truth you control.' It ensures instructions are readable, versioned, and independent of vendor lock-in.",
            "distractor_A": "Option A is incorrect because agent tools do not require cryptographic auditor signatures on markdown files.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because text instruction files do not bypass metered token usage or grant free compute.",
            "distractor_D": "Option D is incorrect because software configuration files have no relationship to CPU thermal thermodynamics."
        }
    },
    {
        "id": 15,
        "subtopic": "Switching Costs and Persistence Architecture",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 4: The account spine (Lines 636-639)",
        "scenario": "A financial advisory firm consolidates all of its client portfolio tracking, custom prompt instructions, and historical session logs inside a single commercial AI vendor's proprietary cloud workspace. What significant operational and strategic risk does this custody model present?",
        "options": {
            "A": "Proprietary cloud workspaces automatically publish confidential client portfolios to public social media platforms.",
            "B": "Commercial language models experience catastrophic syntax failure whenever portfolio balances exceed one million dollars.",
            "C": "Accumulated state creates high switching costs and vendor lock-in unless durable assets exist in portable formats.",
            "D": "Cloud vendors are legally required to confiscate client investment assets if an organization changes software providers."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 4. The text warns: 'The convenience has a price, and the price is custody and dependency. Vendor-managed memory, Projects, sessions, plugins, and files are useful because they pile up, which also makes the account sticky. So keep operational state in the vendor spine while work is active, and give critical state a portable source of truth you control.'",
            "distractor_A": "Option A is incorrect because commercial enterprise platforms maintain private tenant isolation and do not publish to social media.",
            "distractor_B": "Option B is incorrect because large numbers do not trigger model syntax compilation crashes.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because cloud software vendors hold no legal authority to seize client financial assets."
        }
    },
    {
        "id": 16,
        "subtopic": "The Three File Tiers Defined",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 658-666)",
        "scenario": "A hospital billing administrator audits an automated claim reconciliation workflow. The workflow generates temporary math scratch files, saves monthly summary tables in the user's platform workspace, and deposits signed reimbursement PDFs into the hospital's secure AWS S3 archive. How do these three locations map to the Three File Tiers?",
        "options": {
            "A": "Scratch files are Tier 2 (Platform); monthly tables are Tier 1 (Task Filesystem); S3 PDFs are Tier 3 (Exit).",
            "B": "Scratch files are Tier 3 (Exit); monthly tables are Tier 2 (Platform); S3 PDFs are Tier 1 (Task Filesystem).",
            "C": "Scratch files are Tier 2 (Platform); monthly tables are Tier 3 (Exit); S3 PDFs are Tier 1 (Task Filesystem).",
            "D": "Scratch files are Tier 1 (Task Filesystem); monthly tables are Tier 2 (Platform); S3 PDFs are Tier 3 (Exit)."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 5. Tier 1 is the Task Filesystem (temporary scratch space on vendor servers, wiped when work finishes). Tier 2 is Platform Storage (files saved to your account in vendor custody, surviving the task and tab). Tier 3 is The Exit (files entering a system under user/firm control, such as a secure AWS S3 bucket, Google Drive, or on-prem repository).",
            "distractor_A": "Option A is incorrect because scratch files are Tier 1 and monthly workspace tables are Tier 2.",
            "distractor_B": "Option B is incorrect because temporary scratch work is never Tier 3, and S3 archives are not Tier 1.",
            "distractor_C": "Option C is incorrect because scratch work is Tier 1, and external cloud archives are Tier 3.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 17,
        "subtopic": "The Signature Custody Discipline",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 668-674)",
        "scenario": "A corporate compliance officer reviews an AI workflow that drafts formal employee disciplinary letters. The lead analyst intends to leave the finalized letters stored exclusively in the cloud workspace session history. What core deliverable governance rule does this violate?",
        "options": {
            "A": "Finished work exits the platform; deliverables left in Tier 2 remain hostage to vendor custody and retention rules.",
            "B": "All disciplinary letters must be etched onto physical metallic plates before being shown to human resources.",
            "C": "Language models are legally barred from drafting letters that contain employee names or corporate job titles.",
            "D": "Cloud platform storage automatically converts confidential human resource files into publicly accessible web links."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 5. The text establishes the defining discipline: 'Finished work exits the platform. Everything else may stay... A deliverable that exists only in tier 2 is safe today and hostage tomorrow, because it survives only in someone else's custody. A deliverable in tier 3 is yours, under your retention rules, and still there if the vendor's product changes shape.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because disciplinary documentation does not require physical metal engraving.",
            "distractor_C": "Option C is incorrect because models routinely process HR drafts under appropriate authorization and human review.",
            "distractor_D": "Option D is incorrect because Tier 2 platform storage is private to the authenticated account and not automatically made public."
        }
    },
    {
        "id": 18,
        "subtopic": "Public URLs vs. True Custody (ChatGPT Sites)",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 676-677)",
        "scenario": "A marketing specialist uses ChatGPT Work to build an interactive campaign analytics dashboard, which he publishes to a live web URL using ChatGPT Sites. The specialist reports to his director: 'This dashboard is now securely preserved in Tier 3 (Owned Infrastructure).' Why is this classification invalid?",
        "options": {
            "A": "Interactive web dashboards are technically incapable of rendering charts unless hosted on local intranet servers.",
            "B": "A platform-hosted Site is Tier 2 with a public door; it remains under vendor custody rather than firm infrastructure.",
            "C": "Publishing a website immediately revokes the enterprise's copyright ownership over all marketing campaign assets.",
            "D": "Websites generated by artificial intelligence models automatically expire after exactly twelve elapsed seconds."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 5. The text explains: 'Sites can publish a finished web app or dashboard to a shareable URL. But a Site hosted on the platform is still tier 2 with a public door, not tier 3 in your own custody.' It remains hosted on OpenAI's infrastructure, subject to vendor platform availability, format, and access policies.",
            "distractor_A": "Option A is incorrect because modern cloud web apps render complex charts seamlessly across public and private networks.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because hosting on a vendor platform does not automatically transfer copyright ownership to the public domain.",
            "distractor_D": "Option D is incorrect because hosted sites persist indefinitely according to platform account retention terms."
        }
    },
    {
        "id": 19,
        "subtopic": "Enforcing the Tier Decision in Briefs",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 5: The three file tiers (Lines 680-686)",
        "scenario": "A procurement manager drafts an autonomous agent brief to analyze vendor bids and generate a contract award recommendation memo. To prevent generated deliverables from getting lost in scratch space or locked in vendor custody, which specific instruction should terminate the brief?",
        "options": {
            "A": "Encrypt all output text using custom hexadecimal rot13 ciphers before printing to the user screen terminal.",
            "B": "Re-run the entire bid evaluation five times consecutively and take the mathematical average of the token counts.",
            "C": "List every file created and its destination tier: temporary scratch, platform storage, or a system I control.",
            "D": "Mandate that the agent delete the vendor's cloud server database upon completing the contract award analysis."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 5. Section 5 provides the exact operational instruction to enforce custody discipline: 'End by listing every file you created and where each one landed: temporary working space, platform storage, or a system I control (connector save, download, local write, or repo commit).' This turns invisible default storage into an auditable operational decision.",
            "distractor_A": "Option A is incorrect because obscuring text with rot13 ciphers prevents human review and does not resolve file custody.",
            "distractor_B": "Option B is incorrect because averaging token counts does not verify output quality or specify file storage locations.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because deleting remote databases is destructive and technically impossible for standard agent accounts."
        }
    },
    {
        "id": 20,
        "subtopic": "Legal & Operational Risks of Platform Link Sharing",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: Check yourself (Lines 700-707)",
        "scenario": "A senior associate at a commercial litigation firm drafts a critical litigation strategy memo in a web agent session and emails the vendor's platform share link directly to the corporate client. Under document governance standards, what two major operational failures occurred?",
        "options": {
            "A": "The email protocol automatically deletes text attachments, and the client's screen cannot render web fonts.",
            "B": "The law firm violated state bar rules by using modern computers, and the cloud server bandwidth was exceeded.",
            "C": "The memo was transmitted without a physical wax seal, and the vendor platform charged an unapproved export tariff.",
            "D": "The memo bypassed the firm's matter retention system, and access depends on vendor sharing rules the firm cannot govern."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 5. The check-yourself analysis notes two fundamental failures: 'First, custody. The memo exists only in tier 2, outside the firm's matter folder and retention system, so the firm's record has a hole in it. Second, access. The link's sharing rules are the platform's, not the firm's, and the firm cannot govern what it does not hold. The fix is tier 3. Save the memo into the document management system, then share from there.'",
            "distractor_A": "Option A is incorrect because email gateways support links and modern operating systems render web typography.",
            "distractor_B": "Option B is incorrect because legal ethics permits technology use, and cloud bandwidth was not the root governance issue.",
            "distractor_C": "Option C is incorrect because wax seals and fictional export tariffs are irrelevant to digital custody standards.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 21,
        "subtopic": "The Four-Rung Reach Ladder",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: Connectors on the web: reach and exit door in one (Lines 754-761)",
        "scenario": "A healthcare systems administrator must configure an agent to retrieve patient appointment schedules from an internal database. The developer proposes writing a computer-use script that takes screenshots and clicks the desktop screen. Why does integration engineering mandate using a structured API or connector instead?",
        "options": {
            "A": "Use the most structured tool available; connectors provide bounded permissions and actions with less ambiguity.",
            "B": "Screen-driving scripts consume 100% of municipal electrical grid output and damage physical hardware displays.",
            "C": "Model Context Protocol connectors are legally required to be written exclusively in compiled assembly language.",
            "D": "Computer use scripts are technically incapable of recognizing numbers or dates on computer monitor screens."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 6. The reach ladder establishes the rule: 'Use the most structured tool that can do the job. Connector before browser. Browser before full computer use.' Structured connectors (APIs/MCP) enforce explicit OAuth scopes, clear data schemas, and auditable actions, minimizing the operational ambiguity and injection surface inherent in screen driving.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because screen-driving scripts do not consume municipal power grids or harm monitor hardware.",
            "distractor_C": "Option C is incorrect because MCP servers are commonly authored in high-level languages like TypeScript or Python.",
            "distractor_D": "Option D is incorrect because computer vision models can parse text and numbers from screen captures, albeit with higher error rates."
        }
    },
    {
        "id": 22,
        "subtopic": "Built-in Cowork Browser vs. Claude in Chrome",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 6: Reach path comparison (Lines 762-777, 1128-1133)",
        "scenario": "An investment research associate needs an AI assistant to: (1) scrape quarterly financial disclosures from a public state utility commission portal overnight, and (2) assist him in summarizing a password-protected Bloomberg terminal web tab currently open on his desktop. Which tools should be routed to each task?",
        "options": {
            "A": "Use Claude in Chrome for the overnight public scraping; use an unverified community plugin for the Bloomberg tab.",
            "B": "Use Cowork's built-in browser for the portal task; use Claude in Chrome for the actively open Bloomberg tab.",
            "C": "Use full desktop computer use for both tasks to ensure that all keystrokes are recorded in system kernel logs.",
            "D": "Use an external command-line terminal for the Bloomberg tab; use a phone SMS assistant for the utility portal."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 6 and Section 10. The text distinguishes the two browser paths: 'Use Claude in Chrome when the work is \"help me with this page\" [the user's existing Chrome session, open tabs, and active logins]. Use the built-in browser when the work is \"go handle this website task for me\" [delegated web work with its own separate browser state].'",
            "distractor_A": "Option A is incorrect because Claude in Chrome requires an active user session and is ill-suited for standalone unattended batch scraping.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because full computer use carries the highest operational risk and violates the reach ladder when browser tools exist.",
            "distractor_D": "Option D is incorrect because SMS assistants cannot navigate complex municipal utility portals or parse secure data feeds."
        }
    },
    {
        "id": 23,
        "subtopic": "Browser Trust Boundaries and Stored Credentials",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: Reach path comparison (Lines 764-765, 793-795)",
        "scenario": "A financial controller signs into the company's primary corporate banking portal using Claude Cowork's built-in browser inside Claude Desktop. Why is this action considered a severe, permanent expansion of the agent's trust boundary?",
        "options": {
            "A": "Signing into a bank portal automatically transfers the corporation's liquid cash reserves into the vendor's stock.",
            "B": "The browser software deletes the user's operating system credentials and forces a complete hardware reformat.",
            "C": "Saved login state in the built-in browser becomes accessible to future unattended Cowork sessions on that machine.",
            "D": "Federal banking regulations automatically suspend commercial banking licenses whenever AI tools navigate web forms."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 6. The text explicitly warns: 'The built-in browser starts separate from your personal browser state. You can sign in as needed... That creates a new trust boundary. Anything you sign into inside Claude's browser can reach future Cowork sessions on that computer. Treat browser login state as a permission... Do not casually import or reuse logins for banking, medical, identity, or other highly sensitive systems.'",
            "distractor_A": "Option A is incorrect because browser logins do not automatically trigger unauthorized equity transfers.",
            "distractor_B": "Option B is incorrect because browser cookies and sessions do not wipe operating system installations.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because banking licenses are not revoked simply because automated tools render banking HTML pages."
        }
    },
    {
        "id": 24,
        "subtopic": "Prompt Injection Dual Condition and Defense Rules",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: The security model changes (Lines 780-792)",
        "scenario": "A real estate property manager configures an agent to read incoming tenant email inquiries and autonomously execute lease contract modifications in the property management database. From a security and prompt injection perspective, why is this architecture exceptionally dangerous?",
        "options": {
            "A": "Email servers automatically corrupt database records whenever incoming messages contain grammatical mistakes.",
            "B": "Real estate lease contracts are legally invalid unless hand-written in blue ink on sheepskin parchment paper.",
            "C": "Language models refuse to process tenant emails unless every tenant provides a notarized biometric passport copy.",
            "D": "The agent reads untrusted outside content while holding authority to take consequential, hard-to-reverse actions."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 6. Section 6 identifies the critical dual condition that creates acute risk: '1. the agent can read content outside your trusted boundary, AND 2. the agent can take a consequential action... Prompt injection means hidden instructions placed in a webpage, email, document, or connector result, written to redirect the agent... Your brief is authority. Outside content is evidence, never a new boss.' An attacker can embed instructions in an email that hijack the model into modifying database records.",
            "distractor_A": "Option A is incorrect because email typos do not cause mechanical database corruption.",
            "distractor_B": "Option B is incorrect because modern digital real estate contracts are recognized under electronic signature statutes.",
            "distractor_C": "Option C is incorrect because language models do not require biometric passports to parse incoming email text.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 25,
        "subtopic": "Permission Scopes, Blast Radius, and Plugins",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: The security model changes (Lines 799-803)",
        "scenario": "A school administrator installs a third-party 'Parent Communications' plugin in Claude Cowork. The plugin requests permissions to read incoming parent emails and send outgoing messages. The administrator reasons: 'Since it only reads emails to draft responses, granting write access is harmless.' How is this permission grant evaluated under least-privilege governance?",
        "options": {
            "A": "Granting send authority widens blast radius; read is not send, and scopes must stay least-privileged.",
            "B": "Parent messaging plugins are strictly classified as military munitions under international export bans.",
            "C": "Language models automatically encrypt all outgoing messages using unbreakable quantum key distributions.",
            "D": "Software plugins cannot execute actions unless the user manually checks every token in a hex editor."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 6. The text instructs: 'A permission label is not a formality. Read is not send, draft is not publish, and view is not edit. If a mail connector can read threads, that does not mean it should send as you. Write access is a separate increase in blast radius, which means the worst damage a wrong action can do. Grant the smallest scope that completes the workflow.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because school communication plugins are not restricted under international arms export treaties.",
            "distractor_C": "Option C is incorrect because standard email delivery protocols do not utilize quantum cryptographic distribution.",
            "distractor_D": "Option D is incorrect because plugins execute automated API calls without requiring manual hex editor verification."
        }
    },
    {
        "id": 26,
        "subtopic": "Claude Cowork Approval Modes: Manual vs. Auto vs. Skip",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: The gate in your pocket (Lines 832-858)",
        "scenario": "An operations lead directs a newly designed agent workflow that updates product inventory counts on an e-commerce platform. When selecting an approval mode in Claude Cowork, what operational trade-off distinguishes 'Auto' mode from 'Manual' and 'Skip' modes?",
        "options": {
            "A": "Auto mode forces the user to approve every single HTTP request while skipping all automated safety screening.",
            "B": "Auto mode lets the agent continue while safety classifiers check actions, consuming more allowance for checks.",
            "C": "Auto mode delegates all purchasing decisions to external public stock market automated algorithmic brokers.",
            "D": "Auto mode permanently disables user account access if any inventory number falls below zero units in stock."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 7. In Cowork: Manual pauses for actions needing approval (tightest oversight). Auto lets Claude continue while a safety classifier checks proposed actions for safety, blocking or escalating unsafe ones; these extra checks consume more usage allowance. Skip removes ordinary approval prompts and bypasses Auto's safety action checking, giving maximum autonomy and highest blast radius.",
            "distractor_A": "Option A is incorrect because Manual mode (not Auto) pauses for individual action approvals.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because Auto mode evaluates action safety and has nothing to do with stock market trading.",
            "distractor_D": "Option D is incorrect because inventory data values do not trigger account termination or lockout."
        }
    },
    {
        "id": 27,
        "subtopic": "The Default Fallacy in Side-Panel Approvals",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: The gate in your pocket (Lines 858-863)",
        "scenario": "A junior analyst launches a new workflow in the Claude Cowork Chrome side panel that interacts with a signed-in financial billing portal. The analyst leaves the approval setting on the side panel's default 'Automatically approve'. Why do operational deployment guidelines caution against this practice for initial runs?",
        "options": {
            "A": "Side panel extensions automatically bill personal credit cards ten thousand dollars upon initial activation.",
            "B": "Automatic approval modes cause computer monitors to emit high-frequency auditory tones that disrupt office staff.",
            "C": "Product defaults are not risk recommendations; new workflows and signed-in sites should start in Manual mode.",
            "D": "Chrome side panels are legally restricted from accessing internet websites between the hours of 9am and 5pm."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 7. The text cautions: 'The current Cowork side panel defaults to Automatically approve. That is a product default, not a recommendation for every first run. For unfamiliar tools, signed-in sites, new plugins, or high-consequence actions, switch to Manual while you learn the workflow. Once a bounded workflow earns trust, Auto reduces interruptions at the cost of more usage.'",
            "distractor_A": "Option A is incorrect because browser extensions do not charge arbitrary $10,000 credit card penalties.",
            "distractor_B": "Option B is incorrect because software approval modes have no physical capability to emit acoustic tones from monitors.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because browser side panels operate without arbitrary daytime time-of-day restrictions."
        }
    },
    {
        "id": 28,
        "subtopic": "Matching Gates to Blast Radius",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 871-879)",
        "scenario": "A credit union risk officer reviews four proposed automated agent tasks: (1) reading public competitor deposit rates, (2) drafting internal loan summary memos, (3) updating member phone numbers in reversible database logs, and (4) wiring escrow funds to title companies. How should the risk officer assign execution gates to these tasks?",
        "options": {
            "A": "Set all four tasks to Skip mode to maximize operational processing velocity across credit union systems.",
            "B": "Mandate Manual approval for reading rates, while permitting autonomous wiring of title company escrow funds.",
            "C": "Assign tasks 1 and 2 to Manual mode, and assign tasks 3 and 4 to completely unmonitored autonomous execution.",
            "D": "Permit automated execution for reading rates, require review for drafts, and enforce strict Manual gates for wiring."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 7. The autonomy ladder matches gates to consequence: 1. Read and summarize (low consequence $\\rightarrow$ automatic execution often reasonable). 2. Draft but do not send (medium consequence $\\rightarrow$ reviewable before leaving). 3. Write to reversible records (higher consequence $\\rightarrow$ stronger gate until proven). 4. Send, publish, purchase, delete, or wire funds (high consequence $\\rightarrow$ Manual or explicit human control). Wiring funds carries high blast radius and requires strict manual intervention.",
            "distractor_A": "Option A is incorrect because placing wire disbursements on Skip mode invites catastrophic financial loss.",
            "distractor_B": "Option B is incorrect because gating public reading while automating wire disbursements inverts basic risk management.",
            "distractor_C": "Option C is incorrect because low-risk reading needs less oversight than irreversible record changes or fund transfers.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 29,
        "subtopic": "Action Gate vs. Output Review Thresholds",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 880-883)",
        "scenario": "A clinical data associate builds an agent that reads public medical trial registrations and generates an executive briefing for the Chief Medical Officer. The associate claims: 'Because reading public websites is Rung 1 on the reach ladder, the finished briefing requires zero human review before distribution.' Why is this claim flawed?",
        "options": {
            "A": "Action gates govern what tools may execute; Anthropic review thresholds govern whether results need human review.",
            "B": "Public clinical trial registries are legally prohibited from being viewed on commercial laptop computer screens.",
            "C": "All medical summaries generated by language models must be approved by a unanimous vote of the United Nations.",
            "D": "Executive briefings automatically trigger hospital emergency sirens unless signed with a physical ink pen."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 7. The text emphasizes separating action gates from output review: 'Keep the two sets apart. The rung picks the gate on the action [what the tool may do]. The four thresholds [stakes, reversibility, audience, regulatory exposure] pick the review on the result. A rung-one summary can still need review if it goes to a client, or if the source data is regulated.' A briefing for the CMO carries high audience and stakes, requiring output validation regardless of how safe the input read action was.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because public clinical registries (e.g., ClinicalTrials.gov) are open access documents.",
            "distractor_C": "Option C is incorrect because medical trial summaries do not require international United Nations ratification.",
            "distractor_D": "Option D is incorrect because hospital emergency sirens are not connected to digital executive document workflows."
        }
    },
    {
        "id": 30,
        "subtopic": "Testing the Escalation Path",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 884-885)",
        "scenario": "A municipal transport planner prepares to launch an unattended scheduled agent that monitors traffic sensor feeds and posts road closure advisories. Before enabling recurring execution, the planner creates a synthetic test step that requires manual confirmation and walks away. Why is this synthetic test an essential operational prerequisite?",
        "options": {
            "A": "Walking away during an agent run is required by federal labor laws to ensure operators take ergonomic desk breaks.",
            "B": "An untested escalation path is only an assumption; operators must verify that requests reach a monitored surface.",
            "C": "Synthetic test steps force the language model to download updated road map geography files from cloud servers.",
            "D": "Testing escalation paths permanently immunizes cloud software platforms against all hardware hardware faults."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 7. The text instructs: 'Before you trust an unattended workflow, ring the gate on purpose. Create one harmless step that should need your input, start the task, walk away, and confirm the request reaches a surface you actually watch. Then deny or approve it and confirm the run responds correctly. An untested escalation path is only an assumption.' If the operator does not receive the prompt, the unattended workflow will stall silently.",
            "distractor_A": "Option A is incorrect because the escalation test is a systems verification protocol, not an ergonomic break mandate.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because testing an approval prompt does not trigger geographic map data downloads.",
            "distractor_D": "Option D is incorrect because software escalation tests cannot prevent physical hardware server component failures."
        }
    },
    {
        "id": 31,
        "subtopic": "Workflow Discovery Interviews",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 8: The delegation loop: brief, plan, approve, review (Lines 911-917, 978-984)",
        "scenario": "A logistics director spends two hours every Friday manually reconciling freight shipping manifests across three legacy portals, frequently missing discrepancies. She wants to delegate this to an agent but cannot clearly define the decision logic. What is the most effective initial delegation prompt?",
        "options": {
            "A": "Paste a single massive 500-line prompt guessing all edge cases and demanding immediate autonomous execution.",
            "B": "Command the agent to delete all discrepancies from the legacy portals to ensure the manifest balances to zero.",
            "C": "Describe the operational frustration and ask the agent to interview her until the workflow is fully understood.",
            "D": "Order the agent to rewrite the legacy portal source code into a mobile gaming application over the weekend."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 8. The text highlights workflow discovery: 'A common beginner mistake is to reach for a longer prompt. Often the better first move is workflow discovery, which means letting the agent help you find the procedure you cannot yet describe... \"Every Monday I spend an hour checking three places and still miss something. Interview me until you understand what I am trying to accomplish, what sources matter, what I never want changed, and what a good finished brief looks like. Then propose the workflow before doing it.\"'",
            "distractor_A": "Option A is incorrect because guessing complex procedures in a monolithic prompt leads to brittle, flawed automations.",
            "distractor_B": "Option B is incorrect because deleting data discrepancies conceals freight errors rather than auditing them.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because rewriting enterprise portal systems into mobile games is irrelevant and absurd."
        }
    },
    {
        "id": 32,
        "subtopic": "Plan-First Requirement in the Four-Step Delegation Loop",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 8: The delegation loop (Lines 918-933)",
        "scenario": "An investment analyst sets Claude Cowork to 'Manual' mode and assumes that because Manual mode pauses before individual tool actions, Claude will automatically generate a complete step-by-step plan for approval before starting work. Why is this operational assumption incorrect?",
        "options": {
            "A": "Manual mode is technically incapable of running in web browsers without purchasing a physical hardware dongle.",
            "B": "Claude is programmed to ignore all user instructions whenever financial investment assets are mentioned in text.",
            "C": "Manual mode automatically converts all text plans into encrypted voice recordings that cannot be reviewed.",
            "D": "Manual mode pauses before individual actions; an upfront plan is an explicit prompt instruction you must brief."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 8. The text highlights a critical callout: 'Plan-first is an instruction, not a guarantee of Manual mode. In the current Cowork side panel, Manual mode does not automatically create a plan for you to approve before starting. Claude may ask clarifying questions, then begins work and asks before individual actions. If you want the Concept 8 safety intercept, put it in the brief: \"Show me your plan first and wait for my approval before taking consequential actions.\"'",
            "distractor_A": "Option A is incorrect because Manual mode is a native software setting requiring no physical hardware dongles.",
            "distractor_B": "Option B is incorrect because Claude processes financial analysis tasks compliant with standard usage guidelines.",
            "distractor_C": "Option C is incorrect because plans are rendered in plain text rather than obfuscated audio recordings.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 33,
        "subtopic": "The Anti-Hallucination Clause for Unattended Work",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 8: A brief for work you will not watch (Lines 948-953)",
        "scenario": "A clinical research associate authors a brief for an unattended agent task that scans five medical journals overnight and compiles an adverse reaction summary. Which critical boundary line must be explicitly included to prevent cascading hallucinations during unattended execution?",
        "options": {
            "A": "If the necessary evidence is missing, state what is missing and halt rather than inventing plausible data.",
            "B": "If any medical journal article is behind a paywall, charge personal credit cards up to five thousand dollars.",
            "C": "If adverse reactions are detected, immediately dispatch an automated ambulance to the journal author's home.",
            "D": "If text contains complex chemical terminology, translate all sentences into seventeenth-century Latin prose."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 8. The text emphasizes: 'Then add one line beginners routinely leave out: \"If the necessary evidence is missing, say what is missing and stop rather than inventing it.\" That line matters more in unattended work, because a confident invention can otherwise travel through several steps before you see it.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because authorizing unconstrained credit card charges exposes the researcher to severe financial loss.",
            "distractor_C": "Option C is incorrect because automated emergency medical dispatching based on literature reviews is completely inappropriate.",
            "distractor_D": "Option D is incorrect because translating medical reports into archaic Latin destroys operational clarity."
        }
    },
    {
        "id": 34,
        "subtopic": "The Device-Independence Rule for Scheduled Tasks",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 9: Scheduled tasks with no device online (Lines 995-1008, 1041-1046)",
        "scenario": "A marketing operations specialist creates a weekly recurring task scheduled to run every Monday at 6:00 AM. The task reads campaign statistics from Google Drive via a cloud connector, checks an active project tracking spreadsheet on his sleeping laptop via a desktop bridge, and emails a summary. What will happen on Monday morning?",
        "options": {
            "A": "The cloud task automatically awakens the physical laptop from across the internet by bypassing office power cords.",
            "B": "The task fails or produces an incomplete report because the bridged local file is unreachable while the laptop sleeps.",
            "C": "The scheduled task transfers its execution to the Google Drive cloud servers and re-formats the spreadsheet.",
            "D": "The cloud platform sends a physical mail courier to the specialist's residence to retrieve the laptop hard drive."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 9. The cardinal rule of scheduling states: 'A schedule is truly device-independent only if every required tool is also reachable without your device.' While the cloud agent loop fires on schedule and reads Google Drive, the bridged local spreadsheet requires the desktop app to be awake and connected. Without it, the bridged tool is unavailable and the task cannot complete normally.",
            "distractor_A": "Option A is incorrect because cloud software cannot wirelessly bypass disconnected power supplies to boot sleeping hardware.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because Google Drive storage APIs do not execute arbitrary external agent loops.",
            "distractor_D": "Option D is incorrect because cloud software platforms do not dispatch physical courier personnel."
        }
    },
    {
        "id": 35,
        "subtopic": "Runtime Evidence vs. Outcome Evidence ('Ran is Not Worked')",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 9: Ran is not the same as worked (Lines 1015-1023)",
        "scenario": "A facilities manager inspects an automated scheduled agent that checks HVAC temperature logs every morning at 5:00 AM. The cloud scheduler console displays a green checkmark indicating 'Status: Completed (Exit Code 0)'. Why is relying solely on process exit codes considered an operational risk?",
        "options": {
            "A": "Green checkmarks in web consoles indicate that the cloud server was infected by a malicious computer virus.",
            "B": "Exit Code 0 is technically reserved for tasks that encountered fatal syntax crashes during loop initialization.",
            "C": "Runtime completion proves the mechanism fired; only verified Tier 3 deliverables prove the work was successful.",
            "D": "HVAC temperature sensors are legally prohibited from communicating with artificial intelligence software models."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 9. The text insists: 'Ran is not the same as worked. A scheduler can tell you that a run started or completed. That does not prove the output was correct, complete, or delivered. Give every recurring workflow an observable success signal: items processed, a dated file created, the tier-3 destination used, or an explicit \"no new items\" result.' Runtime success is not proof of substantive outcome accuracy.",
            "distractor_A": "Option A is incorrect because standard success status indicators do not denote malware infection.",
            "distractor_B": "Option B is incorrect because Exit Code 0 is the universal computing standard for clean execution without unhandled errors.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because industrial IoT sensors routinely interface with analytical and AI systems."
        }
    },
    {
        "id": 36,
        "subtopic": "The Three Routing Questions",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Web, desktop, or terminal (Lines 1057-1070)",
        "scenario": "An enterprise systems architect establishes an intake standard for internal AI automation requests. Rather than allowing employees to select tools based on recent product hype, the architect mandates evaluating three decisive architectural questions. Which three questions govern this operational routing?",
        "options": {
            "A": "Which model has the highest benchmark score, which vendor has the most funding, and which UI looks modern?",
            "B": "What color is the application icon, how many employees follow the vendor on Twitter, and what is token cost?",
            "C": "How fast does the user type prompts, which monitor brand is used, and what is the office Wi-Fi bandwidth?",
            "D": "What does the work touch, must it run while devices are off, and who is allowed to hold and process the data?"
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 10. The three governing routing questions are: 1. What does the work touch? (files, connectors, databases, codebases). 2. Must it run while my device is off? (cloud vs. local dependency). 3. Who is allowed to hold and process the data? (compliance, regulatory custody, BAA coverage).",
            "distractor_A": "Option A is incorrect because raw benchmark scores and vendor venture funding do not determine workflow routing.",
            "distractor_B": "Option B is incorrect because superficial UI colors and social media metrics are irrelevant to systems architecture.",
            "distractor_C": "Option C is incorrect because user typing speed and monitor brands do not dictate data custody or runtime boundaries.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 37,
        "subtopic": "HIPAA, PHI, and BAA Realities on Managed Surfaces",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Regulated or contractually restricted data (Lines 1118-1123, 1751, 1761)",
        "scenario": "A hospital clinical research administrator wants to deploy Claude Cowork to summarize electronic health records containing patient names and cancer staging diagnoses. The administrator points out that the hospital holds an Enterprise agreement with Anthropic. Why does compliance governance forbid this deployment?",
        "options": {
            "A": "Cowork is not covered under Anthropic's BAA for HIPAA use; enterprise account visibility is not legal permission.",
            "B": "Electronic health records are technically incapable of being converted into digital text format for AI review.",
            "C": "HIPAA regulations require that all cancer patient records be reviewed exclusively by veterinary medicine doctors.",
            "D": "Commercial AI models refuse to process medical terms unless approved by an act of the United States Congress."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 10. The text explicitly warns: 'Anthropic now exposes Cowork activity to Enterprise compliance tooling... That approves no regulated workload by itself. As of this fact check, Anthropic states that Cowork is not covered under its BAA for HIPAA use. OpenAI makes the same point. Event-triggered Work tasks in ChatGPT for Healthcare are not BAA-covered and must not process PHI. Product availability is not permission.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because EHR systems natively export structured digital records (e.g., HL7, FHIR, text).",
            "distractor_C": "Option C is incorrect because human oncology records are governed by medical boards, not veterinary doctors.",
            "distractor_D": "Option D is incorrect because congressional statutory acts are not required for individual healthcare data processing workflows."
        }
    },
    {
        "id": 38,
        "subtopic": "De-identification as an Operational Routing Strategy",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Regulated or contractually restricted data (Lines 1121-1123)",
        "scenario": "A healthcare insurance claims analyst wants to use Claude Cowork to identify fraudulent billing patterns across 50,000 claim line items. Because Cowork lacks BAA coverage for protected health information, how can the analyst legitimately route this task under data protection rules?",
        "options": {
            "A": "Transmit the claims data during weekend hours when federal regulatory compliance officers are out of office.",
            "B": "Strip or mask direct and quasi-identifiers, routing the underlying mathematical billing patterns instead of PHI.",
            "C": "Rename the claim spreadsheet column headers into an invented foreign language to conceal patient identities.",
            "D": "Upload the records to public web forums first and then instruct the agent to scrape the data from the internet."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 10. The text explains: 'Ask what the task needs: the identifiers, or only the pattern. A spending-trend analysis rarely needs customer names. Remove them, check what is left against your organization's standard, and you may not be routing regulated data at all. Removing what the task does not need is a route, not an evasion.' Removing regulated identifiers transforms the payload into safe, non-PHI pattern data.",
            "distractor_A": "Option A is incorrect because regulatory compliance laws apply 24/7 and cannot be bypassed by weekend scheduling.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because translating column names into foreign words does not de-identify underlying patient data.",
            "distractor_D": "Option D is incorrect because publishing confidential patient records to public forums constitutes an egregious data breach."
        }
    },
    {
        "id": 39,
        "subtopic": "The Open Path Trade-Off (Spine vs. Custody)",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 11: The open path: no vendor cloud (Lines 1153-1179)",
        "scenario": "A non-governmental organization handling sensitive political refugee relocation records evaluates whether to adopt commercial web agent platforms or deploy an open-source alternative (like OpenWork with self-hosted models). What fundamental operational trade-off governs the choice between these two architectural paths?",
        "options": {
            "A": "Commercial platforms charge zero dollars for enterprise accounts, whereas open-source tools require gold payments.",
            "B": "Open-source software tools are illegal to run in democratic nations without written United Nations clearance.",
            "C": "Vendors sell a working spine but hold custody; the open path gives custody and choice but requires you to build the spine.",
            "D": "Commercial platforms delete user accounts every twenty-four hours, whereas open tools provide free lifetime hardware."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 11. The fundamental trade is defined succinctly: 'The companies sell you a spine. The open path makes you build one. On the vendor surface, everything is handed to you and working on day one: sessions, files, sync, the phone gate, the scheduler. But it lives in their custody, in their format, at their price. On the open path, each of those is yours to set up, run, and fix. In exchange you get two things no vendor sells. First, custody, meaning your data on machines you control. Second, choice, meaning which model sees your prompts.'",
            "distractor_A": "Option A is incorrect because commercial platforms charge subscription fees and open-source models do not require gold.",
            "distractor_B": "Option B is incorrect because open-source AI software is fully legal and requires no UN permits.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because vendor platforms do not wipe accounts daily, nor does open software supply free hardware."
        }
    },
    {
        "id": 40,
        "subtopic": "Rented vs. Owned Enforcement Across the Five Harness Verbs",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Appendix D: Harness Engineering, on the web (Lines 1519-1570)",
        "scenario": "A fintech engineering director must decide whether an automated account credit-limit adjustment workflow can remain in a managed Cowork plugin or must transition to an owned harness in CI. Under enterprise engineering standards, what operational condition makes transitioning to an engineered harness mandatory?",
        "options": {
            "A": "When the credit limit adjustment workflow completes its mathematical execution in under fifteen elapsed seconds.",
            "B": "When the fintech firm transitions all of its corporate desktop computers from Windows to macOS laptops.",
            "C": "When the engineering director decides to publish all customer bank balances on public social media websites.",
            "D": "When enforcement rules must be guaranteed by owned infrastructure, CI gates, and code rather than model compliance."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Appendix D. The text outlines when an owned harness is necessary across the five harness verbs (Constrain, Inform, Verify, Correct, Escalate): 'When Harness Engineering becomes necessary: A rule must be enforced even if the model's instructions say otherwise. A path, network destination, branch, command, or data class must be fenced by infrastructure you control. Verification must run as code and block acceptance automatically... The boundary is who enforces the rule. Build your own harness when a control must be provable on your terms.'",
            "distractor_A": "Option A is incorrect because execution latency does not dictate compliance enforcement architecture.",
            "distractor_B": "Option B is incorrect because operating system transitions have no bearing on backend financial risk controls.",
            "distractor_C": "Option C is incorrect because publishing customer balances breaches privacy and banking confidentiality laws.",
            "distractor_D": "N/A (Correct Option)"
        }
    }
]"""
Full artifact generator for PCAO-F & Anthropic CCAO-F Certification Exam Guide
Chapter 09: General Agents on the Web: A Crash Course
Produces:
1. questions.json (40 scenario-based questions with strict option length parity)
2. Compiles finalmcqs.md, quiz.html, print_guide.html, and PDF via compile_chapter.py
"""

import json
import os
import sys
import subprocess
import re

# Ensure UTF-8 stdout on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

QUESTIONS_CH9 = [
    # ----------------------------------------------------
    # Sub-Topic 1: Chat vs. Delegated Agent Surfaces & The Two-Axis Runtime Model (Q1 - Q5)
    # ----------------------------------------------------
    {
        "id": 1,
        "subtopic": "Chat Box vs. Agent Surface Operational Distinction",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 1: Same address, two different things (Lines 347-372)",
        "scenario": "A pricing manager at a wholesale commercial tyre chain argues that because her team uses claude.ai every morning to draft customer discount letters, they are already running autonomous agents. According to Section 1, which single operational test invalidates this assumption?",
        "options": {
            "A": "If the user stops typing, does the task continue moving toward an outcome, or does the system halt?",
            "B": "If the browser window is resized, does the text reflow automatically into responsive screen columns?",
            "C": "If multiple team members login simultaneously, does the session log out due to concurrent session limits?",
            "D": "If an API key is omitted, does the interface revert immediately to a legacy local command-line prompt?"
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 1. The defining test separating a chat box from an agent surface is: 'If I stop typing, does the work stop? Chat box: yes. Agent surface: no.' Plain chat is synchronous and requires the user to initiate every turn. An agent surface is delegated; once assigned an outcome, it plans, uses tools, and keeps working even if the user stops typing or closes the tab.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because responsive CSS text reflow is a front-end rendering behavior unrelated to agentic delegation.",
            "distractor_C": "Option C is incorrect because concurrent session token management is an authentication rule, not the test for delegated execution.",
            "distractor_D": "Option D is incorrect because web chat interfaces do not revert to command-line prompts when end-users interact without developer API keys."
        }
    },
    {
        "id": 2,
        "subtopic": "The Two-Axis Runtime Model",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 2: The remote session: the tab is a window, not the runtime (Lines 381-395)",
        "scenario": "A clinical operations analyst configures a delegated patient intake summary task in Claude Cowork. She assumes that because she opened the session in her laptop's web browser, the model execution and data processing are restricted entirely to her local hardware. Why does Section 2 reject this assumption?",
        "options": {
            "A": "Web browsers automatically redirect all encrypted data packets into decentralized public blockchain nodes.",
            "B": "The browser tab is merely a remote viewing window; the agent loop and processing run on vendor cloud servers.",
            "C": "Local machine hardware lacks the mathematical instruction set required to render web application user interfaces.",
            "D": "Desktop browser sessions are legally prohibited from executing basic string parsing without government oversight."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 2. The chapter instructs operators to separate two runtime questions: Axis 1 (where does the agent loop run?) and Axis 2 (where does each tool execute?). In a cloud session, planning, tool selection, code execution, and task state run on the vendor's servers. The browser tab is only a viewing window onto an active cloud session ID.",
            "distractor_A": "Option A is incorrect because commercial AI vendors do not transmit customer data to public decentralized blockchain nodes.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because client laptops routinely render complex browser interfaces and can run local code when configured.",
            "distractor_D": "Option D is incorrect because local text parsing requires no regulatory legal licensing or external oversight."
        }
    },
    {
        "id": 3,
        "subtopic": "Cloud Session plus Desktop Bridge Offline Failure Modes",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 2: The remote session: the tab is a window, not the runtime (Lines 414-434, 461-465)",
        "scenario": "A logistics coordinator launches a cloud Cowork task that analyzes warehouse shipment records from Google Drive and correlates them with inventory spreadsheets stored in a folder connected through Claude Desktop. Halfway through execution, the coordinator closes her laptop. How will the session behave?",
        "options": {
            "A": "The entire cloud session terminates immediately and permanently erases all processed Google Drive outputs.",
            "B": "The agent loop migrates its execution context to the warehouse local area network routers to complete the run.",
            "C": "The cloud loop continues running with cloud tools, but the bridged local folder disappears from the session.",
            "D": "The session pauses and broadcasts an emergency SMS verification code to the corporate fleet supervisor."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 2. In a hybrid pattern (cloud loop plus desktop bridge), the agent loop runs remotely on vendor infrastructure. If the laptop disconnects or sleeps, the cloud session remains active and continues using cloud-reachable tools (like Google Drive). However, tools borrowed across the desktop bridge vanish. The operational diagnosis is that a tool became unavailable, not that Cowork stopped running.",
            "distractor_A": "Option A is incorrect because closing the laptop does not terminate the remote cloud loop or wipe cloud-synced deliverables.",
            "distractor_B": "Option B is incorrect because cloud agent loops cannot dynamically transfer execution to local networking hardware.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because losing a bridged tool does not trigger automated SMS emergency dispatching."
        }
    },
    {
        "id": 4,
        "subtopic": "Desktop Bridge Data Custody Realities",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 2: Four consequences (Lines 442-450) & Concept 10 (Lines 1124-1127)",
        "scenario": "A legal ops director reviews an analyst who processed privileged corporate merger documents by connecting a local folder to a cloud Cowork session via Claude Desktop. The analyst asserts: 'Because the files sat on my MacBook hard drive, their contents never left my machine.' Why is this assertion false?",
        "options": {
            "A": "MacBook operating systems automatically duplicate local text files into public peer-to-peer torrent networks.",
            "B": "Connecting a folder permanently transfers physical hardware drive ownership rights to the software vendor.",
            "C": "Local desktop folders cannot be read by software tools unless the hard drive is completely unencrypted.",
            "D": "Local files opened across a desktop bridge are transmitted to and processed within the vendor's cloud runtime."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 2 and Section 10. The text explicitly warns: 'A local file opened this way is processed in the vendor's cloud... A bridge is a convenience, not a custody loophole. If a cloud Cowork session reads a local file through Claude Desktop, its contents are processed in Anthropic's cloud. So do not route sensitive work to \"local file\" and assume local custody. The first question is where the processing happens, not where the file was sitting five seconds earlier.'",
            "distractor_A": "Option A is incorrect because macOS does not transmit user documents to peer-to-peer file-sharing networks.",
            "distractor_B": "Option B is incorrect because software connections have no effect on physical hardware property ownership.",
            "distractor_C": "Option C is incorrect because desktop bridge connectors read local file systems without requiring full-disk decryption.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 5,
        "subtopic": "Enterprise Controls: Work Cloud vs. Work Local",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 2: Axis 1 and ChatGPT Work (Lines 436-439)",
        "scenario": "A municipal cybersecurity auditor inspects an enterprise deployment of ChatGPT Work across government workstations. The agency's data retention mandate strictly forbids government records from entering cloud task environments. How can an administrator enforce this boundary within the platform settings?",
        "options": {
            "A": "Enable Work Local controls while disabling Work Cloud, confining agent execution strictly to local machines.",
            "B": "Configure all workstation monitors to run at reduced refresh rates to prevent remote screen capture tools.",
            "C": "Mandate that employees type all prompts exclusively in capital letters to block automated cloud ingestion.",
            "D": "Uninstall web browser extensions while leaving default unauthenticated public cloud ports open on servers."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 2. The text notes that OpenAI exposes Work Cloud and Work Local as separate enterprise administrative controls: 'An administrator can enable Work Local without Work Cloud, so members work locally and cannot start cloud tasks.' This enforces strict data locality by ensuring tasks and files remain on the local device.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because monitor refresh rates have no bearing on network routing or cloud data transmission.",
            "distractor_C": "Option C is incorrect because letter capitalization does not prevent cloud language models from ingesting prompts.",
            "distractor_D": "Option D is incorrect because leaving unauthenticated cloud ports open actively breaches security boundaries."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 2: The Six-Part Harness Anatomy & Vendor Packaging (Q6 - Q10)
    # ----------------------------------------------------
    {
        "id": 6,
        "subtopic": "The Six-Part Universal Harness Anatomy",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 471-479)",
        "scenario": "An enterprise systems architect evaluates competing agent products from emerging AI startups. Rather than relying on vendor marketing jargon, the architect applies the universal six-part harness framework defined in Chapter 9. Which complete set of components represents this architectural lens?",
        "options": {
            "A": "Prompt optimizer, vector embedding cache, token serializer, gradient checkpoint, loss curve, and hyperparameter.",
            "B": "Heartbeat (trigger), Reach (tools), Run-until-done loop, State spine (persistence), Human gate, and Body (runtime).",
            "C": "Customer billing ledger, sales pipeline CRM, marketing email sequencer, web scraper, analytics tracker, and CMS.",
            "D": "Local subnet mask, default gateway router, DNS resolution table, SSL certificate, firewall rule, and proxy port."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 3. The six universal parts of every serious agent harness are: 1. Heartbeat: what starts a run. 2. Reach: what the run can read and act on. 3. Run-until-done loop: how it keeps moving toward an outcome. 4. State spine: what persists across runs. 5. Human gate: where autonomy stops or gets screened. 6. Body: where the work actually executes.",
            "distractor_A": "Option A is incorrect because token serializers and loss curves are internal model training and inference mechanics.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because CRMs, email sequencers, and CMS platforms are external enterprise business applications.",
            "distractor_D": "Option D is incorrect because subnets, DNS tables, and firewalls are standard networking infrastructure components."
        }
    },
    {
        "id": 7,
        "subtopic": "Claude Cowork vs. ChatGPT Work Packaging Alignment",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 480-547)",
        "scenario": "A technology director compares how Claude Cowork and ChatGPT Work package their respective agent capabilities. When mapping their specific product features to the universal six-part harness, which alignment accurately reflects their structural equivalence?",
        "options": {
            "A": "Cowork Scheduled Tasks represent the Gate, while ChatGPT Work Approval Prompts represent the Heartbeat component.",
            "B": "Cowork MCP Connectors represent the Body, while ChatGPT Work Cloud Sandboxes represent the Reach tool part.",
            "C": "Cowork Connectors and ChatGPT Plugins map to Reach; Cowork Sessions and ChatGPT Synced Sessions map to Spine.",
            "D": "Cowork Manual Mode represents the State Spine, while ChatGPT Work Plan Mode represents the Heartbeat component."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 3 (Figure 3 and comparison table). Connectors in Cowork and Plugins in ChatGPT Work map to Reach (what the agent can read and act on). Saved sessions, Projects, and files map to the State Spine (what persists). Scheduled tasks map to Heartbeat, approval modes map to Gate, and cloud sandboxes/execution environments map to Body.",
            "distractor_A": "Option A is incorrect because Scheduled Tasks are the Heartbeat (trigger), and Approval Prompts are the Gate.",
            "distractor_B": "Option B is incorrect because Connectors represent Reach (tools), while cloud sandboxes represent the Body (execution environment).",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because Manual Mode is a Human Gate setting, and Plan Mode is part of the Run-until-done loop.",
        }
    },
    {
        "id": 8,
        "subtopic": "Plan Mode as an Execution Loop Discipline",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Two vendors, one shape (Lines 544-545)",
        "scenario": "A product manager notices that ChatGPT Work features an explicit 'Plan mode' that gathers context, asks clarifying questions, and proposes a step-by-step approach before executing actions. How does Section 3 classify this feature within the six-part harness framework?",
        "options": {
            "A": "It is an entirely new seventh architectural harness component that replaces the need for a State spine.",
            "B": "It is a hardware virtualization hypervisor that partitions remote cloud CPU cores across tenant accounts.",
            "C": "It is an autonomous network security protocol designed to block denial-of-service traffic on cloud servers.",
            "D": "It is an interactive implementation of the Run-until-done loop that surfaces intent before execution begins."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 3. The text explains: 'ChatGPT Work Plan mode is a current example. It gathers context, asks questions, creates a step-by-step plan, and lets you approve it before execution. That is not a seventh part. It is Concept 8 built into a product.' It operationalizes the Run-until-done loop by making the agent's planned trajectory inspectable before expensive or consequential actions begin.",
            "distractor_A": "Option A is incorrect because Plan mode does not create a seventh component or replace persistent context storage.",
            "distractor_B": "Option B is incorrect because planning is a software reasoning and orchestration layer, not a hardware hypervisor.",
            "distractor_C": "Option C is incorrect because Plan mode addresses task delegation rather than DDoS network traffic filtering.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 9,
        "subtopic": "Identical Shape vs. Identical Trust",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 3: Two warnings (Lines 550-555)",
        "scenario": "An IT compliance officer evaluates an agent workflow that can interact with the corporate CRM either via an authenticated Model Context Protocol (MCP) connector or by driving a web browser through screen clicks. Why does Section 3 warn that 'same shape does not mean same trust'?",
        "options": {
            "A": "Connectors offer structured, permission-scoped actions, whereas browser automation introduces wider exposure and ambiguity.",
            "B": "Browser-based screen driving is legally recognized as a certified cryptographic signature across all federal jurisdictions.",
            "C": "MCP connectors are technically incapable of transmitting text data across standard internet firewall boundaries.",
            "D": "Web browsers automatically prevent language models from interpreting malicious instructions found in website code."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 3. The text explicitly warns: 'Same shape does not mean same trust. A connector call and a browser click can reach the same business system with different permissions, visibility, and exposure to hidden instructions... Connectors come first because structure gives you clearer permissions, clearer actions, and less ambiguity than screen-driving.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because automated browser clicks do not constitute legally binding cryptographic signatures.",
            "distractor_C": "Option C is incorrect because MCP connectors operate over standard client-server network protocols (e.g., HTTP/SSE, stdio).",
            "distractor_D": "Option D is incorrect because browsers directly expose models to untrusted web content and indirect prompt injections."
        }
    },
    {
        "id": 10,
        "subtopic": "The Harness Wars Market Shift",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Appendix G: The harness war, industry-wide (Lines 1701-1725)",
        "scenario": "A venture partner evaluating artificial intelligence startups notes that frontier model intelligence benchmarks have largely converged. According to Appendix G, where has the primary competitive battleground across major frontier AI providers shifted?",
        "options": {
            "A": "Competing exclusively on reducing physical semiconductor chip manufacturing facility construction times.",
            "B": "Competing on the complete agent harness: persistent state, browser reach, tools, schedules, and governance.",
            "C": "Competing on establishing proprietary closed-source programming languages to replace modern JavaScript.",
            "D": "Competing on marketing consumer desktop monitors with higher display pixel resolutions to office workers."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Appendix G. The text emphasizes: 'The durable market signal is not a model ranking. It is that major vendors compete on the whole agent system: memory, tools, browser reach, schedules, plugins, approvals, runtime, identity, and governance. That is the harness war.' The competitive differentiator is the surrounding harness rather than marginal raw model capability.",
            "distractor_A": "Option A is incorrect because AI software vendors compete on software harnesses, not foundry chip fabrication construction.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because AI providers rely on standard languages (Python, TypeScript) rather than replacing JavaScript.",
            "distractor_D": "Option D is incorrect because display hardware manufacturing is unrelated to agent software ecosystem competition."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 3: The Persistent Context Stack & State Spine Architecture (Q11 - Q15)
    # ----------------------------------------------------
    {
        "id": 11,
        "subtopic": "The Five Layers of the Persistent Context Stack",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 578-618)",
        "scenario": "A project lead at a commercial property consultancy wants Claude to apply a specific 20-page regional building lease analysis rubric across twelve different property evaluation tasks over the next four months. In which layer of the Persistent Context Stack should this rubric reside?",
        "options": {
            "A": "A single temporary Task Filesystem scratch pad that wipes automatically after each property review runs.",
            "B": "Global user-level Semantic Memory shared indiscriminately across all personal and non-work conversations.",
            "C": "A dedicated Project workspace holding the shared files, instructions, and context for that ongoing workstream.",
            "D": "The browser cache history of the local computer terminal used to launch the first introductory property chat."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 4. The 5-layer stack partitions persistence: Session history (what happened in this task), Project (what belongs to this continuing body of work), Semantic memory (cross-session facts/preferences), Standing instructions (recurring behavioral rules), and User-owned context files. A dedicated Project workspace is the exact architectural layer engineered for an ongoing multi-task initiative with shared reference files and guidelines.",
            "distractor_A": "Option A is incorrect because the Task Filesystem is Tier 1 scratch space that gets wiped when each task ends.",
            "distractor_B": "Option B is incorrect because storing a 20-page commercial rubric in global personal memory pollutes unrelated chat contexts.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because browser cache history is a client web artifact, not an agent persistence layer."
        }
    },
    {
        "id": 12,
        "subtopic": "The Old Session Fallacy",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 620-625)",
        "scenario": "An accountant preparing corporate quarterly tax filings maintains a single 400-turn chat conversation that began eight months ago. When asked why she refuses to start a fresh session, she replies: 'If I start a new chat, the AI will forget my company's accounting rules.' Why does Section 4 label this practice an anti-pattern?",
        "options": {
            "A": "Old chat conversations automatically convert financial numbers into random negative integers after 100 turns.",
            "B": "Enterprise cloud security protocols automatically delete all active conversations at midnight every Friday.",
            "C": "Language models refuse to process tax forms unless the user re-enters their credit card details every turn.",
            "D": "An old session is not memory; massive conversation history creates context noise and increases model drift."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 4. The text cautions: 'An old session is not memory. A Project is not memory either. A global instruction is not memory. They all persist, for different reasons... Start a fresh session when the old conversation is noise. Continue when the history is part of the job. Memory does not replace deliberate context.' Long monolithic sessions degrade performance through context contamination and cost, whereas durable rules belong in Projects or instructions.",
            "distractor_A": "Option A is incorrect because language models do not deliberately invert numbers based on turn counts.",
            "distractor_B": "Option B is incorrect because platform sessions persist in account storage and are not purged weekly.",
            "distractor_C": "Option C is incorrect because models do not demand credit card re-entry during standard conversational sessions.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 13,
        "subtopic": "Semantic Memory Controls in Claude Cowork",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 620-631)",
        "scenario": "A talent recruitment coordinator uses Claude Cowork for executive candidate research. Following the August 2026 update, Claude notices that the coordinator prefers candidates with medical device experience. How is this preference managed across the Cowork ecosystem?",
        "options": {
            "A": "It enters shared cloud Semantic Memory, where the user can inspect, edit, or delete the topic at any time.",
            "B": "It is permanently etched into the underlying foundational model weights during overnight retraining runs.",
            "C": "It is broadcast automatically to public recruitment job boards via an unauthenticated webhook integration.",
            "D": "It is saved exclusively to local laptop hard drives and cannot be accessed from cloud Cowork sessions."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 4. The August 25 update integrated semantic memory across Claude chat and cloud Cowork: 'Cloud Cowork tasks now use the same memory as Claude chat, so what Claude remembers from chat can reach a cloud Cowork task, and what matters in Cowork can carry back. You can inspect memory topic by topic and edit or delete it.' It is inspectable and user-governed, not baked into base weights.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because user preferences are stored in retrieval memory, not fine-tuned into base model weights.",
            "distractor_C": "Option C is incorrect because private conversational memory is never broadcast to external public job boards.",
            "distractor_D": "Option D is incorrect because cloud Cowork memory is hosted in the vendor's cloud and synchronizes across cloud surfaces."
        }
    },
    {
        "id": 14,
        "subtopic": "The Strategic Role of Portable Context Files (`CLAUDE.md`)",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 4: The account spine (Lines 632-635)",
        "scenario": "A software agency operations lead directs multiple client projects across Claude Cowork, Claude Code, and local command-line tools. Why does Section 4 recommend maintaining a standalone `CLAUDE.md` file rather than relying solely on vendor-managed account memory?",
        "options": {
            "A": "Vendor cloud servers refuse to execute code unless a markdown file is cryptographically signed by an auditor.",
            "B": "A markdown file provides an inspectable, version-controlled, vendor-neutral source of truth you own and export.",
            "C": "Creating a `CLAUDE.md` file grants the user unlimited free compute tokens on commercial cloud platforms.",
            "D": "Local markdown files prevent computers from experiencing physical hardware overheating during agent runs."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 4. The text explains: 'CLAUDE.md is a plain markdown file of standing instructions that some Claude tools read at the start of a task. It makes an excellent portable context file. But native memory and instructions are first-class mechanisms now. Use the file for portability... give critical state a portable source of truth you control.' It ensures instructions are readable, versioned, and independent of vendor lock-in.",
            "distractor_A": "Option A is incorrect because agent tools do not require cryptographic auditor signatures on markdown files.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because text instruction files do not bypass metered token usage or grant free compute.",
            "distractor_D": "Option D is incorrect because software configuration files have no relationship to CPU thermal thermodynamics."
        }
    },
    {
        "id": 15,
        "subtopic": "Switching Costs and Persistence Architecture",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 4: The account spine (Lines 636-639)",
        "scenario": "A financial advisory firm consolidates all of its client portfolio tracking, custom prompt instructions, and historical session logs inside a single commercial AI vendor's proprietary cloud workspace. What significant strategic risk does Section 4 highlight regarding this approach?",
        "options": {
            "A": "Proprietary cloud workspaces automatically publish confidential client portfolios to public social media platforms.",
            "B": "Commercial language models experience catastrophic syntax failure whenever portfolio balances exceed one million dollars.",
            "C": "Accumulated state creates high switching costs and vendor lock-in unless durable assets exist in portable formats.",
            "D": "Cloud vendors are legally required to confiscate client investment assets if an organization changes software providers."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 4. The text warns: 'The convenience has a price, and the price is custody and dependency. Vendor-managed memory, Projects, sessions, plugins, and files are useful because they pile up, which also makes the account sticky. So keep operational state in the vendor spine while work is active, and give critical state a portable source of truth you control.'",
            "distractor_A": "Option A is incorrect because commercial enterprise platforms maintain private tenant isolation and do not publish to social media.",
            "distractor_B": "Option B is incorrect because large numbers do not trigger model syntax compilation crashes.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because cloud software vendors hold no legal authority to seize client financial assets."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 4: The Three File Tiers & Custody Discipline (Q16 - Q20)
    # ----------------------------------------------------
    {
        "id": 16,
        "subtopic": "The Three File Tiers Defined",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 658-666)",
        "scenario": "A hospital billing administrator audits an automated claim reconciliation workflow. The workflow generates temporary math scratch files, saves monthly summary tables in the user's platform workspace, and deposits signed reimbursement PDFs into the hospital's secure AWS S3 archive. How do these three locations map to the Three File Tiers?",
        "options": {
            "A": "Scratch files are Tier 2 (Platform); monthly tables are Tier 1 (Task Filesystem); S3 PDFs are Tier 3 (Exit).",
            "B": "Scratch files are Tier 3 (Exit); monthly tables are Tier 2 (Platform); S3 PDFs are Tier 1 (Task Filesystem).",
            "C": "Scratch files are Tier 2 (Platform); monthly tables are Tier 3 (Exit); S3 PDFs are Tier 1 (Task Filesystem).",
            "D": "Scratch files are Tier 1 (Task Filesystem); monthly tables are Tier 2 (Platform); S3 PDFs are Tier 3 (Exit)."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 5. Tier 1 is the Task Filesystem (temporary scratch space on vendor servers, wiped when work finishes). Tier 2 is Platform Storage (files saved to your account in vendor custody, surviving the task and tab). Tier 3 is The Exit (files entering a system under user/firm control, such as a secure AWS S3 bucket, Google Drive, or on-prem repository).",
            "distractor_A": "Option A is incorrect because scratch files are Tier 1 and monthly workspace tables are Tier 2.",
            "distractor_B": "Option B is incorrect because temporary scratch work is never Tier 3, and S3 archives are not Tier 1.",
            "distractor_C": "Option C is incorrect because scratch work is Tier 1, and external cloud archives are Tier 3.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 17,
        "subtopic": "The Signature Custody Discipline",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 668-674)",
        "scenario": "A corporate compliance officer reviews an AI workflow that drafts formal employee disciplinary letters. The lead analyst intends to leave the finalized letters stored exclusively in the cloud workspace session history. What signature rule from Chapter 9 does this violate?",
        "options": {
            "A": "Finished work exits the platform; deliverables left in Tier 2 remain hostage to vendor custody and retention rules.",
            "B": "All disciplinary letters must be etched onto physical metallic plates before being shown to human resources.",
            "C": "Language models are legally barred from drafting letters that contain employee names or corporate job titles.",
            "D": "Cloud platform storage automatically converts confidential human resource files into publicly accessible web links."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 5. The text establishes the defining discipline: 'Finished work exits the platform. Everything else may stay... A deliverable that exists only in tier 2 is safe today and hostage tomorrow, because it survives only in someone else's custody. A deliverable in tier 3 is yours, under your retention rules, and still there if the vendor's product changes shape.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because disciplinary documentation does not require physical metal engraving.",
            "distractor_C": "Option C is incorrect because models routinely process HR drafts under appropriate authorization and human review.",
            "distractor_D": "Option D is incorrect because Tier 2 platform storage is private to the authenticated account and not automatically made public."
        }
    },
    {
        "id": 18,
        "subtopic": "Public URLs vs. True Custody (ChatGPT Sites)",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: The three file tiers (Lines 676-677)",
        "scenario": "A marketing specialist uses ChatGPT Work to build an interactive campaign analytics dashboard, which he publishes to a live web URL using ChatGPT Sites. The specialist reports to his director: 'This dashboard is now securely preserved in Tier 3.' Why does Section 5 refute this classification?",
        "options": {
            "A": "Interactive web dashboards are technically incapable of rendering charts unless hosted on local intranet servers.",
            "B": "A platform-hosted Site is Tier 2 with a public door; it remains under vendor custody rather than firm infrastructure.",
            "C": "Publishing a website immediately revokes the enterprise's copyright ownership over all marketing campaign assets.",
            "D": "Websites generated by artificial intelligence models automatically expire after exactly twelve elapsed seconds."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 5. The text explains: 'Sites can publish a finished web app or dashboard to a shareable URL. But a Site hosted on the platform is still tier 2 with a public door, not tier 3 in your own custody.' It remains hosted on OpenAI's infrastructure, subject to vendor platform availability, format, and access policies.",
            "distractor_A": "Option A is incorrect because modern cloud web apps render complex charts seamlessly across public and private networks.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because hosting on a vendor platform does not automatically transfer copyright ownership to the public domain.",
            "distractor_D": "Option D is incorrect because hosted sites persist indefinitely according to platform account retention terms."
        }
    },
    {
        "id": 19,
        "subtopic": "Enforcing the Tier Decision in Briefs",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 5: The three file tiers (Lines 680-686)",
        "scenario": "A procurement manager drafts an autonomous agent brief to analyze vendor bids and generate a contract award recommendation memo. To prevent generated deliverables from getting lost in scratch space or locked in vendor custody, which specific instruction should terminate the brief?",
        "options": {
            "A": "Encrypt all output text using custom hexadecimal rot13 ciphers before printing to the user screen terminal.",
            "B": "Re-run the entire bid evaluation five times consecutively and take the mathematical average of the token counts.",
            "C": "List every file created and its destination tier: temporary scratch, platform storage, or a system I control.",
            "D": "Mandate that the agent delete the vendor's cloud server database upon completing the contract award analysis."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 5. Section 5 provides the exact operational instruction to enforce custody discipline: 'End by listing every file you created and where each one landed: temporary working space, platform storage, or a system I control (connector save, download, local write, or repo commit).' This turns invisible default storage into an auditable operational decision.",
            "distractor_A": "Option A is incorrect because obscuring text with rot13 ciphers prevents human review and does not resolve file custody.",
            "distractor_B": "Option B is incorrect because averaging token counts does not verify output quality or specify file storage locations.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because deleting remote databases is destructive and technically impossible for standard agent accounts."
        }
    },
    {
        "id": 20,
        "subtopic": "Legal & Operational Risks of Platform Link Sharing",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: Check yourself (Lines 700-707)",
        "scenario": "A senior associate at a commercial litigation firm drafts a critical litigation strategy memo in a web agent session and emails the vendor's platform share link directly to the corporate client. According to the analysis in Section 5, what two major governance failures occurred?",
        "options": {
            "A": "The email protocol automatically deletes text attachments, and the client's screen cannot render web fonts.",
            "B": "The law firm violated state bar rules by using modern computers, and the cloud server bandwidth was exceeded.",
            "C": "The memo was transmitted without a physical wax seal, and the vendor platform charged an unapproved export tariff.",
            "D": "The memo bypassed the firm's matter retention system, and access depends on vendor sharing rules the firm cannot govern."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 5. The check-yourself analysis notes two fundamental failures: 'First, custody. The memo exists only in tier 2, outside the firm's matter folder and retention system, so the firm's record has a hole in it. Second, access. The link's sharing rules are the platform's, not the firm's, and the firm cannot govern what it does not hold. The fix is tier 3. Save the memo into the document management system, then share from there.'",
            "distractor_A": "Option A is incorrect because email gateways support links and modern operating systems render web typography.",
            "distractor_B": "Option B is incorrect because legal ethics permits technology use, and cloud bandwidth was not the root governance issue.",
            "distractor_C": "Option C is incorrect because wax seals and fictional export tariffs are irrelevant to digital custody standards.",
            "distractor_D": "N/A (Correct Option)"
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 5: The Reach Ladder, Browser Paths & Prompt Injection Defense (Q21 - Q25)
    # ----------------------------------------------------
    {
        "id": 21,
        "subtopic": "The Four-Rung Reach Ladder",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: Connectors on the web: reach and exit door in one (Lines 754-761)",
        "scenario": "A healthcare systems administrator must configure an agent to retrieve patient appointment schedules from an internal database. The developer proposes writing a computer-use script that takes screenshots and clicks the desktop screen. Why does Section 6 mandate using a structured connector instead?",
        "options": {
            "A": "Use the most structured tool available; connectors provide bounded permissions and actions with less ambiguity.",
            "B": "Screen-driving scripts consume 100% of municipal electrical grid output and damage physical hardware displays.",
            "C": "Model Context Protocol connectors are legally required to be written exclusively in compiled assembly language.",
            "D": "Computer use scripts are technically incapable of recognizing numbers or dates on computer monitor screens."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 6. The reach ladder establishes the rule: 'Use the most structured tool that can do the job. Connector before browser. Browser before full computer use.' Structured connectors (APIs/MCP) enforce explicit OAuth scopes, clear data schemas, and auditable actions, minimizing the operational ambiguity and injection surface inherent in screen driving.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because screen-driving scripts do not consume municipal power grids or harm monitor hardware.",
            "distractor_C": "Option C is incorrect because MCP servers are commonly authored in high-level languages like TypeScript or Python.",
            "distractor_D": "Option D is incorrect because computer vision models can parse text and numbers from screen captures, albeit with higher error rates."
        }
    },
    {
        "id": 22,
        "subtopic": "Built-in Cowork Browser vs. Claude in Chrome",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 6: Reach path comparison (Lines 762-777, 1128-1133)",
        "scenario": "An investment research associate needs an AI assistant to: (1) scrape quarterly financial disclosures from a public state utility commission portal overnight, and (2) assist him in summarizing a password-protected Bloomberg terminal web tab currently open on his desktop. Which tools should be routed to each task?",
        "options": {
            "A": "Use Claude in Chrome for the overnight public scraping; use an unverified community plugin for the Bloomberg tab.",
            "B": "Use Cowork's built-in browser for the portal task; use Claude in Chrome for the actively open Bloomberg tab.",
            "C": "Use full desktop computer use for both tasks to ensure that all keystrokes are recorded in system kernel logs.",
            "D": "Use an external command-line terminal for the Bloomberg tab; use a phone SMS assistant for the utility portal."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 6 and Section 10. The text distinguishes the two browser paths: 'Use Claude in Chrome when the work is \"help me with this page\" [the user's existing Chrome session, open tabs, and active logins]. Use the built-in browser when the work is \"go handle this website task for me\" [delegated web work with its own separate browser state].'",
            "distractor_A": "Option A is incorrect because Claude in Chrome requires an active user session and is ill-suited for standalone unattended batch scraping.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because full computer use carries the highest operational risk and violates the reach ladder when browser tools exist.",
            "distractor_D": "Option D is incorrect because SMS assistants cannot navigate complex municipal utility portals or parse secure data feeds."
        }
    },
    {
        "id": 23,
        "subtopic": "Browser Trust Boundaries and Stored Credentials",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: Reach path comparison (Lines 764-765, 793-795)",
        "scenario": "A financial controller signs into the company's primary corporate banking portal using Claude Cowork's built-in browser inside Claude Desktop. Why does Section 6 highlight this action as a severe, permanent expansion of the agent's trust boundary?",
        "options": {
            "A": "Signing into a bank portal automatically transfers the corporation's liquid cash reserves into the vendor's stock.",
            "B": "The browser software deletes the user's operating system credentials and forces a complete hardware reformat.",
            "C": "Saved login state in the built-in browser becomes accessible to future unattended Cowork sessions on that machine.",
            "D": "Federal banking regulations automatically suspend commercial banking licenses whenever AI tools navigate web forms."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 6. The text explicitly warns: 'The built-in browser starts separate from your personal browser state. You can sign in as needed... That creates a new trust boundary. Anything you sign into inside Claude's browser can reach future Cowork sessions on that computer. Treat browser login state as a permission... Do not casually import or reuse logins for banking, medical, identity, or other highly sensitive systems.'",
            "distractor_A": "Option A is incorrect because browser logins do not automatically trigger unauthorized equity transfers.",
            "distractor_B": "Option B is incorrect because browser cookies and sessions do not wipe operating system installations.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because banking licenses are not revoked simply because automated tools render banking HTML pages."
        }
    },
    {
        "id": 24,
        "subtopic": "Prompt Injection Dual Condition and Defense Rules",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: The security model changes (Lines 780-792)",
        "scenario": "A real estate property manager configures an agent to read incoming tenant email inquiries and autonomously execute lease contract modifications in the property management database. According to Section 6, why is this specific architecture exceptionally dangerous?",
        "options": {
            "A": "Email servers automatically corrupt database records whenever incoming messages contain grammatical mistakes.",
            "B": "Real estate lease contracts are legally invalid unless hand-written in blue ink on sheepskin parchment paper.",
            "C": "Language models refuse to process tenant emails unless every tenant provides a notarized biometric passport copy.",
            "D": "The agent reads untrusted outside content while holding authority to take consequential, hard-to-reverse actions."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 6. Section 6 identifies the critical dual condition that creates acute risk: '1. the agent can read content outside your trusted boundary, AND 2. the agent can take a consequential action... Prompt injection means hidden instructions placed in a webpage, email, document, or connector result, written to redirect the agent... Your brief is authority. Outside content is evidence, never a new boss.' An attacker can embed instructions in an email that hijack the model into modifying database records.",
            "distractor_A": "Option A is incorrect because email typos do not cause mechanical database corruption.",
            "distractor_B": "Option B is incorrect because modern digital real estate contracts are recognized under electronic signature statutes.",
            "distractor_C": "Option C is incorrect because language models do not require biometric passports to parse incoming email text.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 25,
        "subtopic": "Permission Scopes, Blast Radius, and Plugins",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 6: The security model changes (Lines 799-803)",
        "scenario": "A school administrator installs a third-party 'Parent Communications' plugin in Claude Cowork. The plugin requests permissions to read incoming parent emails and send outgoing messages. The administrator reasons: 'Since it only reads emails to draft responses, granting write access is harmless.' How does Section 6 evaluate this decision?",
        "options": {
            "A": "Granting send authority widens blast radius; read is not send, and scopes must stay least-privileged.",
            "B": "Parent messaging plugins are strictly classified as military munitions under international export bans.",
            "C": "Language models automatically encrypt all outgoing messages using unbreakable quantum key distributions.",
            "D": "Software plugins cannot execute actions unless the user manually checks every token in a hex editor."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 6. The text instructs: 'A permission label is not a formality. Read is not send, draft is not publish, and view is not edit. If a mail connector can read threads, that does not mean it should send as you. Write access is a separate increase in blast radius, which means the worst damage a wrong action can do. Grant the smallest scope that completes the workflow.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because school communication plugins are not restricted under international arms export treaties.",
            "distractor_C": "Option C is incorrect because standard email delivery protocols do not utilize quantum cryptographic distribution.",
            "distractor_D": "Option D is incorrect because plugins execute automated API calls without requiring manual hex editor verification."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 6: The Human Gate, Approval Modes & Blast Radius Calibration (Q26 - Q30)
    # ----------------------------------------------------
    {
        "id": 26,
        "subtopic": "Claude Cowork Approval Modes: Manual vs. Auto vs. Skip",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: The gate in your pocket (Lines 832-858)",
        "scenario": "An operations lead directs a newly designed agent workflow that updates product inventory counts on an e-commerce platform. When selecting an approval mode in Claude Cowork, what operational trade-off distinguishes 'Auto' mode from 'Manual' and 'Skip' modes?",
        "options": {
            "A": "Auto mode forces the user to approve every single HTTP request while skipping all automated safety screening.",
            "B": "Auto mode lets the agent continue while safety classifiers check actions, consuming more allowance for checks.",
            "C": "Auto mode delegates all purchasing decisions to external public stock market automated algorithmic brokers.",
            "D": "Auto mode permanently disables user account access if any inventory number falls below zero units in stock."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 7. In Cowork: Manual pauses for actions needing approval (tightest oversight). Auto lets Claude continue while a safety classifier checks proposed actions for safety, blocking or escalating unsafe ones; these extra checks consume more usage allowance. Skip removes ordinary approval prompts and bypasses Auto's safety action checking, giving maximum autonomy and highest blast radius.",
            "distractor_A": "Option A is incorrect because Manual mode (not Auto) pauses for individual action approvals.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because Auto mode evaluates action safety and has nothing to do with stock market trading.",
            "distractor_D": "Option D is incorrect because inventory data values do not trigger account termination or lockout."
        }
    },
    {
        "id": 27,
        "subtopic": "The Default Fallacy in Side-Panel Approvals",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: The gate in your pocket (Lines 858-863)",
        "scenario": "A junior analyst launches a new workflow in the Claude Cowork Chrome side panel that interacts with a signed-in financial billing portal. The analyst leaves the approval setting on the side panel's default 'Automatically approve'. Why does Section 7 caution against this practice for initial runs?",
        "options": {
            "A": "Side panel extensions automatically bill personal credit cards ten thousand dollars upon initial activation.",
            "B": "Automatic approval modes cause computer monitors to emit high-frequency auditory tones that disrupt office staff.",
            "C": "Product defaults are not risk recommendations; new workflows and signed-in sites should start in Manual mode.",
            "D": "Chrome side panels are legally restricted from accessing internet websites between the hours of 9am and 5pm."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 7. The text cautions: 'The current Cowork side panel defaults to Automatically approve. That is a product default, not a recommendation for every first run. For unfamiliar tools, signed-in sites, new plugins, or high-consequence actions, switch to Manual while you learn the workflow. Once a bounded workflow earns trust, Auto reduces interruptions at the cost of more usage.'",
            "distractor_A": "Option A is incorrect because browser extensions do not charge arbitrary $10,000 credit card penalties.",
            "distractor_B": "Option B is incorrect because software approval modes have no physical capability to emit acoustic tones from monitors.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because browser side panels operate without arbitrary daytime time-of-day restrictions."
        }
    },
    {
        "id": 28,
        "subtopic": "Matching Gates to Blast Radius",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 871-879)",
        "scenario": "A credit union risk officer reviews four proposed automated agent tasks: (1) reading public competitor deposit rates, (2) drafting internal loan summary memos, (3) updating member phone numbers in reversible database logs, and (4) wiring escrow funds to title companies. How should the officer gate these tasks per Section 7?",
        "options": {
            "A": "Set all four tasks to Skip mode to maximize operational processing velocity across credit union systems.",
            "B": "Mandate Manual approval for reading rates, while permitting autonomous wiring of title company escrow funds.",
            "C": "Assign tasks 1 and 2 to Manual mode, and assign tasks 3 and 4 to completely unmonitored autonomous execution.",
            "D": "Permit automated execution for reading rates, require review for drafts, and enforce strict Manual gates for wiring."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 7. The autonomy ladder matches gates to consequence: 1. Read and summarize (low consequence $\\rightarrow$ automatic execution often reasonable). 2. Draft but do not send (medium consequence $\\rightarrow$ reviewable before leaving). 3. Write to reversible records (higher consequence $\\rightarrow$ stronger gate until proven). 4. Send, publish, purchase, delete, or wire funds (high consequence $\\rightarrow$ Manual or explicit human control). Wiring funds carries high blast radius and requires strict manual intervention.",
            "distractor_A": "Option A is incorrect because placing wire disbursements on Skip mode invites catastrophic financial loss.",
            "distractor_B": "Option B is incorrect because gating public reading while automating wire disbursements inverts basic risk management.",
            "distractor_C": "Option C is incorrect because low-risk reading needs less oversight than irreversible record changes or fund transfers.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 29,
        "subtopic": "Action Gate vs. Output Review Thresholds",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 880-883)",
        "scenario": "A clinical data associate builds an agent that reads public medical trial registrations and generates an executive briefing for the Chief Medical Officer. The associate claims: 'Because reading public websites is Rung 1 on the reach ladder, the finished briefing requires zero human review before distribution.' Why is this claim flawed?",
        "options": {
            "A": "Action gates govern what tools may execute; Anthropic review thresholds govern whether results need human review.",
            "B": "Public clinical trial registries are legally prohibited from being viewed on commercial laptop computer screens.",
            "C": "All medical summaries generated by language models must be approved by a unanimous vote of the United Nations.",
            "D": "Executive briefings automatically trigger hospital emergency sirens unless signed with a physical ink pen."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 7. The text emphasizes separating action gates from output review: 'Keep the two sets apart. The rung picks the gate on the action [what the tool may do]. The four thresholds [stakes, reversibility, audience, regulatory exposure] pick the review on the result. A rung-one summary can still need review if it goes to a client, or if the source data is regulated.' A briefing for the CMO carries high audience and stakes, requiring output validation regardless of how safe the input read action was.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because public clinical registries (e.g., ClinicalTrials.gov) are open access documents.",
            "distractor_C": "Option C is incorrect because medical trial summaries do not require international United Nations ratification.",
            "distractor_D": "Option D is incorrect because hospital emergency sirens are not connected to digital executive document workflows."
        }
    },
    {
        "id": 30,
        "subtopic": "Testing the Escalation Path",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 7: Match the gate to blast radius (Lines 884-885)",
        "scenario": "A municipal transport planner prepares to launch an unattended scheduled agent that monitors traffic sensor feeds and posts road closure advisories. Before enabling recurring execution, the planner creates a synthetic test step that requires manual confirmation and walks away. Why does Section 7 require this test?",
        "options": {
            "A": "Walking away during an agent run is required by federal labor laws to ensure operators take ergonomic desk breaks.",
            "B": "An untested escalation path is only an assumption; operators must verify that requests reach a monitored surface.",
            "C": "Synthetic test steps force the language model to download updated road map geography files from cloud servers.",
            "D": "Testing escalation paths permanently immunizes cloud software platforms against all hardware hardware faults."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 7. The text instructs: 'Before you trust an unattended workflow, ring the gate on purpose. Create one harmless step that should need your input, start the task, walk away, and confirm the request reaches a surface you actually watch. Then deny or approve it and confirm the run responds correctly. An untested escalation path is only an assumption.' If the operator does not receive the prompt, the unattended workflow will stall silently.",
            "distractor_A": "Option A is incorrect because the escalation test is a systems verification protocol, not an ergonomic break mandate.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because testing an approval prompt does not trigger geographic map data downloads.",
            "distractor_D": "Option D is incorrect because software escalation tests cannot prevent physical hardware server component failures."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 7: The Unwatched Delegation Loop & Device-Independent Scheduling (Q31 - Q35)
    # ----------------------------------------------------
    {
        "id": 31,
        "subtopic": "Workflow Discovery Interviews",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 8: The delegation loop: brief, plan, approve, review (Lines 911-917, 978-984)",
        "scenario": "A logistics director spends two hours every Friday manually reconciling freight shipping manifests across three legacy portals, frequently missing discrepancies. She wants to delegate this to an agent but cannot clearly define the decision logic. According to Section 8, what is the best initial prompt?",
        "options": {
            "A": "Paste a single massive 500-line prompt guessing all edge cases and demanding immediate autonomous execution.",
            "B": "Command the agent to delete all discrepancies from the legacy portals to ensure the manifest balances to zero.",
            "C": "Describe the operational frustration and ask the agent to interview her until the workflow is fully understood.",
            "D": "Order the agent to rewrite the legacy portal source code into a mobile gaming application over the weekend."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 8. The text highlights workflow discovery: 'A common beginner mistake is to reach for a longer prompt. Often the better first move is workflow discovery, which means letting the agent help you find the procedure you cannot yet describe... \"Every Monday I spend an hour checking three places and still miss something. Interview me until you understand what I am trying to accomplish, what sources matter, what I never want changed, and what a good finished brief looks like. Then propose the workflow before doing it.\"'",
            "distractor_A": "Option A is incorrect because guessing complex procedures in a monolithic prompt leads to brittle, flawed automations.",
            "distractor_B": "Option B is incorrect because deleting data discrepancies conceals freight errors rather than auditing them.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because rewriting enterprise portal systems into mobile games is irrelevant and absurd."
        }
    },
    {
        "id": 32,
        "subtopic": "Plan-First Requirement in the Four-Step Delegation Loop",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 8: The delegation loop (Lines 918-933)",
        "scenario": "An investment analyst sets Claude Cowork to 'Manual' mode and assumes that because Manual mode pauses before individual tool actions, Claude will automatically generate a complete step-by-step plan for approval before starting work. Why does Section 8 warn that this assumption is incorrect?",
        "options": {
            "A": "Manual mode is technically incapable of running in web browsers without purchasing a physical hardware dongle.",
            "B": "Claude is programmed to ignore all user instructions whenever financial investment assets are mentioned in text.",
            "C": "Manual mode automatically converts all text plans into encrypted voice recordings that cannot be reviewed.",
            "D": "Manual mode pauses before individual actions; an upfront plan is an explicit prompt instruction you must brief."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 8. The text highlights a critical callout: 'Plan-first is an instruction, not a guarantee of Manual mode. In the current Cowork side panel, Manual mode does not automatically create a plan for you to approve before starting. Claude may ask clarifying questions, then begins work and asks before individual actions. If you want the Concept 8 safety intercept, put it in the brief: \"Show me your plan first and wait for my approval before taking consequential actions.\"'",
            "distractor_A": "Option A is incorrect because Manual mode is a native software setting requiring no physical hardware dongles.",
            "distractor_B": "Option B is incorrect because Claude processes financial analysis tasks compliant with standard usage guidelines.",
            "distractor_C": "Option C is incorrect because plans are rendered in plain text rather than obfuscated audio recordings.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 33,
        "subtopic": "The Anti-Hallucination Clause for Unattended Work",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 8: A brief for work you will not watch (Lines 948-953)",
        "scenario": "A clinical research associate authors a brief for an unattended agent task that scans five medical journals overnight and compiles an adverse reaction summary. According to Section 8, which critical boundary line must be explicitly included to prevent cascading hallucinations while the associate sleeps?",
        "options": {
            "A": "If the necessary evidence is missing, state what is missing and halt rather than inventing plausible data.",
            "B": "If any medical journal article is behind a paywall, charge personal credit cards up to five thousand dollars.",
            "C": "If adverse reactions are detected, immediately dispatch an automated ambulance to the journal author's home.",
            "D": "If text contains complex chemical terminology, translate all sentences into seventeenth-century Latin prose."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 8. The text emphasizes: 'Then add one line beginners routinely leave out: \"If the necessary evidence is missing, say what is missing and stop rather than inventing it.\" That line matters more in unattended work, because a confident invention can otherwise travel through several steps before you see it.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because authorizing unconstrained credit card charges exposes the researcher to severe financial loss.",
            "distractor_C": "Option C is incorrect because automated emergency medical dispatching based on literature reviews is completely inappropriate.",
            "distractor_D": "Option D is incorrect because translating medical reports into archaic Latin destroys operational clarity."
        }
    },
    {
        "id": 34,
        "subtopic": "The Device-Independence Rule for Scheduled Tasks",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 9: Scheduled tasks with no device online (Lines 995-1008, 1041-1046)",
        "scenario": "A marketing operations specialist creates a weekly recurring task scheduled to run every Monday at 6:00 AM. The task reads campaign statistics from Google Drive via a cloud connector, checks an active project tracking spreadsheet on his sleeping laptop via a desktop bridge, and emails a summary. What will happen on Monday morning?",
        "options": {
            "A": "The cloud task automatically awakens the physical laptop from across the internet by bypassing office power cords.",
            "B": "The task fails or produces an incomplete report because the bridged local file is unreachable while the laptop sleeps.",
            "C": "The scheduled task transfers its execution to the Google Drive cloud servers and re-formats the spreadsheet.",
            "D": "The cloud platform sends a physical mail courier to the specialist's residence to retrieve the laptop hard drive."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 9. The cardinal rule of scheduling states: 'A schedule is truly device-independent only if every required tool is also reachable without your device.' While the cloud agent loop fires on schedule and reads Google Drive, the bridged local spreadsheet requires the desktop app to be awake and connected. Without it, the bridged tool is unavailable and the task cannot complete normally.",
            "distractor_A": "Option A is incorrect because cloud software cannot wirelessly bypass disconnected power supplies to boot sleeping hardware.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because Google Drive storage APIs do not execute arbitrary external agent loops.",
            "distractor_D": "Option D is incorrect because cloud software platforms do not dispatch physical courier personnel."
        }
    },
    {
        "id": 35,
        "subtopic": "Runtime Evidence vs. Outcome Evidence ('Ran is Not Worked')",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 9: Ran is not the same as worked (Lines 1015-1023)",
        "scenario": "A facilities manager inspects an automated scheduled agent that checks HVAC temperature logs every morning at 5:00 AM. The cloud scheduler console displays a green checkmark indicating 'Status: Completed (Exit Code 0)'. Why does Section 9 insist that 'ran is not the same as worked'?",
        "options": {
            "A": "Green checkmarks in web consoles indicate that the cloud server was infected by a malicious computer virus.",
            "B": "Exit Code 0 is technically reserved for tasks that encountered fatal syntax crashes during loop initialization.",
            "C": "Runtime completion proves the mechanism fired; only verified Tier 3 deliverables prove the work was successful.",
            "D": "HVAC temperature sensors are legally prohibited from communicating with artificial intelligence software models."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 9. The text insists: 'Ran is not the same as worked. A scheduler can tell you that a run started or completed. That does not prove the output was correct, complete, or delivered. Give every recurring workflow an observable success signal: items processed, a dated file created, the tier-3 destination used, or an explicit \"no new items\" result.' Runtime success is not proof of substantive outcome accuracy.",
            "distractor_A": "Option A is incorrect because standard success status indicators do not denote malware infection.",
            "distractor_B": "Option B is incorrect because Exit Code 0 is the universal computing standard for clean execution without unhandled errors.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because industrial IoT sensors routinely interface with analytical and AI systems."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 8: Operational Routing, Compliance Boundaries & Rented vs. Owned Harnesses (Q36 - Q40)
    # ----------------------------------------------------
    {
        "id": 36,
        "subtopic": "The Three Routing Questions",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Web, desktop, or terminal (Lines 1057-1070)",
        "scenario": "An enterprise systems architect establishes an intake standard for internal AI automation requests. Rather than allowing employees to select tools based on recent product hype, the architect mandates evaluating three decisive questions from Section 10. Which three questions govern this operational routing?",
        "options": {
            "A": "Which model has the highest benchmark score, which vendor has the most funding, and which UI looks modern?",
            "B": "What color is the application icon, how many employees follow the vendor on Twitter, and what is token cost?",
            "C": "How fast does the user type prompts, which monitor brand is used, and what is the office Wi-Fi bandwidth?",
            "D": "What does the work touch, must it run while devices are off, and who is allowed to hold and process the data?"
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Section 10. The three governing routing questions are: 1. What does the work touch? (files, connectors, databases, codebases). 2. Must it run while my device is off? (cloud vs. local dependency). 3. Who is allowed to hold and process the data? (compliance, regulatory custody, BAA coverage).",
            "distractor_A": "Option A is incorrect because raw benchmark scores and vendor venture funding do not determine workflow routing.",
            "distractor_B": "Option B is incorrect because superficial UI colors and social media metrics are irrelevant to systems architecture.",
            "distractor_C": "Option C is incorrect because user typing speed and monitor brands do not dictate data custody or runtime boundaries.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 37,
        "subtopic": "HIPAA, PHI, and BAA Realities on Managed Surfaces",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Regulated or contractually restricted data (Lines 1118-1123, 1751, 1761)",
        "scenario": "A hospital clinical research administrator wants to deploy Claude Cowork to summarize electronic health records containing patient names and cancer staging diagnoses. The administrator points out that the hospital holds an Enterprise agreement with Anthropic. Why does Section 10 forbid this deployment?",
        "options": {
            "A": "Cowork is not covered under Anthropic's BAA for HIPAA use; enterprise account visibility is not legal permission.",
            "B": "Electronic health records are technically incapable of being converted into digital text format for AI review.",
            "C": "HIPAA regulations require that all cancer patient records be reviewed exclusively by veterinary medicine doctors.",
            "D": "Commercial AI models refuse to process medical terms unless approved by an act of the United States Congress."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Section 10. The text explicitly warns: 'Anthropic now exposes Cowork activity to Enterprise compliance tooling... That approves no regulated workload by itself. As of this fact check, Anthropic states that Cowork is not covered under its BAA for HIPAA use. OpenAI makes the same point. Event-triggered Work tasks in ChatGPT for Healthcare are not BAA-covered and must not process PHI. Product availability is not permission.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because EHR systems natively export structured digital records (e.g., HL7, FHIR, text).",
            "distractor_C": "Option C is incorrect because human oncology records are governed by medical boards, not veterinary doctors.",
            "distractor_D": "Option D is incorrect because congressional statutory acts are not required for individual healthcare data processing workflows."
        }
    },
    {
        "id": 38,
        "subtopic": "De-identification as an Operational Routing Strategy",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Regulated or contractually restricted data (Lines 1121-1123)",
        "scenario": "A healthcare insurance claims analyst wants to use Claude Cowork to identify fraudulent billing patterns across 50,000 claim line items. Because Cowork lacks BAA coverage for protected health information, how can the analyst legitimately route this task per Section 10?",
        "options": {
            "A": "Transmit the claims data during weekend hours when federal regulatory compliance officers are out of office.",
            "B": "Strip or mask direct and quasi-identifiers, routing the underlying mathematical billing patterns instead of PHI.",
            "C": "Rename the claim spreadsheet column headers into an invented foreign language to conceal patient identities.",
            "D": "Upload the records to public web forums first and then instruct the agent to scrape the data from the internet."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Option B is uniquely accurate per Section 10. The text explains: 'Ask what the task needs: the identifiers, or only the pattern. A spending-trend analysis rarely needs customer names. Remove them, check what is left against your organization's standard, and you may not be routing regulated data at all. Removing what the task does not need is a route, not an evasion.' Removing regulated identifiers transforms the payload into safe, non-PHI pattern data.",
            "distractor_A": "Option A is incorrect because regulatory compliance laws apply 24/7 and cannot be bypassed by weekend scheduling.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Option C is incorrect because translating column names into foreign words does not de-identify underlying patient data.",
            "distractor_D": "Option D is incorrect because publishing confidential patient records to public forums constitutes an egregious data breach."
        }
    },
    {
        "id": 39,
        "subtopic": "The Open Path Trade-Off (Spine vs. Custody)",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 11: The open path: no vendor cloud (Lines 1153-1179)",
        "scenario": "A non-governmental organization handling sensitive political refugee relocation records evaluates whether to adopt commercial web agent platforms or deploy an open-source alternative (like OpenWork with self-hosted models). What fundamental operational trade-off does Section 11 establish between these two paths?",
        "options": {
            "A": "Commercial platforms charge zero dollars for enterprise accounts, whereas open-source tools require gold payments.",
            "B": "Open-source software tools are illegal to run in democratic nations without written United Nations clearance.",
            "C": "Vendors sell a working spine but hold custody; the open path gives custody and choice but requires you to build the spine.",
            "D": "Commercial platforms delete user accounts every twenty-four hours, whereas open tools provide free lifetime hardware."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Option C is uniquely accurate per Section 11. The fundamental trade is defined succinctly: 'The companies sell you a spine. The open path makes you build one. On the vendor surface, everything is handed to you and working on day one: sessions, files, sync, the phone gate, the scheduler. But it lives in their custody, in their format, at their price. On the open path, each of those is yours to set up, run, and fix. In exchange you get two things no vendor sells. First, custody, meaning your data on machines you control. Second, choice, meaning which model sees your prompts.'",
            "distractor_A": "Option A is incorrect because commercial platforms charge subscription fees and open-source models do not require gold.",
            "distractor_B": "Option B is incorrect because open-source AI software is fully legal and requires no UN permits.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Option D is incorrect because vendor platforms do not wipe accounts daily, nor does open software supply free hardware.",
        }
    },
    {
        "id": 40,
        "subtopic": "Rented vs. Owned Enforcement Across the Five Harness Verbs",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Appendix D: Harness Engineering, on the web (Lines 1519-1570)",
        "scenario": "A fintech engineering director must decide whether an automated account credit-limit adjustment workflow can remain in a managed Cowork plugin or must transition to an owned harness in CI. According to Appendix D, what condition makes transitioning to an engineered harness mandatory?",
        "options": {
            "A": "When the credit limit adjustment workflow completes its mathematical execution in under fifteen elapsed seconds.",
            "B": "When the fintech firm transitions all of its corporate desktop computers from Windows to macOS laptops.",
            "C": "When the engineering director decides to publish all customer bank balances on public social media websites.",
            "D": "When enforcement rules must be guaranteed by owned infrastructure, CI gates, and code rather than model compliance."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Option D is uniquely accurate per Appendix D. The text outlines when an owned harness is necessary across the five harness verbs (Constrain, Inform, Verify, Correct, Escalate): 'When Harness Engineering becomes necessary: A rule must be enforced even if the model's instructions say otherwise. A path, network destination, branch, command, or data class must be fenced by infrastructure you control. Verification must run as code and block acceptance automatically... The boundary is who enforces the rule. Build your own harness when a control must be provable on your terms.'",
            "distractor_A": "Option A is incorrect because execution latency does not dictate compliance enforcement architecture.",
            "distractor_B": "Option B is incorrect because operating system transitions have no bearing on backend financial risk controls.",
            "distractor_C": "Option C is incorrect because publishing customer balances breaches privacy and banking confidentiality laws.",
            "distractor_D": "N/A (Correct Option)"
        }
    }
]

def validate_and_save():
    print(f"Validating and balancing 40 questions for Chapter 09...")
    assert len(QUESTIONS_CH9) == 40, f"Expected 40 questions, got {len(QUESTIONS_CH9)}"

    # Validate character length variance & key distribution
    max_var = 0
    total_var = 0
    key_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    
    for q in QUESTIONS_CH9:
        key_counts[q["correct"]] += 1
        opts = q["options"]
        lens = [len(opts[k]) for k in ["A", "B", "C", "D"]]
        variance = max(lens) - min(lens)
        total_var += variance
        if variance > max_var:
            max_var = variance
        if variance >= 15:
            print(f"[!] Warning: Question {q['id']} has length variance {variance}: {lens}")
            
    print(f"Option Length Validation:")
    print(f"  - Maximum character variance across any question: {max_var} chars")
    print(f"  - Average character variance across all 40 questions: {total_var / 40:.2f} chars")
    print(f"Answer Key Distribution: {key_counts}")
    
    # Save to questions.json
    out_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(out_dir, "questions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(QUESTIONS_CH9, f, indent=2, ensure_ascii=False)
    print(f"[+] Successfully wrote: {json_path}")

    # Trigger compiler
    workspace_root = os.path.abspath(os.path.join(out_dir, ".."))
    compiler_path = os.path.join(workspace_root, ".agents", "skills", "pcao-f-mcq-compiler", "compile_chapter.py")
    if os.path.exists(compiler_path):
        print(f"[*] Running compiler: {compiler_path}")
        cmd = [sys.executable, compiler_path, "--chapter-dir", out_dir, "--title", "General Agents on the Web"]
        res = subprocess.run(cmd, check=True)
        print(f"[+] Compilation completed with exit code {res.returncode}")
    else:
        print(f"[!] Compiler not found at: {compiler_path}")

if __name__ == "__main__":
    validate_and_save()
