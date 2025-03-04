# Creating an Basic AI Assistant

## Setup

### Python version

To get the most out of this course, please ensure you're using Python 3.11 or later. 
This version is required for optimal compatibility with LangGraph. If you're on an older version, 
upgrading will ensure everything runs smoothly.
```
python3 --version
```

#### Windows Powershell
```
PS> python -m venv my-ai-env # my-ai-env can be any name
PS> C:\Python312\python.exe -m venv my-ai-env
PS> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
PS> my-ai-env\scripts\activate
PS> pip install -r requirements.txt
```

### Running notebooks
If you don't have Jupyter set up, follow installation instructions [here](https://jupyter.org/install).
```
$ jupyter notebook
```

### Setting up env variables
Briefly going over how to set up environment variables. You can also 
use a `.env` file with `python-dotenv` library.

#### Example of .env
```
AZURE_OPENAI_API_KEY="rfurefbueb234j...edjebndeibdwuib8932b9"
AZURE_OPENAI_ENDPOINT="https://azure-openai-endpoint/"
LANGCHAIN_API_KEY="led23_kfnrnf...dje_efwef23"
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="my-basic-ai" # can be any name you want
```
#### Check out `setting-up-env.py` to load all env

### Sign up and Set LangSmith API
* Sign up for LangSmith [here](https://smith.langchain.com/), find out more about LangSmith
* and how to use it within your workflow [here](https://www.langchain.com/langsmith), and relevant library [docs](https://docs.smith.langchain.com/)!
*  Set `LANGCHAIN_API_KEY`, `LANGCHAIN_TRACING_V2=true` in your environment
