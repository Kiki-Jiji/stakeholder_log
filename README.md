# Stakeholder Engagement Log

This is a web app to collect stakeholder engagement data for the Best practice and Impact Diversion of the ONS. It has been written primarily using python and the Flask framework, html, CSS (primarily bootstrap)
and javascript for web analytics (Chartjs).

## Setup

 All the instructions are given for a UNIX system. The app has been developed using Ubuntu 18.04 but it should also run on OS X. It will **not** by default run on a windows system and would rewuire additional setup not detailed here. The isntrutions assume you are using the Ubuntu Terminal for WSL or a Ubuntu system.

 First clone the repository.

'''
$ https://github.com/best-practice-and-impact/SHEL.github
'''

If using WSL it will be easier to edit the code if you save the code in the windows filesystem are access this from the Ubuntu terminal using
'''
$ cd /mnt/filepath
'''
In the repository setup a virtual envrim0poment using

'''
$ virtualenv venv
'''
Then activate
'''
$ source venv/bin/activate
'''
You will need to install FLASK and the other dependencies. These are listed in a requirement.txt file in the top level directory. You can install these all in one go into the virtual environment by using

'''
$ pip3 install -r requirements.txt
'''

You will need to create the SQL TABLES
'''
$ flask shell
$ db.create_all(
'''

use
'''
quit()
'''
to exit a python session.

## Populate TABLES
The APP using email verification so you will not be able to access the site without setting up a local email server. This is listed below. An alternative system is to manually create a ADMIn useer allowuing you tyo see the entire APP. You can do this by
'''
$ flask shell
$ you = Post(user="admin", email="admin@example.com", is_admin="True")
$ you.set_password("admin")
$ db.session.add(you)
$ db.session.commit()
'''

There will now be an ADMIN user with the username admin and the password admin. All the password are **HASHED**.
You will also need to populate the POST table, as this displays upcoming events. If empty the index page will **not** load as the site uses negative indexing to display the last three events.
Again, you can use the terminal to manually add values to get started.
'''
$ flask shell
$ post1 = Post(body="event1", location="Place1", date="time1")
$ db.session.add(post1)
$ db.session.commit()

$ post2 = Post(body="event2", location="Place2", date="time2")
$ db.session.add(post2)
$ db.session.commit()

$ post3 = Post(body="event3", location="Place3", date="time3")
$ db.session.add(post3)
$ db.session.commit()
'''

Now that the relevant tables have been populated you can load up the site. Before running it, though, Flask needs to be told how to import it, by setting the FLASK_APP environment variable:
'''
export FLASK_APP=microblog.py
'''
You can now run the web application, with the following command:

'''
$ flask run
 * Serving Flask app "microblog"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
'''
After the server initializes it will wait for client connections. The output from flask run indicates that the server is running on IP address 127.0.0.1, which is always the address of your own computer. This address is so common that is also has a simpler name: localhost. Since this application is running in a development environment, Flask uses the freely available port 5000. Open up your web browser and enter the following URL in the address field:
'''
 http://localhost:5000/
 '''
You will be taken to the log in page and can now freely explore the site. Feel free to raise any issues you find on GitHub.

## Email verification setup:
To enable email verification the following environmental variables need to be created in the terminal and exported:
 - $ export MAIL_SERVER=smtp.googlemail.com
 - $ export MAIL_PORT=587
 - $ export MAIL_USE_TLS=1
 - $ export MAIL_USERNAME=<your-gmail-username> (this can be any gmail email address)
 - $ export MAIL_PASSWORD=<your-gmail-password> (this is the password for the account)

(As the Password is then an environmental variable it will not be written in the config file.)
