#Multi-User Blog

This is a multi-user blog using google app engine that allows users to register/login and add stories and comments to posts. Users can like/unlike users' posts and edit/delete their own posts.

My project can be viewed [here](https://shareyourstory-2017.appspot.com).

##Project Requirements

Frameworks used:

	* [Bootstrap](getbootstrap.com)
	* App is built using google app engine

Blog includes:

    * Front page that lists blog posts.
    * A page to submit story/blog
    * Story/Blog posts have their own page.
    * A page to add a comment

User's Features:

	* User's can add/edit/delete their own posts and add/edit/delete comments
	* User's can like other posts
	* User's cannot like their own post
	* User's cannot delete other user's posts and comments

Registration:

    * Allows a new user to register
    * Displays error messages if they do not sign up properly

Login:

    * Allows registered users to login and also logout
    * Displays error messages if invalid username/password


###Instructions to set up project

1. To run this project, install [python 2.7](https://www.python.org/download/releases/2.7/) if needed. 

2. Install [google cloud sdk](https://cloud.google.com/?utm_source=yahoo&utm_medium=cpc&utm_campaign=2017-q1-cloud-na-gcp-bkws-freetrial-en) into your system.

3. After installation, type in dev_appserver.py into google cloud then add the path of the **app.yaml** document and click enter.

4. Open [localhost8080](http://localhost:8080/) on your browser and you should see the project running. 
