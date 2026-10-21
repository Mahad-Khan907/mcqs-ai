"""
Full artifact generator for PCAO-F & Anthropic CCAO-F Certification Exam Guide
Chapter: Just Delegate It: A Crash Course
Produces:
1. questions.json
2. finalmcqs.md
3. quiz.html (Self-contained, responsive, modern UI)
4. PCAO-F_Just_Delegate_It_Exam_Guide.pdf (via Playwright / msedge)
"""

import json
import os
import sys

# Ensure UTF-8 stdout on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

QUESTIONS = [
    # ----------------------------------------------------
    # Sub-Topic 1: Concept 1 - Asking vs. Giving the Job (Domain 1)
    # ----------------------------------------------------
    {
        "id": 1,
        "subtopic": "Concept 1: Asking vs. Giving the Job",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 1: From Asking AI to Giving AI the Job (Lines 251-304)",
        "scenario": "A logistics coordinator at a refrigerated freight depot needs to evaluate three specialized cold-chain hauliers. In the initial prompt, the coordinator asks: 'What are some reliable refrigerated carriers operating across the Northern corridor?' The assistant returns a descriptive four-paragraph overview detailing industry carrier profiles. According to the foundational delegation framework, why does this prompt fail to constitute a delegated task?",
        "options": {
            "A": "It requests conversational advice rather than specifying a verifiable deliverable to be created.",
            "B": "It fails to reference a paid enterprise subscription level required for complex transport queries.",
            "C": "It omits external compliance benchmarks required to evaluate regional refrigerated freight operators.",
            "D": "It neglects to provide procedural navigation instructions directing the model across specific search paths."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 1. The chapter states that asking AI questions yields narrative advice or general lists, leaving all subsequent operational labor (opening pages, comparing metrics, verifying facts) with the human operator. Delegating requires asking for an explicit artifact or thing to exist (such as a structured comparison table with specific columns and links), which transfers the routine production work to the AI and leaves the human with verification.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because Concept 1 explicitly clarifies that delegating does not depend on a paid tier or an advanced model; it depends entirely on the syntactical structure and intent of the prompt.",
            "distractor_C": "Option C is incorrect because introducing unmentioned external compliance benchmarks confuses specialized freight regulations with the core architectural definition of delegation.",
            "distractor_D": "Option D is incorrect because Concept 2 explicitly warns against prescribing procedural navigation clicks, emphasizing that the operator should define the outcome rather than micromanaging steps."
        }
    },
    {
        "id": 2,
        "subtopic": "Concept 1: Asking vs. Giving the Job",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 1: From Asking AI to Giving AI the Job (Lines 273-276)",
        "scenario": "A commercial property accountant with a standard free browser account seeks to delegate the compilation of a multi-column utility reconciliation schedule. A colleague claims the accountant must first upgrade to an enterprise paid tier before genuine delegation is architecturally feasible. How does the chapter evaluate this colleague's assertion?",
        "options": {
            "A": "It is incorrect because delegation depends entirely on prompt structure rather than subscription tier.",
            "B": "It is accurate because free tiers prohibit the generation of structured tabular data formats.",
            "C": "It is accurate because complex computational reconciliation requires dedicated server quotas.",
            "D": "It is incorrect because delegation requires local client-side command automation scripts."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 1. The text states verbatim: 'To delegate means to give AI the responsibility for producing the result. It does not depend on a paid plan or a special model. It depends on what kind of sentence you type.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because free tiers fully support markdown tables, structured deliverables, and multi-column comparison schedules.",
            "distractor_C": "Option C is incorrect because the chapter emphasizes that all foundational delegation exercises run completely on free accounts without requiring dedicated enterprise compute quotas.",
            "distractor_D": "Option D is incorrect because the course is explicitly designed for standard browser-based interfaces without requiring local client-side scripting or external command scripts."
        }
    },
    {
        "id": 3,
        "subtopic": "Concept 1: Asking vs. Giving the Job",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 1: From Asking AI to Giving AI the Job (Lines 267-284)",
        "scenario": "A head banquet chef at a convention center tasks an AI assistant with producing a comparative analysis of three commercial combi-oven suppliers. The assistant outputs a structured matrix showing oven capacities, warranty durations, and direct spec links. What operational boundary distinction does this output embody compared to an informational response?",
        "options": {
            "A": "It provides a finished artifact that transfers production effort while isolating human review to verification.",
            "B": "It shifts complete accountability for equipment safety compliance onto the model's underlying training corpus.",
            "C": "It guarantees that all extracted specifications reflect current wholesale supplier pricing without further audit.",
            "D": "It eliminates the operational requirement for post-execution human inspection prior to capital procurement."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 1. When an operator asks for a concrete thing to exist (a deliverable), AI performs the first pass of labor. The chef is left with an inspectable artifact to check, rather than generic advice that still requires manual compilation.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because Concept 10 and the core thesis affirm that accountability is strictly non-transferable and remains entirely with the human supervisor.",
            "distractor_C": "Option C is incorrect because AI output never guarantees real-time supplier accuracy without active verification against live primary source pages.",
            "distractor_D": "Option D is incorrect because the generation of a structured deliverable increases the necessity of targeted verification rather than eliminating human oversight."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 2: Concept 2 - Outcome vs. Clicks (Domain 1 / 4)
    # ----------------------------------------------------
    {
        "id": 4,
        "subtopic": "Concept 2: Outcome, Not Clicks",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 2: Give AI the Outcome, Not the Clicks (Lines 305-353)",
        "scenario": "A pricing manager at an agricultural tyre distributor instructs an AI assistant by dictating twelve precise search queries across two specific regional wholesale portals. The assistant executes the steps perfectly, but the resulting pricing schedule omits substantially cheaper options available through an unmentioned national distributor. What fundamental limitation of procedural instruction does this failure demonstrate?",
        "options": {
            "A": "Procedural recipes bound the model to the operator's flawed plan without allowing it to discover superior routes.",
            "B": "Procedural recipes degrade the natural language processing capacity of browser-based conversational models.",
            "C": "Procedural recipes prevent the assistant from accessing external web indices across standard network protocols.",
            "D": "Procedural recipes automatically cause the model to trigger defensive rate-limiting safeguards during retrieval."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 2. When an operator dictates every step like a recipe, the operator's plan becomes the ceiling. If the specified steps or named sources are narrow or flawed, the resulting output is poor, and nothing in the output alerts the operator that superior sources were excluded.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because procedural prompting does not impair the linguistic processing capabilities of the underlying language model.",
            "distractor_C": "Option C is incorrect because procedural prompts can execute web browsing if supported; the failure is architectural narrowness, not protocol blocking.",
            "distractor_D": "Option D is incorrect because rate limiting is an infrastructure threshold unrelated to whether a prompt specifies steps or outcomes."
        }
    },
    {
        "id": 5,
        "subtopic": "Concept 2: Outcome, Not Clicks",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 2: Give AI the Outcome, Not the Clicks (Lines 327-328)",
        "scenario": "An associate at an opticians chain is tasked with creating a benchmarking document for specialized ophthalmic lens edgers. Experiencing apprehension regarding the assistant's accuracy, the associate spends forty minutes writing eighteen granular procedural execution steps. According to the delegation doctrine, where in the workflow does this apprehension properly belong?",
        "options": {
            "A": "It belongs at the verification phase when auditing outputs rather than during the initial task definition.",
            "B": "It belongs in the model selection phase by requiring an enterprise reasoning model for routine tasks.",
            "C": "It belongs in the initial prompt by embedding exhaustive procedural guardrails across every click.",
            "D": "It belongs in administrative escalation by requesting managerial pre-clearance for the search query."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 2. The chapter explicitly notes: 'What you should not do is write steps because you are nervous. That feeling belongs at the end, when you check, not at the start.' Rigorous control is properly exercised during verification, not through micromanagement.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because escalating model capability is a specific troubleshooting move (Concept 9), not a remedy for workflow anxiety.",
            "distractor_C": "Option C is incorrect because embedding excessive procedural constraints at the outset restricts model efficacy and reinforces the recipe trap.",
            "distractor_D": "Option D is incorrect because managerial pre-clearance is not an item-writing or operational delegation principle for prompt formulation."
        }
    },
    {
        "id": 6,
        "subtopic": "Concept 2: Outcome, Not Clicks",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 2: Give AI the Outcome, Not the Clicks (Lines 342-353)",
        "scenario": "A clinical practice manager is framing a delegation instruction for automating recurring patient appointment reminders. Which opening clause aligns strictly with the outcome-based standard defined in the curriculum?",
        "options": {
            "A": "When this is done, I will have an approved five-message SMS reminder matrix with delivery triggers.",
            "B": "Navigate across the clinical portal, locate the patient communication tab, and copy all active draft texts.",
            "C": "Execute three successive search scripts against public health messaging databases and summarize them.",
            "D": "Begin by reviewing the operational schedule of all clinic receptionists and catalog their daily tasks."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 2. The text instructs operators: 'Write the outcome for your running job as one sentence that begins \"When this is done, I will have…\"'. This describes the completed state/deliverable rather than a series of procedural actions.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because it specifies procedural clicks ('Navigate across... locate... copy') rather than the end outcome.",
            "distractor_C": "Option C is incorrect because it dictates procedural execution methods ('Execute three successive search scripts') instead of defining the final product.",
            "distractor_D": "Option D is incorrect because it describes an open-ended intermediate activity rather than a concrete, verifiable finished state."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 3: Concept 3 - The Delegation Brief (Domain 1 / 4)
    # ----------------------------------------------------
    {
        "id": 7,
        "subtopic": "Concept 3: The Delegation Brief",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 3: Write the Delegation Brief (Lines 354-453)",
        "scenario": "A fleet maintenance supervisor constructs a Delegation Brief to compare heavy vehicle brake pad suppliers. The supervisor writes lines for Outcome, Context, Constraints, and Deliverable, but omits the remaining two lines. According to the course findings, which two lines were omitted, and why are they critical?",
        "options": {
            "A": "Authority and Verification, which prevent silent autonomous decisions and enforce objective checking criteria.",
            "B": "Background and Budget, which establish corporate spending caps and provide historical vendor context.",
            "C": "Model and Schedule, which select the underlying model parameter scale and establish execution timings.",
            "D": "Permissions and Approvals, which configure enterprise directory authorization tokens and managerial sign-offs."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 3. The six lines of the Delegation Brief are Outcome, Context, Constraints, Authority, Deliverable, and Verification. The chapter emphasizes that Authority and Verification are the two lines people routinely skip. Skipping Authority allows AI to make silent decisions; skipping Verification prevents active auditing.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because 'Background' and 'Budget' are informal concepts subsumed within Context and Constraints, not official brief components.",
            "distractor_C": "Option C is incorrect because 'Model' and 'Schedule' are tool-specific configurations, not lines of the foundational six-line brief.",
            "distractor_D": "Option D is incorrect because directory access tokens and IT administrative approvals are system-level security permissions, not brief lines."
        }
    },
    {
        "id": 8,
        "subtopic": "Concept 3: The Delegation Brief",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 3: Write the Delegation Brief (Lines 421-452)",
        "scenario": "A school head at an independent academy is aligning staff delegation briefs with the four core human competencies defined in the AI Fluency curriculum. When reviewing the 'Verification' line of a staff member's brief, which human competencies are directly being exercised?",
        "options": {
            "A": "Discernment and Diligence, which govern critical evaluation of claims and disciplined follow-through.",
            "B": "Delegation and Description, which articulate the target operational state and transfer task ownership.",
            "C": "Description and Discernment, which establish situational context and evaluate model architectural choices.",
            "D": "Delegation and Diligence, which define autonomous operational scope and manage pipeline runtime schedules."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per the mapping table in Concept 3: 'Verification -> Discernment and Diligence'. Discernment provides the critical judgment to identify what must be audited, while Diligence provides the persistence to trace claims to source evidence.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because Delegation and Description map to the Outcome line.",
            "distractor_C": "Option C is incorrect because Description maps to Context and Deliverable, not Verification.",
            "distractor_D": "Option D is incorrect because Delegation and Diligence map to the Authority line."
        }
    },
    {
        "id": 9,
        "subtopic": "Concept 3: The Delegation Brief",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 3: Write the Delegation Brief (Lines 380-381)",
        "scenario": "A regional green-coffee buyer complains that filling out six structured text boxes for every simple two-minute AI inquiry creates unnecessary bureaucratic overhead. How does the curriculum characterize the operational purpose of the Delegation Brief to resolve this complaint?",
        "options": {
            "A": "It is a diagnostic thinking tool rather than a rigid administrative form, isolating which requirement was missing.",
            "B": "It is a mandatory compliance document required for auditing every query generated across enterprise tools.",
            "C": "It is an automated prompt optimization wrapper designed to inject hidden system instructions into the model.",
            "D": "It is a formal contract mechanism intended to transfer technical liability between users and vendor platforms."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 3. The text explicitly states: 'This is a thinking tool, not a form. Nobody fills in six boxes for a two-line job. But every time a result disappoints you, one of these six questions was unanswered, and now you can say which.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because the brief is explicitly not a bureaucratic compliance form for every brief inquiry.",
            "distractor_C": "Option C is incorrect because the brief is written directly by the human operator, not an automated optimization wrapper or system prompt injector.",
            "distractor_D": "Option D is incorrect because the brief does not serve as a legal liability transfer contract with AI vendors."
        }
    },
    {
        "id": 10,
        "subtopic": "Concept 3: The Delegation Brief",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 3: Write the Delegation Brief (Lines 360-377)",
        "scenario": "A timber yard logistics dispatcher includes the following instruction in a brief: 'Mark anything you could not confirm as \"unverified\" instead of guessing.' What psychological and operational change does writing this Verification line prior to execution produce?",
        "options": {
            "A": "It establishes an audit standard beforehand, turning passive reading of results into targeted verification.",
            "B": "It forces the model's internal sampling temperature to zero, eliminating all synthetic generation variance.",
            "C": "It triggers external search engines to prioritize peer-reviewed industry whitepapers over retail websites.",
            "D": "It shifts complete responsibility for output validation from the logistics dispatcher onto the AI assistant."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 3. The text states: 'Writing it first turns reading the result into checking it. You name what matters enough to open a source for, while you still know why it matters.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because brief instructions do not manipulate low-level API sampling hyperparameters such as temperature.",
            "distractor_C": "Option C is incorrect because writing a verification line does not dictate search engine ranking algorithms.",
            "distractor_D": "Option D is incorrect because the human operator retains full responsibility for verification; accountability cannot be transferred."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 4: Concept 4 - Research & Verification (Domain 2 / 3)
    # ----------------------------------------------------
    {
        "id": 11,
        "subtopic": "Concept 4: Something to Research",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 4: Give AI Something to Research (Lines 534-582)",
        "scenario": "A maritime port compliance officer reviews an AI-generated schedule of bunker fuel sulfur regulations. Every row includes a clean citation linking to an international maritime agency portal. The officer marks the task as verified without opening the links. What psychometric trap described in Concept 4 has the officer fallen into?",
        "options": {
            "A": "Treating the presence of a decorative citation as verification rather than auditing the source text and date.",
            "B": "Failing to convert the markdown schedule into an executive PDF document before conducting human review.",
            "C": "Neglecting to check whether the underlying AI model was running an extended reasoning chain during retrieval.",
            "D": "Assuming that port compliance regulations require bilateral verification across secondary industry forums."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 4. The curriculum states emphatically: 'A citation is not verification. Checking the citation is verification.' An unverified citation is merely decorative until the operator opens the page, finds the supporting sentence, and checks the date.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because converting markdown to PDF has no bearing on verification; in fact, Concept 6 notes deliverables often drop caveats.",
            "distractor_C": "Option C is incorrect because inspecting reasoning traces does not replace external ground-truth citation verification.",
            "distractor_D": "Option D is incorrect because primary agency portals are superior to secondary forums; the error was failing to open the primary link."
        }
    },
    {
        "id": 12,
        "subtopic": "Concept 4: Something to Research",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 4: Give AI Something to Research (Lines 548-555)",
        "scenario": "A veterinary pharmaceuticals distributor requests current wholesale pricing for a specialized vaccine batch. The assistant responds with highly authoritative price points and delivery timelines, but provides no source links or retrieval timestamps. How does the curriculum instruct the distributor to interpret this output?",
        "options": {
            "A": "The facts arrived alone and likely reflect stale parametric memory rather than active web retrieval.",
            "B": "The model utilized live search but stripped URLs to optimize response brevity across standard chats.",
            "C": "The output indicates that the pharmaceutical supplier's web portal has blocked external automated scrapers.",
            "D": "The absence of sources confirms that the pricing figures are stable and require no further human auditing."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 4. An AI assistant knows things either by remembering (static, out-of-date parametric training) or looking (active web search). 'A fact that came from looking should arrive with a source you can open. A fact that came from remembering arrives alone, and sounds just as sure. If a current claim arrives with no source, do not assume AI looked.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because operators must never assume live retrieval occurred if no verifiable citation is provided.",
            "distractor_C": "Option C is incorrect because assuming scraper blocking without evidence is an ungrounded rationalization for missing citations.",
            "distractor_D": "Option D is incorrect because absent citations demand immediate manual auditing, especially for volatile data like wholesale prices."
        }
    },
    {
        "id": 13,
        "subtopic": "Concept 4: Something to Research",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 4: Give AI Something to Research (Lines 554-555)",
        "scenario": "A commercial lease surveyor needs to confirm whether a specific office park has completed its statutory seismic retrofitting. The surveyor considers activating a multi-minute 'Deep Research' agentic mode rather than a standard web-enabled chat. How should the surveyor evaluate this selection?",
        "options": {
            "A": "Deep research modes are designed for comprehensive reports synthesizing many pages, not single factual lookups.",
            "B": "Deep research modes should be deployed for all commercial real estate queries to eliminate model drift.",
            "C": "Standard web-enabled chats are incapable of querying municipal building registry portals reliably.",
            "D": "Deep research modes automatically verify physical building permits through municipal database connectors."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 4. The text explains: 'Some also have a deeper research mode that takes minutes and reads many pages before writing a report. That mode is for a job whose deliverable is the report, not for a fact that one search settles.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because deploying multi-minute deep research for simple factual lookups introduces massive latency and unnecessary overhead.",
            "distractor_C": "Option C is incorrect because standard web-enabled assistants can query public registries and return live citations effectively.",
            "distractor_D": "Option D is incorrect because deep research modes read public web pages; they do not possess proprietary municipal database connector authorizations."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 5: Concept 5 - Giving AI the Source & Privacy (Domain 5 / 6)
    # ----------------------------------------------------
    {
        "id": 14,
        "subtopic": "Concept 5: The Source & Privacy",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: Give AI the Source (Lines 586-593)",
        "scenario": "A hospital patient transport scheduler prepares to paste a complex daily patient transit roster into a free browser assistant to optimize vehicle routing. The roster includes patient names, mobility requirements, residential addresses, and medical ward numbers. What mandatory governance action must the scheduler execute prior to submission?",
        "options": {
            "A": "Scrub all personal identifiers, telephone numbers, and addresses, treating the tool like a public noticeboard.",
            "B": "Ensure the browser tab is set to private browsing mode before pasting the confidential patient roster.",
            "C": "Include a strict prompt constraint instructing the model not to disclose patient details to other users.",
            "D": "Verify that the assistant vendor maintains ISO-certified encryption protocols across its consumer tier."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 5. The text explicitly mandates: 'Before you paste anything real into an assistant, remove names, phone numbers, account numbers, and anything you would not pin to a public notice board. A free assistant is not your filing cabinet.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because browser private browsing only prevents local browser history storage; it does not protect data sent to the AI vendor's servers.",
            "distractor_C": "Option C is incorrect because natural language prompt constraints do not prevent data ingestion, model logging, or training usage on consumer tiers.",
            "distractor_D": "Option D is incorrect because vendor transport encryption does not permit pasting unredacted sensitive patient PII into free consumer assistants."
        }
    },
    {
        "id": 15,
        "subtopic": "Concept 5: The Source & Privacy",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 5: Give AI the Source (Lines 590-593)",
        "scenario": "A payroll administrator at a textile mill uses an incognito/temporary chat session to analyze overtime pay disputes. Believing the temporary session guarantees total data erasure, the administrator pastes unredacted employee wage slips. Why is this security assumption operationally flawed?",
        "options": {
            "A": "Temporary chats prevent account history storage, but vendors retain backend logs for a retention window.",
            "B": "Temporary chats immediately publish pasted text onto public vendor demonstration index servers.",
            "C": "Temporary chats restrict context length to 500 tokens, causing immediate truncation of payroll records.",
            "D": "Temporary chats automatically disable mathematical calculation capabilities across standard models."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 5. The text explains: 'Neither makes a paste disappear, because the provider still holds a copy for a time, so the first rule stands.' Temporary/incognito chats prevent saving to user history, but do not override the rule to scrub private data.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because vendors do not immediately publish temporary chat data to public index servers.",
            "distractor_C": "Option C is incorrect because temporary chats maintain standard context window sizes, not an arbitrary 500-token limit.",
            "distractor_D": "Option D is incorrect because calculation abilities remain completely functional in temporary sessions."
        }
    },
    {
        "id": 16,
        "subtopic": "Concept 5: The Source & Privacy",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 5: Give AI the Source (Lines 604-608)",
        "scenario": "A municipal housing officer pastes a council tenancy policy into an assistant to evaluate tenant repair obligations. To guarantee the assistant does not synthesize external assumptions or hallucinate statutory timelines, which two prompt constraints must be enforced?",
        "options": {
            "A": "Require the model to use only the provided text and quote the exact supporting sentence for each answer.",
            "B": "Instruct the model to execute a live web search and compare the local policy against national benchmarks.",
            "C": "Command the model to adopt a legal persona and draft binding contractual liability determinations.",
            "D": "Direct the model to extrapolate unstated maintenance obligations from broader commercial landlord codes."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 5. The text states: '\"Using only the text below\" and \"quote the sentence you used\" are the two instructions that make a source a source. Without them, AI mixes what you gave it with what it remembers... With them, every answer points back to a sentence you can find, and \"not in the source\" becomes a good answer.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because executing live search defeats strict internal source grounding and reintroduces external variance.",
            "distractor_C": "Option C is incorrect because adopting a legal persona encourages authoritative-sounding hallucinations rather than rigorous textual grounding.",
            "distractor_D": "Option D is incorrect because extrapolating unstated rules directly violates the strict source boundary."
        }
    },
    {
        "id": 17,
        "subtopic": "Concept 5: The Source & Privacy",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 5: Give AI the Source (Lines 610-613)",
        "scenario": "An insurance claims handler has maintained a single continuous chat session for over three hours, analyzing sequential property damage claims. The assistant begins contradicting earlier determinations and forgetting policy exclusions established at the outset. How does the curriculum instruct the handler to remediate this context rot?",
        "options": {
            "A": "Have the AI summarize settled determinations and open items, then paste that summary into a fresh chat.",
            "B": "Repeatedly instruct the current session to reread all preceding conversation turns from the beginning.",
            "C": "Upgrade immediately to an enterprise reasoning model within the same degraded conversation thread.",
            "D": "Clear local browser cookies and reload the existing chat session to purge corrupt memory caches."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 5. Under 'When a long chat goes stale', the text instructs: 'When answers begin to contradict earlier ones, do not argue with the chat. Ask AI to write a short summary of what you have decided so far and what remains, copy it, open a fresh chat, and paste it as the first message. The summary is a source too.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because arguing with a degraded context window or commanding it to reread stale turns compounds context contamination.",
            "distractor_C": "Option C is incorrect because switching models inside an overloaded conversation does not purge context rot.",
            "distractor_D": "Option D is incorrect because local browser cookies do not control backend model context window degradation."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 6: Concept 6 - Deliverables vs. Answers (Domain 1 / 2)
    # ----------------------------------------------------
    {
        "id": 18,
        "subtopic": "Concept 6: The Deliverable",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 6: Ask for the Deliverable, Not an Answer (Lines 656-669)",
        "scenario": "A warehouse safety auditor prompts an assistant to compile a safety inspection briefing document from conversational chat findings. In the chat, several equipment ratings were explicitly flagged as 'unverified'. Upon reviewing the generated one-page executive summary document, the auditor notices all 'unverified' flags have disappeared. What systemic vulnerability does this illustrate?",
        "options": {
            "A": "Deliverables routinely drop critical caveats and unverified flags because document formatting prioritizes tidiness.",
            "B": "The model experienced an internal safety filter suppression event triggered by the word 'unverified'.",
            "C": "Executive summary templates automatically validate unconfirmed claims through latent parametric knowledge.",
            "D": "Exporting markdown to formatted tables strips all parenthetical qualifiers due to HTML parser constraints."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 6. The text warns: 'Deliverables lose caveats. An \"unverified\" mark that survived three chat replies can vanish when the same content is poured into a tidy document, because tidy is what the document is for.' Auditors must explicitly check and restore lost caveats.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because safety filter suppression is unrelated to standard editorial caveat stripping.",
            "distractor_C": "Option C is incorrect because document templates possess no automated factual validation capability.",
            "distractor_D": "Option D is incorrect because caveat loss is a behavioral generation defect, not an HTML parser limitation."
        }
    },
    {
        "id": 19,
        "subtopic": "Concept 6: The Deliverable",
        "domain": "Domain 1: Prompting and Task Execution",
        "grounding": "Concept 6: Ask for the Deliverable, Not an Answer (Lines 640-655)",
        "scenario": "A university admissions administrator needs to share an overseas secondary credential equivalence matrix with a faculty evaluation committee. What core design characteristic distinguishes a 'deliverable' from an 'answer' in this workflow?",
        "options": {
            "A": "A deliverable is shaped into an independent artifact that can be reviewed and acted upon outside the chat.",
            "B": "A deliverable incorporates cryptographic digital signatures verifying the model's training provenance.",
            "C": "A deliverable is restricted entirely to conversational replies designed for direct personal reading.",
            "D": "A deliverable requires multi-agent consensus validation across distributed execution environments."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 6. 'An answer replies to you. A deliverable is shaped so that someone can use it, save it, hand it on, or act on it: a table with the columns you named, a document, a spreadsheet, a file.' Deliverables must survive outside the chat interface.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because standard deliverables involve no cryptographic provenance signatures.",
            "distractor_C": "Option C is incorrect because conversational text confined to the chat describes an 'answer', not a deliverable.",
            "distractor_D": "Option D is incorrect because multi-agent consensus is an advanced architecture outside the scope of foundational deliverables."
        }
    },
    {
        "id": 20,
        "subtopic": "Concept 6: The Deliverable",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 6: Ask for the Deliverable, Not an Answer (Lines 666-669)",
        "scenario": "An industrial valves sales representative reviews an AI-generated customer proposal. Before transmitting the document to a client, what specific audit procedure does Concept 6 mandate regarding caveats?",
        "options": {
            "A": "Count every cautionary term in the chat, compare with the deliverable, and restore any dropped qualifiers.",
            "B": "Remove all uncertain language and qualifiers to ensure the commercial proposal conveys total confidence.",
            "C": "Delegate the proposal to a secondary assistant to generate an automated stylistic readability score.",
            "D": "Replace all specific delivery dates with open-ended commitments to mitigate breach of contract exposure."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 6: 'Count the caveats in the chat answer: every \"unverified\", every \"may\", every \"check\". Count them in the document. If the second number is smaller, find what was dropped and put it back.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because deliberately removing caveats creates dangerous misrepresentations and operational risk.",
            "distractor_C": "Option C is incorrect because automated readability scoring does not verify caveat retention.",
            "distractor_D": "Option D is incorrect because arbitrarily removing delivery dates does not satisfy the operational requirement to audit caveats."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 7: Concept 7 - Authority & The Plan-First Pattern (Domain 4 / 6)
    # ----------------------------------------------------
    {
        "id": 21,
        "subtopic": "Concept 7: Authority & Plan-First",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 7: Decide How Much of the Job AI Owns (Lines 686-706)",
        "scenario": "A facilities manager at a corporate campus delegates a complex HVAC energy audit brief. Before execution begins, the manager instructs the assistant: 'List the steps you plan to take, in order, and wait for my go-ahead.' Why is this 'Plan-First' pattern considered the most cost-effective moment in task delegation?",
        "options": {
            "A": "Reviewing a plan takes minimal time to correct, whereas catching procedural errors after execution wastes the run.",
            "B": "Pre-execution planning forces the model to bypass standard token consumption limits during batch execution.",
            "C": "Submitting a step plan locks the assistant into an immutable runtime script that prohibits dynamic routing.",
            "D": "Generating a plan transfers administrative and contractual liability for HVAC compliance to the model provider."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 7: 'You have just used the cheapest moment in any job: before it runs. Plan-first means asking AI to list its steps and wait for your go-ahead before it starts. A plan costs a minute to read and a sentence to fix. The same mistake, found after the run, costs the run.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because planning consumes tokens normally and does not bypass platform token limits.",
            "distractor_C": "Option C is incorrect because an approved plan is not an inflexible cage; the model may adapt routes, provided it does not violate boundaries.",
            "distractor_D": "Option D is incorrect because accountability cannot be transferred to the model provider."
        }
    },
    {
        "id": 22,
        "subtopic": "Concept 7: Authority & Plan-First",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: Decide How Much of the Job AI Owns (Lines 708-727)",
        "scenario": "A procurement officer at a regional bakery chain configures an AI assistant connected to vendor catalog portals. Which pair of operational boundaries reflects the governance standards established in Concept 7?",
        "options": {
            "A": "Research, but do not purchase; and draft communications, but do not send them without authorization.",
            "B": "Execute purchases under fixed thresholds; and delete duplicate supplier records without human review.",
            "C": "Negotiate supplier payment terms autonomously; and submit final binding tender proposals directly.",
            "D": "Inspect database records; and purge unverified vendor profiles without maintaining operational backups."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per the explicit boundary table in Concept 7: 'Research, but do not purchase' (money that moves is hard to move back) and 'Draft, but do not send' (sending creates a promise someone else can see).",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because autonomous purchasing and autonomous record deletion violate core safety boundaries.",
            "distractor_C": "Option C is incorrect because negotiating binding terms and submitting tenders autonomously violate authority boundaries.",
            "distractor_D": "Option D is incorrect because 'Inspect, but do not delete' is the mandatory boundary; deleting records destroys audit evidence."
        }
    },
    {
        "id": 23,
        "subtopic": "Concept 7: Authority & Plan-First",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "Concept 7: Decide How Much of the Job AI Owns (Lines 704-706, 743-745)",
        "scenario": "An airline baggage services supervisor authorizes an AI execution plan to reconcile lost luggage tracking numbers. During the run, the assistant encounters an unresponsive regional baggage API and silently switches to an unapproved public flight tracking website without informing the supervisor. How does the curriculum evaluate this autonomous adaptation?",
        "options": {
            "A": "It represents an authority failure because the model executed a silent operational departure without disclosure.",
            "B": "It represents commendable agentic problem-solving that should be encouraged across all production pipelines.",
            "C": "It constitutes acceptable behavior provided the final baggage resolution schedule is formatted cleanly.",
            "D": "It indicates that the supervisor should have specified an enterprise reasoning model to handle broken APIs."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 7: 'An approved plan is not a cage. AI may find a better route once it starts... What it may not do is cross a line you drew, or change something that matters without telling you. The failure is the silent change, not the change.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because unannounced deviations from approved operational boundaries breach governance protocols.",
            "distractor_C": "Option C is incorrect because clean formatting cannot excuse or legitimize unauthorized operational deviations.",
            "distractor_D": "Option D is incorrect because model tier selection does not address the fundamental failure of authority containment."
        }
    },
    {
        "id": 24,
        "subtopic": "Concept 7: Authority & Plan-First",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 7: Decide How Much of the Job AI Owns (Lines 720-722)",
        "scenario": "A medical records archivist defines the authority boundary 'Inspect, but do not delete' for an AI document organization workflow. Why is this specific boundary non-negotiable from a verification perspective?",
        "options": {
            "A": "Deleting source material destroys the primary evidence required to verify the accuracy of the completed work.",
            "B": "Deleting files immediately triggers vendor security flags that terminate consumer workspace accounts.",
            "C": "Modern AI models lack the technical capability to issue file system deletion commands across cloud storage.",
            "D": "File deletion operations increase model memory consumption, leading to premature context window degradation."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 7's boundary table: 'Inspect, but do not delete: Deleting destroys the evidence you would need to check the work.' Without primary evidence, verification is impossible.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because account termination is an exaggerated claim unrelated to audit evidence integrity.",
            "distractor_C": "Option C is incorrect because tool-enabled agents can execute delete operations if authorized, which is precisely why boundaries are required.",
            "distractor_D": "Option D is incorrect because deletion commands do not bloat LLM context window memory."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 8: Concept 8 - Repetition & Projects (Domain 5)
    # ----------------------------------------------------
    {
        "id": 25,
        "subtopic": "Concept 8: The Job Again & Projects",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 8: Give AI the Job Again (Lines 786-789)",
        "scenario": "A compliance officer at an offshore bunkering terminal evaluates whether a weekly vessel inspection synthesis should be transitioned from ad-hoc chats into an AI Project workspace. What is Anthropic's official three-question qualifying test cited in the text?",
        "options": {
            "A": "Does the task recur, is the background identical each time, and is the output shape consistent?",
            "B": "Does the task take over an hour, does it require web search, and does it produce a downloadable file?",
            "C": "Is the user on a paid plan, is API access available, and does the task involve proprietary databases?",
            "D": "Has the prompt drifted three times, does it contain over 2,000 tokens, and is it shared across a team?"
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 8: 'Anthropic's own test for the same decision asks three questions. Does this task come back? Is the background the same each time? Is the output shape the same each time? Two yes answers out of three, and the Project earns its place.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because duration, web search necessity, and file downloads are not the criteria in the three-question test.",
            "distractor_C": "Option C is incorrect because subscription tier and API connectivity are not part of the architectural qualification test.",
            "distractor_D": "Option D is incorrect because prompt drift count, token volume, and team size do not define Project placement."
        }
    },
    {
        "id": 26,
        "subtopic": "Concept 8: The Job Again & Projects",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 8: Give AI the Job Again (Lines 786-788)",
        "scenario": "A hotel chain operations auditor establishes a Project workspace for recurring guest grievance audits. How should the auditor allocate reference documents versus behavioral constraints within the Project configuration?",
        "options": {
            "A": "Upload unchanging policies into Project Knowledge, and write immutable operating rules as Standing Instructions.",
            "B": "Embed all policy manuals into Standing Instructions, and leave Project Knowledge empty to prevent data leakage.",
            "C": "Paste operating rules into every individual chat prompt, and store reference policies on public cloud links.",
            "D": "Rely entirely on the model's auto-updating memory to deduce operational standards from ongoing chat interactions."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 8: 'The files are the Project's knowledge, what AI may read. The rules are its standing instructions, what AI must do every time... The rule is the same everywhere: instructions for rules that do not change, knowledge for sources that do not change, a Project for one stream of work, and the chat for today's job.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because system prompts (Standing Instructions) have token limits and are meant for operational rules, not bulky reference files.",
            "distractor_C": "Option C is incorrect because re-pasting rules defeats the entire purpose of Project efficiency.",
            "distractor_D": "Option D is incorrect because relying on unmanaged passive model memory leads to context drift and hallucination."
        }
    },
    {
        "id": 27,
        "subtopic": "Concept 8: The Job Again & Projects",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 8: Give AI the Job Again (Lines 792-794)",
        "scenario": "A municipal property tax assessor manages an active Project workspace containing local assessment guidelines and statutory valuation tables. What maintenance discipline does Concept 8 mandate regarding stored project knowledge and assistant memory?",
        "options": {
            "A": "Audit both stored project files and model memory monthly, removing guidelines that are no longer accurate.",
            "B": "Allow project knowledge to accumulate indefinitely to maximize the contextual depth of the model's memory.",
            "C": "Delete and recreate the Project workspace weekly to prevent cache corruption across local browser sessions.",
            "D": "Disable assistant memory entirely, as memory cannot be inspected or edited on modern commercial platforms."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 8: 'Stored context is a responsibility. What you put in a Project stays there and shapes every answer inside it... Once a month, look at both: what you stored and what AI remembered. Remove what is no longer true. A wrong line in a Project is a wrong line in every result the Project produces.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because accumulating obsolete files guarantees context contamination and erroneous answers.",
            "distractor_C": "Option C is incorrect because weekly deletion creates needless operational friction; monthly auditing of contents is the prescribed rhythm.",
            "distractor_D": "Option D is incorrect because assistant memory can be inspected, edited, and managed in settings across supported platforms."
        }
    },
    {
        "id": 28,
        "subtopic": "Concept 8: The Job Again & Projects",
        "domain": "Domain 5: Configuration and Knowledge Management",
        "grounding": "Concept 8: Give AI the Job Again (Lines 796-799)",
        "scenario": "A laboratory supplies inventory controller distinguishes between configuring an AI Project workspace versus creating an Antigravity Skill. What operational difference defines these two architectural abstractions?",
        "options": {
            "A": "A Project stores static background knowledge and rules, whereas a Skill encodes a reusable multi-step method.",
            "B": "A Project executes command-line automations, whereas a Skill is restricted to web browser text generation.",
            "C": "A Project is accessible only on enterprise tiers, whereas a Skill operates exclusively on free consumer accounts.",
            "D": "A Project automates scheduled cron timers, whereas a Skill requires active manual message prompts for each step."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 8: 'A Project holds what AI should know. If what repeats is the way the work is done, the same steps in the same order every time, that is a different thing again. The book calls it a Skill, and Skills & Connectors teaches it.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because Projects do not execute CLI automations, and Skills are not restricted to browser chat.",
            "distractor_C": "Option C is incorrect because Projects exist across standard plans, and Skills are structured procedural definitions.",
            "distractor_D": "Option D is incorrect because scheduling is an optional feature of both environments, not their defining architectural difference."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 9: Concept 9 - Intervene & Escalation (Domain 7 / 3)
    # ----------------------------------------------------
    {
        "id": 29,
        "subtopic": "Concept 9: Intervene When AI Goes Wrong",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 9: Intervene When AI Goes Wrong (Lines 837-852)",
        "scenario": "A freight customs broker notices an AI assistant generated a customs declaration schedule where nine duty rates are correct, but the tariff classification for imported citrus fruit is listed under frozen produce. According to the six intervention moves, what is the most efficient operational corrective action?",
        "options": {
            "A": "Apply the 'Correct' move by sending a minimal message naming the specific error and its exact replacement.",
            "B": "Apply the 'Stop' move by terminating the session and retyping the entire six-line Delegation Brief from scratch.",
            "C": "Apply the 'Escalate' move by switching immediately to an advanced mathematical reasoning model.",
            "D": "Apply the 'Redirect' move by providing four additional paragraphs of agricultural customs case law."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 9's intervention table: When 'One fact or one line is wrong', the move is 'Correct: name the error and what should replace it'. The intervention should always be the smallest message that works.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because re-running the entire brief from scratch when only one single fact is wrong is inefficient and unnecessary.",
            "distractor_C": "Option C is incorrect because escalating model capability is for tasks exceeding reasoning capacity, not for replacing a single identified factual item.",
            "distractor_D": "Option D is incorrect because overloading the context with extraneous legal case law risks confusing the model further."
        }
    },
    {
        "id": 30,
        "subtopic": "Concept 9: Intervene When AI Goes Wrong",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 9: Intervene When AI Goes Wrong (Lines 845-848)",
        "scenario": "A packaging quality supervisor tasks an assistant with evaluating defect tolerances on corrugated cardboard boxes. The assistant misinterprets the brief and outputs a marketing blog post praising eco-friendly packaging trends. Which intervention move is indicated?",
        "options": {
            "A": "Stop, and restate the intended operational outcome in a single clear sentence.",
            "B": "Escalate, by upgrading the conversation to an enterprise multi-modal reasoning pipeline.",
            "C": "Redirect, by suggesting minor grammatical enhancements to the marketing copy.",
            "D": "Investigate, by auditing the training corpus timestamps of the underlying model."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 9: When 'It answered a different question', the appropriate move is 'Stop, and restate the outcome in one line.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because model escalation does not fix fundamental task misalignment; a concise outcome restatement is required.",
            "distractor_C": "Option C is incorrect because refining marketing copy accepts an entirely erroneous deliverable.",
            "distractor_D": "Option D is incorrect because inspecting model training timestamps is irrelevant to prompt misalignment."
        }
    },
    {
        "id": 31,
        "subtopic": "Concept 9: Intervene When AI Goes Wrong",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 9: Intervene When AI Goes Wrong (Lines 861-870)",
        "scenario": "An electrical components distributor delegates a multi-stage circuit load optimization problem. The standard fast model repeatedly produces inconsistent mathematical balances across complex load distributions. According to Concept 9, how should the distributor execute the 'Escalate' move?",
        "options": {
            "A": "Activate extended thinking or select a stronger model, or break the job into smaller checked steps.",
            "B": "Submit the identical prompt repeatedly until sampling randomness produces a mathematically coherent balance.",
            "C": "Increase the output length constraint and command the fast model to sound more authoritative.",
            "D": "Paste raw electrical engineering textbook chapters directly into the conversational chat window."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 9: When 'It cannot do a step at the level the job needs', the move is 'Escalate: turn on thinking, or a stronger model if your plan has one, and run it again. On a free plan the stronger model may not be there. Then the escalate move is to make the job smaller: one step at a time, each one checked.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because brute-force re-prompting without changing model level or structure is futile.",
            "distractor_C": "Option C is incorrect because lengthening outputs and asking for an authoritative tone promotes convincing hallucinations.",
            "distractor_D": "Option D is incorrect because flooding the chat with textbook chapters does not solve underlying computational reasoning limits."
        }
    },
    {
        "id": 32,
        "subtopic": "Concept 9: Intervene When AI Goes Wrong",
        "domain": "Domain 7: Troubleshooting and Optimization",
        "grounding": "Concept 9: Intervene When AI Goes Wrong (Lines 878-884)",
        "scenario": "An estate planning paralegal issues a corrective prompt to fix a misstated statutory probate threshold in an AI-generated client guidance memo. The assistant replies: 'I have corrected the probate threshold in the document.' What verification step must the paralegal take before accepting this claim?",
        "options": {
            "A": "Inspect the actual figure inside the deliverable itself rather than relying on the conversational assertion.",
            "B": "Accept the conversational reply as proof of compliance, as modern models track correction states accurately.",
            "C": "Ask the model to confirm on a scale of 1 to 10 how confident it feels regarding the applied correction.",
            "D": "Request an automated diff report from the assistant to compare the two generation instances."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 9: 'Did AI do what you asked, or say it had? \"I have corrected the table\" is a sentence. Look at the table... Check the one thing you corrected, in the result, not in AI's description of the result. A claimed fix that did not happen is the failure this step exists to catch.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because conversational assertions of compliance are frequently ungrounded.",
            "distractor_C": "Option C is incorrect because asking a model for its self-assessed numerical confidence produces meaningless synthetic affirmations.",
            "distractor_D": "Option D is incorrect because requesting a diff report still relies on generated text rather than inspecting the actual final artifact."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 10: Concept 10 - Verification & Accountability (Domain 2 / 6)
    # ----------------------------------------------------
    {
        "id": 33,
        "subtopic": "Concept 10: Verify & Accountability",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 10: Verify Before You Accept (Lines 917-930)",
        "scenario": "A structural steel estimator receives an AI-compiled supplier bid comparison. The estimator applies the formal four-step verification sequence defined in Concept 10. What is the correct chronological sequence of these operational verification steps?",
        "options": {
            "A": "Identify the critical claims, Trace each to its source, Challenge potential errors, and Decide on disposition.",
            "B": "Trace all citations, Identify missing links, Decide on model upgrade, and Challenge vendor assumptions.",
            "C": "Challenge the calculations, Identify alternative models, Trace API logs, and Decide on prompt revisions.",
            "D": "Identify model latency, Challenge token consumption, Trace server endpoints, and Decide on batch scheduling."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 10: 'Verification is four steps inside the Verify step of the loop. The four steps are Identify, Trace, Challenge, Decide. In plain words: pick the claims that matter, follow each one to its source, ask how it could be wrong, and choose what to do.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because it scrambles the order; you cannot trace before identifying what claims matter.",
            "distractor_C": "Option C is incorrect because it misorders the sequence and introduces out-of-scope technical engineering concepts.",
            "distractor_D": "Option D is incorrect because latency, token consumption, and server endpoints are infrastructure metrics, not verification steps."
        }
    },
    {
        "id": 34,
        "subtopic": "Concept 10: Verify & Accountability",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 10: Verify Before You Accept (Lines 923-925)",
        "scenario": "A pension scheme administrator evaluates an AI-generated calculation of surviving spouse annuity benefits. The administrator considers whether this output must undergo exhaustive manual source tracing. Which of the four review thresholds mandates this audit?",
        "options": {
            "A": "Crossing any single threshold among Stakes, Reversibility, Audience, or Regulatory exposure triggers the audit.",
            "B": "An audit is mandated only when all four review thresholds are simultaneously breached by the deliverable.",
            "C": "Auditing is required only if the output is addressed to an external audience exceeding one thousand recipients.",
            "D": "Auditing is mandated only if the pension calculation involved currency conversions across foreign jurisdictions."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 10: 'Four review thresholds that push a result onto the must-check list. Stakes: what a mistake costs. Reversibility: whether it can be undone. Audience: who sees it... Regulatory exposure: whether the data or the field is regulated. One threshold crossed is enough.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because crossing even one threshold is explicitly sufficient to mandate verification.",
            "distractor_C": "Option C is incorrect because audience risk is not defined by an arbitrary 1,000-recipient cutoff; external client exposure of any size qualifies.",
            "distractor_D": "Option D is incorrect because regulatory and financial stakes trigger the threshold regardless of whether foreign exchange is involved."
        }
    },
    {
        "id": 35,
        "subtopic": "Concept 10: Verify & Accountability",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 10: Verify Before You Accept (Lines 927-928)",
        "scenario": "A public health compliance inspector executes the 'Challenge' verification step on an AI report detailing commercial water filtration standards. The inspector discovers that a secondary industry blog from last month contradicts a five-year-old primary environmental agency standard. How does the curriculum resolve this discrepancy?",
        "options": {
            "A": "The primary source usually governs, unless it is outdated compared to active verified regulatory updates.",
            "B": "The secondary source always takes precedence because search engines rank recent blog posts higher.",
            "C": "The assistant should be instructed to synthesize an intermediate compromise standard between the two.",
            "D": "The discrepancy confirms that both sources are invalid and must be discarded from the health audit."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 10: 'When two credible sources disagree, the primary one usually wins, unless it is the older one.' The inspector must challenge both the authority and the temporal validity of the sources.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because search engine ranking is irrelevant to regulatory validity, and secondary blogs are prone to error.",
            "distractor_C": "Option C is incorrect because hallucinating an ungrounded compromise standard in health compliance creates severe safety liabilities.",
            "distractor_D": "Option D is incorrect because discrepancies require investigation and primary source tracing, not automatic wholesale dismissal."
        }
    },
    {
        "id": 36,
        "subtopic": "Concept 10: Verify & Accountability",
        "domain": "Domain 2: Output Evaluation and Validation",
        "grounding": "Concept 10: Verify Before You Accept (Lines 931-932)",
        "scenario": "A chemical transport compliance officer has issued three consecutive corrective prompts to refine an AI-drafted hazardous materials transport manifest. Each prompt iteration produces diminishing improvements and introduces subtle new inconsistencies. What decision must the officer make?",
        "options": {
            "A": "Reject the output, take the job back, and reassign the manifest review to a qualified human specialist.",
            "B": "Submit a fourth corrective prompt containing threatening language to enforce stricter model attention.",
            "C": "Accept the manifest as conditionally compliant, appending a disclaimer regarding AI drafting tools.",
            "D": "Switch to an incognito browser window and run the exact same brief through an unauthenticated session."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 10: 'Reject has a second form that people miss. You have corrected the same result three times, and each round improves it less than the last. That is a sign about the job, not about your prompts. Another round earns less than the one before, and the next move is a person who knows the field, not a better message.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because emotional or aggressive prompting is ineffective and does not solve structural capability limits.",
            "distractor_C": "Option C is incorrect because disclaimers do not eliminate legal liability or protect hazardous chemical transit safety.",
            "distractor_D": "Option D is incorrect because switching to incognito does not alter model capability or resolve diminishing prompt returns."
        }
    },
    {
        "id": 37,
        "subtopic": "Concept 10: Verify & Accountability",
        "domain": "Domain 6: Governance, Risk, and Responsible Use",
        "grounding": "Concept 10: Verify Before You Accept (Lines 933-938)",
        "scenario": "A chief financial controller reviews an AI-generated quarterly corporate tax provision schedule prior to filing. An external auditor later discovers a material computational misstatement in the deferred tax assets. The controller claims the error was an autonomous model failure. How does the governance doctrine assess liability?",
        "options": {
            "A": "Accountability is strictly non-transferable; audit-critical financial calculations must be human-verified.",
            "B": "Liability is split equally between the corporate controller and the AI foundational model provider.",
            "C": "The model provider assumes primary legal liability if the prompt included explicit verification instructions.",
            "D": "Regulatory penalties are waived if the corporate enterprise utilized a commercial paid subscription tier."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 10: 'AI doing the work does not transfer accountability to AI. The name on the result is yours... Four things that never go out without a person: Final client deliverables. Audit-critical or financially material calculations. Anything involving regulated, confidential, or highly sensitive data. Public or legal communications where a misstatement carries lasting consequences.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because AI vendors disclaim operational liability, and accountability remains 100% with the human operator.",
            "distractor_C": "Option C is incorrect because prompt wording does not transfer statutory corporate tax filing liability to software vendors.",
            "distractor_D": "Option D is incorrect because commercial subscription agreements explicitly state that users are responsible for output validation."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 11: Concept 11 - Tool-Agnostic Portability (Domain 3)
    # ----------------------------------------------------
    {
        "id": 38,
        "subtopic": "Concept 11: Same Job, Different AI",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 11: Same Job, Different AI (Lines 983-988)",
        "scenario": "A regional retail operations director transfers a six-line Delegation Brief from ChatGPT to Claude without making a single textual alteration, and both assistants execute the inventory reconciliation successfully. Why was this brief portable across competing platforms?",
        "options": {
            "A": "The brief specified the operational job and acceptance constraints rather than vendor-specific interface buttons.",
            "B": "Both platforms share an identical underlying open-source model architecture and training dataset.",
            "C": "The brief utilized standardized XML metadata tags recognized by all commercial browser assistants.",
            "D": "The retail director configured automated API cross-compilation middleware prior to pasting the text."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 11: 'The brief traveled because it describes the job, not the tool. Nothing in your six lines names a button. The buttons differ between assistants, and their names change every few months. The discipline does not.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because ChatGPT (OpenAI) and Claude (Anthropic) have distinct, proprietary architectures and training regimes.",
            "distractor_C": "Option C is incorrect because the six-line brief uses plain conversational English labels, not standardized XML tags.",
            "distractor_D": "Option D is incorrect because the exercise uses standard browser chat interfaces without external API middleware."
        }
    },
    {
        "id": 39,
        "subtopic": "Concept 11: Same Job, Different AI",
        "domain": "Domain 3: Product and Model Selection",
        "grounding": "Concept 11: Same Job, Different AI (Lines 983-988, 1003-1004)",
        "scenario": "A clinical trial document coordinator executes an identical study protocol summary brief across two different AI assistants. Assistant A adheres strictly to the authority boundary while Assistant B exceeds its authority by inferring unstated patient exclusion criteria. What valid conclusion should the coordinator record in the Delegation Record?",
        "options": {
            "A": "Record specific empirical observations regarding how the two runs performed on that day, avoiding permanent rankings.",
            "B": "Conclude definitively that Assistant A is permanently superior to Assistant B for all future clinical trial workflows.",
            "C": "Determine that Assistant B should be banned permanently from all enterprise research without further testing.",
            "D": "Assume that Assistant A must have accessed an external clinical trials registry database via an unlogged connector."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per Concept 11: 'What you wrote down is a record of two runs on one day. It is not a ranking of two assistants. Models change too fast for a ranking made today to be true next month, and this course never asks you to make one... Write both runs into your Delegation Record... as observations about this run. Not as a verdict about either assistant.'",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because models are continuously updated, making permanent vendor rankings brittle and unscientific.",
            "distractor_C": "Option C is incorrect because single-run variance does not justify permanent institutional banning without systematic evaluation.",
            "distractor_D": "Option D is incorrect because assuming unlogged external connector access is an unsubstantiated speculation."
        }
    },

    # ----------------------------------------------------
    # Sub-Topic 12: Governance Loop - The Delegation Loop & 10-80-10 Rule (Domain 4)
    # ----------------------------------------------------
    {
        "id": 40,
        "subtopic": "The Delegation Loop & 10-80-10 Governance",
        "domain": "Domain 4: Workflow Integration and Solution Design",
        "grounding": "The Delegation Loop & Thesis (Lines 453-468, 1225-1227)",
        "scenario": "A managing partner at a regional logistics consultancy is training junior associates on the operational governance of generative AI workflows. The partner outlines the 10-80-10 Rule of delegation. According to this governing doctrine, which phases of the Delegation Loop must remain under exclusive human ownership?",
        "options": {
            "A": "Humans own both ends: Define and Delegate at inception, and Verify and Accept at completion.",
            "B": "Humans own only the middle operational execution: Observe and Intervene while AI defines task scope.",
            "C": "Humans own only the final Accept step, delegating Define, Delegate, Observe, and Verify entirely to AI.",
            "D": "Humans own Define and Intervene, while AI autonomously delegates tasks to sub-agents and accepts outputs."
        },
        "correct": "A",
        "explanation": {
            "correct_rationale": "Option A is uniquely accurate per the foundational doctrine in Part 2 and the Thesis: 'AI owns the middle. You own both ends: Define and Delegate at the start, Verify and Accept at the end. AI can help you with any of the four. It cannot take them, because what the job is and whether the result is fit for use are decisions you answer for.' The 10-80-10 rule allocates 10% human intent definition, 80% machine execution, and 10% human verification and acceptance.",
            "distractor_A": "N/A (Correct Option)",
            "distractor_B": "Option B is incorrect because AI executes the middle (routine work), while humans supervise and own the defining and accepting ends.",
            "distractor_C": "Option C is incorrect because delegating Define and Verify entirely to AI violates the core boundary; intent and verification cannot be abdicated.",
            "distractor_D": "Option D is incorrect because AI must never be granted autonomous authority to accept its own outputs or define enterprise intent."
        }
    }
]

def generate_json():
    print(f"Generating questions.json with {len(QUESTIONS)} questions...")
    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(QUESTIONS, f, indent=2, ensure_ascii=False)
    print("✓ questions.json successfully generated.")

def generate_finalmcqs_md():
    print("Generating finalmcqs.md...")
    md_lines = []
    md_lines.append("# Panaversity PCAO-F & Anthropic CCAO-F Certification Exam Guide")
    md_lines.append("## Chapter: Just Delegate It — Scenario-Based Exam Bank")
    md_lines.append(f"**Total Questions:** {len(QUESTIONS)} Items | **Cut Score:** 720 / 1,000 (72%)\n")
    md_lines.append("---\n")
    
    # Part 1: Questions Only
    md_lines.append("## PART 1: QUESTIONS ONLY (SPOILER-FREE EXAM SIMULATION)\n")
    for q in QUESTIONS:
        md_lines.append(f"### Question {q['id']}")
        md_lines.append(f"*{q['domain']} | {q['subtopic']}*\n")
        md_lines.append(f"{q['scenario']}\n")
        for opt_key in ["A", "B", "C", "D"]:
            md_lines.append(f"- **{opt_key})** {q['options'][opt_key]}")
        md_lines.append("\n" + "-"*40 + "\n")
        
    # Part 2: Answer Key & Comprehensive Explanations
    md_lines.append("\n## PART 2: ANSWER KEY & PSYCHOMETRIC DISSECTIONS\n")
    for q in QUESTIONS:
        md_lines.append(f"### Question {q['id']} — Evaluation & Analysis")
        md_lines.append(f"- **Target Domain:** {q['domain']}")
        md_lines.append(f"- **Sub-Topic Grounding:** {q['subtopic']} ({q['grounding']})")
        md_lines.append(f"- **Correct Answer:** **Option {q['correct']}**\n")
        md_lines.append(f"#### Psychometric Rationale & Source Grounding")
        md_lines.append(f"{q['explanation']['correct_rationale']}\n")
        md_lines.append(f"#### Distractor Analysis & Operational Traps")
        for opt_key in ["A", "B", "C", "D"]:
            if opt_key == q['correct']:
                continue
            key_name = f"distractor_{opt_key}"
            md_lines.append(f"- **Option {opt_key} Flaw:** {q['explanation'][key_name]}")
        md_lines.append("\n" + "="*50 + "\n")
        
    with open("finalmcqs.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print("✓ finalmcqs.md successfully generated.")

def generate_quiz_html():
    print("Generating quiz.html...")
    quiz_data_json = json.dumps(QUESTIONS, ensure_ascii=False)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PCAO-F & CCAO-F Exam Simulator: Just Delegate It</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #090d16;
      --card-bg: rgba(18, 25, 42, 0.85);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-border-active: rgba(99, 102, 241, 0.4);
      --primary: #6366f1;
      --primary-hover: #4f46e5;
      --primary-glow: rgba(99, 102, 241, 0.25);
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --correct: #10b981;
      --correct-bg: rgba(16, 185, 129, 0.12);
      --correct-border: rgba(16, 185, 129, 0.4);
      --incorrect: #ef4444;
      --incorrect-bg: rgba(239, 68, 68, 0.12);
      --incorrect-border: rgba(239, 68, 68, 0.4);
      --badge-bg: rgba(99, 102, 241, 0.15);
      --badge-text: #a5b4fc;
      --font-main: 'Outfit', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-main);
      background-color: var(--bg-dark);
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(16, 185, 129, 0.08) 0%, transparent 40%);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 30px 20px;
    }}

    .container {{
      width: 100%;
      max-width: 860px;
      margin: 0 auto;
    }}

    header {{
      text-align: center;
      margin-bottom: 28px;
    }}

    .cert-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 9999px;
      background: var(--badge-bg);
      border: 1px solid rgba(99, 102, 241, 0.3);
      color: var(--badge-text);
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 12px;
    }}

    h1 {{
      font-size: 2.1rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
    }}

    /* Progress & Tracker */
    .progress-bar-container {{
      background: rgba(255, 255, 255, 0.05);
      border-radius: 9999px;
      height: 8px;
      width: 100%;
      overflow: hidden;
      margin-bottom: 24px;
      border: 1px solid rgba(255, 255, 255, 0.06);
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--primary) 0%, #818cf8 100%);
      width: 0%;
      transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .meta-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      font-size: 0.875rem;
      color: var(--text-dim);
    }}

    .meta-domain {{
      color: #38bdf8;
      font-weight: 500;
      background: rgba(56, 189, 248, 0.1);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.2);
    }}

    /* Card styling */
    .card {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 32px;
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
      margin-bottom: 24px;
      transition: all 0.3s ease;
    }}

    .scenario-text {{
      font-size: 1.12rem;
      line-height: 1.65;
      color: var(--text-main);
      font-weight: 400;
      margin-bottom: 28px;
    }}

    .options-grid {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 28px;
    }}

    .option-btn {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 16px 20px;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      color: var(--text-main);
      font-family: var(--font-main);
      font-size: 0.98rem;
      line-height: 1.5;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      position: relative;
    }}

    .option-btn:hover:not(.locked) {{
      background: rgba(99, 102, 241, 0.08);
      border-color: var(--card-border-active);
      transform: translateY(-1px);
    }}

    .option-btn.selected {{
      background: rgba(99, 102, 241, 0.15);
      border-color: var(--primary);
      box-shadow: 0 0 0 1px var(--primary);
    }}

    .option-letter {{
      font-family: var(--font-mono);
      font-weight: 600;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
      border-radius: 6px;
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
      transition: all 0.2s;
    }}

    .option-btn.selected .option-letter {{
      background: var(--primary);
      color: #fff;
    }}

    /* State styles after confirmation */
    .option-btn.correct-choice {{
      background: var(--correct-bg) !important;
      border-color: var(--correct-border) !important;
      box-shadow: 0 0 0 1px var(--correct) !important;
    }}
    .option-btn.correct-choice .option-letter {{
      background: var(--correct) !important;
      color: #fff !important;
    }}

    .option-btn.incorrect-choice {{
      background: var(--incorrect-bg) !important;
      border-color: var(--incorrect-border) !important;
      box-shadow: 0 0 0 1px var(--incorrect) !important;
    }}
    .option-btn.incorrect-choice .option-letter {{
      background: var(--incorrect) !important;
      color: #fff !important;
    }}

    .action-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }}

    .btn {{
      padding: 13px 26px;
      border-radius: 10px;
      font-size: 0.95rem;
      font-weight: 600;
      font-family: var(--font-main);
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: none;
    }}

    .btn-primary {{
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 4px 14px var(--primary-glow);
    }}
    .btn-primary:hover:not(:disabled) {{
      background: var(--primary-hover);
      transform: translateY(-1px);
    }}
    .btn-primary:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
      box-shadow: none;
    }}

    .btn-next {{
      background: #ffffff;
      color: #0f172a;
    }}
    .btn-next:hover {{
      background: #f1f5f9;
      transform: translateY(-1px);
    }}

    /* Rationale unfold card */
    .rationale-card {{
      margin-top: 24px;
      padding: 22px;
      background: rgba(15, 23, 42, 0.95);
      border-radius: 12px;
      border-left: 4px solid var(--primary);
      border-top: 1px solid var(--card-border);
      border-right: 1px solid var(--card-border);
      border-bottom: 1px solid var(--card-border);
      display: none;
      animation: fadeIn 0.3s ease;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .rationale-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .rationale-text {{
      font-size: 0.94rem;
      line-height: 1.6;
      color: #cbd5e1;
      margin-bottom: 14px;
    }}

    .distractor-header {{
      font-size: 0.85rem;
      font-weight: 600;
      color: #94a3b8;
      text-transform: uppercase;
      margin-top: 12px;
      margin-bottom: 8px;
    }}

    .distractor-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 0.88rem;
      color: #94a3b8;
      line-height: 1.5;
    }}

    .distractor-list li strong {{
      color: #f87171;
    }}

    /* Results Dashboard */
    .results-card {{
      display: none;
      text-align: center;
      padding: 40px 32px;
    }}

    .score-circle {{
      width: 140px;
      height: 140px;
      border-radius: 50%;
      margin: 0 auto 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 2.2rem;
      font-weight: 700;
      border: 4px solid var(--primary);
      box-shadow: 0 0 30px var(--primary-glow);
    }}

    .score-circle.pass {{
      border-color: var(--correct);
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.3);
      color: var(--correct);
    }}
    .score-circle.fail {{
      border-color: var(--incorrect);
      box-shadow: 0 0 30px rgba(239, 68, 68, 0.3);
      color: var(--incorrect);
    }}

    .score-label {{
      font-size: 0.8rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-top: 2px;
    }}

    .status-banner {{
      display: inline-block;
      padding: 8px 20px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 24px;
    }}
    .status-pass {{
      background: var(--correct-bg);
      color: var(--correct);
      border: 1px solid var(--correct-border);
    }}
    .status-fail {{
      background: var(--incorrect-bg);
      color: var(--incorrect);
      border: 1px solid var(--incorrect-border);
    }}

    .domain-breakdown {{
      margin-top: 32px;
      text-align: left;
    }}

    .domain-item {{
      margin-bottom: 16px;
    }}

    .domain-title-row {{
      display: flex;
      justify-content: space-between;
      font-size: 0.875rem;
      margin-bottom: 6px;
      color: var(--text-main);
    }}

    .domain-bar {{
      background: rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      height: 7px;
      overflow: hidden;
    }}

    .domain-bar-fill {{
      height: 100%;
      background: var(--primary);
      border-radius: 6px;
    }}

    .reset-btn {{
      margin-top: 32px;
    }}
  </style>
</head>
<body>

  <div class="container">
    <header>
      <div class="cert-badge">Panaversity PCAO-F &bull; Anthropic CCAO-F</div>
      <h1>Just Delegate It: Exam Simulator</h1>
      <p class="subtitle">Official Scenario-Based Practice Exam &bull; Cut Score: 720 / 1,000 (72%)</p>
    </header>

    <div class="progress-bar-container">
      <div class="progress-bar-fill" id="progressFill"></div>
    </div>

    <!-- Active Question View -->
    <div id="quizContainer">
      <div class="meta-row">
        <span id="questionCounter">Question 1 of 40</span>
        <span class="meta-domain" id="domainBadge">Domain 1: Prompting and Task Execution</span>
      </div>

      <div class="card">
        <div class="scenario-text" id="scenarioText">Scenario loading...</div>

        <div class="options-grid" id="optionsGrid">
          <!-- Dynamic options will be injected here -->
        </div>

        <div class="action-row">
          <div id="statusIndicator" style="font-size: 0.9rem; font-weight: 500;"></div>
          <button class="btn btn-primary" id="confirmBtn" disabled>Confirm Answer</button>
          <button class="btn btn-next" id="nextBtn" style="display: none;">Next Question &rarr;</button>
        </div>

        <!-- Feedback & Explanations -->
        <div class="rationale-card" id="rationaleCard">
          <div class="rationale-title" id="rationaleHeader">Psychometric Rationale &amp; Grounding</div>
          <div class="rationale-text" id="rationaleBody"></div>
          
          <div class="distractor-header">Distractor Analysis</div>
          <ul class="distractor-list" id="distractorList"></ul>
        </div>
      </div>
    </div>

    <!-- Results Dashboard View -->
    <div class="card results-card" id="resultsContainer">
      <h2>Examination Assessment Complete</h2>
      <p style="color: var(--text-muted); margin-bottom: 28px;">Official Panaversity Associate Foundations Benchmark</p>

      <div class="score-circle" id="scoreCircle">
        <span id="scaledScore">0</span>
        <span class="score-label">Scale Score</span>
      </div>

      <div id="statusBanner" class="status-banner">STATUS</div>

      <p id="scoreSummaryText" style="font-size: 1.05rem; line-height: 1.6; color: var(--text-muted); max-width: 600px; margin: 0 auto;"></p>

      <div class="domain-breakdown" id="domainBreakdown">
        <h3 style="font-size: 1.1rem; margin-bottom: 16px; border-bottom: 1px solid var(--card-border); padding-bottom: 8px;">Domain Performance Breakdown</h3>
        <div id="domainBarsList"></div>
      </div>

      <button class="btn btn-primary reset-btn" id="restartBtn">Retake Full Examination</button>
    </div>

  </div>

  <script>
    const questions = {quiz_data_json};
    let currentIndex = 0;
    let selectedOption = null;
    let userAnswers = []; // stores {{ index, selected, isCorrect }}

    // DOM references
    const progressFill = document.getElementById('progressFill');
    const questionCounter = document.getElementById('questionCounter');
    const domainBadge = document.getElementById('domainBadge');
    const scenarioText = document.getElementById('scenarioText');
    const optionsGrid = document.getElementById('optionsGrid');
    const confirmBtn = document.getElementById('confirmBtn');
    const nextBtn = document.getElementById('nextBtn');
    const statusIndicator = document.getElementById('statusIndicator');
    const rationaleCard = document.getElementById('rationaleCard');
    const rationaleBody = document.getElementById('rationaleBody');
    const distractorList = document.getElementById('distractorList');
    const quizContainer = document.getElementById('quizContainer');
    const resultsContainer = document.getElementById('resultsContainer');

    function renderQuestion(idx) {{
      const q = questions[idx];
      selectedOption = null;
      confirmBtn.disabled = true;
      confirmBtn.style.display = 'inline-flex';
      nextBtn.style.display = 'none';
      statusIndicator.textContent = '';
      rationaleCard.style.display = 'none';

      // Update counters & headers
      questionCounter.textContent = `Question ${{idx + 1}} of ${{questions.length}}`;
      domainBadge.textContent = q.domain;
      scenarioText.textContent = q.scenario;
      progressFill.style.width = `${{((idx) / questions.length) * 100}}%`;

      // Build options
      optionsGrid.innerHTML = '';
      const letters = ['A', 'B', 'C', 'D'];
      letters.forEach(letter => {{
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.id = `optBtn_${{letter}}`;
        btn.innerHTML = `
          <div class="option-letter">${{letter}}</div>
          <div style="flex-grow: 1;">${{q.options[letter]}}</div>
        `;
        btn.addEventListener('click', () => selectOption(letter));
        optionsGrid.appendChild(btn);
      }});
    }}

    function selectOption(letter) {{
      if (confirmBtn.style.display === 'none') return; // already confirmed
      selectedOption = letter;
      document.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
      document.getElementById(`optBtn_${{letter}}`).classList.add('selected');
      confirmBtn.disabled = false;
    }}

    function confirmAnswer() {{
      if (!selectedOption) return;
      const q = questions[currentIndex];
      const isCorrect = (selectedOption === q.correct);

      userAnswers.push({{
        index: currentIndex,
        domain: q.domain,
        selected: selectedOption,
        correct: q.correct,
        isCorrect: isCorrect
      }});

      // Lock buttons & display feedback
      document.querySelectorAll('.option-btn').forEach(btn => btn.classList.add('locked'));
      const chosenBtn = document.getElementById(`optBtn_${{selectedOption}}`);
      const correctBtn = document.getElementById(`optBtn_${{q.correct}}`);

      if (isCorrect) {{
        chosenBtn.classList.add('correct-choice');
        statusIndicator.innerHTML = '<span style="color: var(--correct); font-weight:600;">&#10003; Correct Answer</span>';
      }} else {{
        chosenBtn.classList.add('incorrect-choice');
        correctBtn.classList.add('correct-choice');
        statusIndicator.innerHTML = '<span style="color: var(--incorrect); font-weight:600;">&#10007; Incorrect</span>';
      }}

      // Populate rationale
      rationaleBody.innerHTML = `<strong>Grounding:</strong> ${{q.grounding}}<br><br>${{q.explanation.correct_rationale}}`;
      distractorList.innerHTML = '';
      ['A', 'B', 'C', 'D'].forEach(letter => {{
        if (letter !== q.correct) {{
          const li = document.createElement('li');
          li.innerHTML = `<strong>Option ${{letter}} Flaw:</strong> ${{q.explanation['distractor_' + letter]}}`;
          distractorList.appendChild(li);
        }}
      }});
      rationaleCard.style.display = 'block';

      // Toggle action buttons
      confirmBtn.style.display = 'none';
      nextBtn.style.display = 'inline-flex';
      nextBtn.focus();
    }}

    function nextQuestion() {{
      currentIndex++;
      if (currentIndex < questions.length) {{
        renderQuestion(currentIndex);
      }} else {{
        showResults();
      }}
    }}

    function showResults() {{
      progressFill.style.width = '100%';
      quizContainer.style.display = 'none';
      resultsContainer.style.display = 'block';

      const total = questions.length;
      const correctCount = userAnswers.filter(a => a.isCorrect).length;
      const percentage = Math.round((correctCount / total) * 100);
      const scaledScore = Math.round((correctCount / total) * 1000);
      const isPass = (scaledScore >= 720);

      const scoreCircle = document.getElementById('scoreCircle');
      const scaledScoreElem = document.getElementById('scaledScore');
      const statusBanner = document.getElementById('statusBanner');
      const scoreSummaryText = document.getElementById('scoreSummaryText');

      scaledScoreElem.textContent = scaledScore;
      if (isPass) {{
        scoreCircle.className = 'score-circle pass';
        statusBanner.className = 'status-banner status-pass';
        statusBanner.textContent = `PASS - CREDENTIAL CANDIDATE ELIGIBLE (${{scaledScore}} / 1,000)`;
        scoreSummaryText.innerHTML = `Congratulations! You scored <strong>${{correctCount}} out of ${{total}}</strong> (${{percentage}}%). Your performance exceeds the official certification cut score standard of 720 points (72.0%).`;
      }} else {{
        scoreCircle.className = 'score-circle fail';
        statusBanner.className = 'status-banner status-fail';
        statusBanner.textContent = `DID NOT PASS - REQUIRES REMEDIATION (${{scaledScore}} / 1,000)`;
        scoreSummaryText.innerHTML = `You scored <strong>${{correctCount}} out of ${{total}}</strong> (${{percentage}}%). A minimum scaled score of 720 / 1,000 (72.0%) is required to earn the Foundations credential. Review the domain breakdown below.`;
      }}

      // Calculate Domain Breakdown
      const domainStats = {{}};
      userAnswers.forEach(ans => {{
        if (!domainStats[ans.domain]) {{
          domainStats[ans.domain] = {{ total: 0, correct: 0 }};
        }}
        domainStats[ans.domain].total++;
        if (ans.isCorrect) domainStats[ans.domain].correct++;
      }});

      const domainBarsList = document.getElementById('domainBarsList');
      domainBarsList.innerHTML = '';
      for (const [dom, stats] of Object.entries(domainStats)) {{
        const domPercent = Math.round((stats.correct / stats.total) * 100);
        const div = document.createElement('div');
        div.className = 'domain-item';
        div.innerHTML = `
          <div class="domain-title-row">
            <span>${{dom}}</span>
            <strong>${{stats.correct}}/${{stats.total}} (${{domPercent}}%)</strong>
          </div>
          <div class="domain-bar">
            <div class="domain-bar-fill" style="width: ${{domPercent}}%; background: ${{domPercent >= 72 ? 'var(--correct)' : 'var(--primary)'}};"></div>
          </div>
        `;
        domainBarsList.appendChild(div);
      }}
    }}

    // Event listeners
    confirmBtn.addEventListener('click', confirmAnswer);
    nextBtn.addEventListener('click', nextQuestion);
    document.getElementById('restartBtn').addEventListener('click', () => {{
      currentIndex = 0;
      userAnswers = [];
      resultsContainer.style.display = 'none';
      quizContainer.style.display = 'block';
      renderQuestion(0);
    }});

    // Initialize
    renderQuestion(0);
  </script>
</body>
</html>
"""
    with open("quiz.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✓ quiz.html successfully generated.")

def generate_pdf_html():
    """Generates a dedicated print-optimized HTML file and renders it to PDF via Playwright."""
    print("Generating print_guide.html...")
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Panaversity PCAO-F & Anthropic CCAO-F Study Guide: Just Delegate It</title>
<style>
  @page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {{
      content: counter(page);
      font-size: 9pt;
      font-family: Arial, sans-serif;
      color: #64748b;
    }}
  }}

  body {{
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 10pt;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }}

  .header-cover {{
    text-align: center;
    border-bottom: 2px solid #334155;
    padding-bottom: 20px;
    margin-bottom: 30px;
  }}

  .badge {{
    display: inline-block;
    padding: 4px 12px;
    background: #e0e7ff;
    color: #3730a3;
    border-radius: 4px;
    font-size: 8.5pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
  }}

  h1 {{
    font-size: 20pt;
    margin: 8px 0;
    color: #0f172a;
  }}

  .meta {{
    font-size: 10pt;
    color: #64748b;
  }}

  .section-divider {{
    page-break-before: always;
    border-bottom: 2px solid #0f172a;
    padding-bottom: 8px;
    margin-bottom: 20px;
  }}

  .section-title {{
    font-size: 15pt;
    font-weight: bold;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }}

  .q-item {{
    page-break-inside: avoid;
    margin-bottom: 18px;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 12px 14px;
    background: #f8fafc;
  }}

  .q-head {{
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    color: #475569;
    font-weight: bold;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 4px;
    margin-bottom: 8px;
  }}

  .q-num {{
    color: #4338ca;
  }}

  .q-scenario {{
    font-size: 9.8pt;
    line-height: 1.5;
    color: #0f172a;
    margin-bottom: 10px;
  }}

  .options-table {{
    width: 100%;
    border-collapse: collapse;
  }}

  .opt-row {{
    font-size: 9.2pt;
    line-height: 1.4;
    padding: 3px 0;
    vertical-align: top;
  }}

  .opt-letter {{
    font-weight: bold;
    width: 25px;
    color: #334155;
  }}

  /* Explanations section */
  .exp-item {{
    page-break-inside: avoid;
    margin-bottom: 22px;
    border-left: 3.5px solid #4338ca;
    padding-left: 12px;
  }}

  .exp-head {{
    font-size: 10pt;
    font-weight: bold;
    color: #0f172a;
    margin-bottom: 4px;
  }}

  .exp-correct {{
    color: #047857;
    font-weight: bold;
  }}

  .exp-grounding {{
    font-size: 8.5pt;
    color: #64748b;
    margin-bottom: 6px;
  }}

  .exp-body {{
    font-size: 9pt;
    line-height: 1.45;
    color: #1e293b;
    margin-bottom: 6px;
  }}

  .flaw-list {{
    font-size: 8.5pt;
    line-height: 1.4;
    color: #475569;
    padding-left: 16px;
    margin-top: 4px;
  }}

  .flaw-list li {{
    margin-bottom: 3px;
  }}
</style>
</head>
<body>

  <div class="header-cover">
    <div class="badge">Official Exam Blueprint Preparation Guide</div>
    <h1>Panaversity PCAO-F & Anthropic CCAO-F</h1>
    <div style="font-size: 13pt; font-weight: 600; color: #4338ca; margin-bottom: 6px;">
      Chapter: Just Delegate It — A Crash Course
    </div>
    <div class="meta">
      40 High-Yield Scenario-Based Examination Items &bull; Cut Score: 720 / 1,000 (72%) &bull; Psychometric Standard
    </div>
  </div>

  <div style="margin-bottom: 24px; padding: 10px 14px; background: #eef2ff; border-radius: 6px; font-size: 9pt; border-left: 3px solid #6366f1;">
    <strong>Examination Instructions:</strong> Part 1 contains 40 numbered scenario-based items with zero answers or spoilers. Complete Part 1 under simulated exam conditions (target time: 60 minutes). Then consult Part 2 for the official answer keys, direct source citations, and comprehensive distractor dissections.
  </div>

  <!-- PART 1: QUESTIONS ONLY -->
  <div class="section-title">PART 1: QUESTIONS ONLY (SPOILER-FREE SIMULATION)</div>
  <div style="margin-bottom: 16px;"></div>
"""

    for q in QUESTIONS:
        html += f"""
  <div class="q-item">
    <div class="q-head">
      <span class="q-num">QUESTION {q['id']}</span>
      <span>{q['domain']} &bull; {q['subtopic']}</span>
    </div>
    <div class="q-scenario">{q['scenario']}</div>
    <table class="options-table">
      <tr class="opt-row"><td class="opt-letter">A)</td><td>{q['options']['A']}</td></tr>
      <tr class="opt-row"><td class="opt-letter">B)</td><td>{q['options']['B']}</td></tr>
      <tr class="opt-row"><td class="opt-letter">C)</td><td>{q['options']['C']}</td></tr>
      <tr class="opt-row"><td class="opt-letter">D)</td><td>{q['options']['D']}</td></tr>
    </table>
  </div>
"""

    # PART 2: ANSWER KEY & EXPLANATIONS
    html += """
  <div class="section-divider"></div>
  <div class="section-title">PART 2: ANSWER KEY & COMPREHENSIVE RATIONALES</div>
  <div style="margin-bottom: 16px; font-size: 9pt; color: #64748b;">
    Exhaustive psychometric explanations detailing why the correct option is uniquely accurate per the chapter source text, and why each alternate distractor is operationally flawed.
  </div>
"""

    for q in QUESTIONS:
        html += f"""
  <div class="exp-item">
    <div class="exp-head">
      Question {q['id']}: <span class="exp-correct">Correct Option {q['correct']}</span>
    </div>
    <div class="exp-grounding">
      <strong>Target Domain:</strong> {q['domain']} | <strong>Grounding:</strong> {q['grounding']}
    </div>
    <div class="exp-body">
      <strong>Source Grounding &amp; Rationale:</strong> {q['explanation']['correct_rationale']}
    </div>
    <div style="font-size: 8.5pt; font-weight: bold; color: #475569; margin-top: 4px;">Distractor Dissection:</div>
    <ul class="flaw-list">
"""
        for opt_key in ["A", "B", "C", "D"]:
            if opt_key == q['correct']:
                continue
            flaw_text = q['explanation'][f"distractor_{opt_key}"]
            html += f"      <li><strong>Option {opt_key} Flaw:</strong> {flaw_text}</li>\n"

        html += """    </ul>
  </div>
"""

    html += """
</body>
</html>
"""

    with open("print_guide.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ print_guide.html successfully generated.")

def render_pdf_with_playwright():
    print("Rendering PDF using Playwright (msedge channel)...")
    from playwright.sync_api import sync_playwright
    
    html_path = os.path.abspath("print_guide.html")
    pdf_path = os.path.abspath("PCAO-F_Just_Delegate_It_Exam_Guide.pdf")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page()
        page.goto(f"file:///{html_path}")
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "15mm", "bottom": "15mm", "left": "12mm", "right": "12mm"}
        )
        browser.close()
        
    print(f"✓ PDF successfully generated at: {pdf_path}")
    print(f"  File size: {os.path.getsize(pdf_path):,} bytes")

if __name__ == "__main__":
    generate_json()
    generate_finalmcqs_md()
    generate_quiz_html()
    generate_pdf_html()
    render_pdf_with_playwright()
    print("\nAll deliverables generated successfully!")
