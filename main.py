from step_2_split_text_to_chunks import read_file_into_text, chunk_text
from const import ARTICLES_TXT

if __name__ == '__main__':
    # read text from /data into list
    for file in ARTICLES_TXT:
        text = read_file_into_text(file)
        chunks = chunk_text(text)
        print('PyCharm')