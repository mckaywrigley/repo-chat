import os
from dotenv import load_dotenv
from langchain.document_loaders import GitLoader

load_dotenv()

loader = GitLoader(
    clone_url=os.environ.get("REPO_URL"),
    repo_path='repo',
    branch=os.environ.get("REPO_BRANCH"),
)

loader.load()