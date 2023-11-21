# La Nonna - An italian pop-up restaurant with a familial atmosphere

La Nonna is a webpage for an italian pop-up restaurant. The atmosphere and the feel of the restaurant are based on nostalgia, family and coziness. These feelings are supposed to be invoked by the style of the home page. This is not a modern and sterile look, but rather a rustic, charming and familial feel, just like sitting in grandma's kitchen. Users can browse the menu, make a table reservation, view their reservation and reach out to staff in order to cancel or place other inquiries.

The webpage has been coded in Django, HTML and styled with CSS and Bootstrap to be enjoyed on all devices.


## Features 

On this webpage we have different feauters, such as call to actions on the index page, in case users want to make a table reservation while reading about the restaurant or wanting to browse the menu.

There is a responsive navbar, which collapses the links inside of a menu to save space on smaller devices such as mobile phones.

Otherwise users are able to make a table reservation, browse the menu in advance, view existing reservations or reach out to staff in case of needing help or wanting to cancel their reservation.

### Existing Features

- __Navbar__

  - The navbar has been designed with Bootstrap, making it responsive even for smaller devices. The esthetics are supposed to give a rustic homey feel, with the darker wood background. The logo and the links are kept white for contrasting and readability, highlighting the them when the user is hovering over them and when being on the active page.

![Navbar laptop](/static/assets/images/index-laptop.png)
![Navbar laptop](/static/assets/images/index-mobile.png)

- __Call to Action__

   On the index.html there are 2 calls to action, one for browsing the menu and one for making a reservation. The change color when hovering over them.
  
  ![CTA](/static/assets/images/cta.png)

  ![CTA](/static/assets/images/cta-hover.png)

- __Menu__

  The menu is designed to be simple and with good readibility. The database model for the menu was created in Django. Staff/admins can easily edit the menu on the admin panel and and exchange dishes for new ones. I chose to have the courses as choices so that staff can categorize meals depening on which course it is.

  ![Menu frontend](/static/assets/images/menu-frontend.png)

  ![Menu backend](/static/assets/images/menu-backend.png)

- __Book a Table__
 
  This page lets the user make a table reservation. In the backend a database model with 2 choice fields was created in order to let users choose, which time slot and how many people are supposed to dine. I chose for the email address to be required as an unique value, so that people cannot make several reservations in the same name. For special requests the user is prompted in the frontend to fill in the contact form. A link is provided.

  ![Front end](/static/assets/images/book-table-frontend.png)
  ![Model](/static/assets/images/book-table-model1.png)
  ![Model](/static/assets/images/book-table-model2.png)

  In the views I decided to check so that users cannot book the same table at the same time and date as another user. If the user chooses the same date and time as another user, they will be redirected to the booking_full.html, prompting them to choose another time and date. This is supposed to be improved upon later on, where only the available time slots for the specific date are supposed to be shown, improving the user experience.

  ![Booking full](/static/assets/images/booking-full.png)

  When successfully making a table reservation, the user will be redirected to another page, showing all the details.

  ![Booking Success](/static/assets/images/booking-success.png)

- __View Reservation__

  The view_reservation.html lets users see their reservation details. It only requires an email adress in order to keep a simple for users. I chose against users being able to making a profile and being able to edit their own reservations, since this is often times not the case in the restaurant business, making it harder for users to cancel and the restaurant having less cancellations, since it requires the user to make contact. As an improved feature, I would like to add that a confirmation mail is sent to all users and that they then are able to cancel by answering to that email.

  The backend is a simple form which only requires an email input. I added an if statement to check if there are any existing reservations connected to that email adress, making it easy to filter it.

  ![View Reservation](/static/assets/images/view-reservation.png) 

- __Contact us__

  The contact us page is designed to let users reach out to staff either for special requests or cancelling their table reservation. The database model is designed so that users have to fill in their email address their name and the subject matter as a text field.

  When submitting the form the user is redirected to a confirmation page, connfirming that the message was received. When further improving on this webpage I would like to send a confirmation email to users as well.

  ![Contact](/static/assets/images/contact.png)

  ![Contact Success](/static/assets/images/contact-success.png)


- __Footer__

  The footer is supposed to let users connect to the restaurant on social media, have the links to the most important pages present, give a small introduction to the restaurant and show some more contact details. It was designed in Bootstrap for responsiveness.

  ![Footer](/static/assets/images/footer.png)


### Django 

- __Complex views__

  - The most complex views are in the booking app. The table reservation views, does not only filter after time and date, it saves also the outcome and redirects users to different pages, depending on the outcome.

- __Forms__

  - All forms have widgets. I made a special time for the date picker and added classes to the input fields in order to be able to style them with bootstrap later on.

- __Different apps__

  - For scalability I have chosen to split the project into different apps, which means that booking, contact and menu are different apps and can be easily adjusted should the restaurant grow, without affecting one another.

- __Admin__

  - As of now, no users except for admins are supposed to be saved. This is because I don't believe in users making profiles for dining once at a restaurant. This is however a matter of personal preference and can be adjusted, should staff not agree with me on that take.

