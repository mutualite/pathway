import pathway as pw
import os
from dotenv import load_dotenv
from common.embedder import embeddings, index_embeddings
from common.prompt import prompt
from pathway.xpacks.llm.parsers import ParseUnstructured
from pathway.xpacks.llm.splitters import TokenCountSplitter
load_dotenv()

def run(host, port):
    # Given a user search query
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )

    input_data = pw.io.jsonlines.read(
        "./data/data.jsonl",
        schema=DataInputSchema,
        mode="streaming"
    )


    # Compute embeddings
    embedded_data = embeddings(context=input_data, data_to_embed=input_data.doc)

    # Construct an index on the generated embeddings in real-time
    index = index_embeddings(embedded_data)

    # Generate embeddings for the query
    embedded_query = embeddings(context=query, data_to_embed=pw.this.query)



    # Build prompt using indexed data
    responses = prompt(index, embedded_query, pw.this.query)

    # Feed the prompt to LLM and obtain the generated answer.
    response_writer(responses)


    # Run the pipeline
    pw.run()


class QueryInputSchema(pw.Schema):
    query: str

class DataInputSchema(pw.Schema):
    doc: str
