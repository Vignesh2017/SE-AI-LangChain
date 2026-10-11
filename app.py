
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tracers.context import collect_runs

load_dotenv(Path(__file__).with_name(".env"))

run_ids = []
llm = ChatOpenAI(model="gpt-4o-mini")
prompts = ["Say some words on organic farming", "How to start organic farming?"]
for p in prompts:
    with collect_runs() as cb:
        print(llm.invoke(p).content)
        run_ids.append(cb.traced_runs[0].id)

print(run_ids)