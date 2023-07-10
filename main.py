from flask import Flask, jsonify
import pandas as pd
articles_data = pd.read_csv('articles.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_articles = articles_data[["timestamp","eventType","contentId","authorPersonId","authorSessionId","authorUserAgent","authorRegion","authorCountry","contentType","url","title","text","lang"]]

# variables to store data
liked_articles=[]
not_liked_articles=[]

def assign_value():
  article={
    "title": all_articles.iloc[0,0]
  }
  return(article)

# method to fetch data from database
# /movies api
@app.route("/movies")
def fetch_data():
  m_data=assign_value()
  return jsonify({
    "data":m_data,
   "status":"success"
   })

# /like api
@app.route("/like")
def like_api():
  global all_articles
  like_data = assign_value()
  liked_articles.append(like_data)
  all_articles.drop([0],inplace=True)
  all_articles=all_articles.reset_index(drop=True)
  return jsonify({
    "data":liked_articles,
     "status":"success"
  })  

# /dislike api
@app.route("/dislike")
def dislike():
  global all_articles
  dislike_data=assign_value()
  not_liked_articles.append(dislike_data)
  all_articles.drop([0],inplace=True)
  all_articles=all_articles.reset_index(drop=True)
  return jsonify({
    "data":not_liked_articles,
    "status":"success"
  })

if __name__ == "__main__":
  app.run()