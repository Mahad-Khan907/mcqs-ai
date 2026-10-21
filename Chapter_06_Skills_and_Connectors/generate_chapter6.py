"""
Generator script for Chapter 06: Skills & Connectors
PCAO-F & Anthropic CCAO-F Certification Exam Guide
"""

import json
import os
import sys

QUESTIONS = [
  {
    "id": 1,
    "subtopic": "The 4-Way Architecture: Skills vs Connectors vs Projects vs Custom Instructions",
    "domain": "Domain 5: Configuration and Knowledge Management",
    "grounding": "Concept 4: Skills vs Connectors vs Projects vs Custom Instructions (Lines 149-198)",
    "scenario": "A regional marketing director manages dozens of client brand accounts. Each brand has its own permanent guidelines, voice principles, and confidential media plans that must never cross-pollinate into other brand workflows. Which persistent customization mechanism is uniquely suited for this requirement?",
    "options": {
      "A": "Authoring a dedicated Skill that encapsulates the reusable formatting rules and loads them on demand.",
      "B": "Deploying an external MCP Connector configured with continuous read-write access across the file system.",
      "C": "Creating an enterprise Project workspace containing all historical cooperative vendor payment records.",
      "D": "Inserting globally active Custom Instructions commanding concise outputs across every conversation."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Section 4. The text specifies that when an operator repeatedly re-explains 'how' to do a repeatable task (formatting, reporting voice, checklists), a Skill is the exact architectural feature designed for that purpose, as it provides reusable procedural instructions loaded dynamically only when relevant.",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because a Connector provides access to data sources or external apps to eliminate manual copy-pasting, rather than teaching procedural formatting rules.",
      "distractor_C": "Option C is incorrect because a Project is designed for standing contextual reference files applied continuously to a specific body of work, not on-demand procedural execution.",
      "distractor_D": "Option D is incorrect because Custom Instructions apply universally across all user interactions, making them unsuitable for task-specific reporting structures."
    }
  },
  {
    "id": 2,
    "subtopic": "Skills vs. Projects Operational Distinction",
    "domain": "Domain 5: Configuration and Knowledge Management",
    "grounding": "Concept 4: Skills vs Connectors vs Projects vs Custom Instructions (Lines 177-195)",
    "scenario": "A lead investigator at a regional environmental consultancy manages twenty ongoing municipal water quality assessments. He needs to establish an operational standard: baseline municipal regulatory codes must be present in every single chat, whereas specialized discharge audit procedures should only activate when requested. How should these two assets be partitioned?",
    "options": {
      "A": "Store both the baseline codes and the discharge procedures inside global Custom Instructions for all chats.",
      "B": "Embed the discharge audit checklist into Custom Instructions, and retain regulatory files inside a Connector.",
      "C": "Store the regulatory codes within a Project workspace, and deploy the discharge audit procedure as a Skill.",
      "D": "Deploy an external MCP Connector for regulatory standards, and maintain the discharge audit in a Project."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 4. Standing knowledge that applies continuously to an entire body of work belongs in a Project (where context loads immediately upon opening a chat), whereas on-demand procedural routines that sleep until specifically matched belong in a Skill.",
      "distractor_A": "Option A is incorrect because overloading global Custom Instructions with specialized technical procedures degrades general conversational performance across unrelated domains.",
      "distractor_B": "Option B is incorrect because Custom Instructions apply universally to all chats rather than specific audit tasks, and Connectors link to live external services rather than static PDF standards.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because static regulatory references do not require an active protocol bridge, and placing on-demand procedures in a Project forces unnecessary token overhead into every interaction."
    }
  },
  {
    "id": 3,
    "subtopic": "Skills vs. Custom Instructions Operational Scope",
    "domain": "Domain 5: Configuration and Knowledge Management",
    "grounding": "Concept 4: Skills vs Connectors vs Projects vs Custom Instructions (Lines 185-198)",
    "scenario": "A medical records archivist at a diagnostic hospital chain wishes to standardize two elements: (1) an unconditional preference that AI responses always use metric measurements, and (2) an eight-stage verification protocol used exclusively when compiling quarterly oncology registry submissions. Which architectural allocation correctly implements these requirements?",
    "options": {
      "A": "Implement metric preferences inside a Connector, and deploy the oncology verification protocol in a Project.",
      "B": "Implement metric preferences via Custom Instructions, and save the oncology protocol as a dedicated Skill.",
      "C": "Embed both the metric preference and the eight-stage verification protocol directly in Custom Instructions.",
      "D": "Configure both the metric preference and the specialized oncology protocol inside an enterprise Connector."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 4. Global preferences that apply universally across all interactions ('always use metric units') belong in Custom Instructions. Conversely, specialized workflows ('when compiling an eight-section oncology report') belong in a Skill, which sleeps until triggered.",
      "distractor_A": "Option A is incorrect because Connectors govern external SaaS connections rather than formatting preferences, and Projects are tied to specific workspace folders rather than procedural tasks.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because packing complex, domain-specific multi-step workflows into global Custom Instructions pollutes the context window of every routine query.",
      "distractor_D": "Option D is incorrect because neither of these requirements involves an API bridge or Model Context Protocol tool access to third-party database records."
    }
  },
  {
    "id": 4,
    "subtopic": "The Operating Layer Paradigm Shift",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 1: From chat box to operating layer (Lines 103-124)",
    "scenario": "A logistics coordinator needs an assistant to format dispatch emails, run delivery route calculations, and flag weight violations whenever a trucking manifest arrives. Which customization mechanism is designed to house this multi-step operational procedure?",
    "options": {
      "A": "Replacing conversational model interfaces entirely with rigid rules-based deterministic spreadsheet macros.",
      "B": "Upgrading user workstations to enterprise GPU hardware capable of running parallel token processing tasks.",
      "C": "Mandating that dispatchers enroll in computer science degree programs to manually script internal APIs.",
      "D": "Transitioning to an operating layer where AI connects directly to data sources and applies stored methods."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Section 1. The chapter defines the transition from an ephemeral 'chat box' to an 'operating layer' as the point where AI stops being a passive window requiring manual copy-pasting and becomes an active partner that directly accesses external tools (Connectors) and executes codified organizational standards (Skills).",
      "distractor_A": "Option A is incorrect because the operating layer leverages model intelligence and flexible tool connectivity rather than abandoning LLMs for legacy rigid macros.",
      "distractor_B": "Option B is incorrect because the operating layer is an architectural workflow concept involving SaaS integrations and skills, not local client-side hardware upgrades.",
      "distractor_C": "Option C is incorrect because the entire foundation of the chapter emphasizes '0 code from you' and non-programmer accessibility.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 5,
    "subtopic": "Diagnosing Repetitive Friction: How vs. Data",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 9: Which problems need a Skill, which need a Connector, which need both? (Lines 334-380)",
    "scenario": "A healthcare compliance manager evaluates a new skill package designed to process patient discharge records. Before enabling the skill across clinic accounts, what evaluation action represents sound operational oversight?",
    "options": {
      "A": "Drafting an ad-hoc, one-off investigative memo explaining a rare electrical transformer failure event.",
      "B": "Extracting inspection logs from Jira and structuring them into the firm's strict FDA audit layout.",
      "C": "Reformatting a raw technician interview transcript into standardized clinical voice within a single chat.",
      "D": "Searching a company Google Drive repository to locate the three most recent vendor calibration certificates."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 9. Extracting live operational data from an external app (Jira) requires a Connector, while enforcing the firm's mandatory, repeatable regulatory reporting structure requires a Skill. When an operator must fetch external data AND format it in a specific repeatable manner, both are required.",
      "distractor_A": "Option A is incorrect because a one-off draft that will not be repeated requires neither a Skill nor a Connector; it simply requires an effective ad-hoc prompt.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because reformatting text provided directly in the prompt requires only a Skill (teaching the 'how') without external app access.",
      "distractor_D": "Option D is incorrect because searching Drive to retrieve documents requires only a Connector (fetching the 'data') without specialized formatting rules."
    }
  },
  {
    "id": 6,
    "subtopic": "SKILL.md Structure & Progressive Disclosure Levels",
    "domain": "Domain 5: Configuration and Knowledge Management",
    "grounding": "Concept 2: What a Skill actually is & Concept 11: Anatomy of a SKILL.md (Lines 125-134, 402-423)",
    "scenario": "A systems administrator at an opticians chain configures thirty specialized clinical and administrative skills for retail branch staff. A junior technician worries that loading thirty comprehensive skill files will saturate the model's context window and create severe processing latency. Why is this technical concern invalid?",
    "options": {
      "A": "The model loads only frontmatter descriptions initially, fetching full instructions only upon matching.",
      "B": "Enterprise account subscriptions compress markdown files into binary bytecode before runtime execution.",
      "C": "Client browser local storage caches all skill instructions in isolated offline memory partitions.",
      "D": "The model permanently compiles all installed skill guidelines directly into its static neural weights."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Sections 2 and 11. Under the progressive disclosure architecture, Claude holds only Level 1 metadata (the short frontmatter name and description) in active context. The detailed instruction body (Level 2) and supplementary resources (Level 3) are loaded dynamically only when the user's prompt matches the description.",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because markdown files are plain-text documents parsed dynamically by the context engine rather than compiled into binary bytecode.",
      "distractor_C": "Option C is incorrect because progressive disclosure is managed within the model context orchestrator, not client-side browser storage partitions.",
      "distractor_D": "Option D is incorrect because skills are external context assets; they never modify or re-train the underlying frozen neural network weights."
    }
  },
  {
    "id": 7,
    "subtopic": "SKILL.md Technical Constraints and Naming Rules",
    "domain": "Domain 5: Configuration and Knowledge Management",
    "grounding": "Concept 11: Anatomy of a SKILL.md (Lines 417-423)",
    "scenario": "A boutique hotel operations manager attempts to upload a custom customer-recovery skill package to Claude.ai. The upload wizard immediately rejects the package with a parsing error. Upon inspecting the directory, which structural flaw represents the actual violation of the Agent Skills specification?",
    "options": {
      "A": "The frontmatter block was bounded at the top and bottom by exactly three horizontal hyphens.",
      "B": "The root instruction file was saved as SKILL.md inside a kebab-case directory named guest-recovery.",
      "C": "The instruction body included three levels of standard markdown headings and clean bulleted items.",
      "D": "The root instruction file was saved as skill.txt inside a folder titled customer_recovery_sop."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Section 11. The specification explicitly dictates that the file must be named exactly 'SKILL.md' (uppercase with .md extension) and the parent folder must use 'kebab-case' (hyphens rather than underscores or spaces). Naming it 'skill.txt' or using snake_case violates core specification rules.",
      "distractor_A": "Option A is incorrect because bounding the YAML frontmatter block with triple dashes (---) is the standard required formatting syntax.",
      "distractor_B": "Option B is incorrect because naming the file SKILL.md inside a kebab-case folder (guest-recovery) is the exact valid syntax.",
      "distractor_C": "Option C is incorrect because standard markdown headings and bulleted instructions are completely permissible and expected within the instruction body.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 8,
    "subtopic": "Role of Supplementary Folders: references, assets, scripts",
    "domain": "Domain 5: Configuration and Knowledge Management",
    "grounding": "Concept 11: Anatomy of a SKILL.md (Lines 417-423)",
    "scenario": "A commercial property accountant is designing a sophisticated lease valuation skill. The workflow requires referencing a 50-page statutory tax depreciation schedule, filling out an exact corporate spreadsheet template, and calculating complex compound interest. How should these supplementary assets be organized within the skill folder?",
    "options": {
      "A": "Store the Python math script in references/, blank templates in scripts/, and tax rules in assets/.",
      "B": "Paste the entire 50-page tax schedule directly into the SKILL.md frontmatter description block.",
      "C": "Store tax schedules in references/, spreadsheet templates in assets/, and math programs in scripts/.",
      "D": "Merge all documentation, formulas, and binary spreadsheet files into a single flat SKILL.md file."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 11. Complex skills organize Level 3 assets into three designated subdirectories: `references/` for extensive background documentation loaded only when needed, `assets/` for templates and boilerplates to be populated, and `scripts/` for deterministic code and computation.",
      "distractor_A": "Option A is incorrect because it swaps the functional roles of the standard folders, misplacing executable scripts into references and templates into scripts.",
      "distractor_B": "Option B is incorrect because the frontmatter description must remain concise and short; pasting 50 pages into it exhausts context tokens and triggers validation errors.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because binary files cannot be embedded into markdown text files, and bloating the primary file degrades model efficiency."
    }
  },
  {
    "id": 9,
    "subtopic": "The Client Mindset in Skill Construction",
    "domain": "Domain 1: Prompting and Task Execution",
    "grounding": "Concept 10: The fastest path: let AI write it (Lines 388-400)",
    "scenario": "An enterprise developer creates a skill package with a 2,000-word instruction guide, but writes only a concise 20-word description in the YAML frontmatter. Why does the progressive disclosure pattern keep full skill instructions in the body while exposing only the description in the YAML frontmatter?",
    "options": {
      "A": "Commissioning an external systems integration firm to compile an offline binary executable program.",
      "B": "Completing an introductory Python scripting module to manually format the underlying JSON schema.",
      "C": "Acting as an inspecting client who articulates clear business logic while skill-creator writes code.",
      "D": "Manually drafting the complete regular expression pattern checks within an IDE code editing terminal."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 10. The text emphasizes that building skills requires zero programming: 'You are the client, not the contractor. A good client does not lay bricks. They write a clear brief and check the result against things they can measure.' The built-in `skill-creator` tool authors the files and code based on natural language interaction.",
      "distractor_A": "Option A is incorrect because commercial AI platforms provide native tools (such as `skill-creator`) that construct production-grade skills within minutes without external agencies.",
      "distractor_B": "Option B is incorrect because manual Python programming is explicitly unnecessary under the 'code you never write' paradigm.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because operators should never manually code regex syntax; AI generates all necessary parsing logic from plain-English descriptions."
    }
  },
  {
    "id": 10,
    "subtopic": "Skill Persistence and Profile Management",
    "domain": "Domain 5: Configuration and Knowledge Management",
    "grounding": "Concept 14: Saving and sharing your skill (Lines 478-490)",
    "scenario": "An educational consultant collaborates with `skill-creator` in a chat session to develop a comprehensive lesson-planning skill. Once the tool finishes generating the files and presenting the preview panel, what operational step is required to make this skill permanently active across all future conversations?",
    "options": {
      "A": "Click the 'Save skill' button in the builder panel to add it directly to Personal Skills.",
      "B": "Download the generated zip file, extract its contents, and re-upload them via a terminal FTP script.",
      "C": "Copy the raw markdown text and paste it into the system prompt window of every subsequent chat.",
      "D": "Submit an administrative service ticket to the cloud provider requesting manual container mounting."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Section 14. Saving a completed skill is turnkey: 'When skill-creator finishes, it shows your skill in a panel beside the chat with a \"Save skill\" button. Click it, and the skill drops into your personal skills, switched on and private to your account. No zip file, no upload.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because manual extraction and FTP re-uploading are completely obsolete and unnecessary in the native interface.",
      "distractor_C": "Option C is incorrect because pasting instructions into every chat regresses back to the manual chat-box friction that skills are designed to eliminate.",
      "distractor_D": "Option D is incorrect because personal skill deployment is fully self-service and does not require third-party cloud infrastructure tickets."
    }
  },
  {
    "id": 11,
    "subtopic": "MCP Governance and Technical Foundations",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 3: What a Connector actually is & Part 4 (Lines 135-148, 498-500)",
    "scenario": "A chief information officer at a legal services partnership reviews a security proposal to integrate external document management connectors. She inquires whether adopting the Model Context Protocol (MCP) introduces a proprietary vendor lock-in risk tied exclusively to Anthropic. How should the lead AI architect answer?",
    "options": {
      "A": "MCP requires all connected external corporate databases to be hosted on Anthropic server clusters.",
      "B": "MCP is a closed, proprietary communications protocol licensed exclusively through commercial tiers.",
      "C": "MCP operates as an undocumented client browser script without formal cross-vendor governance.",
      "D": "MCP is an open standard governed neutrally by the Linux Foundation's Agentic AI Foundation."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Section 3 and Part 4. The chapter explains that MCP (Model Context Protocol) is an open industry standard whose governance was formally transitioned to the Linux Foundation's Agentic AI Foundation, ensuring that connector plumbing is governed neutrally across multiple industry vendors rather than locked to a single proprietary provider.",
      "distractor_A": "Option A is incorrect because MCP connects to external apps via APIs while data remains in the user's existing SaaS infrastructure; data is never relocated to vendor clusters.",
      "distractor_B": "Option B is incorrect because MCP is open-source and governed by an independent non-profit foundation, not closed or proprietary.",
      "distractor_C": "Option C is incorrect because MCP is an officially published, standardized protocol with multi-vendor adoption across desktop, terminal, and cloud systems.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 12,
    "subtopic": "Permission Inheritance Boundary in Connectors",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Concept 3: What a Connector actually is (Lines 141-144, 798-800)",
    "scenario": "A staff radiologist connects her corporate Google Drive account to Claude to assist in summarizing imaging intake schedules. An IT compliance officer expresses concern that connecting Google Drive will inadvertently grant the AI visibility into confidential hospital executive payroll records stored on the same enterprise domain. Why is this fear unfounded?",
    "options": {
      "A": "Cloud AI platforms automatically redact all spreadsheet documents containing financial column headers.",
      "B": "A Connector inherits only the existing access permissions of the specific authenticated account.",
      "C": "Enterprise firewalls automatically restrict AI access to files created within the last forty-eight hours.",
      "D": "Google Drive automatically blocks LLM API connections from indexing files stored in shared folders."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 3. Principle 1 states: 'AI inherits the permissions you already have. If your account cannot open a file, channel, or record, the connector cannot either. Connecting Google Drive does not hand AI your whole company's drive.' The model can never see or touch assets beyond the authenticated user's credentials.",
      "distractor_A": "Option A is incorrect because connectors do not perform heuristic data redaction based on column labels; access control is strictly credential-based.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because connector access is governed by user ACLs, not arbitrary 48-hour timestamp filters.",
      "distractor_D": "Option D is incorrect because Google Drive supports authorized MCP indexing across all shared drives to which the user has legitimate access."
    }
  },
  {
    "id": 13,
    "subtopic": "Read-Only vs. Write Access Ladders",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Concept 3: What a Connector actually is (Lines 144-145, 587-588)",
    "scenario": "A customer support desk configures two custom skills: one named 'process-refunds' and another named 'handle-billing-inquiries'. The assistant frequently invokes the wrong skill when customers ask about invoice adjustments. How should the team resolve this conflict?",
    "options": {
      "A": "Grant immediate unrestricted write access to evaluate automated destructive recovery procedures.",
      "B": "Begin strictly with read-only access, escalating to write permissions only after proven reliability.",
      "C": "Operate write access exclusively on mobile devices while restricting desktop clients to read-only.",
      "D": "Disable read-only access permanently because model inference requires bi-directional sync to operate."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 3 and the Safe-Use Checklist. The text mandates: 'Start read-only. Grant write access only once you trust how the tool behaves.' Read-only allows searching and summarizing without the risk of accidental ticket deletion, modification, or erroneous message transmission.",
      "distractor_A": "Option A is incorrect because granting immediate write access violates blast-radius containment and risks unrecoverable data deletion.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because authorization privileges are governed by connector configuration, not by mobile versus desktop hardware forms.",
      "distractor_D": "Option D is incorrect because read-only access is completely functional for document retrieval, summarization, and analysis without requiring write permissions."
    }
  },
  {
    "id": 14,
    "subtopic": "Per-Conversation Connector Scope Management",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Concept 3: What a Connector actually is (Lines 145-146, 298-301)",
    "scenario": "A commercial property manager has successfully linked five SaaS connectors to her account: Gmail, Google Drive, Slack, Notion, and QuickBooks. When opening a fresh conversation to draft an internal tenant dispute memo, how should connector availability be governed to maintain security?",
    "options": {
      "A": "Rely on the AI model to automatically negotiate external authentication tokens without supervision.",
      "B": "Allow all five connectors to remain continuously active in the background across every single chat.",
      "C": "Uninstall and re-authenticate all external connectors prior to launching each individual query.",
      "D": "Enable only the specific connectors and narrow folders required for the active conversation."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Section 3. Rule 3 specifies: 'You turn connectors on per conversation. Connecting an app once makes it available. You still decide which connectors a chat may use, and you choose the scope, which means how much of the app AI may reach. One folder is a smaller scope than a whole drive, and smaller is safer.'",
      "distractor_A": "Option A is incorrect because authentication tokens require explicit human OAuth authorization and cannot be negotiated autonomously.",
      "distractor_B": "Option B is incorrect because leaving all connectors continuously active leaves unnecessary doors open, expanding security blast radius and saturating tool context.",
      "distractor_C": "Option C is incorrect because connectors only need to be authenticated once; enabling or disabling them per chat is a simple toggle in the menu.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 15,
    "subtopic": "Tool Access Setting: Load-on-Demand",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 7: Connecting your apps (Lines 301-303)",
    "scenario": "A enterprise analyst at a multinational manufacturing conglomerate maintains fourteen active custom and directory MCP connectors to query disparate supply chain endpoints. When inspecting the connector configuration panel, why should the analyst set the 'Tool access' setting to 'load-on-demand'?",
    "options": {
      "A": "It prevents model context saturation by loading specific connector actions only when requested.",
      "B": "It forces third-party database servers to cache all corporate transaction records in local RAM.",
      "C": "It permanently bypasses multi-factor biometric authentication across connected external services.",
      "D": "It converts interactive graphical UI panels into raw non-interactive plain-text terminal logs."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Section 7. The text advises: 'Each connector brings a list of actions, and the settings call those actions tools... With ten or more connectors switched on, choose load-on-demand, which loads an action only when a request needs it.' This prevents bloating the active prompt with dozens of unused tool schemas.",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because tool access settings govern LLM context loading, not third-party database hardware RAM caching.",
      "distractor_C": "Option C is incorrect because load-on-demand has zero bearing on enterprise identity authentication or MFA protocols.",
      "distractor_D": "Option D is incorrect because load-on-demand does not alter the rendering behavior of interactive connectors."
    }
  },
  {
    "id": 16,
    "subtopic": "The Critical Role of the Description Field",
    "domain": "Domain 1: Prompting and Task Execution",
    "grounding": "Concept 12: The description field is the whole game (Lines 424-427)",
    "scenario": "A clinic operations coordinator authors a comprehensive triage preparation skill. She writes eight pages of rigorous clinical protocols inside the body of `SKILL.md`, but enters 'Assists clinical staff with various departmental tasks' in the frontmatter description. In practice, the skill never fires automatically. What architectural mechanism explains this failure?",
    "options": {
      "A": "The clinic coordinator failed to include an explicit credit card billing token in frontmatter.",
      "B": "The model refuses to process markdown instruction files whose word count exceeds five pages.",
      "C": "The model evaluates task relevance exclusively against the description without reading the body.",
      "D": "Clinical triage workflows are blocked by the platform's automated HIPAA compliance engine."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 12. The text establishes: 'The description decides whether your skill ever fires. AI does not read your instructions to judge relevance. A vague description means a skill that never starts, and a sharp one starts exactly when it should.' Because Level 1 progressive disclosure only loads the description, an uninformative description leaves the skill dormant.",
      "distractor_A": "Option A is incorrect because skill configuration does not require payment tokens or billing credentials in frontmatter.",
      "distractor_B": "Option B is incorrect because skills can accommodate extensive reference materials; the length of the body has no bearing on initial description matching.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because the issue is purely semantic matching in progressive disclosure, not regulatory content blocking."
    }
  },
  {
    "id": 17,
    "subtopic": "Trigger Phrases and Description Calibration",
    "domain": "Domain 1: Prompting and Task Execution",
    "grounding": "Concept 12: The description field is the whole game (Lines 426-451)",
    "scenario": "An HVAC maintenance technician embeds a 400-page chiller error code directory directly inside `SKILL.md`. Every time the skill activates, it consumes 120,000 context tokens before the user types a prompt. Why is placing raw reference data inside the procedural instructions file an architectural error?",
    "options": {
      "A": "Writes social captions in our brand voice. Use when drafting Instagram or LinkedIn posts.",
      "B": "A comprehensive enterprise marketing solution for all internal and external communication.",
      "C": "Handles general advertising copywriting and social media content for our commercial business.",
      "D": "Useful for employees who want their marketing documents to sound professional and appealing."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Section 12. The chapter demonstrates that an effective description states precisely what the skill does, the exact operational context, and the natural trigger phrases a user would say: 'Writes social captions in our brand voice (no exclamation marks, question-hook openings). Use when drafting Instagram, LinkedIn, or X captions.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because 'comprehensive enterprise marketing solution' is an uncalibrated buzzword phrase lacking specific user trigger verbs.",
      "distractor_C": "Option C is incorrect because it is overly generic and omits specific platform channels and concrete user invocation terminology.",
      "distractor_D": "Option D is incorrect because vague aspirational statements ('sound professional and appealing') fail to inform the model when to load the skill."
    }
  },
  {
    "id": 18,
    "subtopic": "Negative Triggers to Prevent Eager Over-Firing",
    "domain": "Domain 1: Prompting and Task Execution",
    "grounding": "Concept 12: The description field is the whole game (Lines 454-455)",
    "scenario": "A financial advisory firm creates a 'statutory-pension-audit' skill. Whenever an advisor asks a quick, basic arithmetic question such as 'What is 15% of $80,000?', the system mistakenly triggers the comprehensive 10-page statutory audit template. What engineering modification should be added to the skill's description?",
    "options": {
      "A": "Delete the entire frontmatter description block and leave only the YAML title line intact.",
      "B": "Add a negative trigger explicitly commanding: 'Do NOT use for one-off math or quick queries.'",
      "C": "Increase the temperature hyperparameter in the chat interface to promote creative responses.",
      "D": "Rename the skill directory using uppercase snake_case syntax with embedded exclamation tags."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 12. A 'negative trigger' is an explicit instruction in the description defining when NOT to activate: 'A negative trigger is a line that says when not to use the skill, and it helps when a skill fires too eagerly. For example: \"Do NOT use for one-off calculations or quick questions. Use only for full month-end reports.\"'",
      "distractor_A": "Option A is incorrect because deleting the description prevents progressive disclosure from functioning, causing the skill to never fire automatically.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because temperature hyperparameters do not regulate semantic intent matching in skill loaders.",
      "distractor_D": "Option D is incorrect because directory names must strictly adhere to kebab-case, and changing folder names does not fix semantic over-firing."
    }
  },
  {
    "id": 19,
    "subtopic": "Invocation Modalities Across Different Interfaces",
    "domain": "Domain 1: Prompting and Task Execution",
    "grounding": "Concept 5: The question everyone asks: do I type a slash command, or does AI just know? (Lines 199-249)",
    "scenario": "An executive assistant uses Claude across three distinct workplace surfaces: Claude.ai on the web, Cowork inside Microsoft Excel, and Claude Code in a terminal window. What is the standard, universal behavior for invoking an installed skill across all three surfaces?",
    "options": {
      "A": "Terminal tools require users to manually input raw hexadecimal memory pointers for each skill.",
      "B": "Typing a forward slash command is mandatory on web interfaces to display the active skill menu.",
      "C": "Skills cannot execute in Microsoft Excel without running local client Python terminal scripts.",
      "D": "Describing the task in plain English automatically fires matching skills across all platforms."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Section 5. The summary table and text establish that describing the task in natural language is automatic by default across Claude.ai, Cowork/Office add-ins, and Claude Code. While slash commands exist as optional manual menus in Cowork and terminal tools, automatic plain-English triggering works everywhere.",
      "distractor_A": "Option A is incorrect because command-line tools like Claude Code read standard `SKILL.md` files natively and require zero low-level memory coding.",
      "distractor_B": "Option B is incorrect because Claude.ai relies on automatic semantic matching by default, although naming the skill in plain English also works.",
      "distractor_C": "Option C is incorrect because Cowork and Microsoft 365 add-ins natively integrate skills without requiring terminal scripts.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 20,
    "subtopic": "Diagnostic Probing via Model Self-Reflection",
    "domain": "Domain 7: Troubleshooting and Optimization",
    "grounding": "Concept 12: The description field is the whole game (Lines 452-453, 638-644)",
    "scenario": "A secondary school head administrator authors a 'student-disciplinary-brief' skill. She wants to ensure that the skill will reliably trigger when teachers submit incident summaries, without accidentally taking over routine lesson plan requests. Which diagnostic prompt should she submit to verify the skill's calibration?",
    "options": {
      "A": "'Execute a benchmark stress test by submitting 500 simultaneous automated chat requests.'",
      "B": "'Print the binary machine code assembly instructions underlying this installed skill package.'",
      "C": "'When would you use my student-disciplinary-brief skill, and when would you NOT use it?'",
      "D": "'Decompile the server-side Linux kernel modules currently running this conversational session.'"
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 12 and the Try-This-Now exercises. The recommended debugging technique is to ask the model directly: 'When would you use my [skill-name] skill, and when would you NOT use it?' The model will reflect its understanding of the description back in its own words, instantly revealing if the scope is too broad or too narrow.",
      "distractor_A": "Option A is incorrect because stress-testing throughput does not evaluate whether the semantic description triggers appropriately.",
      "distractor_B": "Option B is incorrect because markdown skills do not compile into machine assembly code, and this prompt yields no semantic calibration data.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because kernel modules are irrelevant to conversational skill description matching."
    }
  },
  {
    "id": 21,
    "subtopic": "The 3-Stage Pipeline: Connector -> Skill -> Review",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 8: The real magic: Skills + Connectors together (Lines 308-330)",
    "scenario": "A green coffee bean importer designs an automated workflow to process weekly container shipment manifests. Her architecture combines an external Google Drive connector, a custom 'import-reconciliation' skill, and a final supervisory checkpoint. What are the discrete functional responsibilities of each component in this pipeline?",
    "options": {
      "A": "The connector authorizes client credit cards, the human formats tables, and the skill executes.",
      "B": "The skill establishes the OAuth network handshake, the connector formats text, and AI reviews.",
      "C": "The human manually parses raw files, the connector drafts summaries, and the skill archives.",
      "D": "The connector fetches live data, the skill formats and flags variances, and the human reviews."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Section 8. The diagram and pipeline text explicitly define the 3-stage division of labor: Stage 1 is the Connector (fetches the real data from external apps), Stage 2 is the Skill (shapes the output, enforces formatting, groups line items, and flags thresholds), and Stage 3 is the human operator (reviews the verified output in minutes rather than hours).",
      "distractor_A": "Option A is incorrect because connectors govern SaaS data access rather than payment billing, and skills automate formatting rather than humans.",
      "distractor_B": "Option B is incorrect because the connector handles network data access while the skill shapes output, not vice-versa, and human oversight is non-delegable.",
      "distractor_C": "Option C is incorrect because the connector automates data fetching precisely to liberate the human from manual file parsing.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 22,
    "subtopic": "Accountant Monthly Close Workflow Mechanics",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 8: The real magic: Skills + Connectors together (Lines 312-327)",
    "scenario": "A senior auditor at an accounting firm tasks Claude with: 'Prepare the March client summary for DEMO Trading from DEMO-ledger-March in my Drive.' With both the Google Drive connector and the 'client-summary' skill active, what automated sequence occurs behind the scenes?",
    "options": {
      "A": "Claude modifies the underlying ledger spreadsheet in place, permanently deleting flagged rows.",
      "B": "The skill searches the public web for tax benchmarks, and Drive sends automated emails to clients.",
      "C": "Drive fetches the file, the skill formats currency and flags thresholds, yielding a 4-part report.",
      "D": "Drive executes a Python terminal script to convert the client ledger into an offline SQL database."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 8. When the single command is issued, the Drive connector fetches the ledger spreadsheet without manual copy-pasting, and the skill enforces reporting currency formatting, groups transactions by expense head, flags payments exceeding the withholding threshold, and outputs the firm's standard four-section report.",
      "distractor_A": "Option A is incorrect because the Drive connector cannot edit spreadsheets in place, and auditing skills flag items rather than deleting financial data.",
      "distractor_B": "Option B is incorrect because the workflow processes internal client ledger files rather than executing open-web scraping or automated outbound emails.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because the process runs within Claude's native document processing engine without requiring external SQL conversions."
    }
  },
  {
    "id": 23,
    "subtopic": "The Capabilities Toggle Requirement",
    "domain": "Domain 3: Product and Model Selection",
    "grounding": "Concept 6: The skills that come built in (Lines 256-276, 305-307)",
    "scenario": "A commercial property analyst instructs Claude to generate a downloadable, formatted Excel spreadsheet containing thirty amortized lease schedules. The model outputs a simple markdown text table in chat and states it cannot create the standalone `.xlsx` file. What system setting was neglected?",
    "options": {
      "A": "The 'Code execution and file creation' capability toggle was switched off in account settings.",
      "B": "The analyst forgot to type a mandatory forward slash command before naming the spreadsheet.",
      "C": "The user failed to install an external third-party macro compiler from a developer forum.",
      "D": "The browser window was running in private incognito mode, which disables tabular generation."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Section 6. The built-in document generation skills (Word, Excel, PowerPoint, PDF) depend entirely on a single master toggle: 'Code execution and file creation' under Settings $\\rightarrow$ Capabilities. The label explicitly notes: 'Required for skills.' If disabled, Claude cannot execute the code required to assemble binary office files.",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because slash commands are not required in Claude.ai to generate documents; requests are expressed in natural language.",
      "distractor_C": "Option C is incorrect because document generation is a native, built-in Anthropic capability that requires no external third-party macro tools.",
      "distractor_D": "Option D is incorrect because browser incognito sessions do not restrict server-side document generation capabilities."
    }
  },
  {
    "id": 24,
    "subtopic": "Diagnosing Operational Friction Across Workflows",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 9: Which problems need a Skill, which need a Connector, which need both? (Lines 334-380)",
    "scenario": "A sports physiotherapist dictates patient intake notes into Claude. In every session, she has to manually remind the model: 'Always extract subjective complaints first, list objective range-of-motion measurements second, format in SOAP sections, and never use Latin medical jargon.' What exact architectural tool solves this specific friction?",
    "options": {
      "A": "An external Model Context Protocol Connector linking her browser directly to PubMed.",
      "B": "A dedicated SOAP-formatting Skill that codifies these clinical structural rules once.",
      "C": "An automated web scraping script deployed in a headless server environment overnight.",
      "D": "A global Custom Instruction mandating that all conversational outputs be under 100 words."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 9. The friction described is: 'I paste the same formatting, voice, or method rules every time.' The diagnostic guide explicitly maps this symptom to a Skill (e.g., SOAP clinical notes). Because the data is being dictated directly in the prompt, no external app connector is needed.",
      "distractor_A": "Option A is incorrect because linking to PubMed does not teach the AI how to format patient intake notes in the clinic's preferred SOAP structure.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because scraping public medical websites is completely irrelevant to standardizing personal clinical documentation.",
      "distractor_D": "Option D is incorrect because an arbitrary word-count restriction would truncate essential medical assessments rather than structuring them correctly."
    }
  },
  {
    "id": 25,
    "subtopic": "Interactive Connectors vs. Standard Text Connectors",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Concept 3: What a Connector actually is & Concept 7: Connecting your apps (Lines 147-148, 303)",
    "scenario": "A UI/UX design lead connects Figma and Canva to Claude.ai. While inspecting the directory, she notices that certain connectors display an 'Interactive' badge. What unique operational capability distinguishes an interactive connector from a standard connector?",
    "options": {
      "A": "It automatically executes local command-line bash scripts without user confirmation prompts.",
      "B": "It grants the model permanent administrative write access to overwrite cloud server backups.",
      "C": "It renders an active, responsive visual UI canvas directly inside the conversational chat.",
      "D": "It translates all incoming foreign language prompt tokens into English before processing."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Sections 3 and 7. The text defines interactive connectors: 'An interactive connector draws a live panel inside the chat instead of returning only text.' This enables rich visual canvases, interactive design previews, and embedded UI controls within the dialogue stream.",
      "distractor_A": "Option A is incorrect because interactive connectors do not run autonomous local bash scripts without human supervision.",
      "distractor_B": "Option B is incorrect because interactive badges denote UI display capabilities, not destructive server administration privileges.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because visual UI rendering is unrelated to multi-lingual token translation."
    }
  },
  {
    "id": 26,
    "subtopic": "Failure Timing: Immediate Inception Errors",
    "domain": "Domain 7: Troubleshooting and Optimization",
    "grounding": "Concept 13: Test, then iterate (Lines 467-472)",
    "scenario": "A warehouse logistics manager creates an 'inventory-discrepancy' skill. Upon testing it in a brand-new chat with a realistic inventory log, the model completely ignores the skill's formatting rules from the very first response, outputting generic conversational prose. According to the timing taxonomy in Section 13, where does the root cause reside?",
    "options": {
      "A": "The cloud provider's physical server hardware experienced an unrecoverable memory fault.",
      "B": "The conversation context window became saturated from excessive multi-turn dialogue history.",
      "C": "The underlying third-party enterprise database connector lost network socket connectivity.",
      "D": "The defect is inside the skill file itself, specifically a vague description or loose instructions."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Section 13. The timing taxonomy establishes: 'Wrong from the first reply. The problem is in the file itself. It never starts (description too vague), starts on the wrong things (description too broad), or output is off (an instruction is loose).' Because the failure occurred immediately in a fresh chat, context saturation is ruled out.",
      "distractor_A": "Option A is incorrect because cloud hardware faults produce system HTTP errors, not syntactically coherent generic prose.",
      "distractor_B": "Option B is incorrect because this was the first reply in a fresh conversation, meaning the context window was completely clear.",
      "distractor_C": "Option C is incorrect because the scenario describes a skill formatting failure on user-provided prompt data, not a connector network outage.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 27,
    "subtopic": "Failure Timing: Context Degradation Over Long Chats",
    "domain": "Domain 7: Troubleshooting and Optimization",
    "grounding": "Concept 13: Test, then iterate (Lines 473-474)",
    "scenario": "A municipal archivist uses a specialized 'records-classification' skill. For the first twenty document summaries, the assistant adhered flawlessly to the required 5-part classification schema. By the thirty-fifth turn in the same chat, the model begins omitting section headers and drifting in tone. How should the archivist remediate this issue?",
    "options": {
      "A": "Rewrite the underlying SKILL.md instruction body to add repetitive strict formatting warnings.",
      "B": "Open a fresh chat session and restate the task, leaving the original skill file unmodified.",
      "C": "Uninstall the skill, re-authenticate your user profile, and clear browser cookies and cache.",
      "D": "Downgrade the account from an enterprise tier to a free tier to reset model inference quotas."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 13. The timing diagnostic states: 'Right at first, worse as the chat grows. The chat got long and AI lost track. The skill is fine, so do not edit the file. Start a fresh chat and restate the task.' Editing a perfectly good skill file in response to context degradation is a common operational error.",
      "distractor_A": "Option A is incorrect because editing a functional skill file does not solve context contamination caused by excessively long conversation histories.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because browser cache and cookie resets have zero effect on conversational token drift within an active chat thread.",
      "distractor_D": "Option D is incorrect because downgrading subscription tiers reduces available context and capabilities rather than fixing drift."
    }
  },
  {
    "id": 28,
    "subtopic": "Failure Timing: Deterministic Calculation Errors & Script Migration",
    "domain": "Domain 7: Troubleshooting and Optimization",
    "grounding": "Concept 13: Test, then iterate (Lines 474-475)",
    "scenario": "A payroll supervisor designs a skill to audit employee overtime hours. Despite repeatedly tightening the natural language prompt wording ('Ensure you accurately multiply overtime hours by exactly 1.5x before summing'), the model consistently makes subtle arithmetic rounding mistakes across complex 50-row timesheets. What structural remedy solves this failure?",
    "options": {
      "A": "Migrate the exact arithmetic calculation step into a code script inside the scripts/ folder.",
      "B": "Add additional capitalization and exclamation points to the natural language instructions.",
      "C": "Instruct the model to adopt the persona of a world-champion mental calculation prodigy.",
      "D": "Paste the entire company employee handbook directly into the YAML frontmatter description."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Section 13. The timing taxonomy notes: 'The same mistake every run, even after you tightened the wording. The step is in the wrong place. An exact step, such as a sum or a threshold check, belongs in a small program, because code is exact and a sentence gets read differently each time. Ask skill-creator to move it.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because adding emotional intensity or capital letters does not alter the fundamental probabilistic nature of token generation for arithmetic.",
      "distractor_C": "Option C is incorrect because persona prompting cannot guarantee deterministic mathematical precision across large numerical tables.",
      "distractor_D": "Option D is incorrect because bloating the frontmatter with an employee handbook pollutes Level 1 progressive disclosure without fixing arithmetic rounding."
    }
  },
  {
    "id": 29,
    "subtopic": "Failure Timing: Environmental and Template Drift",
    "domain": "Domain 7: Troubleshooting and Optimization",
    "grounding": "Concept 13: Test, then iterate (Lines 475-476)",
    "scenario": "A medical clinic administrator observes that an 'insurance-preauthorization' skill, which functioned with 100% accuracy throughout 2025, suddenly began producing malformed, rejected claims in June 2026, despite nobody having modified the `SKILL.md` file. What operational reality explains this failure?",
    "options": {
      "A": "The model's underlying neural network weights degraded due to natural operational bit-rot.",
      "B": "External dependencies drifted, such as updated insurer claim templates or portal data schemas.",
      "C": "The user's local operating system automatically revoked read permissions on text files.",
      "D": "Markdown syntax specifications were officially deprecated across cloud server operating systems."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Section 13. The guide explains: 'It used to work and now does not. The skill did not change, so something around it did. Your threshold, your template, a file the connector reads, or how your team now works. Read the skill again against how you work today. Nothing warns you when a skill goes out of date.'",
      "distractor_A": "Option A is incorrect because frozen neural network weights do not suffer from physical bit-rot or random cognitive degradation.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because local OS permissions do not silently mutate to block specific markdown files while leaving others intact.",
      "distractor_D": "Option D is incorrect because markdown remains the universal standard for LLM documentation and has not been deprecated."
    }
  },
  {
    "id": 30,
    "subtopic": "The Colleague Readability Quality Benchmark",
    "domain": "Domain 2: Output Evaluation and Validation",
    "grounding": "Concept 13: Test, then iterate (Lines 460-462)",
    "scenario": "A pricing manager at a national tyre wholesale distributor audits a junior analyst's newly drafted `SKILL.md`. The instructions contain the line: 'Carefully flag all unacceptably high fleet discount percentages.' How should this instruction line be evaluated under operational clarity standards?",
    "options": {
      "A": "It fails the colleague test because subjective terms cause inconsistent outputs across runs.",
      "B": "It passes the colleague test because experienced commercial pricing analysts understand discounts.",
      "C": "It fails because skills are strictly prohibited from analyzing numerical percentage values.",
      "D": "It passes because LLMs possess intrinsic knowledge of commercial tyre retail profit margins."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Section 13. Rule 2 specifies the benchmark: 'Read the draft before you test it. Ask one question of every instruction line: would two colleagues who read it do the same thing? \"Flag the big payments\" fails. \"Flag any single payment above the withholding threshold with a WITHHOLDING note\" passes. A failing line shows no error message. The output just comes out different each run.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because subjective interpretations of 'unacceptably high' vary wildly among colleagues and yield unpredictable model behavior.",
      "distractor_C": "Option C is incorrect because skills frequently process numerical thresholds, provided the criteria are expressed with explicit mathematical boundaries.",
      "distractor_D": "Option D is incorrect because foundation models have no psychic awareness of a specific firm's proprietary internal discount tolerance thresholds."
    }
  },
  {
    "id": 31,
    "subtopic": "Community Skill Threat Vectors: Prompt Injection",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Concept 6 & Part 5: Use this safely (Lines 283-284, 574-577)",
    "scenario": "A junior financial analyst downloads a free 'automated-crypto-reconciliation' skill package posted by an anonymous user on an internet community forum. During execution, the skill quietly instructs the model to ignore safety guidelines and print system configuration variables. What security threat vector does this demonstrate?",
    "options": {
      "A": "A transient network socket timeout during public model API token serialization routines.",
      "B": "Hardware failure caused by running unauthorized client scripts on enterprise workstations.",
      "C": "Prompt injection embedded within an unvetted community skill's natural language instructions.",
      "D": "An official automated deprecation notice broadcast by the Linux Foundation MCP committee."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 6 and Part 5. The text warns: 'A free skill from a stranger is a text file you are about to let AI follow... Malicious skills are the first risk. A skill is a text file, and possibly some programs, so a bad actor can write one whose hidden instructions tell AI to leak data or contact a suspicious server. The named danger is prompt injection.'",
      "distractor_A": "Option A is incorrect because the behavior stems from malicious adversarial text instructions, not network connectivity timeouts.",
      "distractor_B": "Option B is incorrect because prompt injection is an algorithmic and cognitive attack on model instruction parsing, not physical workstation hardware damage.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because protocol governance committees do not inject adversarial bypass commands into community repositories."
    }
  },
  {
    "id": 32,
    "subtopic": "Community Skill Threat Vectors: Data Exfiltration",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Part 5: Use this safely (Lines 574-577)",
    "scenario": "A human resources coordinator installs an unverified third-party resume screening skill. Hidden inside an optional Python script within the `scripts/` folder is a command that transmits applicant contact details and salary histories to an external HTTP webhook. What specific security violation has taken place?",
    "options": {
      "A": "Sycophantic alignment drift, where the assistant flatters the operator instead of screening.",
      "B": "Progressive disclosure failure, where frontmatter exceeds the platform working memory limits.",
      "C": "Cross-site script injection, which corrupts the local browser client session cache storage.",
      "D": "Data exfiltration, wherein corporate records are secretly transmitted to external endpoints."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Part 5. The chapter explicitly defines this threat: 'data exfiltration, which means the skill sending your information out in secret. That is why \"I downloaded a free skill from social media\" is a sentence that should make you pause.' Bundled executable scripts that reach external networks pose severe exfiltration risks.",
      "distractor_A": "Option A is incorrect because sycophancy refers to uncritical conversational agreement, not criminal data theft.",
      "distractor_B": "Option B is incorrect because progressive disclosure relates to context staging, not illicit unauthorized network transmissions.",
      "distractor_C": "Option C is incorrect because transmitting data via an outbound backend script is exfiltration, not a browser client DOM script execution flaw.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 33,
    "subtopic": "The Scope Dial Asymmetry: Skills vs. Connectors",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Part 5: The safe-use checklist (Lines 588-590)",
    "scenario": "A compliance auditor reviews access controls for an enterprise AI workspace. A junior developer asserts: 'We do not need to read or audit community skills before installing them, because we can simply set the skill's permission scope dial to read-only.' Why is the developer's assertion fatally flawed?",
    "options": {
      "A": "Skills possess no scope dial; they operate with the full reach of whatever permissions the chat has.",
      "B": "Community skills automatically override enterprise single-sign-on administrative policies.",
      "C": "Read-only mode can only be enforced on mobile smartphone applications, not desktop browsers.",
      "D": "The Model Context Protocol automatically grants write access to all installed skill folders."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Part 5. The safe-use checklist emphasizes this critical asymmetry: 'Scope is a connector idea, not a Skill idea. A connector has scopes you grant and can narrow. A Skill has no such dial. It runs with whatever access its chat already has, so its reach is everything that chat can reach, not only what its task needs. That is why reading a skill first is the control for Skills.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because skills cannot override SSO protocols; their danger lies in utilizing the chat's existing authorized access.",
      "distractor_C": "Option C is incorrect because permission scopes are architectural platform parameters, not mobile-specific features.",
      "distractor_D": "Option D is incorrect because MCP connectors support granular read-only authorization and do not unconditionally grant write access."
    }
  },
  {
    "id": 34,
    "subtopic": "Plain-Language Security Auditing Protocol",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Part 5 & Project 5: Audit a skill before you trust it (Lines 584-586, 742-752)",
    "scenario": "A legal assistant intends to install an open-source contract analysis skill created by a third-party developer. Before enabling it across her corporate workspace, what rapid verification protocol should the assistant execute to confirm the skill's safety?",
    "options": {
      "A": "Rename the skill's frontmatter description tag to include an unverified cryptographic digital key.",
      "B": "Submit the skill files to an external dark-web auditing forum for crowd-sourced vulnerability analysis.",
      "C": "Recompile the entire operating system kernel before and after launching each conversational session.",
      "D": "Instruct Claude to inspect the skill files and flag external server contacts or credential handling."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Part 5 and Project 5. The text prescribes this turnkey auditing method: 'Read a skill before enabling it. Open the SKILL.md and any bundled files, or ask AI: \"Read this skill and tell me exactly what it instructs you to do. Flag anything that contacts external servers, handles credentials, or could leak my data.\"' This leverages model reasoning to deconstruct hidden instructions in seconds.",
      "distractor_A": "Option A is incorrect because embedding arbitrary strings in YAML tags does not validate the underlying instruction safety.",
      "distractor_B": "Option B is incorrect because uploading internal or candidate assets to unverified public forums introduces catastrophic data leakage risks.",
      "distractor_C": "Option C is incorrect because OS kernel recompilation is absurdly disproportionate and irrelevant to inspecting plain-text markdown skills.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 35,
    "subtopic": "Connector API Action Constraints vs In-Place Editing",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Concept 7 & Part 5 (Lines 306-307, 578-582)",
    "scenario": "An office manager connects Google Drive to an assistant and requests: 'Update row 14 in our master client phone directory on Google Drive to change the contact number.' The assistant creates a brand-new file instead of editing the existing sheet. Why did the assistant create a new file instead of modifying the existing spreadsheet?",
    "options": {
      "A": "The manager's workstation browser failed to complete the secondary hardware encryption handshake.",
      "B": "The connector's API tool actions only support saving new files, not editing documents in place.",
      "C": "Google Drive automatically locks all files against modification when accessed from AI clients.",
      "D": "The model's neural network weights suffered token context exhaustion during row identification."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Sections 7 and Part 5. The text explicitly clarifies: 'The Drive connector reads your documents but cannot edit them in place, so the \"write\" step means saving a new file... Access is only half of a connector's reach. The other half is the list of actions it was built to perform... A limit like that is not a bug and not a permissions problem. It is the shape of the tool.'",
      "distractor_A": "Option A is incorrect because connector capability boundaries are dictated by implemented MCP tool definitions, not browser hardware encryption.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because Drive APIs fully support file updates if the software client implements update endpoints; the limitation is the connector's tool design.",
      "distractor_D": "Option D is incorrect because context exhaustion produces truncation or hallucination, not clean file creation behavior."
    }
  },
  {
    "id": 36,
    "subtopic": "Enterprise Skill Distribution and Governance",
    "domain": "Domain 6: Governance, Risk, and Responsible Use",
    "grounding": "Concept 14: Saving and sharing your skill (Lines 489-490, 591)",
    "scenario": "An enterprise risk committee at an international consultancy establishes guidelines for deploying skills across 5,000 consultants. What distribution architecture ensures version control, security oversight, and organizational compliance across enterprise teams?",
    "options": {
      "A": "Require individual consultants to manually copy and paste raw instruction text from email chains.",
      "B": "Permit consultants to distribute skill zip packages freely via informal team chat channels.",
      "C": "Publish vetted skills to the central organization directory, where updates propagate automatically.",
      "D": "Prohibit custom skills entirely, forcing all staff to rely solely on public social media prompts."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Section 14 and the Safe-Use Checklist. The text mandates: 'On Team or Enterprise plans you can share a skill with named colleagues, or publish it to your organization's directory... Shared skills are view-only and update themselves when you change the original, which standardizes how a whole firm produces its documents... route shared skills through your organization's directory, where an owner has reviewed them, not by passing zip files around.'",
      "distractor_A": "Option A is incorrect because manual copy-pasting from email chains reintroduces human error, version fragmentation, and operational friction.",
      "distractor_B": "Option B is incorrect because passing unvetted zip archives across informal channels bypasses administrative security audits and destroys version synchronization.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because enterprise plans are designed to leverage curated, proprietary organizational skills rather than banning them."
    }
  },
  {
    "id": 37,
    "subtopic": "Cross-Platform Portability & The Agent Skills Standard",
    "domain": "Domain 3: Product and Model Selection",
    "grounding": "Part 4: The same skill, five places (Lines 493-500, 547-553)",
    "scenario": "A software team lead creates a 'git-commit-audit' skill within an agent CLI tool. A colleague asks whether this skill can be used across competing vendor CLI tools without rewriting the underlying prompt logic. How does cross-vendor portability operate across modern AI agent command-line tools?",
    "options": {
      "A": "It requires manual re-encoding into binary C++ libraries before execution on Google or OpenAI tools.",
      "B": "It cannot run outside Claude Code because instruction markdown files are proprietary to Anthropic.",
      "C": "It runs across diverse vendor CLI tools because all adhere to the open Agent Skills standard.",
      "D": "It can run only if both developers purchase identical enterprise hardware mainframe servers."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Part 4. The text explains: 'In December 2025 Anthropic published the Agent Skills open standard at agentskills.io... Because Agent Skills is an open standard, the command-line tools from OpenAI and Google, Codex CLI and Gemini CLI, read the same SKILL.md files. So do VS Code and Cursor. A skill is the one piece of this course that is not locked to Claude.'",
      "distractor_A": "Option A is incorrect because Agent Skills files are plain-text markdown assets; they require no binary compilation or C++ wrapping.",
      "distractor_B": "Option B is incorrect because Agent Skills is an open specification designed specifically to eliminate proprietary vendor lock-in.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because portability is governed by software file standard compliance, completely independent of underlying hardware server brands."
    }
  },
  {
    "id": 38,
    "subtopic": "Proprietary Walled Gardens: Custom GPTs vs. Gems vs. Skills",
    "domain": "Domain 3: Product and Model Selection",
    "grounding": "Part 4: What about ChatGPT and Gemini? (Lines 547-560)",
    "scenario": "An enterprise AI strategist prepares an executive briefing evaluating multi-model resilience. She contrasts custom assistants built within consumer chat ecosystems against skills built under the Agent Skills standard. What critical strategic limitation distinguishes ChatGPT's Custom GPTs and Google's Gems?",
    "options": {
      "A": "Custom GPTs and Gems do not support the storage of uploaded knowledge files or reference tables.",
      "B": "Custom GPTs and Gems are siloed within proprietary ecosystems and cannot travel between platforms.",
      "C": "Custom GPTs and Gems are restricted exclusively to academic institutions and university students.",
      "D": "Custom GPTs and Gems require users to manually type binary machine assembly code into the chat."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Part 4. The chapter details: 'On \"teach it once\" inside the consumer chat apps, each vendor has its own version, and none of them travel. Custom GPTs live only inside ChatGPT. Gems live only inside Google's apps. The difference that matters is portability... If your strategy spans more than one model, which this book argues it should, Skills are the future-proof choice.'",
      "distractor_A": "Option A is incorrect because both Custom GPTs and Gems support knowledge file attachments; their fatal limitation is lack of cross-platform portability.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because both proprietary products are widely available to commercial, enterprise, and individual consumers.",
      "distractor_D": "Option D is incorrect because both tools provide no-code, conversational configuration interfaces."
    }
  },
  {
    "id": 39,
    "subtopic": "The Market-of-One Validation Test",
    "domain": "Domain 2: Output Evaluation and Validation",
    "grounding": "Section: Projects & Market-of-One test (Lines 46, 659-663)",
    "scenario": "A freelance copywriter considers building twelve custom skills for various everyday tasks. Her mentor advises her to apply the 'market-of-one test' before investing time in building each asset. What criterion determines whether a task truly justifies building a dedicated skill?",
    "options": {
      "A": "A skill is justified whenever a task involves searching public internet search engines for news.",
      "B": "A skill is justified only if you plan to monetize and sell the asset on a public commercial marketplace.",
      "C": "A skill is justified when the underlying instruction file contains at least five thousand words of code.",
      "D": "A skill is justified when it captures your specific repeated method that no commercial app provides."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per the Glossary and Projects section. The text defines the market-of-one test: 'a skill earns its place when it captures your specific repeated way, the thing no app does for you. Nobody sells an app that writes your class notes in your format. A task an app already does for everybody is just a good prompt.'",
      "distractor_A": "Option A is incorrect because basic public search queries are standard one-off prompts that do not warrant a permanent procedural skill asset.",
      "distractor_B": "Option B is incorrect because the market-of-one test is explicitly about codifying private, internal idiosyncratic workflows rather than commercial marketplace distribution.",
      "distractor_C": "Option C is incorrect because skills can be as brief as a single paragraph of plain-English formatting rules; word count has no bearing on justification.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 40,
    "subtopic": "Headless Execution and Surface Graduation",
    "domain": "Domain 4: Workflow Integration and Solution Design",
    "grounding": "Part 4: The same skill, five places & Project 4 (Lines 521-545, 726-740)",
    "scenario": "A data analysis team initially authors and validates a 'sales-outlier-detection' skill within the web interface of Claude.ai. As batch reporting volumes grow, they migrate the workflow to run directly on local CSV files inside Cowork and Claude Code. What operational advantage does this surface graduation deliver?",
    "options": {
      "A": "The exact same SKILL.md runs against local computer files without copy-pasting or file re-uploading.",
      "B": "Local execution automatically eliminates all mathematical hallucination across every model query.",
      "C": "Terminal tools allow the team to permanently bypass corporate data compliance and security logging.",
      "D": "Desktop applications completely dispense with the need for human review of generated reports."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Part 4 and Project 4. The guide explains: 'The recipe you wrote hangs in many kitchens... In Cowork and Claude Code, enabled skills appear on their own or can be saved straight to a folder... plus files already on your computer.' The same `SKILL.md` executes seamlessly against local file paths, eliminating the need to upload files manually to the web browser.",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because surface graduation changes file access plumbing; it does not alter the fundamental probabilistic nature of LLM token generation.",
      "distractor_C": "Option C is incorrect because enterprise command-line tools maintain strict audit logging and compliance requirements.",
      "distractor_D": "Option D is incorrect because supervisory human verification remains mandatory regardless of whether execution occurs in a browser or terminal."
    }
  }
]

def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(out_dir, "questions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(QUESTIONS, f, indent=2, ensure_ascii=False)
    print(f"[+] Successfully wrote {len(QUESTIONS)} questions to {json_path}")

if __name__ == "__main__":
    main()
