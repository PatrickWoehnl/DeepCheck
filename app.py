from newspaper import Article
from flask import Flask
from flask import request
from flask import jsonify
import prediction
import newspaper

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/DeepCheck/api/v1.0/GetArticleText', methods=['GET'])
def GetArticleText():
    url = request.args.get('url')

    if url.startswith(('http', 'www.')):
        url = url
        article = Article(url)
        article.download()
        article.parse()  
        p = prediction.predict(article.text)    
        return jsonify(
        text=article.text,
        min=str(p[0][0]),
        max=str(p[0][1])
        )
 

    p = prediction.predict(url)    
    return jsonify(
        text=url,
        min=str(p[0][0]),
        max=str(p[0][1])
        )
    # text weiter verarbeiten
       

def Test():
    url = 'https://nbpostgazette.com/florida-woman-dies-of-flesh-eating-bacteria-while-after-stumbling-on-beach/'
    if url.startswith(('http', 'www.')):
        url = url
        article = Article(url)
        article.download()
        article.parse() 
        print(article.text)

if __name__ == '__main__':
    app.run(port=int("5000"), debug=True)
    #host='0.0.0.0', 
    

    
