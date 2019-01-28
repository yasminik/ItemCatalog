# Catalog App

This application is a web application which shows some categories and some items belogns to those categories and codded by Yasemin Arslan.

## Application Specifications

This application works on vagrant virtual machine. The server functionality is codded with Python with Flask framework with SQLAlchemy module.
For the Oauth2 authentication Google Oauth2 Api is used.

## Running the App
<ol>
<li>Run this application you first need to run the vagran virtual machine by typing <code>vagrant up</code> then <code>vagrant ssh</code> in the command line.</li>
<li>Get to the directory of the application.</li>
<li>You need to first create the database by typing <code>python database_setup.py</code> to create catalog_app.db.</li>
<li>Populate the database by typing <code>python database_populate.py</code>.</li>
<li>Run the application by typing <code>python application.py</code>. </li>
<li>After the last step your web server starts and you can use the application from the web browser by entering web address http://localhost:8000.</li>
</ol>

## Some Usage and Assumptions
<ol>
	<li>You need to have Google account in order to use this application</li>
	<li>With google authentication catalog app can retrieve the user name, however since some user accounts does not have google plus account tied to google account, the user name cannot be retrieved. In this case the email address is stored instead of username</li>
	<li>Category name is unique in this application so you cannot have two categories wiht the same name (eg. Tennis). If you manupulate the database_populate.py file and add two categories with same name the application will use always the forst one in the database. </li>
</ol>