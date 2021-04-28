# How To

[View the live project here.](https://how-to-takudzwa.herokuapp.com/get_hows/)

A How To website to share knowledge

## UX

### Project purpose

Main purpose of this project is to share knowledge with users and to get useful knowledge from the users  wtith the help of How To tips.

### Database Schema

categories collection:
{
    category_name
}

hows collection:
{
    category_name,
    hows_title,
    hows_descripton,
    created_by,
}

users collection:
{
    user_name,
    password,
}

#### Site user goals - Kids

- Easy to Use 
- Easy to navigate 
- Able to find the information they need with the help of How To tips

How To website meets all the goals as the interface is simple to navigate and the information is presented in the first page of the website to prevent them from taking time finind the information.
#### Site user goals - adults(parents and guardians)

- Easy to Use 
- Easy to navigate 
- Able to find the information they need with the help of How To tips

How To website meets all the goals as the interface is simple to navigate and the information is presented in the first page of the website to prevent them from taking time finind the information.

#### User stories

- As a user I want to find the information that l need wtith the help of How To tips
- As a user I want to be able to navigate the website with relative ease 
- As a user I want to be able to edit and my information that l have put on the website


### Design decisions

#### Colour scheme

Colours that were picked had to match the theme of this website.

![Colour palette](https://github.com/TChauruka/how_to/blob/main/images/pallet.jpg)

## Features

### Existing features(for all users)

- Navigation tab to navigate through the website.
- Search bar to query the website for informmation 
- Information section for the informaton to be put for users to see.
- Log in page that allows the user to log on and add new how to.
- Registration page for new users to register their username and password.
- Add How To page that allows users to add new how to.
- Edit How To page to edit the How to  that users put and also delete them.
- A profile page to show who is logged in.

### For Admin Profile
- Add new categories for all uses to select from.
- Edit categories page to edit any categories
- Delete categories from the Database

## Technologies

### Languages

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [JavaScript](https://www.w3schools.com/js/)
- [Python](https://www.w3schools.com/python/)

### Framework 
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

### Libraries
- [Font Awesome](https://fontawesome.com/)
- [jquery](https://jquery.com/) 
- [materializecss](https://materializecss.com/)

### Tools

- [Git](https://git-scm.com/) - for version control
- [GitHub](https://github.com/) - code stored and shared remotely
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) - testing the page through the development process


## Testing

Testing details can be found in separate testing.md [file](https://github.com/TChauruka/how_to/blob/main/testing.md)

## Deployment

Deploying this page from GitHub repository to GitHub Pages was achieved by following these steps:

1. Logging into **GitHub**
2. Picking **tchauruka/how_to/** repository for the list of repositories
3. Selecting **Settings** - from menu items on the top of the page (top, right hand corner)
4. Scrolling down to the **GitHub Pages** section
5. Picking **Master Branch** from the "**Source**" drop-down menu in GitHub Pages (changing from the default "none" to master branch)
6. Awaiting for the page to be refreshed and website to be deployed - this happens automatically when step 5 is actioned
7. Scrolling back down to the **GitHub Pages** section to check/retrieve the link of newly deployed website

### How to run this project locally

To clone this project from this repository following steps need to be taken:

1. **Scroll up** to the repository section on this page
2. **Click "Clone or download"**(green button on the right hand side, just above the file list) - this will open "Clone with HTTPS" section
3. **Copy** the clone **URL** for the repository from "Clone with HTTPS" section
4. **Open** your local **IDE**
5. **Open** your favourite **terminal** (e.g. in your local IDE)
6. **Change** the current **working directory** to the location where you want the cloned directory to be
7. Type **git clone**, paste **the URL** you copied in Step 3 then press **Enter** to create your local clone. In this project the command should be:

```console
git clone <https://tchauruka.github.io/how_to/>
```

Further reading or help with cloning can be found on this GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

## Credits

The content of this page was written by me however following people & their work have influenced me and this project:

- [404 and 500 css animation](https://codepen.io/saransh/pen/aezht)

I have also used following for researching:

- [Stack overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)

