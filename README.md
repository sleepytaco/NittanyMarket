# Nittany Market Phase 2 Progress Review

This project is part of the Phase 2  progress review for the NittanyMarket project. This project consists
of an already populated `db.sqlite3` file (using the provided dataset folder), and has the login and logout features implemented. This project has been run and 
tested on Windows 10 using Python3.9.

## Setting up the project

Make sure you have Python3.6+ installed on your computer, and 
follow these steps to set it up NittanyMarket locally and get it running:
- Open the terminal in the project root folder (i.e, where the `manage.py` file is).
- Create a virtual environment by running `python -m venv venv` in the terminal.
- Activate the virtual environment by running `.\venv\Scripts\activate`
- Once in the virtual environment, you should see a `(venv)` on your terminal screen. If 
you do, that means you have set up the venv correctly and activated it.
- Next, we install all the dependencies required for NittanyMarket project to run.
Run `pip install -r requirements.txt` to install all the required dependencies into our created
virtual environment.

## Running the project

Make sure you have set up the project by following the above instructions.
By now, you must be inside the virtual environment and have installed all the 
dependencies. Do the following to run the project:
- Run the following to start the server: run `python manage.py runserver`
- You can then access the website on your web browser by visiting `http://127.0.0.1:8000/`
- Please check the Notes section if you would like for to see instructions for checking out the tables in the database.

## Notes
- `database_population_script.py` is a script I wrote to populate the `db.sqlite` file with data
from the `dataset` folder. 
- The `db.sqlite3` file **has already been populated prior to submission.** 
  - I used the Django provided User table as it already contains the email and password fields. Furthermore, using 
  the default provided User table has its advantages as I can use Django's in-built features for authentication.
  - The User table takes about ~25 mins to get populated because it hashes 6000 raw passwords before they are stored in the User table.
- To **view the contents of the tables** I created, you can use the Django admin interface.
  - Make sure you **open a new incognito window** on your browser and visit `http://127.0.0.1:8000/admin`. This is because 
  the admin account is a completely different from the users dataset.
  - I have already created an admin account. To log in to the admin interface, use the following credentials:
  ```
  username: admin
  password: 123
  ```
  - Once logged in, on the left side you should see the names of the tables
  I created. (Please ignore the Groups table, it is a default one Django created)