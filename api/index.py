from flask import Flask
import ollama
import re

#START YOUR VENV: venv\Scripts\Activate.ps1, OR source myvenv/bin/activate

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

app = Flask(__name__)


@app.route("/api/python")
def summarize(url: str) -> None:

    if (not re.match(regex, url)):
        print("Invalid url, please try again")
        return
    
    stream = ollama.generate(
        model='llama3',
        prompt='summarize this article: https://apnews.com/article/israel-gaza-rafah-offensive-us-united-nations-403a7c44b248b828559253206140eae5',
        stream=True,
    )
    for chunk in stream:
        print(chunk['response'], end='', flush=True)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

# TODO: DON"T RUN THIS
if __name__ == "__main__":
    summarize("httpx://www.google.com")
