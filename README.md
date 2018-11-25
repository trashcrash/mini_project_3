# mini_project_3
mini_project_1 with database</br>
mini_project_1 link is [here](https://github.com/trashcrash/EC601-P1)
## Using mysql
### Install mysql-connector
```
$ pip install mysql-connector-python
```
[Here](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html) is a simple tutorial of operating MySQL with python. 
### Install python twitter tools API
```
$ git clone https://github.com/sixohsix/twitter.git
```
Then go to the cloned directory and setup
```
python setup.py install
```
### Twitter developer credentials
In order to use twitter APIs, you will need a twitter developer account from this [link](https://developer.twitter.com/content/developer-twitter/en.html). Generate your keys and tokens and put these values in ```tweet_video_tagger.py```, line 26~29. 
### Download google cloud sdk
Follow this [link](https://cloud.google.com/sdk/install) to install google cloud sdk, and initialize it using
```
$ gcloud init
```
### Google cloud credentials
Register and log in your google cloud account, enable ```videointelligence``` API and download videointelligence
```
pip install --upgrade google-cloud-videointelligence
```
Create your credential json file and use
```
export GOOGLE_APPLICATION_CREDENTIALS=[PATH TO YOUR JSON FILE]
```
to add your json file to system environment. Then you should be good to go (Please open an issue if it does not work, it's possible that I have missed something). 
### Create a database
In order to create a database, a MySQL account is needed (or not), depending on your MySQL settings. 
```
$ python create_database.py
```
A database named pic_contents is then created. The tables are listed below. </br>
<img src="https://github.com/trashcrash/mini_project_3/blob/master/tables.png" width="300"></br>
And the table structure is like:</br>
<img src="https://github.com/trashcrash/mini_project_3/blob/master/structure.png" width="1000"></br>
### Add data
Run the program modified from mini_project_1: </br>
```
$ python tweet_video_tagger.py
```
Follow the instructions and the data obtained will be inserted into your database. 
### Search twitter name by tag
Run
```
$ python search_twitter_by_tag.py
``` 
and enter the tag of your desire. The output will be the corresponding twitter names. 
### Check statistics
Run 
```
$ python statistics.py
```
and the program will show the most frequently used tag and the number of tweets (of different accounts) included in your database. 
