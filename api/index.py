from enum import Enum
from flask import Flask, render_template, request
import ollama
import re

# START YOUR VENV: venv\Scripts\Activate.ps1, OR source myvenv/bin/activate
# python -m venv <directory>
# make sure its python 3.4+, then <pip install -r /path/to/requirements.txt>

# State Variables(WOW THIS IS SO CLEAN[its not])
class CurrentJob(Enum):
    IDLE = 0
    SUMMARY = 1
    NLP = 2
    REFFERALS = 3
    


url_cache: str = ""
is_processing: bool = False 
project_state: CurrentJob = CurrentJob.IDLE

def set_project_state(desired_project_state: CurrentJob, desired_processing_state: bool):
    global project_state, is_processing
    project_state = desired_project_state
    is_processing = desired_processing_state

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

app = Flask(__name__)


@app.route("/api/summarize")
def summarize(url: str = "") -> None:

    global url_cache
    url1 = request.args.get('url')
    if (url1 is not None): 
        url_cache = url1
    else: 
        url_cache = url

    if (not re.match(regex, url_cache)):
        print("Invalid url, please try again")
        return None
    
    set_project_state(CurrentJob.SUMMARY, True)
    # is_processing = True
    # project_state = CurrentJob.SUMMARY
    
    stream = ollama.generate(
        model='llama3',
        # prompt= 'say hi',
        prompt= f'summarize this article : {url_cache}',
        stream=True,
    )

    # map()
    endResult: str = ""
    for chunk in stream:
        endResult += chunk['response']
        print(chunk['response'], end='', flush=True)
    
    set_project_state(CurrentJob.IDLE, False)
    # is_processing = False
    # project_state = CurrentJob.IDLE

    return endResult

@app.route("/api/identify_bias")
def identify_bias() -> None:

    if (not re.match(regex, url_cache)):
        print("Invalid url, please try again")
        return None
    
    # is_processing = True
    set_project_state(CurrentJob.NLP, True)
    
    stream = ollama.generate(
        model='llama3',
        # prompt= 'say hi',
        prompt= f'Identity the political/country bias in the article : {url_cache}',
        stream=True,
    )
    endResult: str = ""
    for chunk in stream:
        endResult += chunk['response']
        print(chunk['response'], end='', flush=True)
    
    set_project_state(CurrentJob.IDLE, False)

    return endResult

@app.route("/api/link_refer")
def link_refer() -> None:

    if (not re.match(regex, url_cache)):
        print("Invalid url, please try again")
        return None
    
    set_project_state(CurrentJob.REFFERALS, True)
    
    stream = ollama.generate(
        model='llama3',
        # prompt= 'say hi',
        prompt= f'Refer me to links of articles that provide opposite or alternative perspectives\
            to this article : {url_cache}. Make the repsonse a list of these links and nothing else',
        stream=True,
    )

    endResult: str = ""
    for chunk in stream:
        endResult += chunk['response']
        print(chunk['response'], end='', flush=True)
    
    set_project_state(CurrentJob.REFFERALS, False)

    return endResult

# TODO: DON"T RUN THIS
if __name__ == "__main__":
    # summarize("https://apnews.com/article/israel-gaza-rafah-offensive-us-united-nations-403a7c44b248b828559253206140eae5")
    app.run(debug = True, threaded = True)
