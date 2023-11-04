from fastapi import FastAPI
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-albert-small-v2", cache_folder='./albert/')
app = FastAPI()


@app.get("/")
def get_hello():
    return "Hello"


@app.get("/is_similar")
def compute_similarity(sentence1, sentence2):
    embeddings1 = model.encode(sentence1)
    embeddings2 = model.encode(sentence2)
    score = util.cos_sim(embeddings1, embeddings2)
    return {'score': str(score.numpy()[0, 0])}
