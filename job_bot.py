import faiss
from sentence_transformers import SentenceTransformer
import subprocess

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("jobs.index")

with open("jobs_data.txt") as f:
    jobs = [line.strip() for line in f.readlines()]


def ask_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout


while True:
    q = input("\nAsk job bot: ")

    if q == "exit":
        break

    q_emb = model.encode([q])
    D, I = index.search(q_emb, k=3)

    context = "\n".join([jobs[i] for i in I[0]])

    final_prompt = f"""
You are a job assistant.

User query: {q}

Relevant jobs:
{context}

Suggest the best jobs and explain why.
"""

    print(ask_llm(final_prompt))
