# legal-research
The goal here is to have an automated research function take information about a legal situation as input, ask follow up questions to obtain additional information, identify the applicable laws, identify potential outcomes for the case, and provide potential next steps for the client and/or legal representative.

## Test Case

This describes the data required to test a single legal case for the legal research question of "what laws apply to the facts?".

### Input-Output for AI function testing

input:
- case material facts: markdown text string
- source bodies of laws in the jurisdiction/context: list of (markdown text string, metadata)
- source bodies of case-law in the jurisdiction/context: list of (markdown text string, metadata)
- past private legal case info: list of (markdown text string, metadata)

output:
- actual laws applicable to the case: markdown text string
    - could perhaps be output as: list of (markdown text string, metadata) for each individual applicable law

extension output:
- ambiguities in material facts
- almost applicable laws

### Where the data comes from

case-law document for this particular case:
- case material facts: markdown text string
- actual laws applicable to the case: markdown text string
- actual case-law applicable to the case: markdown text string

jusridiction legal sources:
- source bodies of laws in the jurisdiction/context
- source bodies of case-law in the jurisdiction/context

private legal sources from the law firm (optional):
- past private legal case info

### Challenges with this

how do we obtain the source bodies of laws and case-law?

how do we determine whether a given law or past case applies to the current case?

how do we determine when the story contains ambiguity?

how do we determine when a given law or past case almost apply?

### Possible workflow

need to:
- define using Colang.
- prioritize (have a prioritized queue of ambiguities/follow-up-questions to ask the client)
- if the client has little detail to add in their story, quickly transition to summary of what's known and where the gaps are
- resolve jurisdictional nuances (international vs. federal vs. state vs. local)
- is it worth it to employ secondary research to determine statute applicability?

Legal Agent Workflow from intake of a client to providing them with next steps.

1. client asks how you can help them:
    - tell them provide me with a legal situation and I'll tell you: which laws apply to your case, the different ways to address your case and their associated potential outcomes, costs, timelines, etc.
    - inform the cilent that the information that they share will stay strictly confidential between the agent and the client. "Your information is secure and confidential as we work through this."
    - confirm that the client understands what is being asked of them
2. specify what the user needs to provide (legal juridiction, material facts/story, legal questions/issues, etc.)
    - "Please provide the key facts of your situation, the state or country where this issue is happening, and any specific legal questions you have."
    - if it they say something ambiguous, flag it in a queue to ask for clarification on that point ("I need clarification on [specific point, e.g., ‘you mentioned a contract but didn’t specify its terms’]. Could you provide more details?", "Could you share more about [specific aspect, e.g., ‘what happened during the incident’] to help me identify the right laws?")
    - if they say something that contradicts what they previously said, present to the client their two contradicting statements and ask them how to resolve this contradiction (e.g. "I noticed two details that seem to conflict. Could you clarify which is correct?" or "I noticed you said [statement A] but also [statement B]. Could you clarify which is correct or provide more context?")
    - otherwise ask them to please tell you more about their story
        - if they have nothing more to say, tell them about the laws that apply to their story
3. find laws that apply to their story
    - statutes first:
        - query list of statutes, for each law, obtain the preconditions for their application, then check and see if each precondition is met by the story. For each precondition of a law, tally whether it is explicitly satisfied, explicitly disatisfied, or if it is ambiguous and more information from the client is needed. For each law, if the law itself is ambiguous in any way, find previous applications of the law to disambiguate the conditions.
        - List laws in increasing order of relevance (e.g. the number of preconditions not explicitly satisfied or some other metric), for each law in this order, for each precondition of each law, we want the client to provide: information to disambiguate uncertain preconditions, supporting evidence to fortify explicity satisfied preconditions, supporting evidence to fortify explicitly disatisfied preconditions. _Not sure which order is best to ask these questions, this would require foresight on what the potential outcomes of the case are_.
    - precedents or case-law first:
        - query cases in the same legal jursidiction that are similar to that of the client story, ensure that the case is still relevant, determine which laws applied in those cases and how the application of the laws in that case disambiguates the applicability and outcome of the law
        - provide this info to the client
    - resolve ambiguities: "To apply this law, I need to know [specific fact]. Can you provide that?" or "This law requires a written contract. Can you confirm if your agreement was written?"
    - If the cilent doesn't have more information to provide to their story, inform them of this in some way (tell client a summary of what has been said so far and what the next steps are, such as "Based on your story, here are the potential laws and gaps we need to address.")
3. Given laws that apply to the situation determine likely client outcomes
    - "A 2023 case in California applied this law to a similar breach, ruling [X]."
    - Use precedents to estimate success rates (e.g., "In 80% of similar cases, plaintiffs won when [condition] was met.")
    - Consider multiple resolution paths: litigation, settlement, mediation, or arbitration.
    - Factor in practical considerations: costs (legal fees, court costs), timelines (e.g., “Litigation may take 6–18 months”), and risks (e.g., “Appeals could extend the timeline”).
    - Include emotional or financial impacts (e.g., “Settling may be faster but could yield a lower payout.”).
    - Ask for their priorities (e.g., “Do you prefer a quick resolution or maximizing compensation?”) to tailor outcome analysis.
4. Tell the client a summary: what they have said so far, what laws you have identified as applicable to their story, what the options are to address their concerns, what ambiguities/contradictions are currently unresolved about their situation or about the state of the law, immediate next steps to be taken at this point by the law firm, and options for the client to make a decision.
