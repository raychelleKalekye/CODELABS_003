import pandas as pd
import torch
from transformers import LaBSETokenizer, LaBSEModel
from sklearn.metrics.pairwise import cosine_similarity

# Load LaBSE model and tokenizer
def load_labse_model():
    tokenizer = LaBSETokenizer.from_pretrained("bert-base-multilingual-cased")
    model = LaBSEModel.from_pretrained("bert-base-multilingual-cased")
    return tokenizer, model

# Encode names using LaBSE
def encode_names(names, tokenizer, model):
    inputs = tokenizer(names, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
    return embeddings

# Compute similarity matrix
def compute_similarity_matrix(male_names, female_names, tokenizer, model):
    male_embeddings = encode_names(male_names, tokenizer, model)
    female_embeddings = encode_names(female_names, tokenizer, model)
    similarity_matrix = cosine_similarity(male_embeddings, female_embeddings)
    return similarity_matrix

# Filter similarities based on a threshold
def filter_similarities(similarity_matrix, male_names, female_names, threshold=0.5):
    results = []
    for i, male_name in enumerate(male_names):
        for j, female_name in enumerate(female_names):
            if similarity_matrix[i][j] >= threshold:
                results.append({
                    'male_name': male_name,
                    'female_name': female_name,
                    'similarity': float(similarity_matrix[i][j])
                })
    return results

# Save results to a JSON file
def save_results_to_json(results, output_file):
    import json
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)
