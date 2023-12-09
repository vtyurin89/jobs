# JOBS
#### Video Demo: <https://www.youtube.com/watch?v=eVhgddtPeFM>
#### Description: A job board website which allows users to either post job ads (as employers) or search for jobs that they need.

# Distinctiveness and Complexity

#### Jobs is basically two web applications in one! Depending on what type of account the user creates (Employer or Jobseeker), the website will behave in two entirely different ways.
#### Jobseeker account allows the user to *create and edit resumes, search for job postings, add job postings to favourites and apply for job positions*.
#### Employer account allows the user to *create job postings, archive job postings which are no longer relevant and receive notifications when another user applies for a job*.
#### Jobs is not similar to any other projects that I worked on during CS50 Web course. Jobs is not a social media app and not an e-commerce website.
#### As for complexity, I used Django with 9 models (some of which are reasonably complex), several javascript files on the frontend. Some of the views utilize quite complex queries with an unspecified number of arguments. The web application has responsive design and adjusts to different screen sizes.

# Technologies

- Python
- Django
- SQLite3
- JavaScript
- HTML
- CSS
- Bootstrap 5

# Features

### Login / Register Page

The users need to create an account and log in to use the application. 

The register page utilizes javascript to switch between two forms: Jobseeker form and Employer form. After creating a user account, the application will automatically create an additional profile of either a Jobseeker or Employer and redirect the user to index page. From now on the user will be considered, respectively, as a Jobseeker or Employer.

If the user is an Employer, they will need to choose Company name. The company name will be displayed on the page of every Job ad they create.

If the user is a Jobseeker, they may specify their country and city of residence (although it's not required). 

The Jobseeker can choose one of 7 countries:

 - Russia
 - Kazakhstan
 - Belarus
 - Uzbekistan
 - Azerbaijan
 - Georgia
 - Kyrgyzstan

The register page creates a dynamic javascript dropdown when the user is choosing the city: it fetches the list of cities from Country State City API and changes dynamic dropdown depending on what the user types in.

If the account was not created on the register page (for example, by using the command 'createsuperuser'), the application will create a Jobseeker profile.

### Index Page

The content of the index page will change depending on the status of the user.

If the user is an Employer, the front page will show a list of recently created job postings and some simple statistics: the number of created vacancies and the number of received notifications.

If the user is a Jobseeker, the front page will be a little bit more complex.

Depending on the city chosen during the registration the application will get 12 most recent job postings in the selected location as well as a list of relevant industries. If the user changes the city on the settings page, the job postings and relevant industries on the front page will change accordingly.

### Create a job posting (Employer)

The Employer can create a new job posting by filling the form.

### My job postings (Employer)

The Employer can observe the list of all job postings they created. The list also shows which job postings are still active and which were archived. Pagination is implemented on this page.

### My notifications (Employer)

Here the Employer can find the list of all notifications they received. Each notification includes the name of the vacancy, the title of the resume received and a timestamp. A notification is automatically created each time a Job Seeker applies for a job by sending resume.

### Job Posting Page (Employer and Jobseeker)

Both Employers and Jobseekers can read the contents of the Job posting, and they can interact with this page in different ways.

If the Job posting was archived, nobody can interact with it - it will just be marked as "archived".

The Jobseeker can Like or Unlike the Job posting by pressing the heart button - this will either add the job posting to their favourites or remove it from favourites. The button sends fetch requests using JavaScript code.

The Jobseeker can also apply for a job by pressing the "Respond" button. If the Jobseeker hasn't created any resumes, they will be redirected to the Resume creation page. If the Jobseeker created one or several resumes, they can choose a resume in the dropdown list and send it. The Employer that created the job posting will receive a notification.

The Employer that created the Job posting can archive it by pressing the "Archive" button. The Job posting will be archived and forever removed from the search page of Jobseekers.

### Create a resume (Jobseeker)

Jobseekers can create a new resume by filling a form.

### View my resume (Jobseeker)

This page is fairly complex. The user can read the contents of their resume and also press the links to edit three main parts of it:
 - Edit main info (name, age, location, etc.).
 - Edit education.
 - Edit work experience.

### Edit main part of the resume (Jobseeker)

The user can edit the resume by filling a form. 

### Edit education in the resume (Jobseeker)

The education part is divided into blocks. For example, If the user graduated from Yale and Harvard, they can create two blocks. The JavaScript code on this page allows to dynamically create new blocks or delete the existing ones. 

### Edit work experience in the resume (Jobseeker)

Same as education, work experience part is also divided into blocks which can be dynamically created or deleted thanks to Javascript code.

Each work experience block is basically a job with a start date and an end date (or without an end if the user is still employed). The application will arrange all of them in chronological order on the resume page.

### My resumes (Jobseeker)

The idea behind this application is that each Jobseeker may want to apply for different jobs and therefore need different resumes. These resumes may have different titles and include different info. On this page the user can see the list of all of their resumes and press a link to go to the page of the corresponding resume.

On this page the user can also delete any resume forever.

### Selected (favourite) job postings (Jobseeker)

If the Jobseeker liked a job posting, it will be added to this page. The Jobseeker can observe the list of their favourite job postings and unlike the ones which no longer seem interesting. The like\unlike is implemented with JavaScript, so the contents of the page will change after a manual refresh.

### Search (Jobseeker)

This page includes a search bar and several filters so that the Jobseeker could find their dream job! The search result will never include archived job postings.

The filters are:
 - Job type (remote, part-time).
 - Country and city.
 - Industry.
 - Salary level.
 - Exclude words.

The user can apply one or several filters to find a job posting which satisfies all of their requirements. Also pagination is implemented on this page to split the search results.

### Edit profile (Jobseeker and Employer)

Both Employers and Jobseekers can edit their main profile information.

# Files information

 - utils.py includes the additional functions which are used in views.py: country_name_by_ISO_3166_1_alpha_2_code(), salary_radio_value(), get_filter_kwargs(), get_excluded_clauses(), calculate_age(), generate_post_dict().
They are mostly used in queries.
 - forms.py includes 4 Django forms which are used to create corresponding models.
 - Templates folder includes all the html temlates.
 - Static folder includes CSS file and several js files which run JavaScript code in django templates:
   - create_job_posting.js - creates dynamic city dropdown in create_job_posting.html.
   - edit_resume_education.js - creates and removes education blocks.
   - edit_resume_work_experience.js - creates and removes work experience blocks.
   - favourite_job_postings.js - does fetch requests to add a job posting to favourites or remove it from favourites in favourite_job_postings.html.
   - job_posting.js - does fetch requests to add a job posting to favourites or remove it from favourites in job_posting.html.
   - register.js - switches between Employer register form and Jobseeker register form, also creates dynamic city dropdown in register.html.
   - resume_main.js - creates dynamic city dropdown in resume_main.html.
   - search.js - creates dynamic city dropdown and does fetch requests to add a job posting to favourites or remove it from favourites in search_for_jobs.html.
 - requirements.txt includes the project dependencies.

# How to run the application

 - Install project dependencies by running 'pip install -r requirements.txt'
 - Make and apply migrations by running 'python manage.py makemigrations' and then 'python manage.py migrate'.
