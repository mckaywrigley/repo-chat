# Repo Chat

Repo chat allows you to ask questions about a GitHub repository.

## Requirements

In this project we use [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings) and [Supabase with pgvector](https://supabase.com/docs/guides/database/extensions/pgvector) as our vector database.

You can switch out either of these with your own preference.

## How To Run

1. Run the `schema.sql` file in Supabase's SQL editor.

2. Configure the `.env` file.

3. Run `pip install -r requirements.txt` to install the dependencies.

4. Run the `load.py` script to clone the repo.

5. Run the `embed.py` script to embed the repo.

6. Run the `main.py` script to ask questions about the repo.

## Contact

If you have any questions, feel free to reach out to Mckay on [Twitter](https://twitter.com/mckaywrigley)!
