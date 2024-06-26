from enum import Enum
from flask import Flask, jsonify, redirect, render_template, request, Response
from flask_cors import CORS
import ollama
import re
import time

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
summary_message: str = ""
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
app.debug = True
CORS(app)

def text_generator(stream):
    global summary_message
    set_project_state(CurrentJob.SUMMARY, True)

    start_time = time.time()
    for chunk in stream:
        # endResult += chunk['response']
        text = chunk['response']
        if (text != ''):
            print(text, end='', flush=True)
            summary_message += text
            yield text  

    print("\n --- %s seconds ---" % (time.time() - start_time))

    set_project_state(CurrentJob.IDLE, False)

    # return render_template('index.html', name=summary_message)
        # print(chunk['response'], end='', flush=True)

@app.route("/api/summarize", methods=['GET'])
def summarize(url: str = ""):
    # start_time = time.time()

    global url_cache
    url1 = request.args.get('url')
    if (url1 is not None): 
        url_cache = url1
    else: 
        url_cache = url

    print(url_cache + 'LOOK FOR ME HERE')

    if (not re.match(regex, url_cache)):
        print("Invalid url, please try again")
        return None
    
    stream = ollama.generate(
        model='llama3',
        # prompt= 'say hi',
        prompt= f'summarize this article in less than 20 words: {url_cache}',
        stream=True,
    )

    global summary_message
    set_project_state(CurrentJob.SUMMARY, True)

    start_time = time.time()
    for chunk in stream:
        text = chunk['response']
        if (text != ''):
            print(text, end='', flush=True)
            summary_message += text

    print("\n --- %s seconds ---" % (time.time() - start_time))

    set_project_state(CurrentJob.IDLE, False)

    output: str = summary_message

    response = {'text': summary_message}

    return jsonify({'text': output}), 200

@app.route("/api/identify_bias")
def identify_bias() -> str:
    
    # is_processing = True
    set_project_state(CurrentJob.NLP, True)

    set_project_state(CurrentJob.NLP, False)
    
    endResult: str = ""

    return summary_message

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

    

