# Testing

## **Bugs**

* __Issue__
  
  Form did not show all of the placeholder text in smaller screen

__Fix__
  
  Form and text boxes made wider for small screens

**Issue**
Title in header too big for smaller screen and drops down outside of the header
**Fix**
Media Queries used to use smaller text as screen size gets smaller

**Issue**
Card panels jumped up and caused lower card panel to move to the bottom of the page when opened.
**Fix**
Realised that it was due to the card class being used to change the height of the card. Changed the CSS to use the card-title class. Cards now function as intended

**Issue**
The flash on login now says Welcome, None
**Fix**
Corrected the code in app.py from users to username

**Issue**
When updating the tasks, the task changed to "Whole Chorus"
**Fix**
Amended code from {% if homework.section_name == homework.section_name %} to {% if section.section_name == homework.section_name %}

**Issue**
The Belles of Three Spires text in the header will take the user to the homework.html page even when not logged in. 


## **User testing**

**Page**
*Log in
    *Username field gives an error, shown by a red line if a username is not entered
    *Password field gives an error, shown by a red line if a password is not entered
    *If the incorrect username and/or password is entered, a flash message stating that "Username and/or password is incorrect flashes up at the top of the screen.
    *When log in details are correct, the LOG IN button takes the user to the "Homework Tasks" page. A flash message then appears at the top of the screen stating
        "Welcome, {username}
    *If the user is a new user, they can press the "Need to register? Please click here" button and will then be redirected to the Registration page.

   

*Registration


*Log out


*Add_tasks
    *when logged in as music team


    *when logged in as standard member

 



*Edit_tasks
    *when logged in as music team


    *when logged in as standard member

 

*delete_task
    *when logged in as music team


    *when logged in as standard member

 

*whole_chorus
    *when logged in as music team


    *when logged in as standard member

 

*lead.html
    *when logged in as music team


    *when logged in as standard member

 

*tenor.html
    *when logged in as music team


    *when logged in as standard member

 

*bari.html
    *when logged in as music team


    *when logged in as standard member

 

*bass.html
    *when logged in as music team


    *when logged in as standard member

 


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