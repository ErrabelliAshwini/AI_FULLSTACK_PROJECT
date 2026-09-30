from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
with open("ai_sample.txt","r") as file:
    text = file.read()
#print(text)
chunks = []
chunk_size = 25
chunk_overlap = 20
step = chunk_size - chunk_overlap
for i in range(0,len(text),chunk_overlap):
    chunk = text[i:i+chunk_size]
    chunks.append(chunk)
# print("No.of chunks:",len(chunks))
# for i in range(len(chunks)):
#     print(f"Chunk {i} ->{chunks[i]}")
# Embeddings
embeddings = model.encode(chunks)
# print("Embedding created successfully")
# print(len(embeddings))
# print(embeddings[0])
print(embeddings.shape)