- __Database__

  - The database based on the models created for the different apps, was created in [ElephantSQL](https://customer.elephantsql.com/).

- __Cloudinary__

  - Since Heroku cannot store any static files over time, I have decided to use Cloudinary. I have changed the settings so that images can be loaded from Cloudinary.

### Features Left to Implement

- I would like to be able to send automated emails.
- Only display available time slots to users.
- Add automated tests.
- Add favicon
- Maybe let users create a profile.
- Implement a different field for phone number.

## Testing 
- All testing has been done manually, by checking the terminal or DevTools. Every time a new functionality had been added, I made sure to test it thoroughly with different scenarios to ensure that it was working as expected.

- __Responsiveness__

  - Responsiveness has been tested in DevTools in order to be able to test on as many devices and screen sizes as possible.

  - An example of iPhone 5 screen size (320 x 568)

    - ![iPhone 5](/static/assets/images/iphone5.png)
 

  - An of examples of iPad screen size (820 x 1024)

    - ![iPad](/static/assets/images/ipad.png)
    - ![iPad Pro](/static/assets/images/ipad-pro.png)

  - An of examples of laptop screen size (1240 x 1024)

    - ![Laptop](/static/assets/images/desktop.png)
  
  - Summary of testing, summarized in a table

    - Everything is running as expected.


- __Bugs__

  Bugtesting has been done in DevTools and the terminal.
  - I wrote the wrong action in the form element for book_table.html. It would not render the form and crash everything. After thorough inspection I finally found my mistake and adjusted to the right url.
  - The phone field was a phone numberfield, which was however making problems when not having the correct (american) format when entering your phone number as a user. This led to frustration, which is the reason why I changed it to an IntegerField. This is not optimal either because if a phone number starts with 0 the 0 won't be displayed.
  - I had misspelled widgets, which resulted in that the contact_us form wasn't displayed properly.
  - My menu.html wasn't rendering at all because I did not specify the template location in my view.
  - After deploying my project to Heroku I could not access my static files folder/css file. After much trouble shooting and reading error messages, getting support, I found that I had the wrong Cloudinary settings and the wrong static file settings, resulting in a lot of "test commits and pushes".  

- __Browser Compatibility__

  - I tested the page on Chrome, Edge, Firefox and Opera. I do not have access to Safari and can therefore not test it on that browser.
  - Everyting is running as expected.

  ![Browser compatibility](/static/assets/images/browser.png)

- __Lighthouse__

  - Performance test for desktop 
    - ![Lighthouse desktop](/static/assets/images/lighthouse.png)

   - Performance test for mobile 
    - ![Lighthouse mobile](/static/assets/images/lighthouse-mobile.png)
    

### Validator Testing 

- PEP8 CI Linter
  - No errors were returned when passing through the [PEP8 CI Linter](https://pep8ci.herokuapp.com/#). 

- CSS
  - No errors were found when passing through the official W3C CSS validator [Jigsaw validator](https://jigsaw.w3.org/css-validator/validator). 


### Unfixed Bugs

There are some weird underscores in the footer, social media links that I cannot make disappear without compromising the entire footer. I will erase them as fast as possible, with more time. 

## Deployment 

The site was deployed to Heroku and build on the Code Institute template. This means that all steps for deploying the project are for when using the Code Institute template. The steps to deploy are as follows: 
  - On Heroku, choose the "New" button in the upper left corner of the webpage and select "Create new app".
  - On the "Create New App" page, choose a name for your project. It has to be unique and when having multiple words, use the dash (-) symbol to link them. Select then the region you live in and click on the "Create app" button.
  - On your personal page for the new app, go to the "Settings" tab (all the way to the right on the navigation bar under your project's name).
  - Head now over to ElephantSQL and link your database. On the Dashboard click on "Create New Instance".
    - Give your plan a name (project name)
    - Select "Tiny Turtle" for the free plan
    - Leave the "Tags" field blank.
    - Select the appropriate Region
    - Click on "Create Instance"
    - Return to the Dashboard and click on the "database instance name"
    - Copy your url
  - __IMPORTANT!__ You must choose your settings first, before deploying.
    - On the "Settings" page, click on the "Reveal Config Vars" button.
    - When using the Code Institute Python template, you need to write PORT (must be uppercase) in the "key" input field and 8000 in the "value" input field. Click then on "add".
    - Add then your SECRET_KEY and value, 
    - Add DATABASE_URL with your SQL database url
    - Do the same for Cloudinary
  - Go now to the "Deploy" page.
    - Click on the "Connect to GitHub" button and search for your repository.
    - Enter the exact name of your repository (not the link but only the name) in the input field "repo-name" and click on "Search", and when found on "Connect".
    - Scroll then down to "automatic deploys" and click then on "Enable Automatic Deploys". That way your app will be rebuild every time new changes are pushed to your GitHub repository.
    - When finished, click on the "View" button and a new tab will open with your deployed project

The live link can be found here - https://la-nonna-22c142432f24.herokuapp.com/


## Credits 

### Code - Coding help

- I read a lot on the Django documentation for [Model.forms](https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/) and [Widgets](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/) and [here](https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/).
- I took inspiration on how to use Cloudinary from the [I Think - Therefore I blog Walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/9236975633b64a12a61a00e0cca7c47d/).
- I generated my GitHub and GitPod from the [Code Institute GitPod template](https://github.com/Code-Institute-Org/gitpod-full-template)
- I looked at this [Tutorial](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78) to get some ideas on how to get started on my own project.


### Content 

- The icons for the buttons were taken from [Font Awesome](https://fontawesome.com/)
- The fonts were taken from [Google Fonts](https://fonts.google.com/)
- I used [Code Institutes template](https://github.com/Code-Institute-Solutions/readme-template) for creating this README.
- The footer and the navbar are from [Bootstrap](https://getbootstrap.com/)


### Media

- Images were taken from [Pexels](https://www.pexels.com/).