<div align="center">
     <h1>webpAIge</h1>

    <p align="center"> Chat with webpages </p>
</div>

## About

webpAIge let's you chat with webpages using the Pathways framework to access in realtime the webpage's content.

## Prerequisites
1. Create an [Gemini API Key](https://ai.google.dev/) 

    Then, follow the easy steps to install and get started using the sample app.

## Installation

1. Clone the repo
    ```sh
    git clone https://github.com/Shivsay/webpAIge.git
    ```

2. Create a conda environment using environment.yml file 
    ```sh
    conda env create -f environment.yml
    ```

3. Activate the environment using the command
    ```sh
    conda activate webpAIge_env
    ```

3. Create a .env file with following content
    ```sh
    GEMINI_API_TOKEN= {YOUR_API_TOKEN}
    EMBEDDER_LOCATOR=models/text-embedding-004
    EMBEDDING_DIMENSION=768
    MODEL_LOCATOR=gemini/gemini-pro
    MAX_TOKENS=8000
    TEMPERATURE=0.0
    HOST="localhost"

4. Install packages
    ```sh
    pip install --upgrade -r requirements.txt
    ```
## Running

### Starting the pathway backend
1. Go to the directory with the main.py file
2. Run the command
    ```sh
    python main.py
    ```
### Starting the streamlit ui
1. Go to the ui directory
2. Run the command
    ```sh
     streamlit run ui.py
    ```

