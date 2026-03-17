# Gamers Guild

Deployed link: [Gamers Guild]( "Gamers Guild | Heroku")

## Contents
* [Project Overview](#project-overview)
* [User Goals](#user-goals)
* [User Stories](#user-stories)
* [Website Goals and Objectives](#website-goals-and-objectives)
* [Target Audience](#target-audience) 
* [Wireframes](#wireframes)
* [Design Choices](#design-choices)
  + [Typography](#typography)
  + [Colour Scheme](#colour-scheme)
  + [Images](#images)
* [Security Measures and Protective Design](#security-measures-and-protective-design)
  + [User Authentication](#user-authentication)
  + [Password Management](#password-management)
  + [Form Validation](#form-validation)
  + [Database Security](#database-security)
* [Features](#features)
* [Future Enhancements](#future-enhancements)  
* [Technologies Used](#technologies-used)  
  + [Languages](#languages)  
  + [Libraries and Frameworks](#libraries-and-frameworks)  
  + [Tools and Programmes](#tools-and-programmes)  
* [Database Design and Data Modelling](#database-design-and-data-modelling)  
  + [Data Model](#data-model)  
  + [Entity Relationship](#entity-relationship)  
  + [Entity Relationship Diagram](#entity-relationship-diagram)  
* [Testing](#testing)  
  + [Bugs](#bugs)  
  + [Responsiveness Tests](#responsiveness-tests)  
  + [Code Validation](#code-validation)  
  + [Automated Testing](#automated-testing)  
  + [User Story Testing](#user-story-testing)  
  + [Feature Testing](#feature-testing)  
  + [Error Page Testing](#error-page-testing)  
  + [Accessibility Testing](#accessibility-testing)  
  + [Lighthouse Testing](#lighthouse-testing)  
  + [Browser Testing](#browser-testing)  
* [Deployment](#deployment)  
  + [Local Deployment](#local-deployment)  
  + [Heroku Deployment](#heroku-deployment)  
* [Credits](#credits)
  + [Feedback, advice and support](#feedback-advice-and-support)
  + [Learning Resources and Guidance](#learning-resources-and-guidance)
  + [Images](#images)
  + [Content](#content)
  + [Visual Content](#visual-content) 

----------------------------------------------

## Project Overview
Gamers Guild is a [brief description of your project here].  

- **Purpose:** [state the main purpose or goal]  
- **Audience:** [target users: gamers, communities, etc.]  
- **Platform:** [web app, responsive design, etc.]

[Back to contents](#contents)

---------------------------------------------

## User Goals

[Back to contents](#contents)

---------------------------------------------

## User Stories

| User Story | Expected Outcome | Pass Criteria | Evidence |
|------------|----------------|---------------|----------|
| As a public user, I want to browse a list of games and view individual game details so that I can explore the content without registering. | Public users can see game titles, images, descriptions, and links to more details. | Game list displays correctly, detail pages load without login. | ![Game List Preview](#) |
| As a new user, I want to register an account securely so that I can participate in discussions and save favorites. | Users can register with validation, receive success feedback, and verify account details. | Registration form validates input and displays confirmation message. | ![Register Page Preview](#) |
| As a registered user, I want to log in securely so that I can access my profile and interact with content. | Users can log in with credentials, authentication protects private data. | Login form accepts valid credentials and denies invalid attempts. | ![Login Page Preview](#) |
| As a logged-in user, I want to post reviews or comments on games so that I can share my opinions and interact with other users. | Comments/reviews are posted under the game, with moderation if needed. | Comment form works and displays posted reviews after submission. | ![Comment Section Preview](#) |
| As a user, I want to edit my own reviews/comments so that I can correct mistakes or update my opinion. | Users can update their own comments, changes are saved and marked as edited. | Only comment author can edit, edit confirmation displayed. | ![Edit Comment Preview](#) |
| As a user, I want to delete my own reviews/comments so that I can remove content I no longer want visible. | Users can delete their own comments after confirmation, removed content is gone from display. | Delete confirmation and success feedback function correctly. | ![Delete Comment Preview](#) |
| As a registered user, I want to save my favorite games so that I can easily revisit them later. | Users can “favorite” games and view a personal list in their profile. | Favorite button toggles correctly, saved games appear in user profile. | ![Favorites Preview](#) |
| As an admin, I want to add new games or content so that fresh material is available to the community. | Admins can create new games through the admin panel, new content appears on the site. | Admin can create game entries with images, description, and metadata. | ![Admin Add Game Preview](#) |
| As an admin, I want to edit existing games or content so that I can correct errors or update information. | Admins can update game details, changes reflect immediately on front end. | Changes are saved successfully and visible to users. | ![Admin Edit Game Preview](#) |
| As an admin, I want to delete outdated or inappropriate games so that the content remains current and safe. | Admins can remove content, confirmed via admin panel, removed items no longer appear to users. | Delete confirmation displayed, database updated correctly. | ![Admin Delete Game Preview](#) |
| As an admin, I want to moderate user comments/reviews so that inappropriate or spam content is removed. | Admins can approve, decline, or delete comments, moderation reflected on front end. | Only admins can perform moderation, moderated content is hidden or removed. | ![Admin Moderation Preview](#) |
| As a public or registered user, I want responsive design so that the website works well on mobile, tablet, and desktop. | Website layout adjusts seamlessly across devices. | No broken elements, navigation and content are readable at all screen sizes. | ![Responsive Preview](#) |

[Back to contents](#contents)

---------------------------------------------

## Website Goals and Objectives

[Back to contents](#contents)

---------------------------------------------

## Target Audience

[Back to contents](#contents)

---------------------------------------------

## Wireframes

[Back to contents](#contents)

---------------------------------------------

## Design Choices

### Typography

### Colour Scheme

[Coolors](https://coolors.co/1b1b1d-2c2a36-d4af37-e6e6e6-b63e3e-4c8c4a "Coolors") was used to create a fitting colour scheme for Gamers Guild, it has been designed to create a dark, immersive medieval-fantasy atmosphere while maintaining strong usability and readability. A deep near-black (`#1B1B1D`) serves as the primary background to reduce eye strain and establish a moody foundation, complemented by a slightly lighter accent (`#2C2A36`) to add depth and separation between sections such as cards and panels. A rich gold (`#D4AF37`) is used for highlights, buttons, and key UI elements, evoking themes of treasure, armor, and prestige while standing out clearly against the dark background. A muted red (`#B63E3E`) provides contrast for alerts and important feedback, reinforcing a fantasy tone associated with danger or urgency. An additional complementary green (`#4C8C4A`) is used for success messages and positive user feedback. This earthy, muted tone fits naturally within the medieval-fantasy palette, resembling forest and herbal hues often associated with healing and vitality, while still providing clear visual distinction from error states. Finally, a soft off-white (`#E6E6E6`) ensures high readability for text without the harshness of pure white. Together, these colours create a cohesive, thematic interface that balances aesthetic immersion with accessibility and clear visual hierarchy. 

![Coolors Scheme](docs/coolors.png)

[Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%20%231B1B1D%0D%0A%232C2A36%0D%0A%23D4AF37%0D%0A%23E6E6E6%0D%0A%23B63E3E%0D%0A%234C8C4A&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid") was used to determine the best colour combinations to ensure the website was visually appealing whilst remaining easy for the user to read the content.

![Contrast Grid](docs/contrast-grid.png)

|CSS Name               |HEX          |Use
|-----------------------|-------------|------------------------------------------------|
| --primary | `#1B1B1D` | Backgrounds (pages, sections, navbars) |
| --secondary | `#2C2A36` | Cards, panels, footers  |
| --primary-highlight | `#D4AF37` | BButtons, hover states, important text, borders |
| --text | `#E6E6E6` | Body text, headers, links |
| --secondary-highlight | `#B63E3E` | Alerts, error messages, warnings, accent highlights |
| --success | `#4C8C4A` | Success buttons (send, submit) |


### Images

[Back to contents](#contents)

---------------------------------------------

## Security Measures and Protective Design

### User Authentication

### Password Management

### Form Validation

### Database Security

[Back to contents](#contents)

---------------------------------------------

## Features

[Back to contents](#contents)

---------------------------------------------

## Future Enhancements

[Back to contents](#contents)

---------------------------------------------

## Technologies Used

### Languages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)  
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)  
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  
- [Python](https://www.python.org/)  

### Libraries and Frameworks
- [Bootstrap v5.3](https://getbootstrap.com/)  
- [Django](https://www.djangoproject.com/)  
- [Font Awesome](https://fontawesome.com/)  
- [Google Fonts](https://fonts.google.com/)  

### Tools and Programmes
- [Black](https://pypi.org/project/black/)  
- [Dev Tools](https://developer.chrome.com/docs/devtools)  
- [GitHub](https://github.com)  
- [Heroku](https://www.heroku.com/)  
- [W3C Validators](https://validator.w3.org/)  
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/)  
- [Contrast Grid](https://contrast-grid.eightshapes.com/)  
- [Coolors](https://coolors.co/)  

[Back to contents](#contents)

---------------------------------------------

## Database Design and Data Modelling

### Data Model
The Gamers Guild database supports a secure, interactive community platform. Entities include:  
- **User** – Registered accounts, roles, profile info.  
- **Game/Content** – Game entries or posts with title, description, media, genre, and ratings.  
- **Comment/Review** – Comments linked to users and games. Includes content, timestamps, and moderation status.  

### Entity Relationship
- A User can create multiple Comments or Reviews (1-to-many).  
- A Game/Content can have multiple Comments/Reviews (1-to-many).  
- Admins have elevated permissions, stored in the User entity.  

### Entity Relationship Diagram

[Back to contents](#contents)

---------------------------------------------

## Testing

### Bugs
| Bug Description | Resolved | Resolution Description |
|-----------------|----------|-----------------------|
| Example bug | Yes/No | Example fix description |

### Responsiveness Tests



### Code Validation



### Automated Testing



### User Story Testing
## User Story Testing Table

| User Story | Expected Outcome | Result | Pass/Fail | Evidence |
|------------|----------------|--------|-----------|----------|
| Browse games as a public user | Public users can view game list and details | | | ![Game List Preview](#) |
| Register new user account | Users can register successfully | | | ![Register Page Preview](#) |
| Login securely | Users can log in and access profile | | | ![Login Page Preview](#) |
| Post reviews/comments | Logged-in users can post reviews/comments | | | ![Comment Section Preview](#) |
| Edit own reviews/comments | Users can update their own comments | | | ![Edit Comment Preview](#) |
| Delete own reviews/comments | Users can remove their own comments | | | ![Delete Comment Preview](#) |
| Save favorite games | Users can favorite games and view list | | | ![Favorites Preview](#) |
| Admin add new game/content | Admin can create new game entries | | | ![Admin Add Game Preview](#) |
| Admin edit game/content | Admin can update existing game details | | | ![Admin Edit Game Preview](#) |
| Admin delete game/content | Admin can remove outdated or inappropriate games | | | ![Admin Delete Game Preview](#) |
| Admin moderate comments | Admin can approve/decline/delete user comments | | | ![Admin Moderation Preview](#) |
| Responsive design | Site works on all devices | | | ![Responsive Preview](#) |

### Feature Testing



### Error Page Testing



### Accessibility Testing



### Lighthouse Testing



### Browser Testing

[Back to contents](#contents)

---------------------------------------------

## Deployment

### Local Deployment


### Heroku Deployment

[Back to contents](#contents)

---------------------------------------------

## Credits

### Feedback, advice and support

- [Richey Malhotra](https://github.com/richey-malhotra "GitHub | richey-malhotra")

### Learning Resources and Guidance

- [Code Institute](https://codeinstitute.net/ "Code Institute")
- [MDN](https://developer.mozilla.org/en-US/ "MDN | Homepage")
- [Slack](https://slack.com/intl/en-gb/ "Slack")
- [Stack Overflow](https://stackoverflow.com/ "Stack Overflow")
- [W3 Schools](https://www.w3schools.com/ "W3 Schools")

### Images:



### Content:

- 

### Visual Content:

- 

[Back to contents](#contents)