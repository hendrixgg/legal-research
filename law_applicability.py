import asyncio
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from model import case_text

# Initialize the chat model
llm = init_chat_model(
    "gpt-3.5-turbo",
    model_provider="openai",
    temperature=0)

template_text = """given the following case text and legal reference, please answer the question.
Case Text: {case_text}
Law Information: {law_information}
Question: {question_text}
"""

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["case_text", "legal_reference", "question_text"],
    template=template_text
)
law_informations = [
    """
Excerpt from the case: 1100997 Ontario Ltd. v. North Elgin Centre Inc., 2016 ONCA 848, at para. 19.

[19]      A cause of action is “a factual situation the existence of which entitles one person to obtain from the court a remedy against another person”: Letang v. Cooper, [1965] 1 Q.B. 232 (C.A.), at pp. 242-43, as adopted by this court in July v. Neal (1986), 1986 CanLII 149 (ON CA), 57 O.R. (2d) 129 (C.A.), at para. 23.
""",
    """
Excerpt from the case: 1100997 Ontario Ltd. v. North Elgin Centre Inc., 2016 ONCA 848, at para. 19.
[20]      In Morden & Perell, The Law of Civil Procedure in Ontario, 2nd ed. (Markham: LexisNexis Canada Inc., 2014), at p. 142, the authors state:

A new cause of action is not asserted if the amendment pleads an alternative claim for relief out of the same facts previously pleaded and no new facts are relied upon, or amount simply to different legal conclusions drawn from the same set of facts, or simply provide particulars of an allegation already pled or additional facts upon which the original right of action is based. [Footnotes omitted.]
""",
    """
Excerpt from the case: Timber Estate v. Bank of Nova Scotia, 2011 ONSC 3639, at para. 13.

[13]           A cause of action is defined as a factual situation the existence of which entitles one person to obtain from the court a remedy against another person.  When a proposed amendment relates to material facts that were not substantially pleaded in the original claim or are essential to support the claim being advanced, the amendment raises a new cause of action [see Ascent Inc. v. Fox 40 International Inc., [2009] No. 2964 (S.C.J.) and Bank of Nova Scotia v. PCL Constructors Inc., [2009] O.J. No. 4347 (S.C.J.)].
"""
]

irrelevant_law_informations = [
    """
Excerpt from the case: 671122 Ontario Limited v. Sagaz Industries Canada Inc., 2000 CanLII 5624 (ON CA), at para. 25.

[25] The circumstances in which an appellate court will substitute its own findings in the face of an explicit finding of credibility by the trial judge are, to say the least, exceptional. The best the appellant could hope for in the circumstances of the present case would be a new trial, and even that remedy will be rare where the trial judge has considered contested evidence and found a witness to be credible.
""",
    """
Excerpt from the case: 671122 Ontario Limited v. Sagaz Industries Canada Inc., 2000 CanLII 5624 (ON CA), at para. 30.

[30] In this regard, I note that a recent English case dealing with a motion to re-open a trial, Charlesworth v. Relay Roads Ltd., [1999] 4 All E.R. 397 (Ch. D.) at p. 404, Neuberger J. adopted the test laid down by Lord Denning in Ladd v. Marshall, [1954] 3 All E.R. 745 at p. 748, [1954] 1 W.L.R. 1489 (C.A.) for admission of new evidence on appeal:

    . . . first, it must be shown that the evidence could not have been obtained with reasonable diligence for use at the trial; second, the evidence must be such that, if given, it would probably have an important influence on the result of the case, although it need not be decisive; third, the evidence must be such as is presumably to be believed, or in other words, it must be apparently credible, though it need not be incontrovertible.

    While I think that these three factors should be in the forefront of the mind of the court when considering an application to admit new evidence after judgment has been handed down, but before the order has been drawn up, I incline to the view that the court is entitled to be somewhat more flexible, and not to proceed on the strict basis that each of these three conditions always has to be fully satisfied before fresh evidence can be admitted before judgment.

(Emphasis added)

I note that it has been suggested in Ontario as well that a more flexible approach may be warranted on motions to re-open a trial: see Castlerigg Investments Inc. v. Lam (1991), 1991 CanLII 7355 (ON SC), 2 O.R. (3d) 216 at p. 223, 47 C.P.C. (2d) 270 (Gen. Div.); Scott v. Cook, 1970 CanLII 331 (ON SC), [1970] 2 O.R. 769, 12 D.L.R. (3d) 113 (H.C.J.). In Canada, the test for admission of new evidence on appeal includes a similar criterion of credibility: "the evidence must be credible in the sense that it is reasonably capable of belief". (See R. v. Palmer, 1979 CanLII 8 (SCC), [1980] 1 S.C.R. 759 at p. 775, 106 D.L.R. (3d) 212; R. v. Warsing, 1998 CanLII 775 (SCC), [1998] 3 S.C.R. 579 at p. 592, 233 N.R. 319.)
""",

]

question_texts = [
    """How could the legal reference be applied to determine the outcome of the case?
Truthfully answer the question based on the case text and Law Information provided. If the legal reference is not applicable, state that it is not applicable and explain why.""",
    """Can the provided legal reference be used to proceed with this case? Please explain your reasoning based on the case text and law information provided. Condlude the answer on a final line with 'Yes' or 'No'."""
]


def basic_test():

    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=prompt.format(case_text=case_text,
                                           law_information=irrelevant_law_informations[1],
                                           question_text=question_texts[1]))
    ]

    # Generate a response
    response = llm.invoke(messages)
    # Print the response
    print(response.content)


async def batch_test():
    llm_tasks = []
    question_text = question_texts[1]
    for law_information in law_informations:
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=prompt.format(case_text=case_text,
                                               law_information=law_information,
                                               question_text=question_text))
        ]

        # queue up the coroutines for relevant law information
        llm_tasks.append(asyncio.create_task(llm.ainvoke(messages)))

    for law_information in irrelevant_law_informations:
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=prompt.format(case_text=case_text,
                                               law_information=law_information,
                                               question_text=question_text))
        ]

        # queue up the coroutines for irrelevant law information
        llm_tasks.append(asyncio.create_task(llm.ainvoke(messages)))
    # Await all tasks to complete
    for result in await asyncio.gather(*llm_tasks):
        print(result.content)
        print("-" * 80)

    # Run all relevant tasks concurrently
    pass


if __name__ == "__main__":
    # basic_test()

    asyncio.run(batch_test())
