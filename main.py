from dotenv import load_dotenv
import os

load_dotenv()

# Plain OpenAI API Request
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key=os.environ.get("api_key"))
res = llm.invoke("how can langsmith help with testing?")
print(res)

# OpenAI API Request with Prompt
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a world class technical documentation writer."),
        ("user", "{input}"),
    ]
)
chain = prompt | llm
res = chain.invoke("how can langsmith help with testing?")
print(res)

# OpenAI API Request with Prompt and Output Parser
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
chain = prompt | llm | output_parser
rest = chain.invoke({"input": "how can langsmith help with testing?"})
print(rest)
