(Not solwed)

# test-wiki-vectorization
Goal is to take a set of text, vectorize it and make it searchable by indexing it in a vector DB

## How to up redis
1. `docker-compose build` - build container
2. `docker-compose up -d` - run  container with Redis and Redis Insight

### Steps to run
1. Create virtual env in directory
2. Activate it: `source /venv/bin/activate`
3. Run `pip install -r requirements.txt`
4. Run step 4 to create index
5. Run step 5 to save the data from articles
6. Run step 6 to search something

### Try to improve searching quality
1. Try smaller chunks, not 1000 chars, but 250 to improve relevancy - not works


что сказал иишка - что мой трасформер от гугл говно. это раз. и что для бд нужно использовать не redis, а некую 
"замена Redis на встраиваемую ChromaDB и сырого BERT на BAAI/bge-small-en-v1.5 с перечислением ключевых преимуществ (легковесность, точность, автономность)."
BAAI/bge-small-en-v1.5 - а где брать
еще везде нужно переписать интерфейсы взаимодействия с chromadb и новым трансформером,
но надеюсь у меня интерфейс на трансформере будет такой же, как и на BERT

BAAI/bge-small-en-v1.5 - https://huggingface.co/BAAI/bge-small-en-v1.5