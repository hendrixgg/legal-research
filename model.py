from typing import List, Tuple

# a situation occurs, you obtain a description of the situation,
# given a description of a new situtation, check for contradictions and ambiguitie, if there are any, return errors,
# given a non-contradictory and disambiguated description of situation,
# establish the location/jurisdiction of situation
# then determine the sources of all available laws for that jurisdiction: legal statutes, regulations, and binding case law
# then determine the laws that have some relevance to the case at hand
# then determine exactly to what degree laws apply by some form of pattern matching score of law to the situation description, also associate the corresponding substantiating evidence with each claim in the situation description that relates directly to the law
# based on the pattern matching, if a pattern contradicts the facts of the case, then it must discarded; if a pattern is a perfect match, list it as top score; if a pattern is a partial match, list it as a lower score and determine which parts of the pattern match but need substantiation, parts that contradict the pattern, parts of the pattern that are missing, and parts of the pattern that are ambiguous

# This function will not work correctly because every legal statute must be interpreted in the context of the entire legal system.
# A more sophisticated approach is needed, either:
#   to interpret the statute with limited context and identify the ambiguities due to the absence of context, or
#   to interpret the statute with the context of the legal system hierarchy.


# keyword extraction from legal statutes: https://github.com/LIAAD/yake
# my current problem is that I don't know where to source all the legal statutes and case law from.
def extract_statute_conditions(context, statute_text) -> List:
    """
    Extract the conditions for a given legal statute to apply.
    """
    return []


def satisfies_condition(facts, condition) -> bool:
    """
    Check if the given facts satisfy the specified condition.
    """
    return True


def disambiguate_case(case_text) -> Tuple[List, List]:
    """
    Convert unstructured case text into structured lists of independent statements.

    (disambiguated_claims, ambiguous_claims)
    """
    return [], []  # Placeholder for disambiguated facts and conditions


def statute_applicability(statute_preconditions, disambiguated_case_facts) -> bool:
    """
    Determine if the statute applies to the case based on the facts and conditions.
    """
    return all(
        satisfies_condition(disambiguated_case_facts, condition)
        for condition in statute_preconditions
    )


"""
statute

conditions set by law
- context within the Act 
- context within the legal system

consequences if conditions not met
"""

"""
given:
{definitions of terms present in the legal statute}
{the legal statute text}
{facts of a case}

determine:
- whether each condition of the statute is satisfied by the facts

"""


"""
questions about canadian legal system: 
- https://grok.com/chat/a331478f-70ea-4e13-8795-8b5da4664d7f
- ontario employment law sources: https://grok.com/chat/7c4f07d5-c47f-4564-87f8-db590d32b051
- ontario law: https://www.ontario.ca/laws

"""

"""
Actual Example case that I'm using:
- 

"""

