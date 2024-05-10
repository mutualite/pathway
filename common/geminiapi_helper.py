from dotenv import load_dotenv
import os
import pathway as pw
from pathway.xpacks.llm.embedders import LiteLLMEmbedder
from pathway.xpacks.llm.llms import LiteLLMChat, prompt_chat_single_qa

import google.generativeai as genai

load_dotenv()


embedder_locator = os.environ.get("EMBEDDER_LOCATOR", "models/text-embedding-004")
api_key = os.environ.get("GEMINI_API_TOKEN", "")
model_locator = os.environ.get("MODEL_LOCATOR", "gemini/gemini-pro")
max_tokens = int(os.environ.get("MAX_TOKENS", 200))
temperature = float(os.environ.get("TEMPERATURE", 0.0))

genai.configure(api_key=api_key)

def gemini_embedder(data):
    embedder = genai.embed_content(
    model="models/embedding-001",
    content='Some text',
    task_type="RETRIEVAL_QUERY")

    return embedder['embedding'];

def gemini_chat_completion(prompt):
    model = LiteLLMChat(
        api_key=api_key,
        model=model_locator,
        temperature=temperature,
        retry_strategy=pw.asynchronous.FixedDelayRetryStrategy(),
        cache_strategy=pw.asynchronous.DefaultCache(),
        max_tokens=max_tokens
    )

    return model(prompt_chat_single_qa(prompt))
