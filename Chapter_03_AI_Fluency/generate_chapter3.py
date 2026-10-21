import json
import os
import sys
import re

QUESTIONS = [
    # ----------------------------------------------------
    # Sub-Topic 1: Core AI Fluency & The 4 Qualities vs Mere Access (Q1 - Q3)
    # ----------------------------------------------------
    {
        "id": 1,
        "subtopic": "Core AI Fluency: Effective, Efficient, Ethical, Safe",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Part 1, Section 1: AI access is not AI fluency",
        "scenario": "Two financial analysts at a commercial bank subscribe to the identical advanced generative model. Analyst A generates a client risk assessment in ten minutes that is immediately approved by compliance. Analyst B spends four hours generating dozens of verbose revisions, ultimately discarding the output due to unverified regulatory claims. What core principle distinguishes their outcomes?",
        "options": {
            "A": "Working with AI reflects human decision quality across efficiency, safety, and goal attainment rather than system access.",
            "B": "Enterprise model tiers automatically calibrate statistical confidence to match the user's institutional rank.",
            "C": "Analyst A utilized proprietary prompt tokens that bypassed the foundation model's public safety guardrails.",
            "D": "Commercial reasoning engines dynamically allocate higher compute bandwidth to accounts with lower error logs."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "AI access is not AI fluency. Two individuals using the exact same model achieve vastly different results because fluency is defined by human competency: working effectively (achieving the goal), efficiently (conserving time and tokens), ethically (transparent and fair), and safely (protecting privacy and institutional data).",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Models do not adjust statistical accuracy or confidence based on user organizational status.",
            "distractor_C": "Fluency depends on clear problem definition and verification, not secret tokens or bypassing safety guardrails.",
            "distractor_D": "Compute allocation is uniform across subscription tiers and does not adjust based on user error logs."
        }
    },
    {
        "id": 2,
        "subtopic": "Stateless Nature & Working Memory vs Human Learning",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Opening: Imagine a talented new colleague joins your team",
        "scenario": "A clinical research administrator instructs an assistant on Monday regarding institutional formatting rules for pediatric oncology trial reports. When opening a fresh chat on Thursday to draft a new protocol, the assistant reverts to generic adult oncology formatting. What architectural attribute explains this behavioral reset?",
        "options": {
            "A": "The enterprise platform cleared user working memory caches following an automated server security overhaul.",
            "B": "The model is stateless across independent chats, requiring contextual constraints to be re-supplied each time.",
            "C": "The assistant detected conflicting medical formatting standards across published clinical research guidelines.",
            "D": "The model token consumption optimizer automatically purged low-frequency pediatric terminology branches."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Unlike human colleagues who retain memory across weeks, foundation models carry nothing from one chat session into the next. Each new conversation starts completely stateless with read-only frozen weights, requiring instructions and formatting rules to be re-supplied or stored in persistent Project knowledge.",
            "distractor_A": "Session resets are an inherent architectural property of stateless models, not an administrative server purge.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "The reversion is caused by lack of conversational continuity, not conflict resolution among clinical guidelines.",
            "distractor_D": "Tokenizers are static lookup tables and do not selectively purge specialized vocabulary branches."
        }
    },
    {
        "id": 3,
        "subtopic": "Economic Efficiency & Token Conservation",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Part 1, Section 1: Effective, Efficient, Ethical, Safe",
        "scenario": "A legal consultancy audits an enterprise lease summarization workflow. Staff members routinely paste entire 300-page lease agreements into a general chat window with generic prompts like 'summarize key risks', forcing the model to repeatedly re-read full texts across dozens of iterative questions. Why is this workflow flagged as inefficient?",
        "options": {
            "A": "It triggers automatic model hallucination subroutines whenever ingested token volume exceeds ten thousand tokens.",
            "B": "It violates statutory commercial standards requiring all contracts to be summarized exclusively by human lawyers.",
            "C": "It consumes excessive tokens and compute budget without structured target scoping or information boundaries.",
            "D": "It permanently degrades foundation model weights by filling shared global context buffers with private data."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Efficiency requires minimizing wasted time, human effort, and tokens. Ingesting 300-page raw agreements repeatedly for unfocused queries consumes millions of unnecessary input tokens, inflates enterprise billing, and degrades output precision through context overcrowding.",
            "distractor_A": "Context windows do not possess automatic hallucination subroutines triggered by token volume.",
            "distractor_B": "The operational failure flagged is technical inefficiency and resource waste, not statutory legal prohibition.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Inference prompts do not modify or degrade frozen foundation model weights."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 2: Work Modalities: Automation, Augmentation, Agency (Q4 - Q7)
    # ----------------------------------------------------
    {
        "id": 4,
        "subtopic": "Three Modalities: Automation (Script Writer)",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 1, Section 2: Automation: 'Do this task'",
        "scenario": "A municipal logistics coordinator writes a prompt instructing an assistant: 'Extract the delivery date, container serial number, and customs duty amount from this manifest PDF, then format the output into a 3-column CSV table.' What operational work modality and human role does this task illustrate?",
        "options": {
            "A": "Context engineering, where the platform autonomously synthesizes domain knowledge from external sources.",
            "B": "Augmentation, where the human and model engage in collaborative exploratory thinking to reach decisions.",
            "C": "Agency, where the model operates autonomously on behalf of third-party clients across future workflows.",
            "D": "Automation, where the user functions as a script writer defining a rigid, repeatable task for the model."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Automation fits clear, repeatable tasks where the model executes a predefined procedure with zero autonomous decision-making. The human acts like a script writer dictating inputs, extractions, and output formats.",
            "distractor_A": "Context engineering relates to system knowledge infrastructure, not user execution modalities.",
            "distractor_B": "Augmentation involves two-way exploratory ideation and discussion, not deterministic data extraction.",
            "distractor_C": "Agency involves setting broad goals for autonomous execution while the user is absent.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 5,
        "subtopic": "Three Modalities: Augmentation (Thinking Partner)",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 1, Section 2: Augmentation: 'Help me think'",
        "scenario": "A university department head works with an AI model for two hours to restructure an undergraduate degree program. The department head proposes curriculum sequences, the AI identifies prerequisite bottlenecks, the head challenges its assumptions regarding laboratory hours, and the AI refines its proposal. What operational modality is occurring?",
        "options": {
            "A": "Augmentation, where the human and artificial intelligence interact iteratively as co-creative thinking partners.",
            "B": "Automation, where the user executes fixed multi-step procedural scripts to extract structured academic data.",
            "C": "Agency, where the system executes autonomous administrative enrollments without direct human supervision.",
            "D": "Delegation, where all curriculum design decisions are fully offloaded to an external artificial intelligence."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Augmentation is a multi-turn, collaborative thinking partnership. The model is not merely executing fixed instructions; it acts as a sounding board, challenging assumptions and co-creating solutions while the human remains firmly in control of decisions.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "The process is dynamic and exploratory, not a fixed extraction script.",
            "distractor_C": "The model is not acting autonomously in the future for others; the human is present throughout.",
            "distractor_D": "Curriculum strategy requires institutional judgment and cannot be completely offloaded."
        }
    },
    {
        "id": 6,
        "subtopic": "Three Modalities: Agency (Director, Future & For Others)",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 1, Section 2: Agency: 'Pursue this goal for me'",
        "scenario": "A customer success director configures an assistant: 'Monitor the incoming client support queue overnight. Resolve tier-1 billing inquiries within policy boundaries, flag cancellation threats for morning review, and request my approval before issuing refunds over $100.' What key characteristics define this operational mode?",
        "options": {
            "A": "The model executes continuous real-time model retraining based on sentiment analysis of inbound tickets.",
            "B": "The assistant operates independently in the future and for others within established goal boundaries.",
            "C": "The user maintains synchronous, turn-by-turn verification over every operational decision in the queue.",
            "D": "The system replaces human organizational accountability by assuming legal liability for refund checks."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Agency is defined by two operational realities: 'Future' (the system acts when the operator is not in the room) and 'For others' (the system interacts directly with third parties). The human steps back from turn-by-turn execution and acts as a director establishing boundaries and approval triggers.",
            "distractor_A": "Agents run via runtime tools and prompts, not continuous base model retraining.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Agency specifically eliminates synchronous turn-by-turn human supervision for routine actions.",
            "distractor_D": "Software systems cannot assume legal liability; human operators and firms retain accountability."
        }
    },
    {
        "id": 7,
        "subtopic": "Modality Failure Modes: Script Writer vs Director",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 1, Section 2: Automation and agency comparison table",
        "scenario": "An e-commerce operations manager transitions a product catalog enrichment task from an automated script (which formatted raw supplier specs) to an autonomous agent (empowered to re-categorize merchandise). The new deployment experiences widespread failures. What is the most likely root cause of this operational breakdown?",
        "options": {
            "A": "The model underlying neural network experienced catastrophic forgetting of previously acquired vocabulary rules.",
            "B": "The platform context window overflowed due to processing complex structured JSON product schemas simultaneously.",
            "C": "The system misunderstood broad organizational goals and boundaries rather than making a single tactical error.",
            "D": "The manager failed to provide low-level procedural pseudo-code for every individual catalog categorization event."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "In automation, failures typically occur because 'a procedural step was executed badly.' In agency, because the human specifies objectives and constraints rather than micro-steps, the dominant failure mode is that 'the goal or boundary was misunderstood or ambiguous.'",
            "distractor_A": "Frozen models do not experience catastrophic forgetting during standard inference execution.",
            "distractor_B": "Context windows easily handle JSON product records; the issue is semantic boundary ambiguity.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Supplying pseudo-code for every categorization step reverts the system back to rigid automation."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 3: Delegation: Problem Awareness & Business Boundaries (Q8 - Q11)
    # ----------------------------------------------------
    {
        "id": 8,
        "subtopic": "Delegation: Problem Awareness & Business Questions",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3.1: Problem awareness: know what you are trying to accomplish",
        "scenario": "A medical clinic administrator wants to deploy an AI agent to handle patient appointment cancellations and rescheduling via text messages. Before drafting any system prompt or selecting software, what primary action must the administrator execute?",
        "options": {
            "A": "Drafting advanced few-shot prompting templates containing simulated patient dialogue examples and medical jargon.",
            "B": "Benchmarking inference token latency across competing proprietary and open-source foundation model providers.",
            "C": "Configuring vector database indexing pipelines to ingest all past historical clinic patient consultation records.",
            "D": "Establishing clinical escalation rules, late cancellation fees, emergency handling protocols, and approval limits."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Problem awareness requires clarifying fundamental business, operational, and ethical rules before touching the AI. In clinic scheduling, questions regarding emergency triage, fee thresholds, and escalation pathways are human policy decisions, not prompt engineering choices.",
            "distractor_A": "Prompt templates belong to Description; writing them before establishing policy is a critical beginner error.",
            "distractor_B": "Benchmarking model latency addresses infrastructure selection, not operational problem definition.",
            "distractor_C": "Ingesting confidential clinical consultation transcripts violates patient privacy regulations.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 9,
        "subtopic": "Delegation: Boundaries of Authority (Read vs Send)",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3.1: Hard business questions",
        "scenario": "An accounts receivable team designs an AI agent to follow up on overdue client invoices. During planning, the finance director insists that the agent be permitted to read billing ledgers and draft reminder emails, but strictly prohibited from sending emails or modifying account balances without human sign-off. Why is this distinction critical?",
        "options": {
            "A": "It establishes precise operational boundaries between autonomous computation and mandatory human-in-the-loop approval.",
            "B": "It prevents the foundation model from exceeding its internal token bandwidth quota during external email transmission.",
            "C": "It bypasses corporate compliance auditing requirements by classifying the automated agent as a passive data cache.",
            "D": "It eliminates the need to provide the agent with accounting terminology definitions or invoice overdue thresholds."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Delegation requires defining the exact boundary between automated analysis and human execution. Permitting an assistant to read records and draft correspondence while withholding transmission and balance modification powers ensures high-risk financial actions require human approval.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Network email dispatch does not consume model context window tokens.",
            "distractor_C": "Restricting execution authority is an active risk control, not an audit evasion tactic.",
            "distractor_D": "Drafting accurate reminders still requires clear definitions of billing rules and overdue timelines."
        }
    },
    {
        "id": 10,
        "subtopic": "Delegation as Workflow Design vs Offloading",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3: Delegation: decide who should do what",
        "scenario": "A software engineering director reviews a proposal to 'delegate all pull request code reviews to an autonomous AI bot.' The director rejects the proposal, noting that delegation requires workflow design rather than task offloading. What did the proposal fail to structure?",
        "options": {
            "A": "Selecting a cloud model provider with sufficient server cluster capacity to compile and execute binary software builds.",
            "B": "Structuring which review aspects require human architectural judgment versus automated mechanical syntax checks.",
            "C": "Embedding comprehensive dictionary definitions of all programming language keywords directly inside the prompt context.",
            "D": "Configuring the bot to automatically approve and merge all pull requests authored by senior development personnel."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Delegation is not dumping work onto a machine. It is the intentional division of labor: identifying which sub-tasks are routine and verifiable (e.g., syntax linting, style formatting) versus which require strategic human judgment (e.g., architectural coherence, security threat modeling).",
            "distractor_A": "Server capacity is a hosting concern that does not address workflow allocation.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Models natively parse programming keywords; embedding dictionaries is redundant.",
            "distractor_D": "Bypassing review for senior staff creates catastrophic vulnerabilities and violates governance."
        }
    },
    {
        "id": 11,
        "subtopic": "Delegation: Non-Promptable Business Decisions",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3.1: These are business questions, not prompting questions",
        "scenario": "A retail bank develops a loan screening assistant. The project team attempts to prompt the AI to 'independently decide what debt-to-income threshold constitutes an acceptable default risk for small business applicants.' Why is this an operational failure of delegation?",
        "options": {
            "A": "Neural networks cannot perform arithmetic comparisons between applicant debt figures and monthly revenue numbers.",
            "B": "Foundation models automatically default to predatory lending practices when calculating small enterprise interest rates.",
            "C": "Risk tolerance and credit lending thresholds are strategic business policies that humans must explicitly govern.",
            "D": "Inference APIs prohibit commercial financial institutions from querying models about debt or credit balance data."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Credit risk tolerance is a foundational business and fiduciary policy. Asking an AI to invent its own credit threshold abdicates human responsibility. The human institution must determine the threshold; the AI merely applies it to applicant data.",
            "distractor_A": "Language models can easily compare numerical ratios against defined thresholds.",
            "distractor_B": "Models do not have predatory biases, but ungrounded prompts produce erratic risk decisions.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Commercial APIs fully support financial risk workflows under appropriate enterprise agreements."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 4: Delegation: Platform Awareness & Task Division (Q12 - Q15)
    # ----------------------------------------------------
    {
        "id": 12,
        "subtopic": "Platform Awareness: Matching AI Architecture to Task",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3.2: Platform awareness: choose the right kind of AI",
        "scenario": "A forensic accountant needs to verify whether a multinational conglomerate's regulatory filings in 2026 comply with a newly enacted European trade statute that took effect three weeks ago. Which AI platform capability is essential to delegate this task effectively?",
        "options": {
            "A": "A frozen base foundation model possessing massive parameter scale but strict historical training data cutoffs.",
            "B": "An autonomous coding agent specialized exclusively in refactoring legacy relational database stored procedures.",
            "C": "A lightweight embedded model optimized for low-latency offline mobile speech-to-text audio transcriptions.",
            "D": "A search-enabled assistant capable of retrieving and grounding analysis in current external web publications."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Because the statute took effect three weeks ago, static models with historical knowledge cutoffs will hallucinate or fail. Platform awareness dictates choosing an assistant with live web search capabilities to ground analysis in current statutory publications.",
            "distractor_A": "Static frozen models lack knowledge of recent events and will fail this audit.",
            "distractor_B": "Database refactoring agents cannot analyze external trade statutes.",
            "distractor_C": "Offline speech transcription models lack web search and legal analysis capabilities.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 13,
        "subtopic": "Platform Awareness: Multi-Step Reasoning Models",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3.2: Choosing models and tools",
        "scenario": "A civil engineering consultancy needs to evaluate the structural load distribution of a suspension bridge under complex variable wind shear and thermal expansion scenarios involving hundreds of interdependent equations. What system architecture does platform awareness dictate?",
        "options": {
            "A": "A dedicated reasoning model that executes extended multi-step internal verification chains before outputting results.",
            "B": "A high-speed conversational chat assistant optimized for rapid creative brainstorming and informal dialogue.",
            "C": "An unguided autonomous web-scraping agent programmed to aggregate unverified public civil engineering forums.",
            "D": "A consumer text auto-complete extension integrated directly into a standard desktop word processing software."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Complex multi-step physics derivations with interdependent constraints require extended test-time compute. A reasoning model uses internal scratchpads to work through mathematical steps systematically, reducing calculation errors compared to fast conversational models.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Fast conversational models prioritize speed over rigorous multi-step deduction.",
            "distractor_C": "Scraping unverified public forums does not solve deterministic structural load equations.",
            "distractor_D": "Word processor auto-complete tools lack the architectural compute for structural simulation."
        }
    },
    {
        "id": 14,
        "subtopic": "Task Delegation Matrix: Human vs AI Ownership",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3.3: Task delegation: divide the work deliberately",
        "scenario": "A medical publishing house outlines the workflow for developing a new clinical immunology curriculum. Which distribution of responsibilities correctly aligns human authority with AI capabilities?",
        "options": {
            "A": "AI establishes core pedagogical goals and ethical boundaries; humans handle mechanical spelling and grammar cleanup.",
            "B": "Humans determine learning goals and clinical accuracy; AI assists in proposing structures and drafting review sections.",
            "C": "AI independently verifies medical trial factual veracity; humans generate initial rapid drafts without clinical review.",
            "D": "Humans delegate full publication copyright and final sign-off authority to an autonomous educational agent architecture."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "High-fluency delegation assigns intent, pedagogical scope, and clinical verification to human experts, while leveraging AI for structural ideation and rapid initial drafting from approved source materials.",
            "distractor_A": "Relegating humans to copyeditors while letting AI set ethical and clinical goals inverts responsible delegation.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "AI cannot verify factual truth independently; humans must verify clinical claims.",
            "distractor_D": "Copyright ownership and professional accountability cannot be transferred to software agents."
        }
    },
    {
        "id": 15,
        "subtopic": "Task Delegation: Lived Experience & Local Nuance",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 2, Section 3.3: Task delegation table: lived experience",
        "scenario": "A public health agency creates a community health brochure regarding seasonal waterborne illnesses for rural clinics. The communications team uses an advanced model to draft the informational medical copy. When localizing the brochure, why must human staff retain ownership over the contextual case examples?",
        "options": {
            "A": "Commercial language models automatically encrypt output text when regional dialects are detected in system prompts.",
            "B": "Foundation models are strictly prohibited by international treaty from referencing regional geographical locations.",
            "C": "The foundation model lacks lived human experience, local cultural context, and regional community trust dynamics.",
            "D": "Inference token algorithms experience computational arithmetic errors when translating medical concepts into Urdu."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "AI possesses extensive general data but zero lived human experience. Cultural nuances, community relationships, and local health practices require human insight to ensure health messaging is trusted and understood.",
            "distractor_A": "Models do not encrypt text when regional dialects are used.",
            "distractor_B": "No international treaties restrict geographic references in language models.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Translation into regional languages uses standard token mapping without arithmetic errors."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 5: Description: Product Description (Q16 - Q19)
    # ----------------------------------------------------
    {
        "id": 16,
        "subtopic": "Product Description: Completeness Over Cleverness",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 2, Section 4.1: Product description: define the result",
        "scenario": "A venture capital associate needs an executive briefing on a 150-page renewable energy startup filing. Instead of typing 'Summarize this report like an expert,' she specifies: 'Summarize for our investment committee in 3 bulleted pages; cover capital expenditure, patented tech, and regulatory risks; exclude generic marketing jargon.' What prompt design principle is demonstrated?",
        "options": {
            "A": "Embedding explicit word count ceilings triggers internal chain-of-thought mathematical reasoning subroutines.",
            "B": "Negative constraints such as excluding marketing copy guarantee that the foundation model will never hallucinate.",
            "C": "Specifying executive committee personas automatically forces the model to verify startup balance sheet figures.",
            "D": "Product completeness regarding format, audience, and boundaries matters far more than clever prompt phrasing."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "High-quality prompting does not rely on clever phrasing or flattering personas. It depends on completeness: clearly defining target audience, output structure, mandatory focus areas, and explicit exclusions.",
            "distractor_A": "Length limits constrain token generation; they do not trigger mathematical reasoning engines.",
            "distractor_B": "Negative constraints remove clichés, but cannot guarantee zero factual hallucination.",
            "distractor_C": "Persona prompts do not independently audit external financial balance sheets.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 17,
        "subtopic": "Product Description: Audience and Length Constraints",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 2, Section 4.1: What do I want back?",
        "scenario": "A hospital safety officer prompts an assistant to summarize a 40-page hazardous chemical spill protocol. The prompt omits the target audience, reading time constraint, and operational use-case. The assistant returns a 15-page academic essay detailing chemical molecular bonds. Why did the model produce this suboptimal output?",
        "options": {
            "A": "Because AI works only from available context, leaving unstated parameters forces the model to guess intent.",
            "B": "The model underlying neural weights prioritize organic chemistry theory over practical clinical procedures.",
            "C": "The safety officer failed to use specialized system engineering markup tags required for medical prompting.",
            "D": "The hospital network firewall automatically stripped operational directive headers from the prompt payload."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "An assistant can only predict completions based on provided context. When key parameters—such as audience (nurses vs chemists), format (action checklist vs treatise), and length—are omitted, the model guesses statistically, often defaulting to academic prose.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Models do not have an inherent preference for theory over practice; the failure stems from missing prompt constraints.",
            "distractor_C": "Standard plain English defines parameters effectively without proprietary tags.",
            "distractor_D": "Network firewalls do not selectively strip semantic sentences from API payloads."
        }
    },
    {
        "id": 18,
        "subtopic": "Product Description: Context & Empathy Factors",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 1: See it in three minutes",
        "scenario": "A community sports coordinator drafts two separate prompts requesting a welcome email for new participants. Prompt 1 asks for a general welcome message. Prompt 2 specifies nervous beginners riding in heavy morning traffic, a warm reassuring tone, zero exclamation marks, under 150 words, and a note about the weekend assembly point. Why does Prompt 2 produce significantly superior copy?",
        "options": {
            "A": "Prompt 2 accessed an authenticated proprietary database of athletic club communication templates.",
            "B": "Prompt 2 provided detailed situational context, audience empathy factors, and explicit negative constraints.",
            "C": "The model applied advanced reinforcement learning updates during inference to personalize its core weights.",
            "D": "Prompt 2 utilized emotional sentiment tokens that bypass the model standard conversational token limits."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Prompt 2 succeeds because it provides the operational context that Prompt 1 omitted: who the audience is, what anxieties they have, the desired tone, strict length bounds, and concrete logistical details.",
            "distractor_A": "Both prompts ran on the identical public model without external proprietary databases.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Model weights remain completely frozen during inference; no runtime reinforcement learning occurs.",
            "distractor_D": "Emotional words do not alter context window token limits or model quotas."
        }
    },
    {
        "id": 19,
        "subtopic": "Product Description: Explicit Exclusions & Negative Constraints",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 2, Section 4.1: Anything to leave out",
        "scenario": "A corporate communications director instructs an assistant to draft a press release regarding an internal restructuring. The prompt explicitly includes: 'Do not use corporate buzzwords such as synergy, right-sizing, or paradigm shift; do not mention unannounced product roadmaps.' Why are explicit exclusions a key component of product description?",
        "options": {
            "A": "They purge the foundation model pre-trained vocabulary vectors of corporate jargon across the entire session.",
            "B": "They force the inference engine to utilize lower-temperature sampling algorithms for the remainder of the query.",
            "C": "They establish definitive negative boundaries that prevent the model from drifting into clichéd content.",
            "D": "They eliminate the requirement for human legal review by guaranteeing compliance with international press codes."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Explicit exclusions (negative constraints) eliminate common, unwanted statistical defaults. Directing an assistant what NOT to include prevents the generation of hollow corporate jargon and safeguards confidential topics.",
            "distractor_A": "Negative constraints guide generation focus, but do not delete token vectors from model weights.",
            "distractor_B": "Negative wording does not reconfigure the mathematical temperature parameter of the API.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Prompt constraints never replace mandatory human legal review before public disclosure."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 6: Description: Process Description & Multi-Stage Staging (Q20 - Q23)
    # ----------------------------------------------------
    {
        "id": 20,
        "subtopic": "Process Description: Staged Multi-Step Order of Operations",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 2, Section 4.2: Process description: define the approach",
        "scenario": "A procurement manager must evaluate three competing IT vendor proposals across cost, SLA guarantees, and data sovereignty. Instead of submitting all three proposals and requesting an immediate recommendation, the manager instructs the assistant to extract facts into a structured table, verify the cells, and stop before scoring. Why is this staged process critical?",
        "options": {
            "A": "Splitting the task bypasses commercial cloud inference rate limits applied to multi-document comparisons.",
            "B": "Extracting facts into a table forces the model to store vendor bids in persistent browser memory buffers.",
            "C": "Staged processing eliminates the operational requirement for human verification of vendor price quotes.",
            "D": "Separating extraction from evaluation prevents the model from generating premature recommendations."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Process description defines the approach. When complex evaluations are attempted in a single unconstrained prompt, models blend extraction with subjective judgment, often inventing facts to justify a conclusion. Staging extraction first isolates factual data for inspection before scoring.",
            "distractor_A": "Multi-stage prompting is designed for factual accuracy, not bypassing API rate limits.",
            "distractor_B": "Extraction tables exist only in conversation context, not persistent browser memory.",
            "distractor_C": "Staging makes verification easier; it never eliminates the need for human review.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 21,
        "subtopic": "Process Description: Intermediate Verification Checkpoints",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 2, Section 4.2: Staged approach and stopping points",
        "scenario": "A financial auditor uses an assistant to analyze a 200-page corporate financial statement. The auditor structures the prompt: 'First, extract all related-party transactions into a table. Stop and wait for my confirmation before calculating net exposure or drafting findings.' What operational risk is mitigated by this stopping point?",
        "options": {
            "A": "Compounding errors, where unverified extraction mistakes distort all downstream calculations and summaries.",
            "B": "Model parameter corruption, where unverified financial figures alter the underlying weights during inference.",
            "C": "Token rate limit throttling, where continuous generation triggers automated cloud server cooling periods.",
            "D": "Browser session crashes, where simultaneous extraction and calculation exceed workstation physical RAM.",
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "In multi-step analytical workflows, an uncorrected error in step 1 cascades through steps 2 and 3, multiplying inaccuracies. Establishing an explicit stopping point allows the auditor to verify the extracted transactions before allowing the model to compute totals.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Model weights are strictly read-only and cannot be corrupted by incorrect user data.",
            "distractor_C": "Pausing does not prevent rate limits; it enforces human quality gates.",
            "distractor_D": "Text processing in browser tabs consumes minimal local RAM."
        }
    },
    {
        "id": 22,
        "subtopic": "Performance Description: Few-Shot Examples vs Abstract Adjectives",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 2, Section 4.3: Performance description: show what good looks like",
        "scenario": "A marketing lead wants an assistant to draft product release notes in the company's precise brand voice. The lead considers writing: 'Write in a witty, punchy, professional, and sophisticated tone.' How should the lead improve this performance description?",
        "options": {
            "A": "Append ten additional synonyms for witty and sophisticated to ensure the semantic embedding vector is dense.",
            "B": "Provide two concrete examples of approved release notes alongside two examples of rejected release notes.",
            "C": "Command the assistant to run an automated web search across social media to evaluate current slang trends.",
            "D": "Upgrade the user account to a dedicated enterprise tier that natively enforces corporate brand identity."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Abstract adjectives (e.g., 'punchy', 'witty', 'sophisticated') are subjective and interpreted unpredictably by language models. Showing concrete positive examples (what good looks like) and negative examples (what to avoid) provides unambiguous pattern guidance.",
            "distractor_A": "Piling on subjective adjectives increases ambiguity rather than providing clear stylistic boundaries.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Searching social media trends introduces random, unaligned slang that conflicts with company voice.",
            "distractor_D": "Enterprise tiers provide administrative security and quotas, not automatic brand style matching."
        }
    },
    {
        "id": 23,
        "subtopic": "Performance Description: Measurable Quality Rubrics",
        "domain": "Domain 2: Prompt Engineering & In-Context Learning",
        "grounding": "Part 2, Section 4.3: Clear criteria over vague adjectives",
        "scenario": "An insurance claims supervisor instructs an assistant to summarize customer incident reports. Which instruction represents an objective, measurable performance criterion rather than a vague qualitative request?",
        "options": {
            "A": "Ensure the incident summary is completely comprehensive, exceptionally thorough, and deeply insightful.",
            "B": "Write the summary using a dynamic and engaging narrative voice that captures the customer's true emotion.",
            "C": "Include date of loss, policy number, estimated damage amount, and police report ID in bullet points.",
            "D": "Produce a high-quality summary that meets the highest professional standards of modern insurance practice."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Measurable performance criteria specify exact verifiable elements (date of loss, policy number, damage estimate, police ID). Vague adjectives like 'comprehensive', 'insightful', or 'high-quality' cannot be verified objectively.",
            "distractor_A": "Words like 'comprehensive' and 'insightful' are unverifiable qualitative filler.",
            "distractor_B": "Emotionally engaging narratives are inappropriate for objective insurance claim summaries.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "'Highest professional standards' is an ungrounded slogan that gives the model no structural guidance."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 7: Discernment: Output & Process Evaluation (Q24 - Q27)
    # ----------------------------------------------------
    {
        "id": 24,
        "subtopic": "Output Discernment: Surface Fluency vs Truth",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Part 2, Section 5.1: Output discernment: evaluate what the AI produced",
        "scenario": "A junior financial analyst receives an AI-generated equity research memo. The text is beautifully structured, features immaculate grammar, and uses sophisticated investment terminology, but contains an invented EBITDA margin figure. Why did the analyst initially accept the report as accurate?",
        "options": {
            "A": "The analyst used a consumer browser account rather than an authenticated enterprise API connector.",
            "B": "The foundation model was operating with a temperature parameter of zero, guaranteeing factual precision.",
            "C": "The junior analyst verified the EBITDA margin against primary audited filings before submission.",
            "D": "The analyst fell into the fluency trap, mistaking grammatical elegance and confidence for factual truth."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "The fluency trap occurs when human evaluators confuse articulate, authoritative, and grammatically polished prose with factual accuracy. LLMs naturally produce fluent language, making hallucinations deceptively hard to detect without active source verification.",
            "distractor_A": "Subscription tiers do not prevent the human psychological error of the fluency trap.",
            "distractor_B": "Zero temperature reduces sampling randomness, but does not prevent factual hallucinations.",
            "distractor_C": "If the analyst had verified against primary audited filings, the error would have been caught.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 25,
        "subtopic": "Output Discernment: The Fact-Checking Sequence",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Part 2, Section 5.1: How to evaluate output",
        "scenario": "An investigative journalist reviews an AI-generated briefing on municipal real estate zoning decisions. What sequence of actions represents rigorous output discernment?",
        "options": {
            "A": "Identify factual claims, trace them to primary municipal records, challenge anomalies, and decide.",
            "B": "Skim the text for grammatical errors, check sentence length, format fonts, and immediately publish.",
            "C": "Submit the briefing to a second AI assistant and accept the text if the second model praises the draft.",
            "D": "Paste the briefing into an automated grammar checker and approve all sections scoring above ninety."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Rigorous discernment follows a four-step sequence: Identify specific factual claims and figures, Trace them back to primary authoritative sources, Challenge edge cases and discrepancies, and Decide whether to accept, revise, or reject.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Proofreading formatting and grammar checks surface appearance while ignoring factual validity.",
            "distractor_C": "Submitting to another model invites sycophantic praise or compounding hallucinations without external verification.",
            "distractor_D": "Grammar scores evaluate linguistic structure, not whether municipal zoning decisions actually occurred."
        }
    },
    {
        "id": 26,
        "subtopic": "Process Discernment: Detecting Model Drift & Context Rot",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Part 2, Section 5.2: Process discernment: evaluate how the work is going",
        "scenario": "A software engineer engages in a 40-turn chat to debug a complex distributed database issue. By turn 35, the assistant begins suggesting database configurations that directly contradict architectural constraints established in turn 2. What operational issue has occurred?",
        "options": {
            "A": "The server hardware hosting the foundation model experienced permanent memory register degradation.",
            "B": "The conversation outgrew the context window, causing early constraints to be pushed out or diluted.",
            "C": "The assistant was fine-tuned in real time on conflicting database management documentation online.",
            "D": "The engineer utilized deprecated programming keywords that corrupted the active token dictionary."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "As a conversation extends across dozens of turns, the accumulated text fills the context window. Earlier constraints are either truncated or diluted by hundreds of intervening tokens, causing the assistant to drift and contradict early instructions.",
            "distractor_A": "Cloud server hardware does not suffer permanent memory degradation during conversational sessions.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Models are not fine-tuned during inference conversations; weights remain frozen.",
            "distractor_D": "Programming syntax does not corrupt the model's static token dictionary."
        }
    },
    {
        "id": 27,
        "subtopic": "Process Discernment: Knowing When to Reset vs Steer",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Part 2, Section 5.2: Knowing when to steer, when to restart, and when to stop",
        "scenario": "A data analyst notices an assistant repeating a circular calculation error across four consecutive prompts, despite three detailed corrective explanations. According to process discernment, what is the most effective operational move?",
        "options": {
            "A": "Continue the chat and submit identical prompts repeatedly until stochastic sampling breaks the loop.",
            "B": "Add an angry emotional warning in all capital letters threatening to report the model to administrators.",
            "C": "Stop the conversation, open a fresh chat, and re-frame the brief with the calculation formula included.",
            "D": "Switch to an offline image generation model to illustrate the calculation formula graphically."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "When a chat enters a compounding error loop, the faulty reasoning remains in the context history, biasing future tokens. Process discernment dictates cutting losses: open a fresh chat, strip out the conversational baggage, and supply explicit constraints.",
            "distractor_A": "Submitting identical prompts in a contaminated context simply reinforces the error loop.",
            "distractor_B": "Capital letters and emotional threats do not alter mathematical token prediction.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Image generation models produce pictures, not audited numerical calculations."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 8: Discernment: Ethical Discernment & Automation Bias (Q28 - Q31)
    # ----------------------------------------------------
    {
        "id": 28,
        "subtopic": "Ethical Discernment: Bias, Fairness & Representation",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 5.3: Ethical discernment: evaluate whether the work is right",
        "scenario": "A human resources manager uses an assistant to screen job applicants for leadership positions. The manager notices that the model's summaries consistently highlight assertiveness in male candidates while labeling identical phrasing in female candidates as abrasive. What operational action is required?",
        "options": {
            "A": "Accept the summaries because generative models reflect purely objective statistical linguistic data.",
            "B": "Instruct the assistant to upgrade its internal token temperature setting to maximize scoring randomness.",
            "C": "Delegate all leadership screening to an external image recognition model to evaluate candidate photos.",
            "D": "Intervene immediately by establishing objective scoring rubrics and removing gender markers from text."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Ethical discernment requires identifying bias and unfair representation inherited from historical training data. The HR manager must intervene by standardizing criteria, eliminating gender markers, and enforcing structured rubrics rather than accepting ungrounded qualitative labels.",
            "distractor_A": "Training data reflects historical human societal biases; accepting it uncritically perpetuates discrimination.",
            "distractor_B": "Increasing temperature increases randomness and worsens arbitrary, unfair scoring variance.",
            "distractor_C": "Screening candidates based on facial photos is unethical and violates equal opportunity laws.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 29,
        "subtopic": "Automation Bias: Complacency & Uncritical Acceptance",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 5.4: Automation bias and cynicism: two cognitive traps",
        "scenario": "A radiologist uses an AI diagnostic assistant that has accurately flagged 99 consecutive normal chest X-rays. On the 100th scan, the assistant flags the image as normal, missing a subtle pulmonary nodule that the radiologist would have caught during manual inspection. What cognitive failure occurred?",
        "options": {
            "A": "Automation bias, where prolonged exposure to correct AI outputs eroded the human vigilance threshold.",
            "B": "Algorithmic cynicism, where the clinician assumed the system was incompetent and rejected its findings.",
            "C": "Context dilution, where historical X-ray images crowded out the patient's active radiological pixels.",
            "D": "Quantization drift, where hospital server graphics processing units lost numerical floating-point precision."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Automation bias is the human tendency to become complacent when a machine performs reliably over time. The operator relaxes their critical vigilance, trusting the AI's assessment and failing to detect rare but critical errors.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Cynicism is the opposite trap—rejecting AI completely; the radiologist trusted the system too much.",
            "distractor_C": "Inference on the 100th image ran in a fresh context, not an overcrowded context window.",
            "distractor_D": "The failure was human clinical vigilance erosion, not a hardware GPU quantization fault."
        }
    },
    {
        "id": 30,
        "subtopic": "Algorithmic Cynicism: Rejection of Real Utility",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Part 2, Section 5.4: Automation bias and cynicism: two cognitive traps",
        "scenario": "A senior paralegal tries an AI assistant once to draft a contract summary. The draft misses one boilerplate clause. The paralegal declares that 'AI is completely useless for legal work', bans staff from using it, and spends 60 hours manually drafting summaries. What cognitive trap does this reaction illustrate?",
        "options": {
            "A": "Automation bias, accepting the first generated response without verifying underlying court records.",
            "B": "Algorithmic cynicism, rejecting an effective tool entirely due to an early, easily correctable flaw.",
            "C": "Process discernment, accurately concluding that AI is economically unviable for legal practices.",
            "D": "Platform awareness, selecting an unspecialized search model for proprietary contract extraction."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Algorithmic cynicism is the uncritical rejection of AI technology based on an initial mistake. Because the first draft was imperfect, the paralegal dismissed the entire capability, missing opportunities to save dozens of hours through proper prompt description and human review.",
            "distractor_A": "The paralegal rejected the output immediately rather than complacently accepting it.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Banning tools that could safely automate routine drafting is an operational failure, not sound discernment.",
            "distractor_D": "The cognitive trap is the all-or-nothing emotional rejection, not platform selection."
        }
    },
    {
        "id": 31,
        "subtopic": "Process Discernment: Knowing When Doing It Yourself Is Faster",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Part 2, Section 5.2: Knowing when to stop",
        "scenario": "A technical writer spends 45 minutes prompting and re-prompting an assistant to reformat a 2-page equipment maintenance guide. The writer corrects the same table formatting error four times, watches the model drift back, and ultimately rewrites the entire text by hand. What operational failure occurred?",
        "options": {
            "A": "Platform awareness, selecting an advanced cloud reasoning engine instead of an unspecialized search tool.",
            "B": "Creation diligence, failing to obtain commercial software licensing agreements before formatting text.",
            "C": "Process discernment, failing to recognize when steering AI is consuming more effort than manual execution.",
            "D": "Transparency diligence, omitting public citations acknowledging that the model assisted in drafting text."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Process discernment includes recognizing when using AI costs more time and energy than doing the work manually. Spending 45 minutes wrestling with prompts for a 5-minute manual task is an operational failure.",
            "distractor_A": "The issue was failing to stop wrestling with formatting, not cloud model selection.",
            "distractor_B": "Formatting technical manuals does not require specialized external licensing agreements.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Transparency citations are irrelevant when the final text was manually rewritten by hand."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 9: Diligence: Creation, Operation, Transparency (Q32 - Q37)
    # ----------------------------------------------------
    {
        "id": 32,
        "subtopic": "Creation Diligence: Building Reliable Systems",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 6.1: Creation diligence: doing the work properly when you set it up",
        "scenario": "A logistics director designs an automated AI agent to route customer delivery trucks. Which preparatory action demonstrates creation diligence before launching the agent into production?",
        "options": {
            "A": "Setting the assistant sampling temperature to maximum to ensure routing proposals are creative and diverse.",
            "B": "Disabling all human confirmation screens to maximize end-to-end automated dispatch velocity.",
            "C": "Deploying the agent directly to customer fleets on day one to gather real-world error data rapidly.",
            "D": "Testing edge cases, configuring geographic boundaries, and verifying fallback escalation procedures."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Creation diligence means doing the engineering and governance work properly upfront: testing edge cases (e.g., bridge weight limits, severe weather), setting hard operational boundaries, and ensuring human dispatchers can intervene seamlessly.",
            "distractor_A": "High temperature introduces unpredictable routing hallucinations.",
            "distractor_B": "Disabling human review screens removes essential safety guardrails.",
            "distractor_C": "Deploying untested agents into live operations creates severe commercial and physical safety hazards.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 33,
        "subtopic": "Operation Diligence: Human Oversight in Flight",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 6.2: Operation diligence: doing the work properly while it runs",
        "scenario": "A fintech firm runs an autonomous transaction monitoring agent that flags suspicious wire transfers. The compliance officer reviews weekly error logs, spot-checks five percent of cleared transactions, and updates threshold rules monthly. What operational competency is this officer exercising?",
        "options": {
            "A": "Operation diligence, maintaining disciplined human oversight and monitoring while the system runs.",
            "B": "Context engineering, compressing structured banking ledgers into serialized prompt token streams.",
            "C": "Platform awareness, migrating legacy SQL stored procedures into cloud-hosted vector embeddings.",
            "D": "Algorithmic cynicism, rejecting automated transaction scores due to distrust of machine learning."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Operation diligence is ongoing stewardship. Launching a system is not fire-and-forget; operators must monitor error logs, conduct random audits, and refine rules over time as real-world conditions evolve.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Context engineering relates to prompt construction, not ongoing operational audit.",
            "distractor_C": "Database migration is an IT infrastructure project, not operational compliance diligence.",
            "distractor_D": "Spot-checking transactions is standard responsible oversight, not cynical rejection of technology."
        }
    },
    {
        "id": 34,
        "subtopic": "Transparency Diligence: Honest Disclosure",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 6.3: Transparency diligence: being open about what AI did",
        "scenario": "A policy analyst drafts a government white paper using an AI assistant to summarize 50 public stakeholder submissions. In the methodology section, the analyst writes: 'Public submissions were synthesized using Claude 3.5 Sonnet to extract key themes, with all extracted points audited against original submissions by research staff.' Why is this disclosure commendable?",
        "options": {
            "A": "It transfers all legal liability for policy recommendations to the software model provider.",
            "B": "It practices transparency diligence by honestly describing the tool used, the task, and human review.",
            "C": "It guarantees that the white paper will receive automatic fast-track legislative approval.",
            "D": "It eliminates the operational requirement for peer review by academic advisory committees."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Transparency diligence means being clear and honest about where and how AI was used. Stating the exact tool, the specific role it played, and the human verification step provides complete, accountable transparency.",
            "distractor_A": "Public disclosures do not transfer legal liability to commercial software vendors.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "Methodology disclosures inform readers; they do not bypass legislative debate.",
            "distractor_D": "Transparent AI usage increases the need for rigorous peer review rather than eliminating it."
        }
    },
    {
        "id": 35,
        "subtopic": "Transparency Diligence: Misleading AI Claims",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 6.3: Two ways to get transparency wrong",
        "scenario": "A boutique market research agency uses an assistant to clean up grammar and generate charts from human-conducted customer focus groups. In their marketing brochure, the agency writes: 'Our proprietary autonomous neural intelligence conducts end-to-end consumer sentiment analysis.' What operational failure does this represent?",
        "options": {
            "A": "Algorithmic cynicism, understating the genuine computational capabilities of artificial intelligence.",
            "B": "Automation bias, placing uncritical reliance on grammar correction tools to validate qualitative charts.",
            "C": "Failing transparency diligence by overclaiming automation to appear more technologically sophisticated.",
            "D": "Context rot, allowing marketing copy to dilute empirical research findings in client presentation slides."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Transparency can be violated in two directions: concealing AI use, or falsely exaggerating it. Claiming that basic grammar editing and chart drafting represents 'proprietary autonomous neural intelligence' overclaims automation to mislead clients.",
            "distractor_A": "The agency is exaggerating AI capabilities, not cynically dismissing them.",
            "distractor_B": "The failure is misleading marketing claims, not uncritical reliance on software.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Context rot refers to token window overflow, not promotional exaggerations."
        }
    },
    {
        "id": 36,
        "subtopic": "Non-Transferable Accountability",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 6: Diligence: take responsibility for the outcome",
        "scenario": "A cloud security engineer accepts an AI coding assistant's suggestion to bypass TLS certificate validation in a microservice to resolve a connection timeout. When a data breach occurs through this vulnerability, the engineer claims: 'The AI assistant generated the code, so the software vendor is at fault.' Why is this defense invalid?",
        "options": {
            "A": "Bypassing TLS validation is automatically classified as a harmless development convenience under cloud standards.",
            "B": "Commercial coding assistant software licenses explicitly transfer all corporate cybersecurity liability to the vendor.",
            "C": "The engineer should have prompted the AI assistant to assume legal liability before accepting the code suggestion.",
            "D": "AI can automate operational tasks, but human professionals and their organizations retain complete accountability."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Accountability is strictly non-transferable. Tools generate suggestions, but the human engineer who reviews, commits, and deploys the code holds 100% professional and institutional responsibility for security outcomes.",
            "distractor_A": "Disabling TLS validation is an extreme security flaw, never a harmless convenience.",
            "distractor_B": "Software licenses universally disclaim all liability for software defects or data breaches.",
            "distractor_C": "Prompts cannot force an algorithm to assume legal liability.",
            "distractor_D": "N/A (Correct Option)"
        }
    },
    {
        "id": 37,
        "subtopic": "Responsible AI: Environmental & Social Costs",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Part 2, Section 6.4: The wider picture: resource use and labor",
        "scenario": "An enterprise sustainability officer reviews corporate IT resource consumption. The officer discovers that employees routinely run heavy reasoning models with maximum thinking tokens for simple grammar checks and spellchecking. Why does this practice violate operational diligence?",
        "options": {
            "A": "It expends massive energy and compute resources on simple tasks where lightweight models suffice.",
            "B": "It degrades global foundation model neural weights by exhausting international internet bandwidth quotas.",
            "C": "It causes commercial cloud data centers to automatically vent hazardous cooling chemicals into urban areas.",
            "D": "It permanently locks employee workstations out of enterprise word processing licenses due to token overuse."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Reasoning models require significant data center electricity and water cooling per query. Running heavy reasoning compute for trivial spellchecking wastes substantial enterprise budget and environmental resources when lightweight models or local spellcheckers accomplish the task instantly.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Internet bandwidth does not degrade neural network weights.",
            "distractor_C": "Data centers do not vent toxic chemicals into urban areas when running reasoning queries.",
            "distractor_D": "Token consumption does not revoke desktop software licenses."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 10: The Whole System: 10-80-10 Rule & Beginner Mistakes (Q38 - Q40)
    # ----------------------------------------------------
    {
        "id": 38,
        "subtopic": "The 10-80-10 Rule: Allocation of Human Effort",
        "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
        "grounding": "Part 3, Section 7: The whole picture: the 10-80-10 rule",
        "scenario": "A product management team adopts the 10-80-10 operational model to guide their AI development lifecycle. How are human effort and oversight allocated across the workflow?",
        "options": {
            "A": "10% manual data entry, 80% training foundation neural network weights, and 10% marketing final software.",
            "B": "10% setting direction, 80% orchestrating the AI, and 10% judging the result, with diligence throughout.",
            "C": "10% selecting cloud hosting vendors, 80% automated code deployment, and 10% managing external legal litigation.",
            "D": "10% drafting prompts, 80% verifying arithmetic spreadsheets manually, and 10% encrypting production databases."
        },
        "correct": "B",
        "explanation": {
            "correct_rationale": "Under the 10-80-10 rule, humans invest the first 10% defining the problem, constraints, and approach (Delegation and Description); AI performs the middle 80% of routine heavy lifting while the human steers; and humans invest the final 10% verifying claims and deciding acceptance (Discernment). Diligence surrounds the entire 100%.",
            "distractor_A": "Foundation models are pretrained by vendors, not trained manually by product management teams.",
            "distractor_B": "N/A (Correct Option)",
            "distractor_C": "The rule describes task execution effort, not vendor procurement and litigation.",
            "distractor_D": "The middle 80% is AI execution, not manual spreadsheet verification."
        }
    },
    {
        "id": 39,
        "subtopic": "Beginner Mistake 1: Prompting Before Defining the Problem",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Part 3, Section 8: Four common beginner mistakes",
        "scenario": "An operations associate sits down at a computer, immediately opens an AI chat tab, and begins typing fragmented prompts without reviewing the project brief, client objectives, or compliance constraints. Which common operational mistake is the associate committing?",
        "options": {
            "A": "Automation bias, placing uncritical reliance on statistical models to verify regulatory compliance rules.",
            "B": "Algorithmic cynicism, rejecting an effective computational tool due to minor initial formatting defects.",
            "C": "Prompting before defining the problem, jumping directly into text generation without establishing goals.",
            "D": "Context rot, allowing long conversation transcripts to dilute early project instructions and parameters."
        },
        "correct": "C",
        "explanation": {
            "correct_rationale": "Mistake 1 is jumping straight into typing prompts before knowing what you want to achieve, who the audience is, what the boundaries are, and how the output will be checked. High fluency requires defining the problem before opening the tool.",
            "distractor_A": "The associate has not received any output yet to exhibit automation bias.",
            "distractor_B": "The associate is eager to prompt, not cynically rejecting the tool.",
            "distractor_C": "N/A (Correct Option)",
            "distractor_D": "Context rot occurs across dozens of turns in long chats, not before the first prompt is sent."
        }
    },
    {
        "id": 40,
        "subtopic": "Beginner Mistake 2: Treating First Answer as Final",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Part 3, Section 8: Four common beginner mistakes",
        "scenario": "A marketing copywriter types a hasty one-line prompt: 'Write an article about electric vehicles.' The assistant returns a bland, general overview. Frustrated, the copywriter concludes that 'AI is completely useless for serious content creation' and immediately closes the browser. Which beginner mistake does this embody?",
        "options": {
            "A": "Falling prey to automation bias, missing the mathematical skill required to compute token loss distributions.",
            "B": "Prompting before defining the problem, missing the technical ability to train custom transformer tokenizers.",
            "C": "Ignoring data privacy standards, missing the cryptographic skills required to redact proprietary vehicle specs.",
            "D": "Treating the first output as final, missing the iterative description and discernment feedback steering loop."
        },
        "correct": "D",
        "explanation": {
            "correct_rationale": "Mistake 2 is treating the first answer as the final answer. An initial prompt often yields a generic baseline. AI fluency requires inspecting the result (Discernment), providing specific corrective guidance (Description), and steering the output iteratively toward quality.",
            "distractor_A": "The copywriter rejected the output rather than uncritically trusting it.",
            "distractor_B": "Writing content does not require training custom transformer tokenizers.",
            "distractor_C": "No proprietary or private data was leaked in this public marketing query.",
            "distractor_D": "N/A (Correct Option)"
        }
    }
]

def main():
    print("=== Validating Chapter 3 Questions ===")
    assert len(QUESTIONS) == 40, f"Expected 40 questions, got {len(QUESTIONS)}"
    
    # Check answer key distribution
    keys = [q["correct"] for q in QUESTIONS]
    key_counts = {k: keys.count(k) for k in "ABCD"}
    print(f"Key distribution: {key_counts}")
    assert key_counts == {"A": 10, "B": 10, "C": 10, "D": 10}, f"Keys must be exactly 10 A, 10 B, 10 C, 10 D, got {key_counts}"

    meta_patterns = [
        re.compile(r'\bconcept\b', re.I),
        re.compile(r'\bchapter\b', re.I),
        re.compile(r'\bsyllabus\b', re.I),
        re.compile(r'\bframework\b', re.I),
        re.compile(r'\bdoctrine\b', re.I),
        re.compile(r'\bauthor\b', re.I),
        re.compile(r'\bcourse\b', re.I),
        re.compile(r'\btextbook\b', re.I),
        re.compile(r'\blines?\s+\d+', re.I)
    ]
    max_len_diff = 0
    for q in QUESTIONS:
        scen = q["scenario"]
        found_scen = [p.pattern for p in meta_patterns if p.search(scen)]
        assert not found_scen, f"Q{q['id']} has meta words in scenario: {found_scen}"
        
        opt_lens = []
        for k, text in q["options"].items():
            found_opt = [p.pattern for p in meta_patterns if p.search(text)]
            assert not found_opt, f"Q{q['id']} option {k} has meta words: {found_opt}"
            opt_lens.append(len(text))
        
        diff = max(opt_lens) - min(opt_lens)
        if diff > max_len_diff:
            max_len_diff = diff
            
        # Check explanations
        exp = q["explanation"]
        assert "correct_rationale" in exp and len(exp["correct_rationale"]) > 30
        for k in "ABCD":
            assert f"distractor_{k}" in exp

    print(f"Max option length difference across all questions: {max_len_diff} chars")
    
    # Write to questions.json
    out_path = "Chapter_03_AI_Fluency/questions.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(QUESTIONS, f, indent=2, ensure_ascii=False)
    print(f"[+] Successfully saved 40 questions to {out_path}")

    # Also save to generate_chapter3.py
    gen_path = "Chapter_03_AI_Fluency/generate_chapter3.py"
    with open(__file__, "r", encoding="utf-8") as f:
        code = f.read()
    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"[+] Successfully synchronized: {gen_path}")

if __name__ == "__main__":
    main()