case_text = """

SUPERIOR COURT OF JUSTICE – ONTARIO

 

RE:                 Ralph Weekes and Ralph Weekes Financial Planning Professional CORPORATION. Plaintiffs

 

                        AND:

 

                        Investors Group Financial Services Inc. JEFFREY CARNEY, MARK KINZEL, DONALD MACDONALD, WILLIAM CHARLES, PATRICIA KLOEPFER, MARCIE MAGNUSSON, MARISSA TEETER, VAS PACHAPURKAR and JANE DOE 1-100 and JOHN DOE 1-100, Defendant

 

BEFORE:      Davies J.

COUNSEL:   Clarke Tedesco, for the Plaintiffs

                        Jeff Galway and Emily Hazlett, for the Defendant

HEARD at Toronto (by video):   August 10, 2020

 

REASONS FOR DECISION

 

DAVIES J.

A.           Overview

[1]         Ralph Weekes worked as a wealth management advisor for Investors Group Financial Services Inc. from June 1976 until December 31, 2017.

[2]         In June 2017, Investors Group told Mr. Weekes that they were not going to sponsor his registration with the Mutual Fund Dealers Association of Canada in January 2018. Mr. Weekes could no longer work as a wealth management advisor with Investors Group without their sponsorship. Investors Group’s decision not to sponsor Mr. Weekes, therefore, resulted in his termination as of December 31, 2017.

[3]         On June 26, 2019, Mr. Weekes issued a Notice of Action claiming damages for breach of contract. He alleged he was constructively dismissed. He also claimed his employment was terminated without cause and without adequate notice or pay in lieu of notice. In the alternative, Mr. Weekes claimed that Investors Group breached the consultant’s agreement signed by Mr. Weekes. Finally, he claimed that Investors Group’s decision to terminate him was discriminatory.

[4]         On July 26, 2019, Mr. Weekes issued a Statement of Claim in which he asserted that he was an independent contractor and alleges that Investors Group breached the implied terms of his contract.

[5]         In March 2020, Mr. Weekes filed a Fresh as Amended Statement of Claim in which he claims that he was an employee of Investors Group or, in the alternative, a dependent contractor. He now seeks damages for constructive dismissal and wrongful dismissal. He also claims that Investors Group acted in bad faith by terminating his employment and that his dismissal violated the Ontario Human Rights Code, R.S.O. 1990, c. H.19.

[6]         Investors Group brought a motion under Rules 21.01 and 25 and under ss. 4 and 5 of the Limitations Act, 2002, S.O. 2002 c. 24, Sched. B, to strike Mr. Weekes’ claims for constructive dismissal and wrongful dismissal, discrimination and bad faith. Investors Group argues that the constructive dismissal and wrongful dismissal are new claims that are now statute barred. Investors Group also argues that the claims of discrimination and bad faith are inextricably linked to the constructive dismissal and wrongful dismissal claims and cannot survive independent of those claims.

[7]         Mr. Weekes argues that the constructive dismissal and wrongful dismissal claims are not new claims. He argues that they were included in his Notice of Action. Mr. Weekes takes the position that the allegations of wrongful dismissal and constructive dismissal in the Fresh as Amended Statement of Claim simply urge a different legal conclusion about the nature of his relationship with Investors Group based on essentially the same facts that were in the original Statement of Claim.

[8]         There are three issues on this motion:

(a)         Are the constructive dismissal and wrongful dismissal claims new?

(b)         If the constructive dismissal and wrongful dismissal claims are new, should they be struck because they were advanced after the limitation period expired?

(c)         If the constructive dismissal and wrongful dismissal claims are struck, can the claims for discrimination and bad faith survive independently?

[9]         For the reasons that follow, I find that the constructive and wrongful dismissal claims are not new. As a result, I do not have to decide the other issues and the motion is dismissed.

B.           Are the constructive dismissal and wrongful dismissal claims new?

[10]      Mr. Weekes commenced his claim against Investors Group by issuing a Notice of Action on June 26, 2019 in which he advanced alternative theories in respect of the nature of Mr. Weekes’ relationship with Investors Group. He claimed damages for constructive dismissal, termination without cause and without sufficient pay in lieu of notice, breach of his Consultant’s Agreement and discrimination.

[11]      One month later, on July 26, 2019, Mr. Weeks issued a Statement of Claim, in which he asserted that he was an independent contractor with Investors Group and advanced five causes of action:

(a)         Breach of contract: He claimed that Investors Group breached the implied terms of his contract by failing to offer him an Asset Value Plan (“AVP”) and by firing his sons a year after his termination.[1]

(b)         Breach of the Ontario Human Rights Code: He also claimed that Investors Group’s decision to terminate him and not allow him to participate in the AVP violated the Ontario Human Rights Code.

(c)         Unjust enrichment: He claimed that Investors Group unjustly benefited from retaining his book of business without allowing to him to participate in the AVP.

(d)         Intentional interference with economic relations: He claimed that Investors Group intentionally interfered with his economic interests by offering free services to his former clients after his sons were terminated and by reporting to the Mutual Fund Dealers Association that his sons were terminated for cause, thereby triggering an investigation.

(e)         Conspiracy: He alleges that several senior executives at Investors Group acted with a common design to improperly take over Mr. Weekes’ book of business.

[12]      The original Statement of Claim details Mr. Weekes’ work history with Investors Group and the decision made by Investors Group not to sponsor his registration with the Mutual Fund Dealers Association. It also details how his sons were treated after he left Investors Group. However, the 2019 Statement of Claim did not particularize the constructive dismissal or wrongful dismissal claims that were set out in the Notice of Action.

[13]      In March 2020, Mr. Weekes issued a Fresh as Amended Statement of Claim in which he asserts that he was an employee or, in the alternative, a dependent contractor of Investors Group and claims he was constructively dismissed and/or wrongfully dismissed. Further particulars about the nature of Mr. Weekes’ relationship with Investors Group and the events leading up to his departure from the company were also added in the Fresh as Amended Statement of Claim.

[14]      The defendant argue that the constructive and wrongful dismissal claims raise new causes of action, ones that Mr. Weekes abandoned when he failed to include them in his Statement of Claim.

[15]      Mr. Weekes argues that the allegations in the Fresh as Amended Statement of Claim were contained in the Notice of Action and were never abandoned. Mr. Weekes also argues that the constructive and wrongful dismissal claims simply urge a different legal conclusion about Mr. Weekes’ relationship with Investors Group from facts alleged in the original Statement of Claim.

                     i.        Did Mr. Weekes abandon the constructive and wrongful dismissal claims?

[16]      Investors Group relies on the decision in Curtis v. Bank of Nova Scotia, 2019 ONSC 7539, to support its position that Mr. Weekes abandoned the constructive and wrongful dismissal claims that were included in his Notice of Action when he filed his Statement of Claim.

[17]      The circumstances here are very different than in Curtis v. Bank of Nova Scotia.

[18]      In Curtis v. Bank of Nova Scotia, Mr. Curtis resigned his position with Bank of Nova Scotia in the midst of a fraud investigation. Mr. Curtis commenced a claim for defamation, wrongful dismissal and constructive dismissal. He also filed a complaint under the Canada Labour Code, R.S.C., 1985, c. L-2, claiming he had been constructively dismissed. The adjudicator appointed under the Canada Labour Code found that Mr. Curtis had resigned and dismissed his complaint. Mr. Curtis sought judicial review of that decision in the Federal Court. Mr. Curtis’s civil claim for wrongful dismissal and constructive dismissal were stayed pending the outcome of the judicial review application. After the stay was issued, Mr. Curtis filed an Amended Statement of Claim removing the wrongful dismissal and constructive dismissal claim, leaving only the defamation claim. Several years later, Mr. Curtis brought a motion for leave to file a further amended Statement of Claim that would have effectively resurrected the wrongful and constructive dismissal claims under the guise of claims for bad faith, breach of employment contract and inducing a breach of an employment contract. The Court dismissed the motion, in part, because Mr. Curtis had voluntarily removed those claims from his pleadings.

[19]      In Curtis v. Bank of Nova Scotia, the plaintiff initiated a claim and then took clear, decisive, deliberate steps to remove some claims that had already been advanced. In those circumstances, the Court found that Mr. Curtis had intentionally abandoned his wrongful and constructive dismissal claims.

[20]      Here, Mr. Weekes issued a Notice of Action that set out alternative theories of liability. He then issued a Statement of Claim that neither clearly nor precisely particularized the wrongful dismissal and constructive dismissal claims. As required by the Rules of Civil Procedure, R.R.O. 1990, Reg. 194, the Notice of Action and Statement of Claim were both served on the defendant (rule 14.08(2)). While a Notice of Action expires if a Statement of Claim is not issued within 30 days, the issuance of a Statement of Claim does not cancel the Notice of Action (rule 14.03(3)). The Notice of Action continues to form part of the pleadings even after the Statement of Claim is issued. The fact that wrongful and constructive claims set out in the Notice of Action were not clearly and precisely particularized in the Statement of Claim is not sufficient to find that Mr. Weekes knowingly and intentionally abandoned those claims.

                    ii.        Does the Fresh As Amended Statement of Claim seek alternative relief based on the same facts?

"""

"""
example that I'm using:
- https://www.canlii.org/en/on/onsc/doc/2020/2020onsc6788/2020onsc6788.html?resultId=a43467e51b6c4acbbe471a85f9f484e3&searchId=2025-05-29T11:11:44:430/ffe0b3dc4f994f3cb939e74ff0bf13b6&searchUrlHash=AAAAAQAaV3JvbmdmdWwgZGlzbWlzc2FsIE9udGFyaW8AAAAAAQ

mores examples:
- https://queensuca-my.sharepoint.com/:x:/g/personal/14cfl_queensu_ca/EUQlEhUQZ7tJpgRo3_za-YoBriz--6u6SVQtQYY6Y5AsMQ?e=gmWwWT

"""

"""
Employment Law situations we will consider:
- wrongful dismissal/termination
- constructive dismissal
- worker classification
- termination notice

"""
