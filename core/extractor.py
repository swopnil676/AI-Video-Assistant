#Actionableitems , Decisions , Questions 
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from core.summarizer import invoke_with_retry
import os


def get_llm():
    return ChatMistralAI(
        model = "ministral-8b-latest",
        mistral_api_key = os.getenv("MISTRAL_API_KEY"),
        temperature=0.2)


def build_chain(system_prompt : str):
    llm = get_llm()
    return (
        RunnablePassthrough() | RunnableLambda(lambda x : {"text": x})
        | ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{text}"),
        ]) | llm | StrOutputParser()
    )


# def extract_action_items(transcript : str) -> str:
#     chain = build_chain(
#         "You are an expert meeting analyst. From the meeting transcript, "
#         "extract all action items. For each provide:\n"
#         "- Task description\n"
#         "- Owner (who is responsible)\n"
#         "- Deadline (if mentioned, else write 'Not specified')\n\n"
#         "Format as a numbered list. If none found say 'No action items found.'"
#     )
#     # return chain.invoke(transcript)
#     return invoke_with_retry(chain, transcript)


# def extract_key_decisions(transcript : str) -> str:
#     chain = build_chain(
#         "You are an expert meeting analyst. From the meeting transcript, "
#         "extract all key decisions made. Format as a numbered list. "
#         "If none found say 'No key decisions found.'"
#     )
#     # return chain.invoke(transcript)
#     return invoke_with_retry(chain, transcript)


# def extract_questions(transcript : str) -> str:
#     chain = build_chain(
#         "From the meeting transcript, extract all unresolved questions "
#         "or topics needing follow-up. Format as a numbered list. "
#         "If none found say 'No open questions found.'"
#     )
#     # return chain.invoke(transcript)
#     return invoke_with_retry(chain, transcript)


def extract_all(transcript: str) -> str:
    chain = build_chain(
        "You are an expert meeting analyst. Analyze the transcript "
        "and extract the following three sections:\n\n"

        "1. ACTION ITEMS:\n"
        "- Task description\n"
        "- Owner\n"
        "- Deadline (if not mentioned, write 'Not specified')\n\n"

        "2. KEY DECISIONS:\n"
        "- List all important decisions.\n\n"

        "3. OPEN QUESTIONS:\n"
        "- List unresolved questions or topics needing follow-up.\n\n"

        "If a section has no results, clearly mention that none were found. "
        "Use clear headings and numbered lists."
    )
    return invoke_with_retry(chain, transcript)