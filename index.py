from sentence_transformers import SentenceTransformer
import faiss

with open("jobs.txt") as f:
    jobs = [line.strip() for line in f.readlines()]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(jobs)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)

faiss.write_index(index, "jobs.index")

with open("jobs_data.txt", "w") as f:
    for j in jobs:
        f.write(j + "\n")

print("Indexed", len(jobs), "jobs")
