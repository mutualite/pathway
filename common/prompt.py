import pathway as pw
from datetime import datetime
from common.geminiapi_helper import gemini_chat_completion


def prompt(index, embedded_query, user_query):

    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        print("STRING:",docs_str)
        #prompt = f"Given the following wepage/s content: \n {docs_str} \nanswer this query: {query}"
        prompt = f"Given the following text snippets from webpages: \n {docs_str} \nanswer this query: {query} \n provide a detailed answer unless specified otherwise"


        #log query
        """
        with open("./data/logquery.txt", "w") as file:
            file.write(prompt)
        return prompt
        """
    
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
