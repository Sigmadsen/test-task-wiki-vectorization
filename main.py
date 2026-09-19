from step_2_split_text_to_chunks import read_file_into_text, chunk_text
from step_3_article_vectorization import vectorize_chunks_with_bge_small
from const import ARTICLES_TXT

if __name__ == '__main__':
    # read text from /data into list
    for file in ARTICLES_TXT:
        text = read_file_into_text(file)
        sentences:list[str] = chunk_text(text, 250)
        embeddings = vectorize_chunks_with_bge_small(sentences)

        hardcoded_embeddings_to_search_in_vector_db = vectorize_chunks_with_bge_small(
            ["What is machine learning", "What is ML", "What is (ML)", "What is (Machine Learning)"]
        )
    print('PyCharm')
        # Once we get the embeddings, we can compute similarity by inner product:
        #
        # similarity = embeddings_1 @ embeddings_2.T
        # print(similarity)