from flask import Flask, render_template, request
import re
import DataCrawling
app = Flask(__name__)

#the method shows the initial index
@app.route('/')
def hello_world():
    return render_template('index.html')


# the method that called after giving the search order
@app.route('/search_post/',methods=['GET',"POST"])
def search_post():
    #This is used for hitting the search button to search on index or search page.
    #Its parameters are not shown on url
    if request.method == "POST":
        keyword = request.form['keyword']
        mKeyword = re.sub(" ","+",keyword)
        if keyword=="":
            return render_template('search.html', message="Please input keyword!")
        try:
            res = DataCrawling.main(mKeyword)
            return render_template('search.html', keyword=keyword, res=res)
        except Exception as e:
            return render_template('search.html',message="DataCrawling error!",keyword=keyword,res="")
    # This is used for using the 'related topic' hyperlink.
    # It is shown on url.
    if request.method == "GET":
        keyword = request.args.get("keyword")
        if keyword=="":
            return render_template('search.html', message="Please input keyword!")
        try:
            mKeyword = re.sub(" ", "+", keyword)
            res = DataCrawling.main(mKeyword)
            return render_template('search.html', keyword=keyword, res=res)
        except Exception as e:
            return render_template('search.html',message="DataCrawling error!",keyword=keyword,res="")




# to debug
if __name__ == '__main__':
    app.run(debug=True)