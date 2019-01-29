# Catalog App

This application is a web application which shows some categories and some items belongs to those categories and codded by Yasemin Arslan.

## Application Specifications

This application works on Apache Server which is installed Amazon Web Service Virtual Machine. The application functionality is codded with Python with Flask framework with SQLAlchemy module.For the Oauth2 authentication Google Oauth2 Api is used.

## Installed Software
This project is using software below:
* Apache2 
* mod_wsgi
* Python
* Flask
* Sqlite
* Git

## IP and URL
The public IP address of the server is `35.182.241.34`
The URL of the of Item Catalog Application is `http://35.182.241.34.xip.io`

## Configurations
* This application has a user called 'grader' which has 'sudo' privilege and can only ssh to server via pubic key - private key combination.
* The remote login of the 'root' user is disabled.
* The ssh port is 2200.
* Incoming connections are allowed only for SSH (port 2200), HTTP (port 80), and NTP (port 123).
* .git file does not accessible from the browser.

## Resources
Besides Udacity Knowledge and StudentHub platforms, the websites below are used while woking on this project.
* Flask Documentation
* SqlAlchemy Documentation
* mod_wsgi documentation
* Numerous stackoverflow.com pages like [this](https://stackoverflow.com/questions/18392741/apache2-ah01630-client-denied-by-server-configuration) or [this](https://stackoverflow.com/questions/44742566/wsgi-cant-find-file-in-same-directory-in-app).
* [digitalocean.com](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
* [bogotobogo.com](https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php)

## Running the App
To run the application in the browser, open internet browser and type the application URL stated aboove to the address bar.

## Connecting to Server
In order to connect to server in the terminal get to the location where the private_key file is and then type `ssh grader@35.182.241.34 -i private_key -p 2200` and hot enter. Now you connect to the server, you can look at the configuration.


## Some Usage and Assumptions
* You need to have Google account in order to use this application
* With google authentication catalog app can retrieve the user name, however since some user accounts does not have google plus account tied to google account, the user name cannot be retrieved. In this case the email address is stored instead of username
* Category name is unique in this application so you cannot have two categories wiht the same name (eg. Tennis). If you manupulate the database_populate.py file and add two categories with same name the application will use always the forst one in the database.
