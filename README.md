<h2>Happy Dental - Dental Booking App</h2>

- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
- [**Design and Site Structure**](#design-structure)
  - [**Functional Structure**](#functional-structure)
  - [**Wireframes**](#wireframes)
- [**Features**](#features)
  - [**Responsive Design**](#responsive-design)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Frameworks and Libraries**](#frameworks)
  - [**Tools**](#tools)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
  - [**Code**](#code)
  - [**Content**](#content)
  - [**Media**](#media)
  - [**Inspiration**](#inspiration)
  - [**Acknowledgments**](#acknowledgments)


  
# Portfolio Project 4 - Happy Dental reservation system  
![](static/assets/img/amiresponsive-light.png)

The deployed [HAPPYDENTAL]() app.

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

![Home page](![homepage](https://github.com/dsouths/happydentalapp/assets/105642587/9c671901-20f1-4833-84fb-ffde7c543783)

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


