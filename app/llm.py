from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import json
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

prompt = PromptTemplate(
    input_variables=["subject", "body"],
    template="""You are a task extraction assistant.

    Read this email and return a JSON object with:
    - "summary": one sentence summary of the email
    - "tasks": list of tasks, each with "title" and "due_date" (empty string if not mentioned)

    Email Subject: {subject}
    Email Body: {body}

    Return raw JSON only. No markdown, no explanation."""
)

chain = prompt | llm | StrOutputParser()


def extract_tasks_from_email(subject: str, body: str) -> dict:
    try:
        raw = chain.invoke({"subject": subject, "body": body})
        clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        return json.loads(clean)
    except Exception as e:
        return {
            "summary": "Failed to summarize",
            "tasks": [],
            "error": str(e)
        }