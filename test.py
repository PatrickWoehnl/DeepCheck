from newspaper import Article
import csv
import newspaper

from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/deepchek/api/v1.0/CheckArticle/<string:url>', methods=['GET'])
def CheckArticle(url):
    if url.startswith('http'):
        url = url
        article = Article(url)
        article.download()
        article.parse()       
    return jsonify({'CheckArticle': article.text})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':

    url = 'https://nbpostgazette.com/florida-woman-dies-of-flesh-eating-bacteria-while-after-stumbling-on-beach/'
    article = Article(url)
    article.download()
    article.parse()
    print(article.text)

    with open('D:\\aa git\\newspaper\\names.csv', 'w', newline='') as csvfile:
        fieldnames = ['text', 'label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'text': article.text, 'label': 0})
        writer.writerow({'text': 'Lovely', 'label': 'Spam'})
        writer.writerow({'text': 'Wonderful', 'label': 'Spam'})
        