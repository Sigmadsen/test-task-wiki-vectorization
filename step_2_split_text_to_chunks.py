import nltk
from nltk.tokenize import sent_tokenize

# Punkt is a pre-trained model for text tokenization.
# Tokenization is the process of breaking text into its constituent parts, such as words or sentences.
# The Punkt model is specifically trained to accurately detect sentence and word boundaries
# in text based on different languages.
nltk.download("punkt_tab")


def chunk_text(text, max_chunk_size:int=1000)-> list[str]:
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) > max_chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            if current_chunk:
                current_chunk += " " + sentence
            else:
                current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def read_file_into_text(link:str="data/Machine_learning.txt")->str:
    with open(link, "r", encoding="utf-8") as file:
        text = file.read()
    return text

if __name__ == "__main__":
    with open("data/Machine_learning.txt", "r", encoding="utf-8") as file:
        text = file.read()

    chunks = chunk_text(text)
    print(chunks)
    for item in chunks:
        print(item)
