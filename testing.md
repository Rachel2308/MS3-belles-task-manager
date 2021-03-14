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