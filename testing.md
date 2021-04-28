# Testing
## Manual testing

### Responsiveness

- **Plan:** this website was planned to be responsive, working on all devices - mobile phones, tablets and desktops. Following this it was planned for materializecss library to be used for a page design.
- **Implementation:** page was **tested in Chrome Developer Tools** throughout the process of putting it together to make sure it was responsive to all devices. "Responsive" slider was used to make sure content is shown correctly on desktop, tablet and mobile, that they look as desired by the developer. Materializecss classes as well as media rules were used to adjust responsiveness.
**Tested** the pages **on** all sizes/devices **available in Chrome**, these were:
  - 360 x 640 Blackberry Z30 & Galaxy Note
  - 375 x 812 iPhone X
  - 375 x 687 iPhone 6/7/8
  - 411 x 731 Pixel 2
  - 411 x 823 Pixel 2 XL
  - 414 x 736 iPhone 6/7/8 Plus
  - 600 x 1024 Blackberry Playbook
  - 768 x 1024 iPad
  - 1024 x 1366 iPad Pro

- **Results:** page is responsive and can be used on all planned devices. There are no elements on this page that are not responding as planned.
- **Conclusion:** all tests that were run on responsiveness were passed therefore page is fully responsive.

### Interaction

- **Plan:** there are elements that are planned to be interactive on this multiple pages, these are buttons, cards , flash message and errors
- **Implementation:** was carried out on many devices and on several browsers, including Chrome, Firefox and Opera. Following elements were tested:
   - Error page will appear when and error has been made.
   - Buttons redirect to the correct pages that they are supposed to go to.
   - Flash messages will appear when a any CRUD action is done.  
   - Unauthorised user will be redirected to the home page.
   - The pop model will show the content when is is clicked.
   - The drop down categories menu will show all the categories
   - Nav bar will shrink to a three line menu and shows the whole nav bar when pressed
   - A red line will show on the text input when there is not text that has been put or is too short 

- **Results:** all tested elements are interactive as planned . There are no elements on this page that are not responding as planned
- **Conclusion:** all tests that were run on interactivity were passed therefore page is interactive


## User stories testing

1. As a user I want to find the information that i need with the help of How To tips:
   - The information simple to see as it is on the first page.
   - The information is easy to find with the help of the search bar

2. As a user I want to be able to navigate the website with relative ease
   - The nav is bar is simple and easy to navigate.
   - The buttons work as they are named 

3. As a user I want to be able to edit and my information that l have put on the website
   - l could be able to created new how to with ease.
   - l could be able to edit my information with ease.
   - l could be able to delete my information with ease.
   - Helpful with showing how to register and log in. 

## Automated testing

### Following online validators were used to test the code:

- [W3C Mark-up Validation Service](https://validator.w3.org/) for HTML validation
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for CSS validation
- [Esprima](https://esprima.org/) for JavaScript validation
- [Extendsclass](https://extendsclass.com/python-tester.html) for Python validation
### HTML validation

| Error message | Action taken|
|-----|-----|
|Bad value {{ url_for('static', filename='css/style.css')}} | No action needed as it come from the python app file|
| Consider adding a lang attribute to the html start tag to declare the language of this document: {% extends "base.html" %}↩{% bl| No action taken as it inherit it from the base.html file|
|Bad value {{ url_for('add_category' )}} | No action needed as it come from the python app file

### CSS validation

- No errors found.

### JavaScript validation
- No errors found.

### Python validation
- No error found 
