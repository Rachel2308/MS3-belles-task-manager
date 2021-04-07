# Testing

## **Bugs**

* **Issue**
  
  Form did not show all of the placeholder text in smaller screen

    **Fix**
  
  Form and text boxes made wider for small screens

* **Issue**

    Title in header too big for smaller screen and drops down outside of the header

    **Fix**

    Media Queries used to use smaller text as screen size gets smaller


*   **Issue**

    Card panels jumped up and caused lower card panel to move to the bottom of the page when opened.

    **Fix**

    Realised that it was due to the card class being used to change the height of the card. Changed the CSS to use the card-title class. Cards now function as intended

*   **Issue**

    The flash on login now says Welcome, None

    **Fix**

    Corrected the code in app.py from users to username

    **Issue**

    When updating the tasks, the task changed to "Whole Chorus"

    **Fix**

    Amended code from {% if homework.section_name == homework.section_name %} to {% if section.section_name == homework.section_name %}

    **Issue**

    The Belles of Three Spires text in the header will take the user to the homework.html page even when not logged in causing errors. 

    **Fix**
    
    If statement added to base.html so that link goes to Login page if not logged in otherwise it links to the View Tasks page


## **User testing**

### **Page**

* Testing has been undertaken on devices down to 320px.

* #### Header
    * When logged in 
        * "The Belles of Three Spires" title links to the View Tasks page
        * The "Add Task", "View Tasks" and "Log Out" links all work and are visible when users are logged in

    * When not logged in, 
        * "The Belles of Three Spires" title links to the Login page
        * Only the "Register" and "Login" links all work and are the only links that are visible when users are not logged in



* #### Log in
    * Username field gives an error, shown by a red line if a username is not entered
    * Password field gives an error, shown by a red line if a password is not entered
    * If the incorrect username and/or password is entered, a flash message stating that "Username and/or password is incorrect flashes up at the top of the screen.
    * When log in details are correct, the LOG IN button takes the user to the "Homework Tasks" page. A flash message then appears at the top of the screen stating
        "Welcome, {username}
    * If the user is a new user, they can press the "Need to register? Please click here" button and will then be redirected to the Registration page.
    * "Register" link in header links to registration page
    * "Log In" link is not shown once the user is logged in
   

* #### Registration
    * If nothing entered in username field, error is shown by red underline.
    * If nothing entered in first name field, error is shown by red underline.
    * If nothing entered in surname field, error is shown by red underline.
    * If nothing entered in password field, error is shown by red underline.
    * If password of fewer than 5 characters entered, error is shown by red underline
    * If a user tries to register a username that is already registered, a flashed message "User is already registered" is displayed 
    * Clicking on the music team toggle button turns on the button, and the user is added as a member of the music team. 
    * When all information is completed, the registration button saves the user information to mongodb, and the user is redirected to the homepage.
    * "Register" link is not shown when the user is logged in


* #### Log out
    * "Log Out" button only shows when the user is log in
    * Clicking on log out will log member out of the site, return user to the Log In screen and display a flashed message.


* #### Add_tasks
    * When logged in as music team


    * When logged in as standard member
        *

 



* #### Edit_tasks
    * When logged in as music team
        * Edit button only shows when logged in as a member of the music team
        * Edit button takes you to the edit task page, where all of the existing data is prefilled into the fields
        * Hitting cancel returns you to the View Tasks homepage
        * Amending the task will update the database correctly
        * Hitting the SAVE CHANGES button will return the user to the View Tasks homepage and a flashed message is displayed "Task Successfully Updated"


    * When logged in as standard member
        * "Edit" button not visible when not logged in as a member of the music team

 

* #### delete_task
    * When logged in as music team
        * Delete button only shows when logged in as a member of the music team
        * Hitting the Delete button displays a modal asking you to confirm if the user wishes to delete the task.
            * Hitting Cancel on this modal returns the user to the View Tasks homepage
            * Hitting Delete on this modal will return the user to the View Tasks homepage and display a flashed message confirming deletion. The deleted task will successfully be removed from the database
        * Hitting cancel returns you to the View Tasks homepage
        * Amending the task will update the database correctly
        * Hitting the SAVE CHANGES button will return the user to the View Tasks homepage and a flashed message is displayed "Task Successfully Updated"


    * When logged in as standard member
        * "Delete" button not visible when not logged in as a member of the music team

 

* #### whole_chorus
    * When logged in as music team


    * When logged in as standard member

 

* #### lead.html
    * When logged in as music team


    * When logged in as standard member

 

* #### tenor.html
    * When logged in as music team


    * When logged in as standard member

 

* #### bari.html
    * When logged in as music team


    * When logged in as standard member

 

* #### bass.html
    * When logged in as music team


    * When logged in as standard member

 


 ## Testing

The HTML and CSS were tested using W3C Markup Validator and W3C CSS Validator to ensure that there 
were no syntax errors on any of the pages of the project. 

* [W3C Markup Validator]()
* [W3C CSS Validator]()

Each page of HTML and the CSS file were all checked. All results came back as completely clear of errors.

* Results
    * HTML
        * []()
    
        

    * CSS
    
        * []()


    * Python

        * []()

### Testing User Stories from User Experience (UX) Section

* **User Stories** 
    * **As a member of the music team**
        1. I want to be able to set tasks for my section so that they know what part of the tracks we neeed to prioritise next.
        2. I want to be able to see what tasks have been set by other members of the music team for their sections
        3. I want to be able to see what tasks have been set for me in the music team tasks section
        4. I want to be able to see what tasks have been set for the whole chorus

    * **As a Non-music team member of the chorus**
        1. I want to be able to see what tasks my section lead has set for me
        2. I want to be able to see what tasks have been set for the whole chorus
    
    * **As the director of the chorus**
        1. I want to be able to set tasks for the individual sections to be able to tell them which specific parts of the tracks they need to work on
        2. I want to be able to communicate tasks and messages to the whole chorus 
        3. I want to be able to set taks for the music team to tell them what we need to be working on next.

### Further Testing

* The Website was tested on:
    * Google Chrome 
    * Internet Explorer 
    * Microsoft Edge 
    * Firefox 
    * Safari 

* The website was viewed on a variety of devices such as 
   * Laptop 
   * iPhone7 
   * iPhone 11 
   * iPhoneX
   * Oppo A9
   * Huawei p20 pro

* Friends were asked to review the site on different devices, screenshot any issues and point out any bugs or 
user experience issues.




---