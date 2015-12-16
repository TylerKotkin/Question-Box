# <div align="center">Question Box</div>

Question Box is a web application that allows users to post questions, answer questions and rate answers given by other users.

## <div align="center">Instructions</div>

* Before the user can run the Question Box application, the user must first clone the `question-box` repo onto their computer. The user must have Python 3 installed.
* To properly run the application, the contents of requirements.txt must be installed.
  * After navigating to the folder containing `requirements.txt`, enter `pip install -r requirements.txt` on the command-line to download the contents of requirements.txt.
* This application is set up to run on PostgreSQL. The local database is named `question_box` with a user of `question_box` and a password of `question_box`. This configuration can be changed in the `settings.py` file. Instructions for setting up PostgreSQL can be found [here](https://github.com/tiyd-python-2015-08/course-resources/blob/master/week7/PostgreSQL-and-Django.md).
* To properly configure the database, the user must navigate to the `question_box` folder that contains `manage.py` and enter `python manage.py migrate` on the command-line.
* The user must run a local server in order to use the application. After navigating to the `question_box` folder which contains `manage.py`, enter `python manage.py runserver` on the command-line to start the local sever. The application can now be accessed by the users web browser at `http://localhost:8000/`.
