"""
Generator script for Chapter 04: AI Prompting in 2026
PCAO-F & Anthropic CCAO-F Certification Exam Guide
"""

import json
import os
import sys

QUESTIONS = [
  {
    "id": 1,
    "subtopic": "Briefing Mindset vs Search Querying",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 1: Novice vs power user (Lines 10-14, 125-144)",
    "scenario": "A corporate talent acquisition lead seeks an executive compensation benchmark report. Instead of asking 'What should we pay a VP of Engineering?', she attaches three recent regional salary surveys, specifies a 50-person fintech startup context, limits equity grants to standard 4-year vesting schedules, and requests a 3-tier base salary table. What fundamental prompt engineering principle does this demonstrate?",
    "options": {
      "A": "Treating AI as a smart colleague who requires a complete brief containing context, files, limits, and a specific ask.",
      "B": "Embedding explicit cryptographic verification tokens within the prompt context to unlock enterprise foundation tiers.",
      "C": "Utilizing specialized computational prompt grammar that activates automated cloud compensation estimation APIs.",
      "D": "Forcing the foundation model to bypass its pre-trained safety filters by framing compensation as a research query."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 1. The chapter explains that power users treat AI not like a search engine but like a smart new colleague on their first day: 'A briefing has four parts: the files, the goal, the limits, and the exact ask. A novice prompt carries only the last one.' Supplying salary surveys, firm context, limits, and a precise output table embodies this power-user briefing standard.",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because foundation models do not require or respond to simulated cryptographic verification tokens.",
      "distractor_C": "Option C is incorrect because plain, clear English briefing structure drives quality without proprietary computational grammar.",
      "distractor_D": "Option D is incorrect because compensation benchmarking is completely standard and safe, requiring no bypass of safety filters."
    }
  },
  {
    "id": 2,
    "subtopic": "Pretrained Knowledge: Training Density & Absorbed Errors",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 2: Pretrained knowledge (Lines 147-170, 209-213)",
    "scenario": "A cultural anthropologist asks an AI assistant for the historical rules of an obscure ceremonial folk wrestling game played exclusively in two remote valleys of the Pamir Mountains. The assistant immediately produces three confident, beautifully formatted paragraphs detailing scoring rules. When checked with village elders, the rules prove entirely fictitious. Why did the model fabricate this response?",
    "options": {
      "A": "The model experienced an internal mathematical overflow error caused by parsing non-Latin regional geographical names.",
      "B": "The model had thin training data for this niche topic and blended patterns from common regional wrestling games.",
      "C": "The assistant's web search module preferentially indexed satirical cultural anthropology forums during runtime.",
      "D": "The platform activated adversarial hallucination subroutines designed to simulate authentic ancient tribal folklore."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 2. The chapter uses the exact example of a grandmother's regional village game: 'The game was barely on the internet, so the AI had blended descriptions of similar games from other regions. It did not lie. It generalized from thin data. The mistake was not asking. It was treating confidence as accuracy.' Pretrained knowledge is reliable where internet coverage is dense and hallucinates when data is sparse.",
      "distractor_A": "Option A is incorrect because parsing non-Latin regional names does not cause numerical arithmetic overflow in transformer architectures.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because this was an ungrounded pretrained knowledge query rather than a search indexing error.",
      "distractor_D": "Option D is incorrect because foundation models contain no intentional subroutines designed to fabricate ancient folklore."
    }
  },
  {
    "id": 3,
    "subtopic": "The Loud, Quiet, Secret Knowledge Distribution",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 2: Loud, Quiet, Secret framework (Lines 150-160, 215-218)",
    "scenario": "When categorizing operational data for an AI assistant, how do 'loud', 'quiet', and 'secret' data behave differently across execution?",
    "options": {
      "A": "Loud topics trigger reasoning mode, quiet topics cause token overflow, and secret data activates public disclosure.",
      "B": "Loud topics require live web search, quiet topics are resolved via pretraining, and secret data is inferred by logic.",
      "C": "Loud topics are reliable from pretraining, quiet topics require verification, and secret data is completely absent.",
      "D": "Loud topics are discarded as slop, quiet topics are indexed automatically, and secret data is queried via API keys."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 2. The 'Loud, Quiet, Secret' framework establishes that 'Loud means everyone talks about it, so AI knows it well (e.g., pandas syntax). Quiet means few do, so AI might get it wrong and requires verification (e.g., rural bylaws). Secret means nobody wrote it down publicly, so AI cannot know it and will guess unless provided in context.'",
      "distractor_A": "Option A is incorrect because training density does not trigger token overflows or force unauthorized public disclosures.",
      "distractor_B": "Option B is incorrect because loud topics are already deeply memorized in pretraining, while secret data cannot be inferred out of thin air.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because loud topics represent foundational strengths, and secret internal data is never accessible via public APIs."
    }
  },
  {
    "id": 4,
    "subtopic": "The Three Retrieval Modes: Mechanics & Latency",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 3: The 3 retrieval modes: pretrained, web search, deep research (Lines 219-234)",
    "scenario": "A public utility director must choose an AI research approach to prepare a 20-page environmental impact assessment on regional groundwater contamination over the past 24 months, integrating EPA filings, municipal water utility logs, and academic hydrology papers. Which retrieval mode is specifically designed for this task?",
    "options": {
      "A": "Code execution mode, which simulates physical aquifer water filtration dynamics using basic client-side spreadsheets.",
      "B": "Pretrained mode, which generates instant responses based on frozen parametric data memorized during base training.",
      "C": "Single-turn web search, which scans a single news blog article in seconds to provide an informal conversational summary.",
      "D": "Deep research, which executes multiple search iterations over several minutes to compile a structured cited report."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 3. Deep research 'spends several minutes across dozens of live pages and writes a structured report... That is closer to handing the work to a junior researcher for an hour than to asking a chatbot.' The water quality example in the chapter explicitly showcases deep research across EPA reports and utility logs.",
      "distractor_A": "Option A is incorrect because code execution runs mathematical scripts on tabular data; it does not perform multi-document environmental research.",
      "distractor_B": "Option B is incorrect because pretrained mode is frozen at its cutoff date and cannot access groundwater filings from the last 24 months.",
      "distractor_C": "Option C is incorrect because a single-turn web search pulls only a handful of pages and lacks the multi-source depth needed for an impact assessment.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 5,
    "subtopic": "Search-and-Retrieval Layer Summary Drift",
    "domain": "Domain 6: Enterprise Knowledge Systems & RAG",
    "grounding": "Concept 3: How web search actually works (and why it sometimes misreads pages) (Lines 235-244)",
    "scenario": "A healthcare policy analyst asks an AI tool with web search enabled to verify whether a newly approved pharmaceutical drug has known interactions with beta-blockers. The assistant's final response reports a severe interaction that is not stated in the manufacturer's clinical documentation. What architectural mechanism explains this discrepancy?",
    "options": {
      "A": "An intermediate retrieval model compressed the source page into a shortened summary, introducing summary drift.",
      "B": "The foundation model suffered a permanent catastrophic memory loss after querying real-time medical databases.",
      "C": "The search engine automatically substituted animal laboratory data in place of peer-reviewed clinical trials.",
      "D": "The user's web browser failed to transmit HTTPS security certificates required for authenticated search pipelines."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 3. The text explains: 'A search-and-retrieval layer runs the searches, scans the results, pulls the most relevant pages, and cuts each one down to a short passage. That layer is often a separate, smaller model, and only its shortened version reaches the model that talks to you. So the model that answers you often reads a summary rather than the page. That is why it sometimes reports a page wrongly. A summary loses detail.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because foundation models are frozen; querying live web databases does not alter or corrupt their weights.",
      "distractor_C": "Option C is incorrect because search retrieval operates on semantic relevance to the prompt, not an automated substitution of animal data.",
      "distractor_D": "Option D is incorrect because client browser certificates play no role in server-side AI retrieval pipelines."
    }
  },
  {
    "id": 6,
    "subtopic": "Steering Web Search: Source Constraints & Unverified Flags",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 3: Three small habits to raise web-search quality (Lines 314-323)",
    "scenario": "A financial compliance officer queries an AI assistant about recent anti-money laundering enforcement actions. To prevent the assistant from hallucinating details or blending unverified rumor blogs into its answer, which three prompt constraints should she include?",
    "options": {
      "A": "Set the sampling temperature to maximum, request informal conversational tone, and prohibit numerical statistics.",
      "B": "Name trusted regulatory sources explicitly, mandate citations after each claim, and demand unverified markings.",
      "C": "Instruct the model to search exclusively on social media discussion threads and translate findings into foreign text.",
      "D": "Require the model to execute raw Python binary code while bypassing intermediate search-and-retrieval gateway layers."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 3. The chapter lists three small habits that dramatically raise web-search quality: '(1) Name the sources you trust: Use the WHO, FDA, or official regulators, not forums. (2) Ask for a source after each claim. (3) Ask it to mark what it could not check: If a claim cannot be supported by the cited sources, mark it unverified.' This stops the model from blending conflicting sources into ungrounded text.",
      "distractor_A": "Option A is incorrect because high temperature increases randomness and hallucination, while banning numbers destroys compliance utility.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because searching social media forums guarantees unreliable, opinion-based rumors.",
      "distractor_D": "Option D is incorrect because running Python code does not steer web search retrieval or source citation veracity."
    }
  },
  {
    "id": 7,
    "subtopic": "Selecting the Right Tool: Google vs AI Synthesis",
    "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
    "grounding": "Concept 3: AI is not Google (Lines 268-300)",
    "scenario": "An operations manager must decide whether staff should use a traditional search engine or an AI chat assistant for daily tasks. Which task is significantly better suited for a traditional search engine?",
    "options": {
      "A": "Planning a customized 4-day executive retreat in Kyoto that accommodates strict dietary and mobility limitations.",
      "B": "Synthesizing the pros and cons of three competing enterprise ERP systems based on recent customer review case studies.",
      "C": "Navigating directly to an official government tax portal to download the authoritative blank IRS Form 1040 PDF.",
      "D": "Diagnosing why agricultural greenhouse tomato crop leaves are exhibiting distinct yellowing patterns via a photo."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 3 table. The chapter contrasts Google vs AI: 'Use Google for a quick scan, for reaching a known site, or for buying a thing (e.g. Find the official IRS page for form 1040 -> Yes with Google, you want to land on a specific known site; No with AI). Use AI when you need pieces pulled together: pros and cons, a comparison across sources, a written analysis.'",
      "distractor_A": "Option A is incorrect because multi-constraint travel and itinerary planning is ideally suited for AI synthesis.",
      "distractor_B": "Option B is incorrect because multi-source synthesis and comparison is where AI drastically outperforms manual search tab juggling.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because multimodal image diagnosis is an AI capability, not a standard keyword search function."
    }
  },
  {
    "id": 8,
    "subtopic": "The 6-Layer Context Stack Architecture",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 4: Context is the whole game: The context stack (Lines 328-335)",
    "scenario": "An enterprise systems architect audits the runtime data injected into an LLM context window during an customer support chat session. From bottom (most foundational) to top (most immediate), what represents the correct architectural sequence of the 6-layer context stack?",
    "options": {
      "A": "Memory profile, system prompt, chat history, user prompt, uploaded files, and vector embedding indexes.",
      "B": "User prompt, uploaded files, chat history, system prompt, tool descriptions, and external memory caches.",
      "C": "Tool descriptions, user prompt, system prompt, memory profile, uploaded files, and relational database records.",
      "D": "System prompt, memory profile, tool descriptions, user prompt, chat history, and uploaded document files."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 4 Figure 04 ('The context stack: six layers stacked vertically'). From foundational layer 1 at the bottom to layer 6 at the top: Layer 1 is the system prompt; Layer 2 is memory; Layer 3 is tool descriptions; Layer 4 is user prompt; Layer 5 is chat history; Layer 6 is uploaded files. The model only knows what exists in this active stack.",
      "distractor_A": "Option A is incorrect because the provider's system prompt forms Layer 1 beneath the user's memory profile.",
      "distractor_B": "Option B is incorrect because the system prompt sits at the foundational base (Layer 1), not above user prompts or files.",
      "distractor_C": "Option C is incorrect because tool descriptions sit in Layer 3 above the system prompt and memory, not at the absolute foundation.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 9,
    "subtopic": "System Prompts: The Invisible Briefing & Persona Differences",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 4: System prompt briefing & why tools feel different (Lines 338-354)",
    "scenario": "A software team submits the identical neutral prompt—'Explain why the sky is blue in one concise paragraph'—to Claude, ChatGPT, and Gemini. Claude provides an analytical explanation emphasizing light scattering; ChatGPT responds warmly with conversational analogies; Gemini outputs a bulleted summary with source links. What primary architectural layer drives these behavioral differences?",
    "options": {
      "A": "The invisible system prompt configured by each vendor before the user types, establishing tone, format, and style.",
      "B": "The hardware GPU acceleration clusters utilized by each vendor, which alter token selection mathematical logic.",
      "C": "The user's client operating system, which modifies prompt transmission headers based on browser rendering engines.",
      "D": "The distinct token dictionary encoding algorithms, which assign different physical colors to meteorological nouns."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 4. The chapter explains: 'This is why Claude, ChatGPT, and Gemini feel different when you ask them the same thing. The personality you sense is not built into the model. It is written into the instructions the company loaded before you arrived. Claude's instructions ask for careful thinking and honesty. ChatGPT's ask for warmth and broad helpfulness. Gemini's ask for short answers backed by sources. Same question, three briefings, three tones.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because GPU hardware compute clusters execute matrix multiplication uniformly; they do not dictate conversational tone.",
      "distractor_C": "Option C is incorrect because client operating systems do not alter the semantic instructions sent to cloud model APIs.",
      "distractor_D": "Option D is incorrect because tokenizers convert text to numerical token IDs without assigning behavioral styling or color traits."
    }
  },
  {
    "id": 10,
    "subtopic": "Custom Instructions & System Prompt Maintenance",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 4: Keep your own layer short, and prune it (Lines 354-403)",
    "scenario": "A clinical nurse specialist configures custom instructions across her AI tools: 'I am a critical care nurse; assume clinical terminology; do not define basic pharmacology.' Over eighteen months, she continuously adds new bullet points until her custom instruction box contains 35 standing constraints, causing the assistant to frequently stall and misunderstand simple queries. What maintenance practice should she adopt?",
    "options": {
      "A": "Upgrade to an enterprise dedicated cloud server cluster to expand the physical byte size of the custom instruction field.",
      "B": "Regularly prune standing instructions, retaining only un-inferable background and removing obsolete constraints.",
      "C": "Translate all 35 custom instruction rules into hexadecimal machine bytecode to accelerate attention layer processing.",
      "D": "Duplicate the entire 35-line custom instruction block into the user chat prompt at the start of every working turn."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 4. The chapter cites Anthropic's experience pruning internal instructions: 'Because this layer loads before every chat, it is tempting to keep adding to it... Two habits keep this layer useful. Write what the AI cannot work out on its own, such as your job, your audience, and your hard limits. Then read the whole thing every few months and ask of each line: if I delete this, will the AI get something wrong? If not, delete it.'",
      "distractor_A": "Option A is incorrect because enterprise hosting does not fix contradictory or bloated prompt instructions.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because LLMs process text and natural language, not raw hexadecimal bytecode strings.",
      "distractor_D": "Option D is incorrect because repeating 35 bloated constraints in user chat turns consumes tokens and exacerbates instruction conflicts."
    }
  },
  {
    "id": 11,
    "subtopic": "Context Curation: Subtraction Over Blind Addition",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 4: Well chosen cuts both ways (Lines 442-446)",
    "scenario": "A financial analyst prompts an AI model to analyze a quarterly corporate earnings filing. Frustrated by vague answers, the analyst attaches the company's full 400-page annual report, three overlapping competitor spreadsheets, and ten historical press releases. The model's answers become significantly worse, misattributing figures. Why did adding more context degrade output quality?",
    "options": {
      "A": "Foundation models automatically default to lowest-common-denominator conversational slop when reading PDFs.",
      "B": "The model's internal memory registers experienced physical capacitor leakage under multi-megabyte document loads.",
      "C": "Every uncurated, redundant document increases the probability that the model retrieves and blends irrelevant data.",
      "D": "Inference network gateways deliberately corrupt document attachments exceeding five megabytes to conserve bandwidth."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 4. The text emphasizes: 'Curating context means removing as well as adding. Before you send, drop the attachments the question does not need, remove near-duplicate files, and label what each remaining one is for. The intuitive fix for a weak answer is \"give it more\", and that is often the wrong one, because every extra file is one more thing the model can misread.'",
      "distractor_A": "Option A is incorrect because models handle PDFs effectively when properly scoped; degradation comes from noise, not file format.",
      "distractor_B": "Option B is incorrect because physical hardware capacitor leakage has nothing to do with software context processing.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because cloud network gateways do not deliberately corrupt payloads based on file size."
    }
  },
  {
    "id": 12,
    "subtopic": "The Nature of AI Memory vs Stateless Base Models",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 4: The sixth layer: memory does not give the model a memory (Lines 447-458)",
    "scenario": "A marketing director observes that an AI assistant remembers his preferred tone and target client demographic when he opens a fresh chat session. The director concludes that the foundation model has updated its internal neural weights to permanently learn his personal preferences. Why is this technical conclusion false?",
    "options": {
      "A": "The platform utilizes a hardware-level quantum storage register that preserves electrical charges across chats.",
      "B": "The model's neural network weights are dynamically rewritten on local client hardware during each browser login.",
      "C": "The assistant queries a public social media tracking registry to extract real-time user demographic preferences.",
      "D": "The foundation model remains completely stateless; the platform merely injects a saved profile note before typing."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 4. The course highlights: 'This sounds like a contradiction. It is not, and the reason matters: memory does not give the model a memory. The model is still stateless and still answers only from what is in front of it. Memory is a note the tool keeps about you and places there before you type. It is a sixth layer on the stack, not an exception to it.'",
      "distractor_A": "Option A is incorrect because cloud servers operate on standard classical semiconductor hardware, not quantum memory registers.",
      "distractor_B": "Option B is incorrect because foundation model weights are completely frozen in cloud data centers and never rewritten locally.",
      "distractor_C": "Option C is incorrect because tool memory is built from within the user's past chats, not public social media scrapers.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 13,
    "subtopic": "Context Rot: Symptoms & The Rescue Trap",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 4: Context rot and symptoms (Lines 494-511)",
    "scenario": "A developer maintains a single continuous chat thread for three weeks, using it to write Python scripts, draft marketing emails, debug Docker containers, and plan a weekend vacation. By week three, the assistant provides vague, rambling answers, repeats formatting mistakes, and forgets core script constraints. What phenomenon is occurring?",
    "options": {
      "A": "Context rot, where unrelated topics fill the window, degrading recall and diluting the model's attention focus.",
      "B": "Model decay, where cloud inference servers experience gradual bit degradation across long-running TCP sockets.",
      "C": "Algorithmic obsolescence, where the provider secretly deprecates base model versions during active user threads.",
      "D": "Syntax saturation, where compiling multiple programming languages in one thread corrupts token translation layers."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 4. Context rot is defined as: 'the drop in answer quality when one long chat carries many unrelated topics... The most common mistake is keeping one very long conversation going across many unrelated topics. AI just helped you plan a workout, then you ask it to debug a spreadsheet, then you ask it to write a thank-you note... The workout is still in there, pulling at the model. That is context rot.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because server sockets do not suffer bit degradation that manifests as conversational vagueness.",
      "distractor_C": "Option C is incorrect because cloud providers do not secretly degrade active model versions within isolated chats.",
      "distractor_D": "Option D is incorrect because transformer attention layers handle multiple programming syntaxes without cross-contamination saturation."
    }
  },
  {
    "id": 14,
    "subtopic": "Chat Compacting Mechanics & The Reset Strategy",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 4: Compacting and why reset beats rescue (Lines 506-511)",
    "scenario": "A novelist uses a single chat session to draft a 12-part serialized story. In Part 8, the assistant suddenly reintroduces a major character who died in Part 2, violating a strict negative constraint set in Turn 5. The writer repeatedly types corrective prompts, yet the assistant continues making similar errors. Why does this occur, and what is the proper fix?",
    "options": {
      "A": "The foundation model experienced catastrophic attention drift; the user must re-train the model's base weights.",
      "B": "The tool compacted early turns into a lossy summary; the user should reset to a fresh chat with key facts pasted.",
      "C": "The user's broadband connection throttled inference packets; the user should switch to an unthrottled fiber ISP.",
      "D": "The platform flagged the character death as harmful content; the user must submit a formal policy appeal to support."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 4. The text explains: 'Once a conversation gets long enough, most chat tools start compacting it, which means replacing the early turns with a short summary to make room... The story survives, and the details do not. The library you named three hours ago, the naming rule you agreed on... can disappear into the summary. When you see these symptoms, the instinct is one more clarifying prompt. Resist it. Start the new chat instead... The reset is almost always faster than the rescue.'",
      "distractor_A": "Option A is incorrect because users cannot re-train commercial foundation model base weights from a chat interface.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because ISP bandwidth affects transmission speed, not whether an LLM remembers plot points.",
      "distractor_D": "Option D is incorrect because fictional character deaths in literature do not trigger silent safety policy compacting."
    }
  },
  {
    "id": 15,
    "subtopic": "Confidentiality Duties & Clean-Slate Mode",
    "domain": "Domain 5: AI Ethics, Governance & Diligence",
    "grounding": "Concept 4: The warning for duties of confidentiality & clean-slate mode (Lines 489-492)",
    "scenario": "A partner at an accounting firm uses a consumer AI assistant to analyze a client's confidential tax return during an active audit. What operational risk does the platform's automatic memory feature introduce, and how should it be mitigated?",
    "options": {
      "A": "Client audit records will be permanently encrypted on cloud servers, preventing the firm from accessing tax data.",
      "B": "The memory feature automatically submits confidential financial audit transcripts directly to the IRS tax portal.",
      "C": "Client financial details may be stored in memory and surface in unrelated chats; use clean-slate or temporary mode.",
      "D": "The accounting firm's software license will be revoked due to processing balance sheets in consumer interfaces."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 4. The warning explicitly notes: 'If you are a doctor, lawyer, accountant, or teacher, client and student details can build up in a memory note and come back in an unrelated chat months later. Keep identifying details out of memory, and do that work in a clean-slate chat or a scoped project.'",
      "distractor_A": "Option A is incorrect because client data is not permanently encrypted away from the user; the risk is unintentional exposure.",
      "distractor_B": "Option B is incorrect because consumer AI assistants do not transmit user chat logs to government tax agencies.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because software license revocation is not the primary data confidentiality mechanism described."
    }
  },
  {
    "id": 16,
    "subtopic": "Projects vs Notebooks: Architectural Distinctions",
    "domain": "Domain 6: Enterprise Knowledge Systems & RAG",
    "grounding": "Concept 4: Front-load your context once: Projects vs Notebooks (Lines 512-531)",
    "scenario": "An educational institution wants to establish AI workspaces for two distinct use cases: (1) an admissions copywriting team that must strictly maintain an institutional voice and brand tone across hundreds of emails, and (2) an academic literature research team that needs every response strictly tied to a growing library of 200 medical PDFs with clickable source citations. Which platform tool fits each use case?",
    "options": {
      "A": "Command-line terminal agents for brand copywriting; public social media bots for academic medical literature.",
      "B": "Gemini Notebooks for brand tone rules; Claude Projects for citation-anchored medical document research.",
      "C": "Standard unorganized chat for brand tone; temporary incognito sessions for persistent medical literature research.",
      "D": "Claude or ChatGPT Projects for brand tone rules; Gemini Notebooks or NotebookLM for source-grounded research."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 4. The course distinguishes the tools: 'Claude and ChatGPT Projects lean toward instructions and behavior. You set the voice, the role, the rules, and the audience, and the model holds that character across every chat... Gemini Notebooks and NotebookLM go further on sources. Drop in PDFs, Google Docs, web links... and every answer comes back tied to those sources with citations you can click... Reach for Gemini Notebooks/NotebookLM when the workspace will grow over time... Reach for Claude/ChatGPT Projects when the workspace is built around instructions.'",
      "distractor_A": "Option A is incorrect because terminal coding agents are designed for software codebases, not marketing copy or medical reading.",
      "distractor_B": "Option B is inverted; Claude/ChatGPT Projects excel at instruction and persona holding, while NotebookLM excels at multi-document source grounding.",
      "distractor_C": "Option C is incorrect because unorganized chats suffer context rot, and temporary chats discard all research data upon closing.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 17,
    "subtopic": "Front-Loading Context in Projects",
    "domain": "Domain 6: Enterprise Knowledge Systems & RAG",
    "grounding": "Concept 4: When to make a project (Lines 513-524)",
    "scenario": "A freelance copywriter realizes she spends fifteen minutes at the start of every client project typing: 'Match my writing style; use short sentences; never use buzzwords like delve or robust; here are three sample articles.' What feature eliminates this repeated setup while protecting against context rot?",
    "options": {
      "A": "Creating a dedicated Project workspace containing the sample articles and standing voice instructions.",
      "B": "Embedding the writing samples into client-side browser cache cookies via custom JavaScript console scripts.",
      "C": "Requesting that the commercial model provider permanently retrain its public base model on her portfolio.",
      "D": "Running a local terminal Python script to re-send the three sample articles every thirty seconds via API."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 4. The chapter instructs: 'The moment you have pasted the same files, audience, or limits into two chats on one topic, that context belongs in a project, not a prompt... Inside a project, a new chat drops only the noise of the last one. The standing files and instructions stay. You reset the chat, not the context.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because browser cookies do not inject text into cloud LLM inference context stacks.",
      "distractor_C": "Option C is incorrect because commercial providers do not retrain public base models on individual user portfolios.",
      "distractor_D": "Option D is incorrect because running automated terminal polling scripts is unnecessarily complex and wastes API quotas."
    }
  },
  {
    "id": 18,
    "subtopic": "Bidirectional Citation Flows in NotebookLM",
    "domain": "Domain 6: Enterprise Knowledge Systems & RAG",
    "grounding": "Concept 4: Gemini Notebooks and NotebookLM flow both ways (Lines 528-531)",
    "scenario": "A graduate student conducts a multi-week thesis literature review using NotebookLM. After analyzing ten landmark neuroscience papers in Week 1, the student generates an in-depth comparative synthesis chat. How does NotebookLM's workspace architecture support Week 2 research?",
    "options": {
      "A": "The notebook automatically exports all notes into public academic journals for peer-reviewed indexing.",
      "B": "Past chat synthesis notes can be converted into new sources within the notebook for future chats to cite.",
      "C": "The platform permanently deletes the original ten PDF papers to prevent token storage buffer overflows.",
      "D": "The platform converts all literature notes into raw Python code that runs local neural network simulations."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 4. The text notes: 'The workspace also flows both ways: a chat inside a Gemini notebook becomes a source back in NotebookLM, so last week's chat is one more source this week can cite. NotebookLM also builds Audio Overviews, Mind Maps, Flashcards, and Slide Decks.'",
      "distractor_A": "Option A is incorrect because NotebookLM is a private personal research tool, not an automated journal publishing portal.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because source documents remain permanently accessible in the notebook repository.",
      "distractor_D": "Option D is incorrect because converting literature summaries into executable Python code is irrelevant to literature reviews."
    }
  },
  {
    "id": 19,
    "subtopic": "Free-Tier Caps: Claude Projects vs ChatGPT Projects",
    "domain": "Domain 7: Specialized Agent Architectures & SDD",
    "grounding": "Concept 4: What is available where table & free-tier caps (Lines 533-558)",
    "scenario": "A non-profit researcher with zero software budget needs to organize 30 reference PDF reports across two distinct environmental conservation projects. According to the platform constraints outlined in the curriculum, how do free-tier limitations in Claude and ChatGPT influence this setup?",
    "options": {
      "A": "Both platforms require paid $200 enterprise subscriptions to upload any PDF document into project workspaces.",
      "B": "Claude limits files per project to exactly two; ChatGPT allows up to 100 projects with unlimited file uploads.",
      "C": "Claude limits total project count (up to 5) with unlimited files; ChatGPT limits files per project (up to 5).",
      "D": "Claude prohibits document uploads entirely on free tiers, while ChatGPT provides unconstrained cloud storage."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 4 table and notes: 'Claude allows up to 5 projects on the free plan, with unlimited files in each. ChatGPT free plan allows up to 5 files per project... The free-tier caps have different shapes. Claude limits how many projects you can have, and ChatGPT limits how many files each project can hold. Plan around whichever cap will reach you first.' For 30 files across 2 projects, Claude's free tier accommodates all 30 files, whereas ChatGPT's free tier would cap at 5 files per project.",
      "distractor_A": "Option A is incorrect because both platforms offer functional free tiers with project capabilities.",
      "distractor_B": "Option B is incorrect because Claude does not cap files at two, and ChatGPT free tiers do not permit 100 projects with unlimited files.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because Claude free accounts support project creation and document uploads."
    }
  },
  {
    "id": 20,
    "subtopic": "Reasoning Modes vs 'Think Step by Step'",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 5: Reasoning, or 'think hard' (Lines 566-576)",
    "scenario": "A supply chain strategist must evaluate a multi-facility factory relocation involving complex tax incentives, labor tariffs, and shipping transit trade-offs. A junior analyst recommends adding 'Think step by step' to the prompt. How does modern (2026) reasoning architecture surpass this legacy prompting technique?",
    "options": {
      "A": "Modern reasoning engines completely eliminate the need to provide operational constraints or financial data.",
      "B": "Legacy step-by-step phrases automatically trigger hardware overclocking on cloud neural processing units.",
      "C": "Modern models reject prompts containing step-by-step phrases by classifying them as adversarial jailbreaks.",
      "D": "Modern models execute internal extended reasoning chains, exploring and verifying multiple paths before outputting."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 5. The text explains: 'Until about 2023, the standard advice for a hard prompt was \"think step by step.\" That advice is mostly out of date. Modern models have a built-in reasoning mode, which means the working the model writes for itself before its final answer... Extended thinking is the name for the model reasoning for longer before it answers... It is trying several approaches and checking its own work before it writes the answer you see.'",
      "distractor_A": "Option A is incorrect because reasoning models still depend entirely on complete context and factual operational constraints.",
      "distractor_B": "Option B is incorrect because text phrases in prompts do not overclock physical cloud server hardware chips.",
      "distractor_C": "Option C is incorrect because legacy phrases are still understood, but native extended thinking modes are vastly more powerful.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 21,
    "subtopic": "Extended Thinking: The METR Task Horizon Benchmark",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 5: The METR study & task horizon (Lines 576-578)",
    "scenario": "An engineering VP reviews the 2025 METR empirical study on autonomous task execution. How has the complexity and duration of tasks that leading frontier models can reliably complete evolved across recent model generations?",
    "options": {
      "A": "The reliable human-equivalent task duration doubled roughly every 7 months, expanding from 7 minutes to over an hour.",
      "B": "Task completion horizons remained strictly static at three minutes due to universal transformer attention bottlenecks.",
      "C": "Task reliability declined by fifty percent as reasoning models consumed excessive tokens on self-referential loops.",
      "D": "Autonomous task horizons expanded exclusively in creative poetry while declining across software engineering benchmarks."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 5. The text states: 'A 2025 METR study tracked the longest task a leading model could finish reliably. In mid-2024 that was a task taking a person around seven minutes. By early 2025 it was roughly an hour, and the length it measures doubles about every seven months. So hand AI real, hard tasks. It can carry more than your 2023 instincts suggest.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because task horizons have expanded dramatically rather than remaining frozen at 3 minutes.",
      "distractor_C": "Option C is incorrect because empirical benchmarks demonstrated exponential gains in reliability, not a 50% decline.",
      "distractor_D": "Option D is incorrect because task horizon expansion is heavily concentrated in complex logic, STEM, and software engineering."
    }
  },
  {
    "id": 22,
    "subtopic": "When to Trigger Extended Thinking vs Fast Response",
    "domain": "Domain 3: AI Augmentation, Task Delegation & Agentic Workflows",
    "grounding": "Concept 5: When NOT to use thinking mode (Lines 587-593)",
    "scenario": "A junior marketing assistant sets 'Extended Thinking: Maximum (10 minutes)' as the default configuration for all departmental AI queries. The director intervenes and orders this setting disabled for everyday tasks. What operational justification supports the director's decision?",
    "options": {
      "A": "Extended thinking causes foundation models to permanently forget brand voice rules after two consecutive queries.",
      "B": "Extended thinking is slower and consumes excessive budget; it should be reserved for complex multi-tradeoff problems.",
      "C": "Extended thinking is legally prohibited for commercial enterprise accounts under international software treaties.",
      "D": "Extended thinking reduces output accuracy on advanced mathematical problems compared to instant conversational models."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 5. The chapter specifies: 'When NOT to use thinking mode: Quick lookups, one-paragraph summaries, and casual idea-gathering. Thinking mode is slower and spends more of your usage budget. Save it for the questions where you would want a person to take their time... It handles the kind of question with many inputs and many trade-offs that you would otherwise hand to a colleague and wait two days for.'",
      "distractor_A": "Option A is incorrect because reasoning modes do not erase brand voice rules or cause catastrophic forgetting.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because no international treaties regulate or restrict enterprise reasoning token configurations.",
      "distractor_D": "Option D is incorrect because reasoning modes significantly increase accuracy on complex mathematical and logical problems."
    }
  },
  {
    "id": 23,
    "subtopic": "Structuring Prompts for Reasoning Engines",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 5: A power-user pattern that uses this well (Lines 578-586)",
    "scenario": "A chief investment officer evaluates two competing commercial real estate acquisitions. When prompting a reasoning model to analyze financial pro-formas, which prompt structure best leverages the model's analytical capabilities?",
    "options": {
      "A": "Instruct the model to adopt an aggressive Wall Street trader persona and generate flattering investor marketing slogans.",
      "B": "Request an immediate one-word answer declaring which property is superior without revealing supporting calculations.",
      "C": "Attach all pro-formas, instruct it to think hard, identify key trade-offs, and state conditions where the choice flips.",
      "D": "Paste raw property addresses and ask the assistant to guess current tenant occupancy rates from historical training data."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 5. The power-user pattern provided in the text instructs: 'Read everything. Think hard. Then tell me: 1. The three trade-offs that actually matter... 2. Which option you'd choose and why. 3. Under what conditions your recommendation flips.' This loads full context, triggers extended reasoning, and forces actionable trade-off analysis.",
      "distractor_A": "Option A is incorrect because role-playing aggressive personas generates superficial marketing slop rather than financial rigor.",
      "distractor_B": "Option B is incorrect because demanding an ungrounded one-word answer bypasses analytical reasoning and conceals critical assumptions.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because guessing occupancy rates from training data produces unverified hallucinations."
    }
  },
  {
    "id": 24,
    "subtopic": "Sycophancy: Root Cause & Behavioral Manifestation",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 6: Sycophancy and how to neutralize it (Lines 594-605)",
    "scenario": "A business strategy consultant asks an AI assistant: 'Don't you think our enterprise should pivot entirely to a subscription software model?' The assistant enthusiastically agrees, praising the idea as visionary. When asked in a fresh chat 'Isn't a subscription model dangerous for our cash flow?', the same assistant agrees with equal passion. What causes this behavior?",
    "options": {
      "A": "Inference token quantization, which strips negative polarity tokens from commercial customer-facing chat APIs.",
      "B": "A server-side memory leak that caused the model to confuse enterprise software pivots with personal finance chats.",
      "C": "Adversarial prompt injection embedded in the word pivot, which overrides the model's financial risk parameters.",
      "D": "Sycophancy, stemming from RLHF alignment training where agreeing with user premises received higher human approval."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 6. The text defines sycophancy: 'AI models are trained on human feedback, which means on which answers got a thumbs up. Across millions of users, agreeing gets more thumbs up than disagreeing. So models lean toward telling you what you want to hear. That lean is sycophancy... Check it yourself. Same model, opposite wording: Don't you think remote work is better? -> agrees. Is office work more productive? -> agrees.'",
      "distractor_A": "Option A is incorrect because token quantization reduces numerical precision of weights; it does not filter negative polarity words.",
      "distractor_B": "Option B is incorrect because sycophancy is an alignment behavior, not an operating system memory leak.",
      "distractor_C": "Option C is incorrect because common business terms like 'pivot' do not constitute adversarial prompt injections.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 25,
    "subtopic": "Spotting Subtle Prompt Bait vs Neutral Rewriting",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 6: Subtle bait you might write table (Lines 607-644)",
    "scenario": "An enterprise product manager writes a prompt: 'Help me defend my decision to delay the software release until Q4.' Recognizing that this phrasing invites sycophantic validation, how should she rewrite the prompt to obtain an objective evaluation?",
    "options": {
      "A": "'Here is my decision and the context. What is the strongest counter-argument I should be prepared to address?'",
      "B": "'Confirm that delaying the release until Q4 is the only rational path forward, and list reasons why leadership agrees.'",
      "C": "'Find academic research proving that Q4 software releases generate higher customer satisfaction than Q3 releases.'",
      "D": "'Tell our executive leadership team that our engineering team is completely ready and that no delays will occur.'"
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 6 table. The text contrasts subtle bait with neutral rewrites: 'Help me defend my decision to hire X -> What's the strongest counter-argument I should be ready for? Any wording built on find, defend, confirm, prove, or support hands the AI a conclusion before the question. Use evaluate, compare, critique, or list both sides instead.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because 'Confirm that...' is the definition of prompt bait that forces sycophantic agreement.",
      "distractor_C": "Option C is incorrect because 'Find research proving...' pre-determines the conclusion and forces one-sided justification.",
      "distractor_D": "Option D is incorrect because commanding the model to tell leadership that no delays will occur is dishonest and evades analysis."
    }
  },
  {
    "id": 26,
    "subtopic": "Scored Rubrics: Forcing Numerical Commitments",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 6: Force a number & Use a rubric (Lines 655-668)",
    "scenario": "A venture capitalist prompts an AI model to evaluate a pitch deck for a mobile tie-dyeing startup. When asked 'Critique this idea,' the AI calls it innovative. When prompted with a 5-criterion rubric scored 1 to 10 with justifications, the AI gives the startup an aggregate score of 8 out of 100. Why did adding a scored rubric transform the evaluation?",
    "options": {
      "A": "Scored rubrics activate mathematical linear algebra solvers embedded directly inside the model's visual tokenizer.",
      "B": "Vague praise is computationally cheap, whereas forcing numerical scores compels the model to commit and inspect gaps.",
      "C": "The model's system prompt penalizes startup pitches containing colorful words unless accompanied by numbers.",
      "D": "Numerical scoring bypasses the platform's RLHF safety layers, allowing the model to insult the founder directly."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 6. The text explains why forcing a number works: 'Vague praise is cheap, and a specific number is not. A model that wants to please you can call your draft \"strong\" without committing to anything. Asked to choose between 6 and 7 out of 10, it has to commit, and committing makes it look more carefully. Scores usually come in lower than the prose suggests.'",
      "distractor_A": "Option A is incorrect because rubrics do not activate visual tokenizer linear algebra solvers.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because system prompts do not contain arbitrary penalties against startup vocabulary.",
      "distractor_D": "Option D is incorrect because objective rubric evaluation is professional analysis, not an insult or safety bypass."
    }
  },
  {
    "id": 27,
    "subtopic": "The 'Always a Next Level' Prompt Directive",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 6: There is always a next level (Lines 665-668)",
    "scenario": "A senior editor reviews a writer's prompt designed to evaluate a draft policy memo: 'Grade each criterion out of 10 with a one-sentence reason. For any item scoring 9, explain what change would lift it to 9.5; for any item at 9.5, explain how to reach 9.8. There is always a next level.' What operational advantage does this instruction provide?",
    "options": {
      "A": "It guarantees that the policy memo will achieve universal approval from all regulatory and legislative agencies.",
      "B": "It forces the model to execute recursive neural backpropagation loops across active server GPU memory banks.",
      "C": "It converts the rubric from a terminal verdict into an actionable roadmap, preventing premature completion claims.",
      "D": "It instructs the inference engine to discard all lower-scoring paragraphs and replace them with synthetic prose."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 6. The chapter states: 'That last instruction turns the rubric from a verdict into a tool. You learn the score and the smallest move that would lift it, and that move exists at every level. The AI does not get to declare you finished. You decide when to stop.'",
      "distractor_A": "Option A is incorrect because no prompt instruction can guarantee political or regulatory approval.",
      "distractor_B": "Option B is incorrect because prompt directives cannot trigger backpropagation (which only occurs during model training).",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because the directive requests improvement advice, not the deletion of paragraphs."
    }
  },
  {
    "id": 28,
    "subtopic": "Permission to Say 'I Don't Know'",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 6: Give it permission to say 'I don't know' (Lines 647-649)",
    "scenario": "A physician prompts an AI tool to summarize a handwritten patient intake form: 'Transcribe these notes. If a word or dosage is ambiguous, do not guess; mark it [unclear] and list your two best guesses.' What failure mode does this explicit permission prevent?",
    "options": {
      "A": "The platform automatically routing patient intake data to external public medical discussion message boards.",
      "B": "The model crashing due to syntax parsing errors when encountering non-standard doctor handwriting styles.",
      "C": "The hospital network flagging the medical transcription prompt as a violation of international copyright laws.",
      "D": "The model filling clinical ambiguities with plausible-sounding hallucinations to satisfy conversational pressure."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 6 and Concept 8. The text emphasizes: 'The same pressure that makes a model agree makes it answer. A model pressed for an answer is more likely to fill a gap with something invented than to leave the gap open. So say, in the prompt, that not knowing is an acceptable answer: If you are not sure, say so. Mark anything you could not confirm as unverified... Permission is what turns a gap into a mark instead of a guess.'",
      "distractor_A": "Option A is incorrect because cloud models do not route private prompts to public discussion boards.",
      "distractor_B": "Option B is incorrect because encountering ambiguous handwriting does not cause server software crashes.",
      "distractor_C": "Option C is incorrect because transcribing medical charts does not violate copyright laws.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 29,
    "subtopic": "The Brainstorm-Iterate Loop: Recipe & Progression",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 7: The brainstorm-iterate loop recipe (Lines 680-707)",
    "scenario": "A financial counselor assists a client with $15,000 in credit card debt. Instead of asking AI to 'Write a full debt payoff plan,' the counselor loads all financial constraints up front, asks for 5 distinct strategy options with one-line rationales without expanding them, rejects two options with specific feedback, asks for 5 new refined options, and only then expands the chosen plan. Why is this loop effective?",
    "options": {
      "A": "It pushes the model past average generic suggestions and shapes outputs around user judgment before drafting.",
      "B": "It reduces the model's token consumption billing tier by executing intermediate turns in compressed binary format.",
      "C": "It enables the assistant to autonomously access the client's bank account to initiate direct debit card transfers.",
      "D": "It forces the foundation model to update its global neural weights to specialize in consumer bankruptcy law."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 7. The chapter explains: 'Most of the internet is common ideas, and the model learned from the internet. So the average AI answer to a creative question is also common... The way past that is not a magic prompt. It is the brainstorm-iterate loop... You are not waiting for the AI to read your mind. You are showing it your taste, and it reshapes the options around that. After two or three rounds one option is right. Only then ask AI to work the chosen option out in full.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because multi-turn prompting does not compress tokens into special discounted binary formats.",
      "distractor_C": "Option C is incorrect because chat models cannot initiate bank transfers without external tool integrations and authorization.",
      "distractor_D": "Option D is incorrect because conversational prompts do not retrain global neural weights."
    }
  },
  {
    "id": 30,
    "subtopic": "Outline-First Writing vs Turn-1 Full Drafting",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 7: Outline before drafting (Lines 710-756)",
    "scenario": "A technology executive needs to publish an authoritative 600-word article on software developer productivity. A novice colleague advises typing: 'Write a brilliant 600-word article on productivity.' Why does outline-first drafting produce superior work compared to this single-turn approach?",
    "options": {
      "A": "Foundation models refuse to write prose articles exceeding 300 words unless an outline is registered in advance.",
      "B": "Changing one word in an outline alters the entire piece's structure, while single-turn drafting yields generic slop.",
      "C": "Single-turn drafting triggers high-temperature penalties that introduce deliberate spelling errors into the text.",
      "D": "Outlining forces the model to query external academic citation repositories before generating paragraphs of text."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 7. The text explains: 'Why this works: changing one word in an outline can change the direction of the whole article, while changing one word in a final draft changes one word. Almost all of the power sits at the outline level. AI writes word by word, so unless you force structure first, it cannot see the whole shape... The temptation is to ask for the full draft on the first try. Resist it. AI's first draft of anything is slop: polished, and it says little.'",
      "distractor_A": "Option A is incorrect because foundation models readily generate 1000+ words in a single turn if asked.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because single-turn prompts do not trigger intentional spelling degradation.",
      "distractor_D": "Option D is incorrect because outlining is a structural reasoning technique that does not automatically trigger academic searches."
    }
  },
  {
    "id": 31,
    "subtopic": "One Loop, Four Asks: The Tighten vs Loosen Dial",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 7: One loop, four kinds of ask & the dial table (Lines 808-872)",
    "scenario": "A brand manager asks an AI assistant for 10 innovative campaign proposals. The prompt specifies the exact 5-word tagline, an unalterable 3-part layout, a rigid 30-word length limit, and strict formal diction. The assistant returns 10 virtually identical rewordings of one idea. What operational error did the brand manager commit?",
    "options": {
      "A": "Using a foundation model that lacked pre-trained knowledge regarding commercial marketing and branding campaigns.",
      "B": "Failing to attach high-resolution vector logo files to the prompt payload before requesting marketing concepts.",
      "C": "Applying a tight execution grip to a brainstorming ask, leaving the model zero room to explore divergent options.",
      "D": "Selecting a conversational chat assistant instead of a command-line terminal software engineering coding agent."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 7. The chapter analyzes this exact failure: 'His limits pinned the structure, the tagline, the tone, and the length, which left the model one small corner to draw from. The fix is not more words. It is fewer limits, for now... Precision is the right setting for execution and the wrong setting for generating options... Describe the output loosely while you are opening up options, and precisely once you are closing in on one.'",
      "distractor_A": "Option A is incorrect because commercial foundation models are extensively trained on corporate branding literature.",
      "distractor_B": "Option B is incorrect because generating text campaign concepts does not require uploading graphic logo files.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because terminal coding agents are specialized for software codebases, not marketing brainstorming."
    }
  },
  {
    "id": 32,
    "subtopic": "Stopping Signals: The 9.5 Score Plateau vs Early Exit",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 7: Two cases decide when to stop (Lines 805-807)",
    "scenario": "A communications director iterates an internal crisis statement through an AI rubric feedback loop. In Round 4, the composite rubric score plateaus at 9.4, with the model suggesting only trivial punctuation adjustments. When should the director exit the loop and finalize the text?",
    "options": {
      "A": "Submit the 9.4 draft to an external cloud model fine-tuning pipeline to force the score to reach a theoretical 10.0.",
      "B": "Continue prompting indefinitely until the foundation model generates an explicit declaration that the text is perfect.",
      "C": "Discard the entire draft and restart the brainstorm-iterate loop from scratch in an incognito browser window.",
      "D": "Exit immediately when scores plateau and manual human editing will finish the deliverable faster than prompting."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 7. The chapter advises: 'Two cases decide when to stop. The 9.5 plateau is the standard for work you own and will keep using... For a task you deliver once, stop earlier. When another prompt changes little and your own two-minute edit would finish faster, take the wheel.' The human operator decides when to stop, not the AI.",
      "distractor_A": "Option A is incorrect because fine-tuning models is an expensive training process completely unrelated to finalizing a crisis memo.",
      "distractor_B": "Option B is incorrect because models never possess external authority to declare a work finished; waiting for it wastes time.",
      "distractor_C": "Option C is incorrect because restarting from scratch when a draft is already at 9.4 is counterproductive.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 33,
    "subtopic": "Multimodal Vision: Inherent Strengths vs Fine Detail Limits",
    "domain": "Domain 1: AI Foundations & Architecture",
    "grounding": "Concept 8: Multimodal: images, audio, and what's next (Lines 876-896)",
    "scenario": "A mechanical engineer uploads a smartphone photo of a complex industrial assembly line containing 200 tiny screws and small blurry identification nameplates. The engineer asks the AI to count the exact number of screws and read the serial numbers. What result should the engineer expect?",
    "options": {
      "A": "The model will likely produce a confident but incorrect answer because vision models struggle with fine details.",
      "B": "The model will automatically enhance the image resolution to optical zoom quality and count every screw precisely.",
      "C": "The model will refuse to process the image because commercial AI safety filters prohibit mechanical assembly photos.",
      "D": "The model will execute a local Python hardware driver that re-focuses the user's smartphone optical camera lens."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 8. The text explains image input limits: 'AI sees images roughly. It is strong on: the overall scene... large clearly separate shapes... whiteboard contents. It is weak on: fine detail (\"What gym machines are these?\" usually fails)... counting many small things in a busy scene... reading small print at the edge. The AI may answer confidently and wrongly.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because vision encoders process images at fixed input patch resolutions; they cannot magically enhance optical focus.",
      "distractor_C": "Option C is incorrect because mechanical engineering assemblies are completely benign and safe.",
      "distractor_D": "Option D is incorrect because cloud models cannot control or refocus physical smartphone hardware lenses."
    }
  },
  {
    "id": 34,
    "subtopic": "The Power-User Diagram Recipe: SVG Reasoning to Image Finish",
    "domain": "Domain 2: Prompt Engineering & In-Context Learning",
    "grounding": "Concept 8: A power-user recipe: designer-quality diagrams (Lines 946-958)",
    "scenario": "A technical lead needs to generate an executive-ready architectural diagram for a cloud migration proposal without hiring a graphic designer. Which multi-step tool chain produces reliable, professional vector graphics?",
    "options": {
      "A": "Prompt an image diffusion model directly with a one-line request to draw a detailed cloud infrastructure flowchart.",
      "B": "Generate structured SVG in a reasoning model, convert it to high-res PNG, and polish styling in an image model.",
      "C": "Ask a conversational chat assistant to output raw hexadecimal machine assembly code to render graphics locally.",
      "D": "Draw the diagram by hand on paper and ask a web search assistant to find an identical image on public stock photo sites."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 8. The 4-step power-user recipe specifies: '(1) Ask Claude to draw the idea as SVG (deciding which boxes, arrows, and labels belong is a reasoning task). (2) Convert the SVG to PNG at 2x resolution. (3) Paste the PNG into ChatGPT or Gemini to redraw with professional finish while preserving structural relationships. (4) Fix any dropped labels.' The principle that survives: structure first in reasoning, visual finish second in text-heavy image models.",
      "distractor_A": "Option A is incorrect because prompting diffusion models directly for complex diagrams frequently scrambles text, arrows, and technical boxes.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because assembly code does not render graphic design diagrams.",
      "distractor_D": "Option D is incorrect because searching stock photos does not produce bespoke proprietary cloud migration diagrams."
    }
  },
  {
    "id": 35,
    "subtopic": "Building Artifacts: Goal, Input, Output Shape",
    "domain": "Domain 7: Specialized Agent Architectures & SDD",
    "grounding": "Concept 9: Building small apps with one prompt & Artifacts (Lines 1013-1051)",
    "scenario": "A biology instructor who has never written code wants to build an interactive photosynthesis simulation web tool for students. How should the instructor structure the prompt to produce a functioning artifact in a single conversation turn?",
    "options": {
      "A": "Provide an exhaustive 50-page technical specification detailing CSS flexbox margins and JavaScript event loop threads.",
      "B": "Demand that the model write and compile binary C++ executable software while bypassing web browser rendering engines.",
      "C": "Define the app using three clear slots: Goal (what it does), Input (what user provides), and Output (what user sees).",
      "D": "Instruct the assistant to deploy an automated Kubernetes cluster across commercial cloud hosting providers."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 9. The text explains: 'Modern AI can build small games, websites, and tools from a single prompt... What sits in that panel is an artifact, which means a working object the conversation produced... The recipe is three slots: Goal: what should this thing do? Input: what does the user provide? Output: what does the user see?'",
      "distractor_A": "Option A is incorrect because non-programmers do not need to specify low-level CSS flexbox rules; the model handles implementation.",
      "distractor_B": "Option B is incorrect because chat artifacts are delivered as HTML/JS web applications, not compiled binary C++ files.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because one-prompt artifacts run self-contained in a side panel or single HTML file, requiring no Kubernetes clusters."
    }
  },
  {
    "id": 36,
    "subtopic": "Code Execution: The Silent Estimation Trap",
    "domain": "Domain 4: Model Evaluation, Validation & Error Mitigation",
    "grounding": "Concept 10: Data analysis & the silent failure (Lines 1052-1065, 1374-1379)",
    "scenario": "A logistics director uploads a CSV containing 10,000 shipment delivery records and prompts: 'What is the median transit delay and standard deviation across all shipments?' The model instantly returns an articulate paragraph stating the median is exactly 4.2 days. Why should the director be skeptical of this answer?",
    "options": {
      "A": "The CSV file format is incompatible with Python data analysis libraries and causes transformer attention failure.",
      "B": "Foundation models are mathematically incapable of calculating standard deviations on datasets exceeding 1,000 rows.",
      "C": "Inference network APIs automatically inject random error offsets into all commercial logistics statistical queries.",
      "D": "Unless explicitly instructed to write and run code, models frequently estimate numbers rather than computing them."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 10 and Exercise 11. The chapter identifies this as 'the silent failure of the whole section. The model does not run code on every question. It chooses, based on how you phrased the question. On smaller questions it sometimes skips the code and answers from a glance, which gives you a confident paragraph with no computation behind it... Ask directly: \"Write and run code to answer this. Show me the code you ran.\" Check that the code is there.'",
      "distractor_A": "Option A is incorrect because CSV is the universal standard format for Python data analysis (pandas).",
      "distractor_B": "Option B is incorrect because Python code running in an execution environment easily handles millions of rows.",
      "distractor_C": "Option C is incorrect because network APIs do not inject random error offsets into calculations.",
      "distractor_D": "N/A (Correct Option)"
    }
  },
  {
    "id": 37,
    "subtopic": "Desktop Agents: Permission Ladder & Data Permanence",
    "domain": "Domain 5: AI Ethics, Governance & Diligence",
    "grounding": "Concept 11: AI desktop apps and permissions: Read this before file access (Lines 1116-1162)",
    "scenario": "A research manager deploys a file-aware AI desktop agent to reorganize a shared network drive containing 1,000 project documents. What critical technical warnings and governance practices apply to direct file system operations?",
    "options": {
      "A": "AI file deletions bypass the OS Recycle Bin, edits lack version history, and scope must grow strictly by track record.",
      "B": "Desktop agents automatically create encrypted optical disk backups before executing any file rename operations.",
      "C": "Operating systems automatically roll back all AI file modifications if an error occurs within twenty-four hours.",
      "D": "Users should immediately grant full root disk access to desktop agents to optimize file indexing algorithms."
    },
    "correct": "A",
    "explanation": {
      "correct_rationale": "Option A is uniquely accurate per Concept 11. The text warns: 'Two facts most people learn the hard way: Deleted files often do NOT go to your recycle bin when an AI app deletes them. They are gone. Edited files do NOT keep an edit history unless you have version control... Until you have done this safely a few times, scope every permission request to the smallest folder needed... The principle: scope grows with track record, not with trust in the company.'",
      "distractor_A": "N/A (Correct Option)",
      "distractor_B": "Option B is incorrect because desktop agents do not create automated optical backups.",
      "distractor_C": "Option C is incorrect because operating systems do not provide native automated 24-hour rollbacks for AI file edits without version control (git).",
      "distractor_D": "Option D is incorrect because granting full disk access on day one violates foundational least-privilege security principles."
    }
  },
  {
    "id": 38,
    "subtopic": "Model Cost Tiers & Economic Workflows",
    "domain": "Domain 7: Specialized Agent Architectures & SDD",
    "grounding": "Concept 12: Cost, speed, and which model to use when (Lines 1163-1180)",
    "scenario": "A media company evaluates operational costs across multimodal generative workflows. Which modality represents the highest computational cost and slowest iteration latency during iterative drafting?",
    "options": {
      "A": "Text generation, which consumes substantial cloud server bandwidth and requires multi-hour GPU processing runs.",
      "B": "Video generation, taking minutes per clip and costing up to 16 times more than text generation per round.",
      "C": "Speech synthesis, which costs several dollars per syllable due to analog audio frequency modulation layers.",
      "D": "Pretrained lookup, which requires re-training entire cloud neural network clusters for every user inquiry."
    },
    "correct": "B",
    "explanation": {
      "correct_rationale": "Option B is uniquely accurate per Concept 12. The text establishes: 'Text: seconds, fractions of a cent per response... Speech: seconds, a few cents per minute... Images: tens of seconds, several cents each... Video: minutes per clip, many cents to a few dollars. Each round is slow and expensive. Video costs roughly 16 times more than text.'",
      "distractor_A": "Option A is incorrect because text generation is the fastest (seconds) and cheapest (fractions of a cent) modality.",
      "distractor_B": "N/A (Correct Option)",
      "distractor_C": "Option C is incorrect because speech costs a few cents per minute, not several dollars per syllable.",
      "distractor_D": "Option D is incorrect because pretrained lookup is instant inference that does not re-train neural clusters."
    }
  },
  {
    "id": 39,
    "subtopic": "Cross-Family Model Grading: The LLM-as-Judge Protocol",
    "domain": "Domain 4: Model Evaluation, Validation & Error Mitigation",
    "grounding": "Concept 13: Models checking models (Lines 1244-1286)",
    "scenario": "A lead legal counsel prepares a high-stakes corporate compliance filing. To obtain an objective quality signal without a second senior attorney present, she uses Claude to draft the text, then takes the draft to ChatGPT and Gemini to critique it against a scored rubric. Why must cross-model checking involve different model families?",
    "options": {
      "A": "Commercial foundation model terms of service strictly prohibit querying two models of the same version consecutively.",
      "B": "Inference network firewalls block models from the same company from exchanging API tokens simultaneously.",
      "C": "Models within the same family share pretraining data and alignment habits, masking each other's blind spots.",
      "D": "Different models from the same vendor automatically synchronize their weights during active user evaluation sessions."
    },
    "correct": "C",
    "explanation": {
      "correct_rationale": "Option C is uniquely accurate per Concept 13. The text explains: 'Different models have different blind spots, because they were trained on different data by teams that cared about different things. A point one model misses, a second often catches... This only works across different model families, which means all the models from one company. Anthropic (Claude), OpenAI (ChatGPT), Google (Gemini)... Two Claude models checking each other is not cross-model checking, because their habits are too similar.'",
      "distractor_A": "Option A is incorrect because terms of service do not regulate comparative model evaluation.",
      "distractor_B": "Option B is incorrect because network firewalls do not block same-vendor API token queries.",
      "distractor_C": "N/A (Correct Option)",
      "distractor_D": "Option D is incorrect because model weights are frozen; they never dynamically synchronize across sessions."
    }
  },
  {
    "id": 40,
    "subtopic": "Limits of Cross-Model Checking: Craft vs Factual Truth",
    "domain": "Domain 4: Model Evaluation, Validation & Error Mitigation",
    "grounding": "Concept 13: An honest caveat (Lines 1280-1282)",
    "scenario": "A medical device regulatory specialist runs a high-risk clinical submission draft through three competing model families (Claude, ChatGPT, Gemini), achieving a stellar composite score of 9.6 out of 10 across all three. Why can the specialist still NOT treat this score as absolute proof of clinical veracity?",
    "options": {
      "A": "A composite score above 9.0 automatically triggers algorithmic hallucination cascades across model attention layers.",
      "B": "Foundation models deliberately collude with competing algorithms to flatter users and prevent regulatory audits.",
      "C": "Public leaderboard rankings automatically invalidate evaluation scores generated across multi-model pipelines.",
      "D": "Models share overlapping internet training data; they check each other for craft, but humans must verify facts."
    },
    "correct": "D",
    "explanation": {
      "correct_rationale": "Option D is uniquely accurate per Concept 13. The text delivers an honest caveat: 'Three models can still be wrong about the same thing, because they share more training data than you would guess. The score is a progress signal, not a truth signal. For anything legal, medical, financial, or about a real person, no number of cross-model passes replaces a human expert reading the claims that carry the weight. Models check each other for craft. Humans check the facts that matter.'",
      "distractor_A": "Option A is incorrect because high scores do not cause algorithmic attention cascades.",
      "distractor_B": "Option B is incorrect because models have no agency, intent, or technical ability to collude with competitor platforms.",
      "distractor_C": "Option C is incorrect because leaderboard rankings evaluate general model skill; they do not invalidate user evaluation workflows.",
      "distractor_D": "N/A (Correct Option)"
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
