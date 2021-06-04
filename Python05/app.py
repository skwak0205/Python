# -*- coding: utf-8 -*-

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json

# pip install flask_cors (자바 서블렛과 연동 시 cors 에러 발생 해결 하기 위함)
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/crawling')
def result_json():
    # 제목, 별점을 {'title': 제목, 'start': 별점} 형태로 크롤링 하여
    # {'movies': [{}, {}, {}, {}, {}, ...]} 형태로 json 객체를 만들어서 리턴하자

    url = ''
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    movies = soup.find_all('dl', class_='lst_dsc')
    
    result_list = list()
    for movie in movies:
        res = dict()
        res['title'] = movie.find('a').text
        res['star'] = movie.select('.num')[0].text
        result_list.append(res)

    result_dict = {'movies': result_list}
    result_json = json.dumps(result_dict, ensure_ascii=False)
    
    return result_json


if __name__ == '__main__':
    app.run(host='localhost', port='8686')
    