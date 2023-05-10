 
<h2>Portfolio Project 4 - Happy Dental - Dental Booking App</h2>

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
- [**Design and Site Structure**](#design-and-site-structure)
  - [**Functional Structure**](#functional-structure)
  - [**Wireframes**](#wireframes)
- [**Features**](#features)
  - [**Responsive Design**](#responsive-design)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Frameworks and Libraries**](#frameworks-and-libraries)
  - [**Tools**](#tools)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Media**](#media)
  - [**Inspiration**](#inspiration)
  - [**Acknowledgments**](#acknowledgments)




![happydental - amiresponsive](https://github.com/dsouths/happydentalapp/assets/105642587/18ad7c68-b626-4123-a8cb-814721b38589)


The deployed [HAPPYDENTAL](https://happydental.herokuapp.com/) app.

The [GitHub repository](https://github.com/dsouths/happydentalapp)



## Project goals

This is my 4th project under the Code Institute Diploma in Full Stack Development program.
This website is a fictional dental practice called HAPPYDENTAL. It is designed to be responsive and accessible on a variety of devices for the ease of use of the site by potential users.


## UX (User Experience)

### User stories

#### First time visitor goals

As a first time visitor, I want:
* understand the main purpose of the site,
* able to easily navigate throughout the site,
* able to register a user account to access all content without restrictions,
* able to reserve a day and time for a treatment with a chosen dentist, view booking details and make changes to created bookings and delete my bookings,
* able to log out of my user account.
       
        
#### Returning and frequent user goals

As a returning user, I want:
* to sign in to my user account,
* to book a treatment with chosen dentist, 
* to view my booking details, 
* to edit my booking details or delete them.
* to sign out of my account to keep my account safe.


#### Site Administrator goals
As a Site Administrator I would like to be able to create, view, edit and delete booking data.    

[Back to the top](#table-of-contents)

#### Agile tools

I used a [Kanban board](https://github.com/users/dsouths/projects/3/views/1) for the development of this project, which made it possible to break down the project execution into subtasks and make it easier to complete and track project progress.  This is located in the GitHub Projects section

#### Design and Site Structure

The site was based on the Gobarber template from the Figma Community site. The look of the site & fonts for the home page were borrowed from the template.
The main page layout can be seen below:

<details>
<summary>Happy Dental website design template </summary>

![Home page](https://github.com/dsouths/happydentalapp/assets/105642587/9c671901-20f1-4833-84fb-ffde7c543783)

</details>
<br />

### Functional Structure

**Home page:** The home page contains a menu, clickable logo (returns to homepage) and an image that gives the user an idea of ​​the type of service provided i.e. a dental booking website. In the middle of the page there are links to register a new user or login for an existing user.

Signup and login are also available from the navigation bar.

**Signup page:** The user must create an account to make a reservation.
To do this, they are asked to fill out a form on the page with the required fields: username and password. There is also an optional email field.

**Login page:** A username and password are required to log in existing users.
The user can use the navigation menu or the link in the center of the home page.
After a successful login, the user receives a message prompt in the middle of the screen and is redirected to the page with their reservations. If the user has no bookings, then they see a message saying they have no bookings & gives a link to make a booking.

**Logout page:** Logging out of the account is done through the menu, after which the user is redirected to the logout page where they must confirm their request to log out of the account. After a successful logout, the user is returned to the home page and receives a message in the middle of the screen.

**Services page:** The page displays the services/treatments provided & cost of each service.  I have only included a small sample of possible treatments available at the dentist for illustrative purposes, this can be increased upon request of the owner of the dental booking app/dental surgery.

Clicking on the price of the selected service redirects the authorized user to the service booking page. An unauthorized user is prompted to register or log into an account before making a booking.

**Booknow page:** The Booknow page is only available to authenticated users.
The user is asked to fill out a form with the required fields - name, phone, service, preferred dentist, time and date, and an optional field - email.
After filling out the form, the user is redirected to the page of current bookings.

**Booking page:** Only authenticated users have access to the Booking page. The link to this page becomes visible in the navigation menu once a user is authenticated. Booking page shows to user information about made bookings and contains Change button and Delete button for manage booking.

**Change booking page:** This page is available only to authenticated users and has the same functionality and form as the Booknow page, where users can change booking details.

**Delete booking page:** This page is only available to authenticated users and has the same functionality and form as the Booknow page, where the user can change the booking details. The user has the ability to delete theur order by selecting the Delete button on the Booking page. After that, they will be redirected to the delete page where they need to confirm their request. After successfully deleting the booking, they will return to the Booking page and receive a message at center of the screen.

If the user changes their mind, they can return to the page by clicking on the Back to my Bookings button.

[Back to the top](#table-of-contents)

### Wireframes


**For Mobile view and small screens**

<br />

**For Desktop view**

## Features

### Navbar

The navigation bar is present on all pages of the site to give uniformity to all pages & allow the user to easily navigate the website. The nav bar changes depending on whether the user is a guest or an authorized visitor and is an adaptive element. On mobile screens it collapses into a hamburger icon.

Navigation bar for an unauthorized user.

![Main navigation](https://github.com/dsouths/happydentalapp/assets/105642587/341d0e8d-144c-452e-8c49-1edb015dbb8b)

Navigation bar for an authorized user, menu items My Bookings and Logout are available.
![Authenticated user's Navigation](https://github.com/dsouths/happydentalapp/assets/105642587/8329b5b9-5671-4a50-afc3-bf46c2d00ce1)

### Home page

On the Home page a user can create an account or Login from the menu or using links provided under the logo. 
![Home page](https://github.com/dsouths/happydentalapp/assets/105642587/0d9abcb6-c36b-4196-b2cb-4dce5f91c737)

### Sign up page

To create an account user should fill in form provided on Sign up page.
![Sign up page](https://github.com/dsouths/happydentalapp/assets/105642587/cc3b4213-fa4e-4d3a-8adb-36a4a35c243e)

### Login page

To login the user should enter credential data that was used during sign up process.

![Login page](https://github.com/dsouths/happydentalapp/assets/105642587/ce27ffa0-ee65-4478-b0bc-3c2fe889aaee)


## Treatments/Services page

The Services page provides information about all available barbershop services. User also can book necessary service straight from the Services page by clicking on the services price.

![treatments page](https://github.com/dsouths/happydentalapp/assets/105642587/5c3ff8d5-1e7a-4cac-84cf-3ba808051abe)


## Book Now page

The Book Now button has a hover effect to provide a better user experience by creating feedback/call to action:


![Book Now button](https://github.com/dsouths/happydentalapp/assets/105642587/0823f3e3-9527-48ac-adb2-4730f2a4330c)


Users must be logged in to make a booking. To book a service, the user must fill in the required fields in the form: name, phone, preferred dentist, services, date, time and an optional email field. The date field will not allow user to make a booking on a Saturday or Sunday as the dental practice is closed, & would create issues if user made a booking when the dentist was not there. I have created functionality when creating a new booking that a user cannot double book a dentist if they are already booked by another user.

#### Book Now page for the logged user

![book_now page (AUTHORISED USER)](https://github.com/dsouths/happydentalapp/assets/105642587/36ca6e0a-91bc-49bc-9874-3b11357de2db)

If the user is not authenticated then the user will be shown a message that the user has to sign up or login.


## Booking page

The Booking page is available only to authorized users. The booking page displays the following data: order ID, date, time, service name and cost of the booked service.


![Booking page](https://github.com/dsouths/happydentalapp/assets/105642587/c55d3c47-4d77-49bf-8a3f-baaaf24a631f)


If the user has not yet booked any services, then the user will be shown a message that the user has no bookings at the moment and there is an opportunity  to make a booking.

![Booking page message](https://github.com/dsouths/happydentalapp/assets/105642587/68d8650a-6fa4-40dd-be69-b9914fcbfc97)


## Change booking page

Each booking can be changed or deleted. The user must be authenticated in order to access the change his bookings.
The change booking page can be accessed for a specific booking. The page Change booking contains an auto-filled booking form. The user can change the fields at his discretion.

![edit your booking](https://github.com/dsouths/happydentalapp/assets/105642587/24a07b46-a93f-4907-8105-a1c1d7459ec7)


## Delete page

The User must be authenticated to delete the booking. The Delete booking page provides two buttons: 'Yes, delete booking' and 'Back to my bookings' if the user changes his mind. 
Deletion will delete the only specific booking for the user.

![Delete booking page](https://github.com/dsouths/happydentalapp/assets/105642587/d5e30c51-ac44-40f1-865c-28b53161f54a)


## Logout page

An authenticated user can logout from account by clicking the Logout button, after which the user will be redirected to the Logout page where the user needs to confirm to logout from account to prevent occasionally log out of user account.

![Logout page](https://github.com/dsouths/happydentalapp/assets/105642587/596d6514-881f-4908-b358-28a23f77eab3)

### Responsive design
The site has been designed to be responsive and adapted for desktop and mobile use.
The project has been tested using a multi-device emulator with different screen sizes in the Google Chrome Developer Dashboard.

## Future features

- payment functionality to allow dental practice to take a deposit &/or full payment from each patient/user. 
- create & populate a google sheet to allow each dentist to see patients booked in for each timeslot on each day
- booking confirmation by email & text if requested

[Back to the top](#table-of-contents)

## Technologies Used

### Languages
  - Python
  - HTML5
  - CSS3

### Frameworks, Libraries, Programs

  - [Django](https://www.djangoproject.com/): python framework used to create all the backend 

### Database:
  - [PostgreSQL](https://www.elephantsql.com/): the database used to store all the static data such as image files.
  
### Programs & Tools

- [Google Fonts:](https://fonts.google.com/) -  incorporate font styles.  
- [Font Awesome](https://fontawesome.com/): - create the icons used on the website.
- [Bootstrap](https://getbootstrap.com/) - create the front-end design.
- [Gitpod:](https://Gitpod.io/) - IDE to commit and push the project to GitHub.
- [GitHub:](https://github.com/) - version control system to manage the code
- [TinyPNG:]() Was used to reduce the size and weight of images and optimizing interaction with the site 
- [Am I Responsive](http://ami.responsivedesign.is/) - generate an image showcasing the website's responsiveness to different screen sizes 
- [Pip3](https://pypi.org/project/pip/) - package manager to install Python modules and libraries.
- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/): "Green Unicorn" is a Python Web Server Gateway to translate HTTP Requests for Python to understand.
- [Spycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter so I can manage the Database in Python. 
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media.
- [Heroku](https://dashboard.heroku.com/): the hosting service used to host the website.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/open/): - debug the website.
- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
- [Github Projects and Kanban board](https://github.com/users/dsouths/projects/3/views/1) - track the progress of the project in general and of every application in the project.
- [Free grammar checker](https://www.zoho.com/writer/free-grammar-checker.html)


### Manual Testing

#### Device Testing

The Project was tested using a multi-device emulator with different display sizes in the Google Chrome Developer Dashboard.

The following devices have been tested:

- Dell Inspiron 27" (Desktop)
- iPad Pro (Tablet)
- iPad Air (Tablet)
- iPad Mini (Tablet)
- Galaxy Tab S4 (Tablet)
- Nexus 7 (Mobile)
- Nokia N9 (Mobile)
- iPhone 5/SE (Mobile)
- iPhone 4 (Mobile)

#### Browsers Tested

Testing has been carried out on the  following browsers: 
  - Google Chrome
  - Firefox
  - Microsoft Edge

The site was constantly tested during the process of creating the site in the Gitpod Environment and the deployed site on Heroku was also tested in terms of user experience.
The available functionality and user experience is reflected in the table below.

| Goals/actions  | As a guest | As a logged user  | Result | Comment |
|--|:--:|:--:|:--:|--|
| I can use menu and navigating through pages | &check; | &check; | Pass | Click on menu item redirects to appropriate page |
| I can see the home page | &check; | &check; | Pass | |
| I can see the Services page | &check; |&check;  |  Pass| |
| I can see the Sign Up page | &check; |&check;  |  Pass| |
| I can see the Login page  | &check; |&check;  |  Pass| |
| I can see the Logout page  | &check; |&check;  |  Pass| |
| I can click the Book Now button  | &check; |&check;  |  Pass| Redirects to the page with a message that the user must register or log in for guest or shows up form for authorized user |
| I can see the Booknow page | &cross; | &check;  | Pass |A page is displayed with a message that the user must register or log in  |
| I can fill fields in the form the Booknow page | &cross; | &check;  | Pass |This page and form are available only to authorized users |
| I can see the Bookings page   | &cross; | &check;  | Pass | This page is available only to an authorized users|
| I can see the Change booking page  | &cross;  | &check;  | Pass | This page is available only to authorized users|
| I can edit booking in the form on the Change booking page  | &cross;  | &check;  | Pass |This page is available only to authorized users ||
| I can see the Delete booking page  |  &cross; | &check;  |Pass  | This page is available only to authorized users |
| |

<br/>

## Validation

### HTML Validation:

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.  I had an issue with W3 validator not recognizing Django code such as {% load static %} so I used the function CTRL + U to get the source code of my website & check it for errors using W3 validator.  I did this as it created errors and warnings in the reports about unclosed elements and tags, incorrect values and types of elements, unnecessary trailing slashes. All errors and warnings were corrected when validating the source code of each page

Initial errors when using W3 Validator to validate Django code

<details><summary>W3 Errors due to Django code</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/b4b90bd3-e327-4f51-946f-fa72f07db9f6)

</details>



<details><summary>Home page</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/59231143-1efd-4628-b8e5-d00d48aea2b7)

</details>

<details><summary>Services page</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/60c46fc9-3fc4-49dd-a007-1df1a4a654b6)

</details>

<details><summary>Sign up page</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/7643d8c8-adf0-4052-b341-7c688ef48519)

</details>

<details><summary>Login page</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/105d909f-2939-4c6f-9d9b-4fd6105ac970)
</details>

<details><summary>Book Now page for authorized users</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/b5306220-9472-48f7-9f37-31f12f55f544)
</details>

<details><summary>Change booking page</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/5863633a-a58f-48dc-9ea0-d5fc93c3055d)

<details><summary>Delete booking page</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/618c1ce6-edb4-4dd9-90d1-85ac92491922)

</details>
 
<details><summary>Logout page</summary>

![](https://github.com/dsouths/happydentalapp/assets/105642587/f8baf4f6-a1c2-41f1-a3c3-ebde8607a124)

</details>
