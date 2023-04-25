import os
from dotenv import load_dotenv
from supabase.client import Client, create_client
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import SupabaseVectorStore
from langchain.document_loaders import TextLoader
from langchain.document_loaders import TextLoader

load_dotenv()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# configure these to fit your needs
exclude_dir = ['.git', 'node_modules', 'public']
exclude_files = ['package-lock.json']

documents = []

for dirpath, dirnames, filenames in os.walk('repo'):
    # skip directories in exclude_dir
    dirnames[:] = [d for d in dirnames if d not in exclude_dir]
    
    for file in filenames:
        # skip files in exclude_files
        if file not in exclude_files:
            file_path = os.path.join(dirpath, file)
            loader = TextLoader(file_path)
            documents.extend(loader.load())


text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

for doc in docs:
    source = doc.metadata['source']
    cleaned_source = '/'.join(source.split('/')[1:])
    doc.page_content = "FILE NAME: " + cleaned_source + "\n###\n" + doc.page_content

embeddings = OpenAIEmbeddings()

vector_store = SupabaseVectorStore.from_documents(
    docs,
    embeddings,
    client=supabase,
    table_name=os.environ.get("TABLE_NAME"),
)