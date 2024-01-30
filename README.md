# Capstone Project - Task 10 Consolidation
<sub>Level 3 Task 10</sub>
## Table of Contents

1. [Introduction](#intro)
2. [Project Description](#description)

   2.1. [Running the Project on your local device](#local)
  
   2.2. [Running the Project using Docker](#docker)
  
3. [What Changes can be made to Imporve the Website](#changes)
4. [Conclusion](#conclusion)
5. [References](#references)

## 1. Introduction <a name ="intro"></a>
The final practical capstone, using an old project from a previous task.The project was based on an online bookstore, where a user previous could purchase books to read on their account. Purchasing books is not available. You can find the documentation of the project, in the docs folder, then nagivate to _build folder, html folder, then click on index.html.

In the project uses the following langauges:
* Python
* HTML
* CSS
* Django
* Bootstrap

There are two ways to run the project, you can create a virutal enviroment on you device, or you can run the project using docker.

## 2. Project Description <a name = "description"></a>
The project was based on an another task about a store, in this case a bookstore, to add items on their online webpage of the products that are on sale. The project went through a number of changes before this project. The website consists of a home page, a blog, a library, a login and a sign up page. The user can navigate to these pages using the navigation bar provided at the top.

If you look on the navigation bar of the website, you will see links to other webpages:
* Home (current page)
* Blog
* Library
* Log in
* Sign up

The home page is the current page that you are on. 

![Home page](https://github.com/Icyfire315/capstone-project-10/blob/main/myWebsite/assets/homepage.PNG) <br>

The Blog consists of post, posted by the admin, about changes, new addtions, and removals of any book or features on the website.

![Blog page](https://github.com/Icyfire315/capstone-project-10/blob/main/myWebsite/assets/blogpage.PNG) <br>

The Library is where current and new books will be made available to user who have created accounts.

![Library page](https://github.com/Icyfire315/capstone-project-10/blob/main/myWebsite/assets/librarypage.PNG) <br>

The Sign in page is where the user creates an user account. The Log in page is where users, who have created accounts, log into their accounts.

![Signup page](https://github.com/Icyfire315/capstone-project-10/blob/main/myWebsite/assets/sign_up_page.PNG) <br>

The Log in page is where users, who have created accounts, log into their accounts.

![Login page](https://github.com/Icyfire315/capstone-project-10/blob/main/myWebsite/assets/login_page.PNG) <br>

The Catalogue is a dropdown link, the navigation items do not link to another webpages. The only pages available for you to access is Home, Blog, Sign up, and Log in.

### 2.1. How to run the project on your local device <a name = "local"></a>
In order to run the project, you will need to create a django enviroment. First you need to create a virual enviroment, on your device, to run the project. Then install the packages, listed in the requirements.txt file, to ensure that the project runs.

Once you have installed all the neccessary packages and created a virual enviroment, migrate the database. Run the project then enter http://127.0.0.1:8000/home/ to redirect you to the home page of the website. You need to have access to the secret key, you will find it in a text file on dropbox.

To access Library do the following:

* Step 1: Click on Sign up to create an user account. You will be asked to enter the following:
    *  First name
    *  Username
    *  Password
    *  Email address
  Once you have filed all the fields, click on the Sign up button. You will be redirected back to the home page.
* Step 2:  Once logged you can click on the Library page to view books on display (sorry for the terrible titles).

If you have already have an account do the following:
* Step 1: On the navigation bar click on Log in, enter your username and password. Then click on Log in button.
   
* Step 2: Then click on Libray to view the books on display (again sorry for the terrible titles).

If you try to click on Library you will be redirected to the Log in page, if you don't have an account click on Sign Up Now to create a user account.

### 2.2. How to run the project using Docker <a name = "docker"></a>
The project has been dockerized, so you won't need to create a virtual enviroment to run the django project. First, you will need a docker account, and you might need to install docker. Next pull the docker repo to run the program. Enter http://127.0.0.1:8000/home/ into the browser to see if it works.

## 3. What Changes can be made to Imporve the Website <a name="changes"></a>
Things I could add to improve the website:
   * Comment section: I could add a comment section to the posts to allow users to comment about the post.
   * Polls: To make the website more engaging I could add polls.
   * Forgot password: for users who have forgotten their password to change their password.

## 4. Conclusion <a name = "conclusion"></a>
This website has gone through so many changes, some of these changes have improved the project by preventing users from accessing pages they should no access, creating poll questions and and their answers, creating blog posts, and (the best part of the project) creativity.

## 5. References <a name = "references"></a>
* PyLessons, 2022. Django messaging tool. [Online] Available at: https://pylessons.com/django-messaging [Accessed 25 December 2023].

* PyLessons, 2022. User login and logout. [Online] Available at: https://pylessons.com/django-login-logout [Accessed 25 Decemeber 2023].

* PyLessons, 2022. User registration & log in. [Online] Available at: https://pylessons.com/user-registration [Accessed 25 December 2023].

* GeeksforGeeks, 2022. How to User model Django?. [Online] Available at: https://www.geeksforgeeks.org/how-to-use-user-model-in-django/ [Accessed 23 Decemeber 2023].

* Thaqi, D., 2021. Create a Blog with Django. [Online] Available at: https://medium.com/geekculture/create-a-blog-with-django-60f529f1d8b6 [Accessed 28 December 2023].

* Anon., 2022. What is a "slug" in Django?. [Online] Available at: https://sentry.io/answers/slug-in-django/#:~:text=Slug%20is%20a%20term%20from,in%20a%20human%2Dfriendly%20form. [Accessed 28 December 2023].

* django, n.d. Using the Django authentication system. [Online] Available at: https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator [Accessed 29 December 2023].

* Jaya, 2023. How to use Login Required in Django: Restrict View Access. [Online] Available at: https://studygyaan.com/django/how-to-restrict-access-with-django-login-required-decorator-function [Accessed 2 January 2024].

* Perales, S., 2021. how to restrict pages in Django? if "@login required(login_url='login')" does not work. [Online] Available at: https://stackoverflow.com/questions/69099712/how-to-restrict-pages-in-django-if-login-requiredlogin-url-login-does-no [Accessed 30 December 2023].

* Dindi, S., 2022. How to Dockerize a Django App. [Online] Available at: https://www.makeuseof.com/dockerize-django-app/ [Accessed 26 January 2024].
  
* Ahtisham, 2019. How to set Django allowed_hosts?. [Online] 
Available at: https://stackoverflow.com/questions/54504142/how-to-set-django-allowed-hosts
[Accessed 24 January 2024].


