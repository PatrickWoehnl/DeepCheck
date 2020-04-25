from newspaper import Article

import newspaper


def GetArticleText(event, context):

    url = event['text']

    if url.startswith(('http', 'www.')):
        url = url
        article = Article(url)
        article.download()
        article.parse()       
    # text weiter verarbeiten
        return article.text
    return url

def Test():
    url = 'https://nbpostgazette.com/florida-woman-dies-of-flesh-eating-bacteria-while-after-stumbling-on-beach/'
    if url.startswith(('http', 'www.')):
        url = url
        article = Article(url)
        article.download()
        article.parse() 
        print(article.text)

if __name__ == '__main__':
    Test()
    

    
