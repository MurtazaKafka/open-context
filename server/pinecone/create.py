from pinecone import Pinecone
from pinecone import ServerlessSpec
import os

pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))

pc.create_index(
  name="example-index2",
  dimension=3072,
  metric="cosine",
  spec=ServerlessSpec(
    cloud="aws",
    region="us-east-1"
  ),
  deletion_protection="disabled"
)
