from langchain.sql_database import SQLDatabase
# from langchain.chains import SQLDatabaseChain
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy import create_engine
from langchain_groq import ChatGroq

# Step 1: Connect to SQLite Database (instead of PostgreSQL)
db_url = "sqlite:///data.db"  # SQLite database URL
engine = create_engine(db_url)
db = SQLDatabase(engine)

# Step 2: Initialize Groq LLM
llm = ChatGroq(api_key=" ", model_name="llama3-70b-8192")  # Replace with your Groq API key

# Step 3: Create the SQL QA Chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# Step 4: Ask a Question in Natural Language
query = "What is the size(acres) of National Park Aracadia ?"  # Example query
response = db_chain.run(query)

print(response)
