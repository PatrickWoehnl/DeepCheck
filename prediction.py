import numpy as np
import pandas as pd
import sklearn
import joblib


sample_text = "Latest industry research report on the Photography Studio Software Market report is an investigative study executed by experts on the basis of global market, which studies the aggressive structure of the global industry all over the globe. Constructed by the practice of proficient systematic tools such SWOT analysis, the global market report offers a complete judgment of global market. Download free sample report @ https://www.fiormarkets.com/report-detail/146313/request-sample The evaluation for CAGR (Compound Annual Growth Rate) is entirely provided by the Photography Studio Software Market report in terms of percentage for accurate period. This will assist users to make beyond question choice-based decisions on predicted chart. The report also wraps up leading and major players in the global market. Income (US$) and volume of the production are the two main units on which the global market size is calculated by the experts in this report. Intense analysis of key fragments of the market as well as the geological division all over the world is also carried out. Multiple properties of the global market such as growth drivers, limitations, and the upcoming aspects of every section have been communicated profoundly. On the basis of these characteristics, the Photography Studio Software Market report decides the standing future of the market globally. This report wraps each and every characteristics of the global market commencing from the fundamental information of the market and moving further to different vital criteria, on the basis of which, the global market is fragmented. Main application areas of the global market are also covered based on their performance. Browse Full Report With TOC @ https://www.fiormarkets.com/report/global-photography-studio-software-market-size-status-and-146313.html The global market report wraps a nearest analysis of current rules, policies, and regulations as well as global industrial chain. Apart from this, other factors such as chain of production, goods, key producers, supply and demand for these goods, and revenue as well as price structures for global market are also wrapped in this report. The report also enumerates the properties of demand and supply, manufacture capacity, the chronological presentation, and detail analysis of the global market all over the world. For more inquiry contact our sales team at sales@fiormarkets.com"


def predict(text):

    filename_model = '/var/www/app/nb_model.joblib.pkl'
    filename_tfidf = '/var/www/app/tfidf.joblib.pkl'
    model = joblib.load(filename_model)
    tfidf = joblib.load(filename_tfidf)
    df = pd.read_pickle('/var/www/app/cleaned_df.pkl')
    dfText = df['clean_text'].values

    result = tfidf.fit_transform(dfText)
    x_text = tfidf.transform([text])

    prediction = model.predict_proba(x_text)

    print(prediction)
    return prediction


if __name__ == "__main__":
    predict(sample_text)
