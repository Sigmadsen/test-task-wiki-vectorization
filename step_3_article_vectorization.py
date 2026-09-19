# import os

import torch

# import numpy as np

from transformers import BertTokenizer, BertModel

# from const import ARTICLES_TXT
# from step_2_split_text_to_chunks import chunk_text

# Downloading pre-trained model BERT and tokenizers
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")


from FlagEmbedding import FlagAutoModel

model_2026 = FlagAutoModel.from_finetuned('BAAI/bge-base-en-v1.5',
                                      query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                                      use_fp16=True)



def vectorize_chunks_with_bert(chunks):
    vectors = []

    for chunk in chunks:
        # Text tokenization
        inputs = tokenizer(
            chunk, return_tensors="pt", truncation=True, padding=True, max_length=512
        )

        # Get output model's data
        with torch.no_grad():
            outputs = model(**inputs)

        # Getting embeddings (using hidden states of the last layer)
        # Average value of tokens in a chunk
        embeddings = outputs.last_hidden_state.mean(dim=1)
        vectors.append(embeddings.squeeze().numpy())

    return vectors

#BAAI/bge-small-en-v1.5
def vectorize_chunks_with_bge_small(chunks:list[str]):
    return model_2026.encode(chunks)


# if __name__ == '__main__':
#     # save to files
#     # for file in ARTICLES_TXT:
#     #     vector_file_name = file.split(".")[0]
#     #     with open(file, "r", encoding="utf-8") as file:
#     #         text = file.read()
#     #     chunks = chunk_text(text)
#     #     vectors = vectorize_chunks_with_bert(chunks)
#     #     np.save(f"{vector_file_name}.npy", vectors)
