# similarity.py

from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
import json

# Load LaBSE model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/LaBSE")
model = AutoModel.from_pretrained("sentence-transformers/LaBSE")

def embed_names(names):
    """Embed names using LaBSE model."""
    with torch.no_grad():
        inputs = tokenizer(names, padding=True, truncation=True, return_tensors="pt")
        embeddings = model(**inputs).last_hidden_state[:, 0, :]
    return embeddings

def compute_similarity_matrix(male_names, female_names):
    """Compute similarity matrix between male and female names."""
    male_embeddings = embed_names(male_names)
    female_embeddings = embed_names(female_names)

    # Calculate cosine similarity
    similarity_matrix = torch.mm(male_embeddings, female_embeddings.T)
    similarity_matrix = similarity_matrix / (torch.norm(male_embeddings, dim=1).unsqueeze(1) * torch.norm(female_embeddings, dim=1))
    return similarity_matrix.numpy()

def save_similarity_results(male_names, female_names, similarity_matrix, threshold=0.5):
    """Save similarity results above a certain threshold to a JSON file."""
    results = []
    for i, male_name in enumerate(male_names):
        for j, female_name in enumerate(female_names):
            similarity_score = similarity_matrix[i][j]
            if similarity_score >= threshold:
                results.append({
                    "male_name": male_name,
                    "female_name": female_name,
                    "similarity_score": float(similarity_score)
                })

    # Save the results to a JSON file
    with open("similarity_results.json", "w") as file:
        json.dump(results, file, indent=4)
    print(f"Similarity results saved to similarity_results.json")