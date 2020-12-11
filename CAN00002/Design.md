The design document discusses the project’s technical implementation details and reasoning behind design decisions.
This project is written in Python and based on the database of google scholar.
There are three parts of the program structure:
 
#Data Crawling
We use the ```urllib``` package to get data from webpages.
Methods:
###askURL
Input a URL Parameter (e.g. https://www.google.com/）
Use ```urllib.Request``` to generate a request.
Use ```urllib.urlopen``` to send the request to the designated website and acquire responses.
Use ```.read()``` to read page contents.

 
#Data Analysis
Collect the following information of each article on page 1-10 of the search results:  
__article title，article URL, the year of the article, the number of cite of the article, the URL of citation, the number of versions, the URL of PDF__
  
Collect the following items of the search results:  
__The total number of research result, the related researching__

Use ‘normalize’ method to Weight the year of the article, and the number of cite of the article, so that their data is mapped on the interval of 0-5.  
The principle of this method is as follows, where X represents each data and min and Max represent the minimum and maximum values of the total data respectively.  

The weighted algorithm is used to select the best five articles, the principle of the weight for each article is
7 * the number of citation + 3 * the number of year.
Then, Choose the five items with the highest scores\


Collect the following information of each of the top 5 articles:  
__The normalized  year of the article in overall.__  
__The normalized citation of the article in overall__  
__The normalized  year of the article in top 5__   
__The normalized  citation of the article in top 5__   
__The number of versions of the articles__  
Return the following of items in the end: 
The information of the top 5 articles, the most citation of the articles, the total number of the research results, the average year, the average cite, the total number of the citation(Divide by 9000 for curve), the related researching.
#Web design
###front-end
 we use a moduled UI generator named Layui. We select what we want for the page from modules and directly download python code for it.  It is convenient to use and has an outstanding UI outlook. 
 
###charts
we generated, we also use a moduled generator named Echarts to draw the radar graph.  The reason is the same as why we selected moduled UI.
 
###web frame
Flask is utilized for our project. We add the html downloaded to the template folder and use render to generate the whole page. Flask is a very flexible and light frame to use since we only build light websites.
 
Here we only talk about our code implementation which is app.py: 
 
Firstly we load our index.html, using ```hello_world```. 
 
When search button is touched, the customer is submitting a form. We get the keyword in it and input it into our programme using ```keyword = request.form[‘keyword’]```.  
The crawling part will launch if the input is not null. Then the result will be shown with a template of the downloaded html. If the “related topic” is searched by clicking, ```get``` method will be called. Otherwise, we will use ```post``` .
 
Note that because developers are in China and cannot easily overcome the Great Wall, so we used some local built-database to test, which is SearchSystem.py


To run the program successfully, we add ```try...except``` to capture errors.