import pathway as pw
from datetime import datetime
from common.geminiapi_helper import gemini_chat_completion


def prompt(index, embedded_query, user_query):

    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        print("STRING:",docs_str)
        #prompt = f"Given the following wepage/s content: \n {docs_str} \nanswer this query: {query}"
        #prompt = f"Given the following text snippets from webpages: \n {docs_str} \nanswer this query using the snippet but also use your own understanding if needed: {query} \n provide a detailed answer unless specified otherwise"
        #prompt = f"Given the following text snippets from webpages: \n {docs_str} \n answer this query: {query} \n provide a detailed answer unless specified otherwise"
        #prompt = f"Answer this query: \n {query} \n Considering the following webpage text:\n {docs_str} \n provide a detailed answer unless specified otherwise"
        #prompt = f"You are a large language model trained for information retrieval and question answering. You can access and process information from provided webpages and conduct your own research through web search. \n Here are some webpage text that might be relevant to the user's query: \n {docs_str} \n The user is asking: \n {query} \n Please answer the user's question using the information provided in the webpages and your own research capabilities, ensuring that your response is based on factual evidence from reliable sources.  If you cannot find a definitive answer, indicate that the information is inconclusive or unknown."


        prompt = f"Here are some webpage text that are relevant to the user's query: \n {docs_str} \n The user is asking: \n {query} \n Please provide an detailed answer to the user's question using the information provided in the webpages and your own research capabilities, ensuring that your response is based on factual evidence from reliable sources.  If you cannot find a definitive answer, indicate that the information is inconclusive or unknown."

        #log query
        with open("./data/logquery.txt", "w") as file:
            file.write(prompt)
        return prompt
    
    query_context = embedded_query + index.get_nearest_items(
        embedded_query.vector, k=3, collapse_rows=True
    ).select(local_indexed_data_list=pw.this.doc).promise_universe_is_equal_to(embedded_query)

    prompt = query_context.select(
        prompt=build_prompt(pw.this.local_indexed_data_list, user_query)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=gemini_chat_completion(pw.this.prompt),
    )
