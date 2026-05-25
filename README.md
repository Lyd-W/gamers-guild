# Gamers Guild

Deployed link: [Gamers Guild](https://gamers-guild-18d9a6433da1.herokuapp.com/ "Gamers Guild | Heroku")

## Contents
* [Project Overview](#project-overview)
* [User Goals](#user-goals)
* [User Stories](#user-stories)
* [Project Goals and Objectives](#project-goals-and-objectives)
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
  + [Payment Security](#payment-security)
* [Features](#features)
  + [Site Overview & Navigation](#site-overview--navigation)
  + [Homepage & Game Discovery](#homepage--game-discovery)
  + [Search System](#search-system)
  + [Boardgame Detail Page](#boardgame-detail-page)
  + [Shop & Product Catalogue](#shop--product-catalogue)
  + [Product Detail & Inventory System](#product-detail--inventory-system)
  + [Shopping Bag (Cart System)](#shopping-bag-cart-system)
  + [Checkout & Payments](#checkout--payments)
  + [Orders & Confirmation System](#orders--confirmation-system)
  + [User Accounts & Authentication](#user-accounts--authentication)
  + [User Profile System](#user-profile-system)
  + [Engagement Features](#engagement-features)
  + [Content Pages](#content-pages)
  + [Admin & Management Tools](#admin--management-tools)
  + [UX, Accessibility & UI Enhancements](#ux-accessibility--ui-enhancements)
  + [Technical Implementation](#technical-implementation)
  + [SEO & Metadata](#seo--metadata)
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
  + [WhiteNoise](#whitenoise)
  + [Stripe Setup](#stripe-setup)
  + [AWS S3 and CloudFront Setup](#aws-s3-and-cloudfront-setup)  
* [Credits](#credits)
  + [Feedback, advice and support](#feedback-advice-and-support)
  + [Learning Resources and Guidance](#learning-resources-and-guidance)
  + [Image Credits](#image-credits)
  + [Content](#content)

----------------------------------------------

## Project Overview

Gamers Guild is a full stack Django web application designed to bring gamers together within a shared, community-driven platform. The application enables users to browse a curated collection of games, explore detailed game pages, and engage with other users through interactive features such as comments and reviews.

The platform prioritises clarity, usability, and meaningful interaction, avoiding unnecessary complexity or distractions. By focusing on community-driven content rather than algorithm-heavy recommendations, Gamers Guild encourages users to share experiences, discover new games organically, and contribute to a collaborative environment.

Built using Django, the project demonstrates full CRUD functionality, secure authentication, and relational database design. It showcases the integration between backend logic and frontend presentation, ensuring a seamless and responsive experience across all devices.

In addition to its community features, Gamers Guild includes an integrated shop that allows users to browse and purchase gaming-related accessories and add-ons. These include items such as game pieces, branded accessories, and enhancements that complement gameplay. This expands the platform beyond discussion into a more complete user experience, while also demonstrating e-commerce functionality within a full stack application.

Gamers Guild is structured across several Django apps: `home` (homepage, boardgame catalogue and reviews), `shop` (product catalogue and filtering), `bag` (shopping cart), `checkout` (Stripe payment processing), `profiles` (user delivery information, order history and boardgame favourites), and `about` (contact form and platform information).

The application includes a comprehensive automated test suite of over 100 tests written using Django's built-in `TestCase` framework, covering model validation, view access control, form behaviour, bag context calculations, stock management signals, and Stripe payment integration.

**Purpose:**

The purpose of Gamers Guild is to provide a welcoming and interactive platform where gamers can explore, discuss, and share their experiences in a structured and engaging environment.

Many existing gaming platforms rely heavily on advertisements, or algorithm-driven suggestions, which can limit authentic interaction. Gamers Guild addresses this by prioritising user-generated content, allowing users to communicate through review comments rather than relying solely on numerical systems.

The inclusion of a shop enhances this experience by connecting community interaction with practical user needs. Users can move seamlessly from discovering games and engaging in game reviews to purchasing related accessories and enhancements, creating a cohesive and engaging user journey.

**Key objectives include:**

- Encourage open discussion and sharing of gaming experiences  
- Support discovery of new games through community insight  
- Provide a clean, distraction-free interface  
- Demonstrate secure and scalable Django development  
- Integrate e-commerce functionality within a community platform   

**Target Audience:**

Gamers Guild is designed for a broad range of users who engage with gaming content in different ways:

- Casual gamers looking to discover new games and read community opinions  
- Enthusiast gamers who enjoy reading reviews, and sharing experiences  
- Beginner to intermediate players seeking guidance and recommendations  
- Users who prefer community-driven platforms over commercial review sites  
- Players interested in saving and organising favourite games  
- Individuals who value a clean, user-friendly interface  

The platform also appeals to users interested in gaming-related purchases:

- Gamers looking for accessories, collectibles, or add-ons  
- Users who enjoy customising their gaming experience  
- Players who value the convenience of browsing and purchasing within one platform 

**Platform:**

Gamers Guild is a fully responsive web application, ensuring usability across desktop, tablet, and mobile devices.

The platform supports multiple levels of user interaction:

- **Public Users**  
  Can browse games, view details, and read review comments without registering  

- **Authenticated Users**  
  Can register, log in, post, edit, and delete review comments, and save/view favourite games  

- **Administrators**  
  Have full control over content, including managing games, moderating user-generated content, and maintaining platform quality via the admin panel and on page controls  

The platform also includes an integrated shop system:

- **Shop Functionality**  
  Users can browse products, view detailed descriptions, and make purchases  

- **Authenticated Users (Extended Features)**  
  Logged-in users can also view their order history and save/update their delivery information 

- **Administrators (Shop Control)**  
  Admins can manage inventory, including adding, editing, and removing products via the admin panel or product management pages 

The application is deployed online and built with scalability, security, and maintainability in mind using Django’s built-in tools and best practices.

[Back to contents](#contents)

---------------------------------------------

## User Goals

- Browse and discover new games easily  
- Read and contribute to community discussions  
- Create an account to interact with content  
- Save favourite games for quick access  
- Access the platform across multiple devices  
- Purchase gaming-related products easily and securely  
- Explore and customise their gaming experience through accessories and add-ons

[Back to contents](#contents)

---------------------------------------------

## User Stories

| User Story | Expected Outcome |
|------------|----------------|
| As a public user, I want to browse a list of games and view individual game details so that I can explore the content without registering. | Public users can see game titles, images, descriptions, and links to more details. |
| As a new user, I want to register an account securely so that I can participate in discussions and save favourites. | Users can register with validation, receive success feedback, and verify account details. |
| As a registered user, I want to log in securely so that I can access my profile and interact with content. | Users can log in with credentials, authentication protects private data. |
| As a logged-in user, I want to post reviews on games so that I can share my opinions with other users. | Reviews are posted under the game, with moderation if needed. |
| As a user, I want to edit my own reviews so that I can correct mistakes or update my opinion. | Users can update their own reviews, changes are saved and marked as edited. |
| As a user, I want to delete my own reviews so that I can remove content I no longer want visible. | Users can delete their own reviews after confirmation, removed content is gone from display. | 
| As a registered user, I want to save my favourite games so that I can easily revisit them later. | Users can “favourite” games and view a personal list in their profile. |
| As an admin, I want to add new games or content so that fresh material is available to the community. | Admins can create new games through the admin panel, new content appears on the site. | 
| As an admin, I want to edit existing games or content so that I can correct errors or update information. | Admins can update game details, changes reflect immediately on front end. |
| As an admin, I want to delete outdated or inappropriate games so that the content remains current and safe. | Admins can remove content, confirmed via admin panel, removed items no longer appear to users. |
| As an admin, I want to moderate user reviews so that inappropriate or spam content is removed. | Admins can approve, decline, or delete comments, moderation reflected on front end. |
| As a public or registered user, I want responsive design so that the website works well on mobile, tablet, and desktop. | Website layout adjusts seamlessly across devices. |
| As a user, I want to browse products in the shop so that I can explore available gaming accessories. | Users can view a list of products with images, names, and prices. |
| As a user, I want to view detailed product information so that I can make informed purchase decisions. | Users can access individual product pages with descriptions and details. |
| As a user, I want to add items to my cart so that I can purchase multiple products. | Users can add items to a cart and update quantities. |
| As a user, I want to complete a purchase securely so that I can buy products safely. | Users can complete checkout with secure handling of data. |
| As an admin, I want to add products to the shop so that new items can be made available. | Admin can create product entries via admin panel or dedicated product management pages. |
| As an admin, I want to edit products so that I can update pricing or descriptions. | Admin can update product details via admin panel or dedicated product management pages. |
| As an admin, I want to delete products so that outdated items are removed. | Admin can remove products from the database via admin panel or dedicated product management pages. |

[Back to contents](#contents)

---------------------------------------------

## Project Goals and Objectives

The primary goal of Gamers Guild is to deliver a full stack Django web application that demonstrates secure, scalable, and maintainable development practices while providing genuine value to its users.

**Developer Goals:**

- Build a fully functional full stack application using Django, demonstrating competency across frontend and backend development
- Implement secure user authentication and authorisation using Django Allauth
- Design and implement a relational database with clearly defined entity relationships
- Integrate third-party services including Stripe for payments and AWS S3 for static and media file storage
- Demonstrate full CRUD functionality across multiple models
- Deploy a production-ready application to Heroku with appropriate environment configuration
- Write clean, well-structured code following Django conventions and PEP8 standards
- Build a comprehensive automated test suite covering models, views, forms, and integrations

**Site Owner Goals:**

- Provide a platform that encourages repeat visits through community engagement features
- Maintain control over content quality through admin moderation tools
- Generate revenue through an integrated e-commerce shop
- Build a recognisable brand identity through consistent design and theming
- Manage products, inventory, and orders through intuitive admin tooling

**User Goals:**

- Discover and explore board games through a well-organised, filterable interface
- Contribute to a community through reviews and ratings
- Save favourite games for future reference
- Purchase gaming accessories and add-ons securely and conveniently
- Access the platform comfortably across all devices


[Back to contents](#contents)

---------------------------------------------

## Wireframes

Wireframes were created using [Canva](https://www.canva.com/ "Canva | Homepage"). A mobile first approach was taken throughout, the wireframes provide a visual representation of the expected layout and structure of the website. Within the wireframes, key element placement is visible for navigation, content and interactive areas. Differences to the Wireframes may occur during the development of the website where improvements are implemented.

[Mobile Wireframes](docs/mobile-wireframes.pdf "Mobile Wireframes")

[Tablet Wireframes](docs/tablet-wireframes.pdf "Tablet Wireframes")

[Desktop Wireframes](docs/desktop-wireframes.pdf "Desktop Wireframes")

[Back to contents](#contents)

---------------------------------------------

## Design Choices

### Typography

[Google Fonts](https://fonts.google.com/ "Google Fonts") was used to import and apply typography consistently across the application using CSS. Typography was carefully selected to reflect the medieval-fantasy theme of Gamers Guild while maintaining strong readability and accessibility.

- **Cinzel** is used for headings and titles to create a bold, immersive aesthetic inspired by classic engraved lettering. This enhances the thematic identity of the platform and complements the gold accent colour used throughout the design.

- **Roboto** is used for body text to ensure clarity and readability across all devices. Its clean and modern appearance balances the more decorative heading font, preventing visual fatigue and improving the overall user experience.

This combination ensures a clear visual hierarchy while maintaining both aesthetic appeal and usability.

### Colour Scheme

[Coolors](https://coolors.co/1b1b1d-2c2a36-d4af37-e6e6e6-b63e3e-4c8c4a "Coolors") was used to create a fitting colour scheme for Gamers Guild, it has been designed to create a dark, immersive medieval-fantasy atmosphere while maintaining strong usability and readability. A deep near-black (`#1B1B1D`) serves as the primary background to reduce eye strain and establish a moody foundation, complemented by a slightly lighter accent (`#2C2A36`) to add depth and separation between sections such as cards and panels. A rich gold (`#D4AF37`) is used for highlights, buttons, and key UI elements, evoking themes of treasure, armour, and prestige while standing out clearly against the dark background. A muted red (`#B63E3E`) provides contrast for alerts and important feedback, reinforcing a fantasy tone associated with danger or urgency. An additional complementary green (`#4C8C4A`) is used for success messages and positive user feedback. This earthy, muted tone fits naturally within the medieval-fantasy palette, resembling forest and herbal hues often associated with healing and vitality, while still providing clear visual distinction from error states. Finally, a soft off-white (`#E6E6E6`) ensures high readability for text without the harshness of pure white. Together, these colours create a cohesive, thematic interface that balances aesthetic immersion with accessibility and clear visual hierarchy. 

![Coolors Scheme](docs/coolors.png)

[Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%231B1B1D%0D%0A%232C2A36%0D%0A%23D4AF37%0D%0A%23E6E6E6%0D%0A%23B63E3E%0D%0A%234C8C4A&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid") was used to determine the best colour combinations to ensure the website was visually appealing whilst remaining easy for the user to read the content.

![Contrast Grid](docs/contrast-grid.png)

|CSS Name               |HEX          |Use
|-----------------------|-------------|------------------------------------------------|
| --primary | `#1B1B1D` | Backgrounds (pages, sections, navbars) |
| --secondary | `#2C2A36` | Cards, panels, footers  |
| --primary-highlight | `#D4AF37` | Buttons, hover states, important text, borders |
| --text | `#E6E6E6` | Body text, headers, links |
| --secondary-highlight | `#B63E3E` | Alerts, error messages, warnings, accent highlights |
| --success | `#4C8C4A` | Success messages |


[Back to contents](#contents)

---------------------------------------------

## Security Measures and Protective Design

### User Authentication

User authentication is handled by [Django Allauth](https://django-allauth.readthedocs.io/en/latest/), which provides a robust and well-tested authentication system. This includes secure registration, login, logout, and session management. Protected views are decorated with `@login_required` to prevent unauthorised access. Views requiring staff or superuser privileges include an additional check using `request.user.is_staff` or `request.user.is_superuser`, redirecting unauthorised users with an appropriate message.

### Password Management

Passwords are never stored in plain text. Django's default password hashing framework uses PBKDF2 with a SHA256 hash, providing strong protection against brute force attacks. Users receive validation feedback if their chosen password does not meet minimum security requirements. Password reset functionality is provided through Django Allauth's built-in email-based reset flow.

### Form Validation

All forms are validated both client-side and server-side. Django's form framework ensures that submitted data is clean, correctly typed, and within expected boundaries before any database interaction occurs. CSRF tokens are included on every form to protect against cross-site request forgery attacks. Custom validation logic is applied where needed, such as preventing duplicate reviews from the same user on the same game, enforced via a `unique_together` constraint on the `Review` model.


### Database Security

Sensitive credentials including the database URL, secret key, Stripe keys, and AWS credentials are stored as environment variables and never committed to version control. A `.gitignore` file is in place to prevent accidental exposure of the `env.py` file locally. The `DEBUG` setting is set to `False` in production, preventing the exposure of sensitive stack trace information to end users.

### Payment Security

Stripe is used to securely process all payments. Sensitive card data is handled entirely by Stripe Elements and is never transmitted to or stored on the application server. Stripe's webhook system is used to confirm payment intent completion server-side, ensuring orders are only confirmed after successful payment verification rather than relying solely on client-side redirects.

[Back to contents](#contents)

---------------------------------------------

## Features

## Site Overview & Navigation

### Responsive Navigation System
Gamers Guild provides a fully responsive navigation experience across all devices.

### Desktop Navigation Bar
- Full width navigation layout
- Inline links to key pages
- Search bar integration
- User account dropdown
- Live shopping bag total

### Mobile Navigation Menu
- Collapsible dropdown menu
- Optimised for smaller screens
- Touch friendly navigation controls

### State aware Profile menu

The profile menu on both desktop and mobile devices is dynamically adjusted depending on the user's authentication state. Authenticated users are shown personalised account options, while guests are presented with login and registration links. Authenticated users are also shown a welcome message including their username in the profile menu.

#### Screenshots
[Navigation for desktop](docs/navigation-desktop.png "Navigation | Desktop")

[Navigation for mobile](docs/navigation-mobile.jpg "Navigation | Mobile")


## Homepage & Game Discovery

### Board Game Display
Board games are displayed using responsive card layouts featuring:

- An image shown in the proportions of the physical board game box
- Title
- Player count
- Recommended age
- Playtime
- Release year
- Average rating, with full, half and empty star iconography

Boardgame card images are a variety of shapes and sizes to mimic the physical proportions of the actual boardgame boxes. This helps users to recognise their favourite boardgames as well as allowing the full artwork to be displayed. 

Each card links to a dedicated game detail page.

#### Screenshots
[Board game grid on desktop](docs/home-board-game-grid.png "Board Game Grid | Desktop")

[Board game card example](docs/home-board-game-card.png "Board Game Card Example | Tablet")

### Sorting Functionality
Users can sort games dynamically by:

- Title (A–Z / Z–A)
- Rating (Low–High / High–Low)
- Playtime (Low–High / High–Low)
- Release year (Oldest–Newest / Newest–Oldest)

#### Screenshots
[Homepage 'sort by...' dropdown](docs/home-sort-dropdown.png "Homepage Sort By Dropdown | Desktop")

### Game Filtering System
Users can refine results using:

- Genre filtering (checkbox based)
- Player count checkbox selection
- Playtime slider filtering

Genre, player count, and playtime filters can be applied simultaneously and combined with the sort options.

#### Screenshots
[Homepage filters closed on desktop](docs/home-filters-closed-desktop.png "Homepage Filters Closed | Desktop")

[Homepage filters - genre open on desktop](docs/home-filters-genre-open-desktop.png "Homepage Filters - Genre Open | Desktop")

[Homepage filters - player count open on desktop](docs/home-filters-player-count-open-desktop.png "Homepage Filters - Player Count Open | Desktop")

[Homepage filters - playtime open on desktop](docs/home-filters-playtime-open-desktop.png "Homepage Filters - Playtime Open | Desktop")

### Mobile Filter Menu
- Collapsible filters used to preserve screen space for game display
- Optimised for mobile screen sizes and touch control

#### Screenshots
[Homepage filters closed on mobile](docs/home-filters-closed-mobile.jpg "Homepage Filters Closed | Mobile")

[Homepage filters - genre open on mobile](docs/home-filters-genre-open-mobile.jpg "Homepage Filters - Genre Open | Mobile")

[Homepage filters - player count open on mobile](docs/home-filters-player-count-open-mobile.jpg "Homepage Filters - Player Count Open | Mobile")

[Homepage filters - playtime open on mobile](docs/home-filters-playtime-open-mobile.jpg "Homepage Filters - Playtime Open | Mobile")

### Tablet Filter Overlay
- Slide-out drawer-style overlay system to increase filter visibility while preserving screen space for game display
- Optimised for touch controls

#### Screenshots
[Homepage filters closed on tablet](docs/home-filters-closed-tablet.jpg "Homepage Filters Closed | Tablet")

[Homepage filters - genre open on tablet](docs/home-filters-genre-open-tablet.jpg "Homepage Filters - Genre Open | Tablet")

[Homepage filters - player count open on tablet](docs/home-filters-player-count-open-tablet.jpg "Homepage Filters - Player Count Open | Tablet")

[Homepage filters - playtime open on tablet](docs/home-filters-playtime-open-tablet.jpg "Homepage Filters - Playtime Open | Tablet")

## Search System

### Global Search Functionality

A unified search system across:

- Board games
- Store products

### Features

- Categorised results view
- Responsive result cards
- Metadata display
- Direct links to detail pages
- Placeholder image fallback system

#### Screenshots
[Search results for board games - desktop](docs/search-boardgame-results.png "Search Results for Board Games| Desktop")

[Search results for products - desktop](docs/search-products-results.png "Search Results for Products | Desktop")

[No games found preview](docs/no-games-found.png "No Games Found Preview")

[No products found preview](docs/no-products-found.png "No Products Found Preview")

## Boardgame Detail Page

### Features

- An image shown in the proportions of the physical board game box
- Title, player count, recommended age, playtime, release year, and average rating with star rating indicators
- Full game description
- Add/remove favourite button with state-dependent heart graphic
- Review and rating section
- Edit and delete controls for the user's own review
- Overwrite original review and rating when a user submits an additional review
- Pending approval status indicator
- Admin review and rating moderation controls

#### Screenshots

[Boardgame detail](docs/boardgame-detail.png "Boardgame Detail")

[Boardgame detail - reviews section](docs/boardgame-detail-reviews.png "Boardgame Detail | Reviews")

## Shop & Product Catalogue

### Product Grid Display
Products are shown using responsive cards featuring:

- Product image
- Product name
- Price
- Category

#### Screenshots
[Shop grid view on desktop](docs/shop-overview.png "Shop Grid View | Desktop")

### Shop Navigation & Filtering
- Horizontal category navigation bar
- Subcategory filtering system
- URL-based filtering

#### Suggested Screenshots
[Shop category navigation on desktop](docs/shop-category-navigation-desktop.png "Shop Category Navigation | Desktop")

[Shop filter on desktop](docs/shop-filter-desktop.png "Shop Filter | Desktop")

### Product Sorting
Users can sort products by:

- Category (A–Z / Z–A)
- Name (A–Z / Z–A)
- Price (Low–High / High–Low)

Filters and sorting can be combined for further refinement of results.

#### Screenshots
[Shop 'sort by...' on desktop](docs/shop-sort-options-desktop.png "Shop Sort By | Desktop")

## Product Detail & Inventory System

### Product Variants

Items available in different sizes have a size selection dropdown, listing all stocked sizes. The dropdown is stock aware, dynamically adjusting to stock levels, and prevents out of stock sizes being added to the basket.

#### Screenshots
[Shop product size selection on desktop](docs/product-size-selection-desktop.png "Shop Product Size Selection | Desktop")

### Quantity & Stock Controls
- Increment/decrement buttons
- Stock-aware quantity limits
- Conditional add-to-bag functionality
- Out of stock notification in size dropdown or dynamic add to bag/out of stock button 

#### Screenshots
[Product quantity selection on desktop](docs/product-quantity-selection-desktop.png "Product Quantity Size Selection | Desktop")

[Product out of stock on desktop](docs/product-no-stock-desktop.png "Product Out of Stock | Desktop")

[Product stock validation on desktop](docs/product-stock-validation-example-desktop.png "Product Stock Validation | Desktop")

[Product all stock in basket validation on desktop](docs/product-all-stock-in-basket-desktop.png "Product All Stock In Basket | Desktop")

## Shopping Bag (Cart System)

### Core Features

- Fully responsive basket layout
- Separate mobile and desktop interfaces
- Quantity update controls
- Remove item functionality (AJAX)
- Live subtotal calculations
- Delivery cost calculation
- Grand total calculation
- Free delivery threshold messaging

#### Screenshots

[Shopping bag empty on desktop](docs/shopping-bag-empty-desktop.png "Shopping Bag Empty | Desktop")

[Shopping bag on desktop](docs/shopping-bag-desktop.png "Shopping Bag | Desktop")

[Shopping bag on mobile](docs/shopping-bag-mobile.jpg "Shopping Bag | Mobile")

### Mobile Optimisation

- Card-based layout
- Simplified order summary
- Touch-friendly controls

## Checkout & Payments

### Checkout Flow

- Secure checkout process via embedded Stripe element
- Order summary breakdown
- Delivery and billing calculation
- Order confirmation system
- Email notifications

#### Screenshots

[Checkout page on desktop](docs/checkout-desktop.png "Checkout Page | Desktop")

[Checkout page on mobile](docs/checkout-mobile.png "Checkout Page | Mobile")

### Stripe Integration

- Secure card payment handling via Stripe Elements

#### Screenshots

[Stripe payment form desktop](docs/stripe-payment-form.png "Stripe Payment Form | Desktop")

### Loading Overlay

- Prevents duplicate submissions via disabling stripe element following submission
- Improves payment UX feedback
- Stripe element reenabled following payment error

#### Screenshots
[Checkout loading overlay on desktop](docs/checkout-loading-screen-desktop.png "Checkout Loading Overlay | Desktop")

## Orders & Confirmation System

### Checkout Success Page
- Unique order number
- Order date
- Item breakdown
- Delivery address summary
- Billing summary
- Total cost display
- Quick link back to shop

#### Screenshots
[Checkout success for desktop](docs/checkout-success-desktop.png "Checkout Success | Desktop")

### Order History
- Accessible via user profile
- Displays past order confirmation, showing purchases, totals and delivery details
- Information toast to improve UX

#### Screenshots
[Order history for desktop](docs/profile-order-history-desktop.png "Order History | Desktop")

## User Accounts & Authentication

### Authentication System
Powered by Django Allauth:

- Registration
- Post registration email confirmation
- Login / logout
- Password reset via email
- Authenticated UI states
- Protected features

#### Screenshots
[Login for desktop](docs/login-desktop.png "Login | Desktop")

[Login error message for desktop](docs/log-in-error.png "Login Error Message | Desktop")

[Registration page for desktop](docs/register-desktop.png "Registration Page | Desktop")

[Post registration email confirmation](docs/confirm-email.png "Email Confirmation | Mobile")

### Protected Features

- Editing and deleting reviews
- Favourites system
- Order history
- Saved delivery information

## User Profile System

### Profile Dashboard

- Order history
- Delivery information management
- Persistent user data

#### Screenshots

[Profile page for desktop](docs/profile-desktop.png "Profile Page | Desktop")

### Favourite Games

- Save and revisit games
- Stored per user account

#### Screenshots

[Profile page - favourites for desktop](docs/profile-favourites-desktop.png "Profile Page - Favourites | Desktop")

## Engagement Features

- Favourite games system
- User specific saved content
- Wishlist ready structure

## Content Pages

### About Page

- Platform overview
- Community focus

#### Screenshots

[About page for desktop](docs/about-desktop.png "About | Desktop")

### Contact Form

- Name, email, subject, message
- Submission feedback system
- Server-side form validation

#### Screenshots

[About page validation for desktop](docs/about-validation-desktop.png "About validation | Desktop")

## Admin & Management Tools

### Game Management

- Via admin panel
- Full CRUD functionality games
- Image upload handling
- Staff-only access
- Game genres selectable using a horizontal filter selection

[Admin panel - add game 1/3](docs/admin-panel-add-game-1.png "Admin Panel | Add Game 1/3")

[Admin panel - add 2/3](docs/admin-panel-add-game-2.png "Admin Panel | Add Game 2/3")

[Admin panel - add game 3/3](docs/admin-panel-add-game-3.png "Admin Panel | Add Game 3/3")

[Admin panel - edit game 1/2](docs/board-game-django-administration-one-desktop.png "Admin Panel | Edit Game 1/2")

[Admin panel - edit game 2/2](docs/board-game-django-administration-two-desktop.png "Admin Panel | Edit Game 2/2")

### Product Management

- Via admin panel and product management pages
- Full CRUD functionality for products
- Image upload handling
- Staff-only access

#### Screenshots

[Admin panel - add product](docs/add-product-page.png "Admin Panel | Add Product")

[Admin panel - edit product 1/2](docs/edit-product-page-ong-of-one.png "Admin Panel | Edit Product 1/2")

[Admin panel - edit product 2/2](docs/edit-product-page-ong-of-two.png "Admin Panel | Edit Product 2/2")

[Product management page - add product 1/2](docs/add-product-management-page-1.png "Product Management Pages | Add Product 1/2")

[Product management page - add product 2/2](docs/add-product-management-page-2.png "Product Management Pages | Add Product 2/2")

[Product management page - edit product 1/2](docs/edit-product-management-page-1.png "Product Management Pages | Edit Product 1/2")

[Product management page - edit product 2/2](docs/edit-product-management-page-2.png "Product Management Pages | Edit Product 2/2")

### Review Moderation

- Approve / delete reviews
- Staff controls

#### Screenshots

[Admin panel - review controls](docs/admin-review-controls.png "Admin Panel | Review Controls")

[Boardgame detail page - review controls](docs/boardgame-detail-review-controls.png "Boardgame Detail Page | Review Controls")

## UX, Accessibility & UI Enhancements

### User Experience Improvements

- Toast notifications for all user actions
- Scroll-to-top button with scroll container awareness
- Empty state handling throughout 
- Custom error pages (400, 403, 404, 500)

Defensive UI states are implemented throughout the site for example stock-aware quantity limits through conditional add-to-bag functionality and out of stock notification in size dropdown or disabled out of stock button.

#### Screenshots

[Toast example - log in](docs/toast-success-log-in.png "Toast Example | Log In")

[Toast example - log out](docs/toast-success-log-out.png "Toast Example | Log Out")

[Toast example - add to favourites](docs/toast-success-favourites.png "Toast Example | Added To Favourites")

[Toast example - message success](docs/toast-message-success.png "Toast Example | Message Success")

[Toast example - review success](docs/toast-review-success.png "Toast Example | Review Success")

[Toast example - review deleted success](docs/toasts-review-deleted-success.png "Toast Example | Review Deleted Success")

[Toast example - past order information](docs/toast-information-previous-order.png "Toast Example | Past Order Information")

[Toast example - warning insufficient stock](docs/toast-warning-insufficient-stock.png "Toast Example | Warning Insufficient Stock")

[Toast example - item removed](docs/toast-item-removed.png "Toast Example | Item Removed")

[Shopping bag empty on desktop](docs/shopping-bag-empty-desktop.png "Shopping Bag Empty | Desktop")

[Review validation on desktop](docs/board-game-detail-form-validation-desktop.png "Review Validation | Desktop")

[Delete review confirmation on desktop](docs/delete-review-confirmation.png "Delete Review Confirmation | Desktop")

[Logged in status on desktop](docs/logged-in-user-display.png "Logged In Status | Desktop")

[Logged out status on desktop](docs/logged-out-user-display.png "Logged Out Status | Desktop")

[Log out danger hover effect](docs/log-out-button-hover.png "Log Out Danger Hover Effect")

[400 error page preview](docs/400-error.png "400 Error Page")

[403 error page preview](docs/403-error.png "403 Error Page")

[404 error page preview](docs/404-error.png "404 Error Page")

[500 error page preview](docs/500-error.png "500 Error Page")

### Accessibility Features

- Semantic HTML throughout (`<header>`, `<main>`, `<footer>`, `<nav>`, `<section>`, `<article>`)
- All SVG icons include `aria-hidden="true"` with associated visible labels or `aria-label` attributes
- Accessible forms with associated labels
- Keyboard navigation support across all interactive elements
- Responsive typography
- Visual feedback systems

## Technical Implementation

### Frontend Stack

- Django templating engine
- Bootstrap 5.3.2 framework (PurgeCSS optimised)
- Custom JavaScript for dynamic behaviour
- Crispy Forms with Bootstrap 5 template pack

### Custom JavaScript

Custom JavaScript is used throughout the application to enhance user experience. Key implementations include:

- Dynamic sort selector handling on the home and shop pages that updates URL parameters without full page reload
- AJAX-based bag item removal that deletes items and reloads the bag without a form submission
- Review edit and delete functionality that pre-populates the review form from existing data and triggers a confirmation modal
- Back-to-top button that detects scroll position on both the window and scrollable card containers
- Accordion filter state persistence using `localStorage`
- Stripe Elements integration for secure card payment handling
- Filter overlay open/close behaviour on home and shop for tablet viewports

### Architecture

- Modular templates with reusable includes
- Reusable components (toasts, filters, sorting)
- Responsive grid system via Bootstrap
- Session-based shopping bag
- Webhook-based payment confirmation

### Version Control

Version control was managed using Git, with the repository hosted on [GitHub](https://github.com/Lyd-W/gamers-guild "GitHub | Lyd-W"). Commits were made regularly throughout development with descriptive messages reflecting the changes made at each stage.

## SEO & Metadata

- Dynamic page titles per template using `{% block title %}`
- Page specific meta descriptions
- Open Graph tags for social sharing
- Keyword optimisation via meta keywords blocks
- Semantic HTML structure supporting search engine indexing

## Future Enhancements

**Product reviews and ratings** 
- Allow users to leave reviews on shop products in the same way they can review board games, creating a more complete community experience across both sections of the platform

**Wishlist sharing**
- Enable users to share their saved game lists and Wishlists with other users or publicly, adding a social dimension to the favourites system

**Advanced filtering** 
- Additional filtering options for the shop including price range sliders, rating filters, and stock availability toggles

**Recommendation engine**
- Suggest games to users based on their favourites, review history, and genre preferences
- Suggest products to users based on their order history, previously viewed items and favourite games

**Admin analytics dashboard**
- Provide site administrators with an overview of order volume, popular products, and user engagement metrics

**Enhanced stock management** 
- Low stock alerts for administrators, automatic out-of-stock handling, and restocking notifications for users
- Reserve stock in basket for 60 minutes

**Expanded community interaction**
- Addition of a forum for users to create topics, leave and reply to comments and share community created content

**Improve Order History system**
- Allow users to search and filter previous orders by item name, size, date range, or order total
- Add pagination to the order history table to improve usability for users with a large number of past orders
- Build a dedicated Order History app to separate this functionality from the Profiles app, improving code organisation and scalability

**Load more on scrollable page sections**
- Implement a load more button on scrollable page sections to improve initial page loading and response times

**Inline critical CSS**
- Set up inline critical CSS to improve initial page loading and response times, especially home and shop

[Back to contents](#contents)

---------------------------------------------

## Technologies Used

### Languages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS")
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML "HTML")
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript "JavaScript")
- [Markdown](https://en.wikipedia.org/wiki/Markdown "Markdown")
- [Python](https://www.python.org/ "Python")

### Libraries and Frameworks

- [Bootstrap v5.3.2](https://getbootstrap.com/ "Bootstrap v5.3 | Homepage")
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "boto3 | Documentation")
- [crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5 "crispy-bootstrap5 | GitHub")
- [Django](https://www.djangoproject.com/ "Django | Homepage")
- [django-allauth](https://django-allauth.readthedocs.io/ "django-allauth | Documentation")
- [django-countries](https://github.com/SmileyChris/django-countries "django-countries | GitHub")
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/ "django-crispy-forms | Documentation")
- [django-storages](https://django-storages.readthedocs.io/ "django-storages | Documentation")
- [Google Fonts](https://fonts.google.com "Google Fonts | Homepage")
- [gunicorn](https://gunicorn.org/ "gunicorn | Homepage")
- [Pillow](https://pillow.readthedocs.io/ "Pillow | Documentation")
- [PostgreSQL](https://dbs.ci-dbs.net "PostgreSQL | Code Institute")
- [psycopg2](https://www.psycopg.org/ "psycopg2 | Homepage")
- [Stripe](https://stripe.com/gb "Stripe | Homepage")
- [Summernote](https://summernote.org/ "Summernote | Homepage")

### Tools and Programmes

- [AWS](https://aws.amazon.com/cloudfront/ "AWS | Homepage")
- [Black](https://pypi.org/project/black/ "Black | Code Formatter")
- [Canva](https://www.canva.com/ "Canva | Homepage")
- [Contrast Grid](https://contrast-grid.eightshapes.com/ "Contrast Grid")
- [Coolors](https://coolors.co/ "Coolors")
- [dbdiagram.io](https://dbdiagram.io/ "dbdiagram.io")
- [Dev Tools](https://developer.chrome.com/docs/devtools "Chrome | Dev Tools")
- [DJLint](https://djlint.com/ "DJLint | Homepage")
- [Favicon.io](https://favicon.io/ "Favicon.io | Homepage")
- [Flake8](https://flake8.pycqa.org/en/latest/ "Flake8 | Homepage")
- [GitHub](https://github.com "GitHub Homepage")
- [Heroku](https://www.heroku.com/ "Heroku")
- [LastPass](https://www.lastpass.com/features/password-generator "LastPass | Homepage")
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/ "Google Chrome Dev Tools | Lighthouse")
- [Prettier](https://prettier.io/ "Prettier | Homepage")
- [PurgeCSS](https://purgecss.com/ "PurgeCSS | Homepage")
- [Squoosh](https://squoosh.app/ "Squoosh | Homepage")
- [Temp-mail](https://temp-mail.org/en/ "Temp-Mail | Homepage")
- [Visual Studio Code](https://code.visualstudio.com/ "VSCode | Homepage")
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS Validation Service Homepage")
- [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML Validation Service Homepage")
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/ "WAVE | Homepage")
- [WhiteNoise](https://whitenoise.readthedocs.io/ "WhiteNoise | Homepage")

[Back to contents](#contents)

---------------------------------------------

## Database Design and Data Modelling

### Data Model

The Gamers Guild database is composed of six Django apps, each containing models that reflect a distinct area of the application's functionality. The schema is designed around two parallel domains: community features (board games, reviews, and favourites) and e-commerce (products, orders, and line items), unified through a shared user model provided by Django's built-in `auth` framework.

**Boardgames App**

The `Boardgame` model is the core community entity. Each game has a title, slug, image, description, release year, playtime, player count range, and minimum age. Games are linked to `Genre` through a many-to-many relationship, and to `User` through a second many-to-many relationship for the favourites system. A foreign key to `User` records which staff member created the entry. Validation is applied at the model level to ensure `min_players` never exceeds `max_players`, and field-level validators constrain `release_year`, `playtime`, and `min_age` to sensible ranges.

The `Review` model links a `User` and a `Boardgame` via foreign keys, and a `unique_together` constraint on `(boardgame, user)` ensures each user can only hold one review per game. Reviews store a rating (1–5), a text comment, timestamps for creation and last update, and an `is_approved` boolean that gates public visibility pending admin moderation.

**Shop App**

The `Category` model uses a self-referential foreign key to support a two-tier hierarchy of parent categories (such as Apparel or Accessories) and subcategories (such as T-Shirts or Dice). This allows the shop navigation bar and filter system to operate at either level.

The `Product` model stores name, description, price, image, SKU, stock level, and a flag indicating whether the product comes in multiple sizes. The `ProductSize` model provides a separate size-and-stock entry per variant, linked back to its parent product via foreign key. The `is_in_stock` property on `Product` handles both sized and non-sized products correctly, checking `ProductSize` stock records when sizes are present.

**Checkout App**

The `Order` model records all delivery and billing details alongside a UUID-based order number, a Stripe payment intent ID, and the original bag contents serialised as JSON for webhook reconciliation. It links to `UserProfile` via a nullable foreign key so that authenticated users' orders appear in their order history. The `update_total` method recalculates order total, delivery cost, and grand total dynamically based on line items.

The `OrderLineItem` model links an `Order` to a `Product`, recording quantity, optional size, and a computed `lineitem_total` that is set automatically on save.

**Profiles App**

The `UserProfile` model extends Django's built-in `User` with a one-to-one relationship, storing default delivery address fields that are pre-populated on the checkout form for returning users.

### Entity Relationship

**Boardgames:**

- User to Boardgame (1-to-many, via author field — one user creates many games)
- User to Boardgame (many-to-many, via favourites — users save multiple games, games can be saved by multiple users)
- Boardgame to Review (1-to-many — one game has many reviews)
- User to Review (1-to-many — one user can review many games)
- Boardgame to Genre (many-to-many — games span multiple genres, genres cover multiple games)

**Shop:**

- Category to Category (self-referential 1-to-many, via parent - parent categories have many subcategories)
- Category to Product (1-to-many — one category contains many products)
- Product to ProductSize (1-to-many — one product has many size variants)

**Orders:**

- User to UserProfile (1-to-1 — each user has one profile)
- UserProfile to Order (1-to-many — one profile has many orders)
- Order to OrderLineItem (1-to-many — one order has many line items)
- Product to OrderLineItem (1-to-many — one product appears in many line items across orders)

### Entity Relationship Diagram

The ERD below was produced during the planning phase of the project using [dbdiagram](https://dbdiagram.io "dbdiagram | Homepage"). It reflects the intended schema at the design stage. The implemented schema closely follows this structure, with refinements made during development, notably the addition of `ProductSize` for variant stock management, the `is_approved` field on `Review` to support moderation, and the `unique_together` constraint on reviews to prevent duplicate submissions. The hint-trick entity was removed from the project and moved to a future enhancement.

[Entity Relationship Diagram](docs/gg-erd.png "ERD")

[Back to contents](#contents)

---------------------------------------------

## Testing

### Bugs

| Bug Description | Resolved | Resolution Description |
|-----------------|----------|------------------------|
| Navbar toggler on mobile displayed a lock icon instead of a hamburger icon due to incorrect SVG being used in the mobile header include | Yes | Replaced the lock SVG with the correct Bootstrap `bi-list` hamburger icon in `mobile-top-header.html` |
| Review star ratings in the reviews list displayed the game's average rating rather than the individual reviewer's rating | Yes | Updated the reviews loop in `boardgame_detail.html` to use `review.rating` instead of `boardgame.avg_rating` |
| Playtime filter submitted two `playtime` parameters (one from slider, one from input) causing unexpected query string behaviour | Yes | Resolved by ensuring only one named input is active on submission, using the apply button to trigger form submission |
| Boardgame average rating displaying half stars instead of empty stars | Yes | Created `star_ratings` property method in boardgame model to generate full, half or empty values to use to display star rating |
| Stripe webhooks receiving unsuccessful responses | Yes | Ran `python manage.py makemigrations` and `python manage.py migrate` then redeployed project |
| Adding items without sizes to the bag caused 'Select a Size' error message and prevented adding to bag | Yes | Added `product.has_sizes and not size` rule to bag/views.py |
----------------------------------------------

### Responsiveness Tests

Responsiveness was tested across a range of real devices and using Chrome DevTools device simulation.

| Page | Mobile (375px) | Tablet (768px) | Desktop (1280px) | Notes |
|------|---------------|----------------|-----------------|-------|
| Home | Pass | Pass | Pass | Filter overlay functions correctly on tablet |
| Shop | Pass | Pass | Pass | Category bar scrolls horizontally on mobile |
| Boardgame Detail | Pass | Pass | Pass | Image and detail columns stack correctly |
| Product Detail | Pass | Pass | Pass | Quantity controls remain accessible |
| Shopping Bag | Pass | Pass | Pass | Card layout on mobile, table layout on desktop |
| Checkout | Pass | Pass | Pass | Form fields stack cleanly on mobile |
| Checkout Success | Pass | Pass | Pass | Order summary readable at all sizes |
| Profile | Pass | Pass | Pass | Delivery form and order history stack on mobile |
| About / Contact | Pass | Pass | Pass | Contact form constrained correctly on large screens |
| Login | Pass | Pass | Pass | |
| Register | Pass | Pass | Pass | |
| Search Results | Pass | Pass | Pass | Cards reflow correctly |
| 404 Error Page | Pass | Pass | Pass | |
----------------------------------------------

### Code Validation

#### HTML Validation

HTML validation was carried out using the [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML Validation Service"). Pages were tested by direct URL input on the deployed Heroku application.

| Page | Result |
|------|--------|
| About | Pass |
| Add Product | Pass |
| Bag | Pass |
| Boardgame Detail | Pass |
| Checkout | Pass |
| Checkout Success | Pass |
| Edit Product | Pass |
| Home | Pass |
| Login | Pass |
| Log out | Pass |
| Product Detail | Pass |
| Profile | Pass |
| Search Results | Pass |
| Shop | Pass |

[about.html - Nu HTML Checker](docs/html-checker-about.png "about.html | Nu HTML Checker")

[add_product.html - Nu HTML Checker](docs/html-checker-add-product.png "add_product.html | Nu HTML Checker")

[bag.html - Nu HTML Checker](docs/html-checker-bag.png "bag.html | Nu HTML Checker")

[boardgame_detail.html - Nu HTML Checker](docs/html-checker-boardgame-detail.png "boardgame_detail.html | Nu HTML Checker")

[checkout.html - Nu HTML Checker](docs/html-checker-checkout.png "checkout.html | Nu HTML Checker")

[checkout_success.html - Nu HTML Checker](docs/html-checker-checkout-success.png "checkout_success.html | Nu HTML Checker")

[edit_product.html - Nu HTML Checker](docs/html-checker-edit-product.png "edit_product.html | Nu HTML Checker")

[home.html - Nu HTML Checker](docs/html-checker-home.png "home.html | Nu HTML Checker")

[login.html - Nu HTML Checker](docs/html-checker-login.png "login.html | Nu HTML Checker")

[logout.html - Nu HTML Checker](docs/html-checker-logout.png "logout.html | Nu HTML Checker")

[product_edit.html - Nu HTML Checker](docs/html-checker-edit-product.png "product_edit.html | Nu HTML Checker")

[profile.html - Nu HTML Checker](docs/html-checker-profile.png "profile.html | Nu HTML Checker")

[search/results.html - Nu HTML Checker](docs/html-checker-search-results.png "search/results.html | Nu HTML Checker")

[shop.html - Nu HTML Checker](docs/html-checker-shop.png "shop.html | Nu HTML Checker")

#### CSS Validation

CSS validation was carried out using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS Validation Service").

All css files passed without errors.

[base.css - Jigsaw](docs/jigsaw-css-validation.png "base.css | Jigsaw")

#### JS Validation

JavaScript files were validated using [JSHint](https://jshint.com/ "JSHint | Homepage").

| File | Result |
|------|--------|
| base.js | Pass |
| bag.js | Pass |
| index.js | Pass |
| reviews.js | Pass |
| shop.js | Pass |
| stripe_elements.js | Pass |

[base.js - JSHint](docs/js-hint-base.png "base.js | JSHint")

[bag.js - JSHint](docs/js-hint-bag.png "bag.js | JSHint")

[index.js - JSHint](docs/js-hint-index.png "index.js | JSHint")

[reviews.js - JSHint](docs/js-hint-reviews.png "reviews.js | JSHint")

[shop.js - JSHint](docs/js-hint-shop.png "shop.js | JSHint")

[stripe_elements.js - JSHint](docs/js-hint-stripe_elements.png "stripe_elements.js | JSHint")

#### Python Validation

Python files were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/ "CI Python Linter") to ensure PEP8 compliance.

| File | Result | Notes |
|------|--------|-------|
| settings.py | Pass | |
| urls.py (project) | Pass | |
| about/forms.py | Pass | |
| about/views.py | Pass | |
| bag/contexts.py | Pass | |
| bag/views.py | Pass | |
| checkout/forms.py | Pass | |
| checkout/models.py | Pass | |
| checkout/signals.py | Pass | |
| checkout/views.py | Pass | |
| checkout/webhooks.py | Pass | |
| checkout/webhook_handler.py | Pass | Long lines accepted for better overall code readability|
| home/forms.py | Pass | |
| home/models.py | Pass | |
| home/views.py | Pass | |
| profiles/forms.py| Pass | |
| profiles/models.py | Pass | |
| profiles/views.py | Pass | Long line accepted for better overall code readability|
| shop/forms.py| Pass | |
| shop/models.py | Pass | |
| shop/views.py | Pass | Long lines accepted for better overall code readability |

[settings.py - Python Linter](docs/python-linter-settings.png "settings.py | Python Linter")

[urls.py - Python Linter](docs/python-linter-urls.png "urls.py | Python Linter")

[about/forms.py - Python Linter](docs/python-linter-about-forms.png "about/forms.py | Python Linter")

[about/views.py - Python Linter](docs/python-linter-about-views.png "about/views.py | Python Linter")

[bag/contexts.py - Python Linter](docs/python-linter-bag-contexts.png "bag/contexts.py | Python Linter")

[bag/views.py - Python Linter](docs/python-linter-bag-views.png "bag/views.py | Python Linter")

[checkout/forms.py - Python Linter](docs/python-linter-checkout-forms.png "checkout/forms.py | Python Linter")

[checkout/models.py - Python Linter](docs/python-linter-checkout-models.png "checkout/models.py | Python Linter")

[checkout/signals.py - Python Linter](docs/python-linter-checkout-signals.png "checkout/signals.py | Python Linter")

[checkout/views.py - Python Linter](docs/python-linter-checkout-views.png "checkout/views.py | Python Linter")

[checkout/webhook_handler.py - Python Linter](docs/python-linter-checkout-webhook-handler.png "checkout/webhook_handler.py | Python Linter")

[checkout/webhooks.py - Python Linter](docs/python-linter-checkout-webhooks.png "checkout/webhooks.py | Python Linter")

[home/forms.py - Python Linter](docs/python-linter-home-forms.png "home/forms.py | Python Linter")

[home/models.py - Python Linter](docs/python-linter-home-models.png "home/models.py | Python Linter")

[home/views.py - Python Linter](docs/python-linter-home-views.png "home/views.py | Python Linter")

[profiles/forms.py - Python Linter](docs/python-linter-profiles-forms.png "profiles/forms.py | Python Linter")

[profiles/models.py - Python Linter](docs/python-linter-profiles-models.png "profiles/models.py | Python Linter")

[profiles/views.py - Python Linter](docs/python-linter-profiles-views.png "profiles/views.py | Python Linter")

[shop/forms.py - Python Linter](docs/python-linter-shop-forms.png "shop/forms.py | Python Linter")

[shop/models.py - Python Linter](docs/python-linter-shop-models.png "shop/models.py | Python Linter")

[shop/views.py - Python Linter](docs/python-linter-shop-views.png "shop/views.py | Python Linter")

#### Flake8

Flake8 was used in the IDE to highlight errors and style issues with python code during development. This allowed the majority of line length issues to be resolved and syntax errors to be caught early, reducing bug introduction.

### Automated Testing

Automated testing was implemented using Django's built-in test framework. Tests were written across all major apps covering model logic, view behaviour, form validation, access control, bag context calculations, and Stripe integration.

#### Running the Tests

```
python manage.py test
```

#### Test Coverage Summary

| App | Test Class | Tests | What is Tested |
|-----|-----------|-------|----------------|
| Home | `HomeViewTests` | 7 | Home page load, game display, genre/player/playtime filtering, sort by title, empty filter results |
| Home | `BoardgameDetailTests` | 4 | Detail page load, review visibility for anonymous users, staff review access, unapproved review visibility for review author |
| Home | `ModelTests` | 4 | Boardgame `__str__`, Review `__str__`, min/max player validation, review unique constraint enforcement |
| Home | `PermissionTests` | 3 | Non-staff cannot approve reviews, staff can approve reviews, favourite toggle requires login |
| Home | `ReviewTests` | 2 | Authenticated user can submit review, unauthenticated review submission redirects to login |
| Home | `SearchViewTests` | 3 | Search returns matching board games, search page loads with product results, empty query returns no results |
| Shop | `ShopViewTests` | 16 | Shop page load, product detail, empty search redirect, search results, sort by name/category/direction, category and parent filters, combined filters, category annotation, name sort annotation |
| Shop | `AdminProductTests` | 9 | Non-admin access denied for add/edit/delete, admin can access add page, admin can add/edit/delete products, invalid form submission handled |
| Shop | `ShopFilterTests` | 2 | Category filter, parent category filter |
| Shop | `ProductModelTests` | 4 | Product `__str__`, `is_in_stock` with and without stock, `get_readable_type` on Category |
| Shop | `ProductSizeTests` | 2 | Size stock affects availability, ProductSize `__str__` |
| Shop | `ProductFormTests` | 4 | Valid product form, invalid form missing name, form has crispy helper, category queryset populated |
| Bag | `BagViewTests` | 9 | Bag renders, add simple product, stock limit respected, add sized product, size required for sized product, adjust quantity, adjust clamps to stock, remove simple and sized products |
| Bag | `BagContextTests` | 3 | Total calculation, delivery calculation, free delivery threshold |
| Bag | `BagTests` | 1 | Add to bag POST request |
| Checkout | `OrderModelTests` | 2 | Line item total calculation, order total update |
| Checkout | `CheckoutViewTests` | 3 | Checkout page load, empty bag redirects, checkout success view |
| Checkout | `CheckoutSignalTests` | 2 | Stock reduction for simple product, stock reduction for sized product |
| Checkout | `StripeIntentTests` | 1 | Stripe PaymentIntent created on checkout page load (mocked) |
| Checkout | `WebhookHandlerTests` | 1 | Webhook handler returns 200 for unknown event |
| Checkout | `WebhookPaymentSuccessTests` | 1 | Payment success handler returns 200 |
| Checkout | `CheckoutEdgeCaseTests` | 2 | Checkout redirects with empty bag, invalid form submission handled |
| Checkout | `CheckoutIntegrationTests` | 1 | Full checkout POST flow creates order and clears bag |
| Checkout | `SaveInfoTests` | 1 | Checkout success view loads for authenticated user |
| Profiles | `ProfileViewTests` | 4 | Profile page load, profile update, invalid update handled, favourites display |
| Profiles | `ProfileOrderHistoryTests` | 1 | Past order appears in profile order history |
| Profiles | `OrderHistoryViewTests` | 1 | Order history view loads correct template |
| Profiles | `ProfileOwnershipTests` | 1 | Profile shows only the logged-in user's data |
| Profiles | `OrderIsolationTests` | 1 | User cannot see another user's orders |
| Profiles | `FavouriteIsolationTests` | 1 | Favourites are user-specific |
| Profiles | `ProfileUpdateIsolationTests` | 1 | Profile update does not affect other users |
| About | `AboutViewTests` | 4 | About page load, contact form in context, valid form submission, invalid form validation |

**Total: 100+ automated tests across all apps**

#### Key Testing Decisions

**Stock management** 
- The bag and checkout signal tests verify that stock is correctly decremented for both standard products and size variants when an order line item is saved. This tests a critical piece of custom business logic.

**Access control** 
- Admin product management tests confirm that unauthenticated and non-staff users receive 302 redirects when attempting to access protected views, while staff users can access them correctly. Review permission tests verify that only staff can approve reviews, and that the favourite system correctly requires authentication.

**Data isolation** 
- Profile isolation tests confirm that users cannot see each other's orders, favourites, or profile data, directly verifying the security of user-specific data.

**Stripe integration** 
- The Stripe PaymentIntent creation test uses `unittest.mock.patch` to mock the Stripe API, allowing the checkout flow to be tested without live API calls. The webhook handler tests verify that the handler responds correctly to both known and unknown event types.

**Model-level validation** 
- The `min_players` / `max_players` validation test confirms that the custom `clean()` method on `Boardgame` raises a `ValidationError` when `min_players` exceeds `max_players`. The `unique_together` constraint on `Review` is tested by attempting to create two reviews from the same user for the same game, verifying that an `IntegrityError` is raised.

----------------------------------------------

### User Story Testing
## User Story Testing Table

| User Story | Expected Outcome | Result | Pass/Fail | Evidence |
|------------|----------------|--------|-----------|----------|
| Browse games as a public user | Public users can view game titles, images, descriptions, and details without logging in | Site is browsable by non-authorised users | Pass | [Game list preview](docs/home-board-game-grid.png "Home Page") |
| Register a new account | Users can register with validation and receive confirmation feedback | Users can register for an account and receive an email allowing them to confirm their email address | Pass | [Register page preview](docs/register-desktop.png "Registration Page") |
| Login securely | Users can log in with valid credentials and are denied with invalid ones | Users who input correct credentials are redirected to the home page and can access their profile to view protected information. Invalid credentials display an error and prevent access to protected information | Pass | [Login page preview](docs/login-desktop.png "Login Page") |
| Post reviews | Logged-in users can submit reviews that appear under game details | Authorised users can write a review which appears visible to the review author and moderators, pending moderation. After moderation reviews are visible to all users. Unauthorised users are directed to log in or sign up before leaving a review | Pass | [Review section preview](docs/board-game-detail-with-reviews-tablet.png "Review Section") |
| Edit own reviews | Users can update their own reviews and see confirmation feedback | Authorised users can edit their own reviews using the edit button which dynamically fills the review form with their original content. The Submit Review button changes state to Update Review to indicate an edit is occurring. Edited reviews are then subject to moderation before being viewable by all users. Edit button is not visible to non-review author users | Pass | [Edit review preview](docs/boardgame-detail-edit-review.png "Edit Review") |
| Delete own reviews | Users can delete their own reviews with confirmation | Authorised users can click the delete button below their review to delete it after confirming the deletion in a pop up box. Delete button is not visible to non-review author users | Pass | [Delete review preview](docs/boardgame-detail-delete-review.png "Delete Review") |
| Save favourite games | Users can favourite games and view them in their profile | Authorised users can click the add to favourites button to add a boardgame to their favourites list. Favourited boardgames show an alternate state including a coloured heart icon and remove from favourites text. | Pass | [Favourites preview](docs/profile-favourites-desktop.png "Favourites") |
| Admin adds new game | Admin can create new game entries via admin panel | Staff and superusers can access the admin panel and use it to add new games, including use of a WYSIWYG rich text description field | Pass | [Admin add game review 1/3](docs/admin-panel-add-game-1.png "Admin Panel Add Game" ) <br><br> [Admin add game preview 2/3](docs/admin-panel-add-game-2.png "Admin Panel Add Game" ) <br><br> [Admin panel add game preview 3/3](docs/admin-panel-add-game-1.png "Admin Panel Add Game")|
| Admin edits game | Admin can update game details and changes reflect on frontend | Staff and superusers can access the admin panel and use it to edit the information about games, including use of a WYSIWYG rich text description field. Changes occur immediately on the frontend | Pass | [Admin edit game preview 1/2](docs/board-game-django-administration-one-desktop.png "Admin panel Edit Game" ) <br><br> [Admin edit game preview 2/2](docs/board-game-django-administration-two-desktop.png "Admin Panel Edit Game" ) |
| Admin deletes game | Admin can remove games and they no longer appear on the site | Staff and superusers can access the admin panel and use it to delete games, which immediately reflects on the frontend | Pass | [Admin delete game preview](docs/admin-panel-delete-game.png "Admin Panel Delete Game") |
| Admin moderates reviews | Admin can approve, decline, or delete reviews | Review moderation can be carried out by staff or superusers either through the admin panel or via on screen buttons below each review. On screen buttons are shown dynamically depending on each review's moderation status. Non-staff or superuser accounts cannot view the moderation buttons | Pass | [Admin moderation preview on page](docs/boardgame-detail-review-controls.png "Admin Controls on Page Review Control") <br><br> [Admin moderation preview in admin panel](docs/admin-review-controls.png "Moderation Controls in Admin panel")|
| Responsive design | Site adapts correctly across mobile, tablet, and desktop | Site layout was created following a mobile first approach, with media queries used to adapt elements as needed as screen size increases | Pass | [Home responsive preview mobile](docs/home-responsive-mobile.jpg "Mobile Home") <br> <br> [Home responsive preview tablet](docs/home-responsive-tablet.jpg "Tablet Home") <br> <br> [Home responsive preview desktop](docs/home-board-game-grid.png "Desktop Home") |
| Browse shop products | Users can view a list of products with images, names, and prices | All users can access the shop and view the product catalogue| Pass | [Shop preview](docs/shop-overview.png "Shop Page") |
| View product details | Users can access individual product pages with full details | All users can access the product detail pages to view further information and descriptions of each item in the product catalogue, as well as see whether the item or individual sizes of the item are in stock | Pass | [Product detail preview](docs/product-detail-desktop.png "Product Detail Page") |
| Add items to cart | Users can add products to cart and update quantities | All users can add in stock items to their basket and can view the basket, showing the quantity of each item in the basket. Item quantity can be adjusted using on screen buttons, up to the available stock limit. Items can also be removed using the remove button, or reducing the quantity to zero. | Pass | [Bag preview](docs/shopping-bag-desktop.png "Shopping Bag") |
| Complete purchase | Users can securely complete checkout and receive confirmation | All users can complete secure checkout using the embedded Stripe element on the checkout page. Authorised users can additionally save their delivery information to their profile for future purchases. All users are directed to their order confirmation page, after payment has been successful, showing the items ordered and the shipping details along with order total and unique order number.| Pass | [Checkout preview](docs/checkout-desktop.png "Checkout Page") |
| Admin adds product | Admin can create new products via admin panel | Staff and Superusers can add new products via the admin panel, with a WYSIWYG rich text description field or via the add product page. New products are immediately visible on the frontend  | Pass | [Admin add product](docs/add-product-page.png "Admin Panel Add Product") <br><br> [Product management page - add product 1/2](docs/add-product-management-page-1.png "Product Management Pages - Add Product 1/2") <br><br> [Product management page - add product 2/2](docs/add-product-management-page-2.png "Product Management Pages - Add Product 2/2") |
| Admin edits product | Admin can update product details such as price and description | Staff and Superusers can edit products via the admin panel, with a WYSIWYG rich text description field or via the edit product page. Changes are reflected immediately on the frontend | Pass | [Admin panel - edit product 1/2](docs/edit-product-page-ong-of-one.png "Admin Panel) Edit Product 1/2") <br><br> [Admin panel - edit product 2/2](docs/edit-product-page-ong-of-two.png "Admin Panel - Edit Product 2/2") <br><br> [Edit product Page 1/2](docs/edit-product-management-page-1.png "Product Management Pages - Edit Product 1/2") <br><br> [Edit product Page 2/2](docs/edit-product-management-page-2.png "Product Management Pages - Edit Product 2/2") |
| Admin deletes product | Admin can remove products and they no longer appear in shop | Staff and Superusers can delete products via the admin panel or via the delete product page. Deletions are reflected immediately on the frontend | Pass | [Admin delete product](docs/admin-panel-delete-product.png "Delete Product Admin Panel") |

### Feature Testing

Manual feature testing was carried out on the deployed Heroku application across desktop, tablet, and mobile viewports. Testing was carried out by the developer, friends and family on a variety of devices and browsers. As part of feature testing, authentication emails were sent to a genuine email address to test layout and domain name settings.

[Order confirmation email](docs/gamers-guild-order-confirmation-email.pdf "Example confirmation email")

[Email address confirmation](docs/confirm-email.png "Example Confirmation Email")

[Confirm email verification page](docs/confirm-email-verification.png "Confirm Email Verification Page")

[Account already exists email](docs/account-exists-email.png "Account Already Exists Email")


### Error Page Testing

The error pages can be viewed by:
- **400**: In home/views.py import 'BadRequest' from Django.core.exceptions then define the function for testing 400.
```
def test_400(request): 
    raise BadRequest
```
In home/urls.py add a new path at the top of urlpatterns to connect to the new view.
```
urlpatterns = [
    path("tests-400/", views.test_400),
]
```
Run the local server and then navigate to the [local deployment](http://127.0.0.1:8000)/test-400/ to view the error page. Once viewing of the error page is complete, remove all code edits to prevent users accessing the 400 error page mistakenly.
<br>
- **403**:  In home/views.py import 'PermissionsDenied' from Django.core.exceptions then define the function for testing 403.
```
def test_403(request):
    raise PermissionDenied
```
In home/urls.py add a new path at the top of urlpatterns to connect to the new view.
```
urlpatterns = [
    path("tests-403/", views.test_403),
  ]
```
In settings.py, set
<br>
`DEBUG = False`
<br>
Run the local server and then navigate to the [local deployment](http://127.0.0.1:8000/)/test-403 to view the error page. Once viewing of the error page is complete, remove all code edits to prevent users accessing the 403 error page mistakenly.
<br>
- **404**: - Visit the website at: 
<br>
https://gamers-guild-18d9a6433da1.herokuapp.com/incorrectlink 
<br>
The path does not need to be 'incorrectlink', it needs to be something other than a valid path. Once done, the error page should be displayed.
<br>
- **500**: - In home/index.html, prevent the block content code from running correctly, for example
<br>
`{% block content}`
<br>
Run the local server and the error page should be displayed.

### Accessibility Testing

Accessibility testing was carried out using the [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) and manual keyboard navigation testing.

All pages passed without errors. The checkout page could not be tested as an empty checkout instance redirects to the shop page as part of the site's defensive UI.

| Page | Result |
|------|--------|
| About | Pass |
| Bag | Pass |
| Boardgame Detail | Pass |
| Checkout Success | Pass |
| Home | Pass |
| Login | Pass |
| Product Detail| Pass |
| Search Results | Pass |
| Shop | Pass |
| Signup | Pass |

[About - Wave](docs/wave-about.png "About | Wave")

[Bag - Wave](docs/wave-bag.png "Bag | Wave")

[Boardgame Detail - Wave](docs/wave-boardgame-detail.png "Boardgame Detail | Wave")

[Checkout Success - Wave](docs/wave-checkout-success.png "Checkout Success | Wave")

[Home - Wave](docs/wave-home.png "Home | Wave")

[Login - Wave](docs/wave-login.png "Login | Wave")

[Product Detail - Wave](docs/wave-product-detail.png "Product Detail | Wave")

[Search Results - Wave](docs/wave-search-results.png "Search Results | Wave")

[Shop - Wave](docs/wave-shop.png "Shop | Wave")

[Signup - Wave](docs/wave-signup.png "Signup | Wave")

Manual testing of keyboard navigation highlighted no navigation issues.

**Additional accessibility measures implemented:**

- All images include descriptive `alt` attributes
- All interactive SVG icons include `aria-hidden="true"` and associated visible labels or `aria-label` attributes
- Form inputs are associated with labels using `for` and `id` attributes
- Colour contrast ratios meet WCAG AA standards across all colour combinations in use, as verified by the Contrast Grid
- Semantic HTML elements are used throughout, including `<header>`, `<main>`, `<footer>`, `<nav>`, `<section>`, and `<article>`
- Keyboard navigation is supported across all interactive elements


### Lighthouse Testing

Lighthouse audits were carried out using Chrome DevTools on the deployed Heroku application. Initial testing was performed on the home page as the most content-heavy page, containing 24 board game cards with images, filtering, and sorting functionality.

#### Initial Scores

| Page | Device | Performance | Accessibility | Best Practices | SEO |
|------|--------|-------------|---------------|----------------|-----|
| Home | Desktop | 71 | 98| 100| 91|
| Home | Mobile | 65 | 98| 100 | 100|

#### Issues Identified

The following performance issues were identified from the initial audit:

| Issue | Detail |
|-------|--------|
| Images slow to render | Resize and compress images | 
| Render-blocking CSS | Bootstrap CDN (26.9 KB) and base.css blocking initial render |
| Unused CSS | ~25 KB of Bootstrap CSS not used on any page |
| HTTP/1.1 used | Implement CloudFront for S3 buckets |
| Unused JS | ~23 KB of unused JS |
| Bootstrap icon font | Large size ~131 KB and long render chain|
| Short cache TTL | CloudFront serving static assets with only 1 day cache lifetime |

#### Changes Made

**1. Image resizing and compression**

All images were resized using [Squoosh](https://squoosh.app/ "Squoosh | Homepage") to more closely match displayed size on desktop devices and quality was reduced to ~80% to maintain visual impact.

**2. Bootstrap CSS optimisation using PurgeCSS**

The full Bootstrap 5.3.2 stylesheet (26.9 KB transfer) was analysed and stripped of all unused rules using [PurgeCSS](https://purgecss.com/ "PurgeCSS | Homepage"). All HTML templates, includes, and JavaScript files were scanned to identify every Bootstrap class in use across the project. A safelist was maintained to preserve classes applied dynamically via JavaScript, such as those used by Bootstrap's collapse, dropdown, accordion, and toast components.

The resulting purged stylesheet was served locally via CloudFront rather than the CDN, reducing the Bootstrap CSS transfer size from 26.9 KB to 11.7 KB — a reduction of 56%.

**3. CloudFront Implementation**

[AWS CloudFront](https://aws.amazon.com/cloudfront/ "AWS CloudFront | Homepage") was implemented using the gamers-guild S3 bucket as the origin. This resulted in faster content delivery and implementation of HTTP/2. It also allowed for efficient caching of static files, improving experience for returning visitors.

The `AWS_S3_OBJECT_PARAMETERS` setting was updated in `settings.py` to increase the cache lifetime of static assets from 1 day to 1 year:

```python
AWS_S3_OBJECT_PARAMETERS = {
    "Expires": "Fri, 1 Jan 2099 20:00:00 GMT",
    "CacheControl": "max-age=31536000, immutable",
}
```

This ensures that returning visitors load cached assets instantly rather than re-downloading them on every visit.

**4. Removal of Bootstrap Icon Font**

Originally, Bootstrap Icon Font was used to provide iconography across the site. Approximately 15 icons were used across all pages, with the total font size being ~131KB and introducing a long render chain on page load. Bootstrap Icon Font was removed and replaced with inline svg icons, significantly reducing the initial page load and reducing the length of the render chain.

#### Results After Optimisation

Following the series of optimisations Lighthouse testing was rerun, starting with the home page.

| Page | Device | Performance | Accessibility | Best Practices | SEO |
|------|--------|-------------|---------------|----------------|-----|
| Home | Desktop | 87 | 98| 100| 100|
| Home | Mobile | 73 | 98| 100| 100|
| Boardgame Detail | Desktop | 92 | 96| 96| 100|
| Boardgame Detail | Mobile | 90 | 95| 100| 100|
| Shop | Desktop | 83 | 96| 100| 100|
| Shop | Mobile | 82 | 95| 100| 100|
| Product Detail | Desktop | 94 | 100| 96| 100|
| Product Detail | Mobile | 90 | 100| 100| 100|
| Bag | Desktop | 93 | 94| 100| 91|
| Bag | Mobile | 87 | 93| 100| 91|
| Checkout | Desktop | 86 | 89| 78| 100|
| Checkout | Mobile | 88 | 89| 79| 100|
| Checkout Success | Desktop | 90 | 100| 100| 100|
| Checkout Success | Mobile | 92 | 100| 100| 100|
| About | Desktop | 96 | 100| 100| 100|
| About | Mobile | 92 | 100| 100| 100|
| Profile | Desktop | 92 | 92| 100| 100|
| Profile | Mobile | 91 | 92| 100| 100|

[Home desktop - Lighthouse](docs/lighthouse-home-desktop-report.pdf "Home Desktop | Lighthouse")

[Home mobile - Lighthouse](docs/lighthouse-home-mobile-report.pdf "Home Mobile | Lighthouse")

[Boardgame detail desktop - Lighthouse](docs/lighthouse-boardgame-detail-desktop-report.pdf "Boardgame Detail Desktop | Lighthouse")

[Boardgame detail mobile - Lighthouse](docs/lighthouse-boardgame-detail-mobile-report.pdf "Boardgame Detail mobile | Lighthouse")

[Shop desktop - Lighthouse](docs/lighthouse-shop-desktop-report.pdf "Shop Desktop | Lighthouse")

[Shop mobile - Lighthouse](docs/lighthouse-shop-mobile-report.pdf "Shop Mobile | Lighthouse")

[Product detail desktop - Lighthouse](docs/lighthouse-product-detail-desktop-report.pdf "Product Detail Desktop | Lighthouse")

[Product detail mobile - Lighthouse](docs/lighthouse-product-detail-mobile-report.pdf "Product Detail Mobile | Lighthouse")

[Bag desktop - Lighthouse](docs/lighthouse-bag-desktop-report.pdf "Bag Desktop | Lighthouse")

[Bag mobile - Lighthouse](docs/lighthouse-bag-mobile-report.pdf "Bag Mobile | Lighthouse")

[Checkout desktop - Lighthouse](docs/lighthouse-checkout-desktop-report.pdf "Checkout Desktop | Lighthouse")

[Checkout mobile - Lighthouse](docs/lighthouse-checkout-mobile-report.pdf "Checkout Mobile | Lighthouse")

[Checkout success desktop - Lighthouse](docs/lighthouse-checkout-success-desktop-report.pdf "Checkout Success Desktop | Lighthouse")

[Checkout success mobile - Lighthouse](docs/lighthouse-checkout-success-mobile-report.pdf "Checkout Success Mobile | Lighthouse")

[About desktop - Lighthouse](docs/lighthouse-about-desktop-report.pdf "About Desktop | Lighthouse")

[About mobile - Lighthouse](docs/lighthouse-about-mobile-report.pdf "About Mobile | Lighthouse")

[Profile desktop - Lighthouse](docs/lighthouse-profile-desktop-report.pdf "Profile Desktop | Lighthouse")

[Profile mobile - Lighthouse](docs/lighthouse-profile-mobile-report.pdf "Profile Mobile | Lighthouse")

#### Remaining Considerations

The mobile score is affected by factors outside the scope of this project:

- **Heroku Eco dyno cold starts** — Eco dynos sleep after 30 minutes of inactivity, adding latency to the initial server response on mobile simulations. Upgrading to a Basic dyno would eliminate this.
- **Render-blocking CSS** — The remaining 16.8 KB of CSS (base.css + purged Bootstrap) still blocks initial render. Full elimination would require critical CSS inlining, which is a significant implementation effort.
- **Image payload** — 24 board game cards load on the home page simultaneously. Pagination or a "load more" pattern would reduce initial image requests, but was not implemented as it would conflict with the desktop scrollable card layout UX.

These are documented in [Future Enhancements](#future-enhancements).

The best practice score for Checkout is reduced due to the use of third party cookies, necessary for Stripe functionality.



### Browser Testing

| Browser | Home | Shop | Checkout | Profile | Notes |
|---------|------|------|----------|---------|-------|
| Chrome | Pass | Pass | Pass | Pass | Primary development browser |
| Firefox | Pass | Pass | Pass | Pass | |
| Safari | Pass | Pass | Pass | Pass | Tested on macOS and iOS |
| Edge | Pass | Pass | Pass | Pass | |

[Back to contents](#contents)

---------------------------------------------

## Deployment

### Local Deployment

To run this project locally on an Apple Mac, start by cloning the repository using the following steps.

1. Navigate to the GitHub repository for this project: [Gamers Guild GitHub repository](https://github.com/Lyd-W/gamers-guild. "GitHub | Gamers Guild Repository").
2. Click the **Code** button and copy the HTTPS repository URL.
3. Open the terminal in your IDE and run the following command:
```
git clone https://github.com/Lyd-W/gamers-guild.git
```
<br>

Next,

1. Run the following command in the terminal to create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
2. Run the following command in the terminal to install the required dependencies for the project:
```
pip install -r requirements.txt
```
3. Create a directory level file called **env.py**
4. Add the newly created **env.py** file to **.gitignore**
5. Inside **env.py**, assign the following variables:
```
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME
EMAIL_HOST_USER
EMAIL_HOST_PASS
```
6. Run database migrations by running the following code in the terminal:
```
python3 manage.py migrate
```
7. Run the following command in the terminal to create a new superuser:
```
python3 manage.py createsuperuser
```
8. Run the following command in the terminal to run the local development server:
```
python3 manage.py runserver
```
9. In your chosen web browser, navigate to: http://127.0.0.1:8000/ to view the project locally.

----------------------------------------------

### Heroku Deployment

The project was deployed to Heroku from VS Code, using GitHub integration, early on. This allowed for more opportunity to notice errors, as well as to view and test the website at regular intervals. The steps used for deployment were as follows:

**1. Create a New Heroku App**

- Log into Heroku and access your dashboard.
- Click **"New"** from the top right corner of your dashboard and select **'Create new app'**.
- Enter a unique name for your app and choose your closest region (EU or USA), click **'Create app'** to create your app.

**2. Configure Environment Variables**

- Go to the **'Settings'** tab of your new app, in the **'Config Vars'** section, click **'Reveal Config Vars'**.
- Add the following keys and values:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Your Django secret key |
| `DATABASE_URL` | Your PostgreSQL database URL |
| `STRIPE_PUBLIC_KEY` | Your Stripe publishable key |
| `STRIPE_SECRET_KEY` | Your Stripe secret key |
| `STRIPE_WH_SECRET` | Your Stripe webhook signing secret |
| `AWS_ACCESS_KEY_ID` | Your AWS access key |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret key |
| `AWS_STORAGE_BUCKET_NAME` | Your S3 bucket name |
| `USE_AWS` | `True` |
| `EMAIL_HOST_USER` | Your email address |
| `EMAIL_HOST_PASS` | Your email app password |
| `DISABLE_COLLECTSTATIC` | `1` (remove before final deployment) |

**3. Prepare the Project for Deployment in the IDE**

- Create a `requirements.txt` file to list all of the dependencies required by your project. This can be done by running `pip3 freeze --local > requirements.txt` in the terminal, it can then be updated to include any other packages installed by running `pip3 freeze > requirements.txt`  in the terminal.
- Install **'gunicorn'** using the command `pip3 install gunicorn` in the terminal and update **'requirements.txt'**.
- Create a **'Procfile'** in the root directory of the project, add the following line of code to the Procfile `web: gunicorn project_name.wsgi` Ensure project_name matches the project's name.
- Update the `ALLOWED_HOSTS` list in `settings.py` to include **'.herokuapp.com',**.
- Commit changes to Github using the following commands
```
git add .
git commit -m "Deployment configuration"
git push
```

**4. Connect Your GitHub Repository to Heroku**

- On the Heroku dashboard, click on the **'Deploy'** tab, in the **'Deployment method'** section, click **'Connect to GitHub'** where you will be prompted to authenticate with GitHub.
- Type your project repo name into the search box and click **'Search'**, select the correct repo name.
- Scroll down to the **'Manual Deploy'** section, ensure the **'Choose a branch to deploy'** is set to **'main'**, then click on the **'Deploy Branch'** button.
- Once the **'Your app was successfully deployed.'** message is displayed, click the **'View'** button to open your deployed project in a new tab.

----------------------------------------------

### WhiteNoise

Gamers Guild uses [WhiteNoise](https://whitenoise.readthedocs.io/) to serve static files directly from the Django application in production, without requiring a separate static file server.

WhiteNoise is configured as middleware in `settings.py`:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]
```

It sits immediately after `SecurityMiddleware`, which is the recommended position. In this project, WhiteNoise handles static file serving locally and as a fallback, while in production on Heroku with `USE_AWS` enabled, static files are served via AWS S3 and CloudFront instead. WhiteNoise remains in the middleware stack in both environments without causing conflicts.

To install WhiteNoise use the command

```
pip install whitenoise
```

It requires no additional configuration beyond the middleware entry — Django's `STATIC_ROOT` and `STATICFILES_DIRS` settings are sufficient for it to locate and serve files correctly.

### Stripe Setup

Gamers Guild uses [Stripe](https://stripe.com "Stripe | Homepage" ) to handle payment processing. Follow the steps below to configure Stripe for both local development and production.

**Create a Stripe account and get API keys:**

1. Register or log in at [https://stripe.com](https://stripe.com "Stripe | Homepage")
2. From the Stripe dashboard, navigate to **Developers > API Keys**
3. Copy your **Publishable key** and **Secret key**
4. Add these to your `env.py` for local development:
```python
os.environ["STRIPE_PUBLIC_KEY"] = "pk_test_..."
os.environ["STRIPE_SECRET_KEY"] = "sk_test_..."
```
5. Add these as Config Vars in Heroku for production

**Set up a webhook:**

Stripe webhooks allow the server to confirm payment success independently of the client redirect, protecting against failed or interrupted connections after payment.

1. In the Stripe dashboard, navigate to **Developers > Webhooks**
2. Click **Add destination**
3. For local development, use the [Stripe CLI](https://stripe.com/docs/stripe-cli "Stripe | CLI Docs") to forward webhooks:
```
stripe listen --forward-to localhost:8000/checkout/wh/
```
4. For production, set the destination URL to:
```
https://your-app-name.herokuapp.com/checkout/wh/
```
5. Select the following events to listen for:
   - `payment_intent.succeeded`
   - `payment_intent.payment_failed`
6. After creating the webhook, copy the **Signing secret** and add it to your environment:
```python
os.environ["STRIPE_WH_SECRET"] = "whsec_..."
```

**Test payments:**

1. Use Stripe's test card numbers during development. The standard test card is:

| Field | Value |
|-------|-------|
| Card number | `4242 4242 4242 4242` |
| Expiry | Any future date |
| CVC | Any 3 digits |
| Postcode | Any valid postcode |

2. In the Stripe dashboard, navigate to **Developers > Events**

3. Check the logged events for `payment_intent.created`,`payment_intent.succeeded`, `charge.succeeded` and `charge.updated` with a `200 OK` Status.

4. To test `payment_intent.payment_failed, use this test card:

| Field | Value |
|-------|-------|
| Card number | `4000 0000 0000 0002` |
| Expiry | Any future date |
| CVC | Any 3 digits |
| Postcode | Any valid postcode |

5. In the Stripe dashboard, navigate to **Developers > Events**

6. Check the logged events for `payment_intent.payment_failed` with a `200 OK` Status.

----------------------------------------------

### AWS S3 and CloudFront Setup

Gamers Guild uses [AWS S3](https://aws.amazon.com/s3/ "AWS S3 | Homepage") to store static files and media uploads in production, served via [AWS CloudFront](https://aws.amazon.com/cloudfront/ "AWS CloudFront | Homepage") as a CDN for improved performance.

**Create an S3 bucket:**

1. Log in to the [AWS Management Console](https://aws.amazon.com/ "AWS | Homepage")
2. Navigate to **S3** and click **Create bucket**
3. Give the bucket a unique name (e.g. `gamers-guild-static`)
4. Select the AWS region closest to your users
5. Uncheck **Block all public access** — the bucket needs to be publicly readable for static file serving
6. Click **Create bucket**

**Configure the bucket:**

1. Open the bucket and navigate to **Permissions → CORS configuration** and add the following:
```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
2. Navigate to **Permissions → Bucket policy** and add a policy to allow public read access:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

**Create an IAM user:**

1. Navigate to **IAM → Users → Add user**
2. Give the user a name (e.g. `gamers-guild-staticfiles-user`)
3. Select **Programmatic access**
4. Attach the **AmazonS3FullAccess** policy
5. Complete the process and download the CSV containing the **Access Key ID** and **Secret Access Key**
6. Add these to your environment:
```python
os.environ["AWS_ACCESS_KEY_ID"] = "your-access-key-id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your-secret-access-key"
os.environ["AWS_STORAGE_BUCKET_NAME"] = "your-bucket-name"
os.environ["AWS_S3_REGION_NAME"] = "your-region"
```

**Set up CloudFront:**

CloudFront serves static files from edge locations geographically close to the user, significantly reducing load time. Gamers Guild uses a CloudFront distribution with a 1-year cache TTL on static assets, which contributed to the Lighthouse performance improvements documented in the testing section.

1. Navigate to **CloudFront > Create distribution**
2. Set the **Origin domain** to your S3 bucket URL
3. Under **Default cache behaviour**, set **Viewer protocol policy** to **Redirect HTTP to HTTPS**
4. Click **Create distribution** and copy the **Distribution domain name** 
5. In `settings.py`, set the custom domain:
```python
AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")
```
6. Add this to your environment:
```
AWS_S3_CUSTOM_DOMAIN = "your-distribution-id.cloudfront.net"
```

**Configure Django to use S3:**

The `settings.py` file contains the following AWS configuration block (already present in this project):

```python
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Fri, 1 Jan 2099 20:00:00 GMT",
        "CacheControl": "max-age=31536000, immutable",
    }
    STATICFILES_LOCATION = "static"
    MEDIAFILES_LOCATION = "media"
    STORAGES = {
        "default": {"BACKEND": "custom_storages.MediaStorage"},
        "staticfiles": {"BACKEND": "custom_storages.StaticStorage"},
    }
```

A `custom_storages.py` file in the project root defines the custom storage backends:

```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

Once `USE_AWS` is set to `True` in Heroku Config Vars and `DISABLE_COLLECTSTATIC` is removed, running `python manage.py collectstatic` will push all static files to your S3 bucket automatically on the next deployment.

---------------------------------------------

[Back to contents](#contents)

---------------------------------------------

## Credits and Acknowledgements

### Feedback, advice and support

- With thanks to [Richey Malhotra](https://github.com/richey-malhotra "GitHub | richey-malhotra") who has been encouraging, supportive, and above-all, consistent. His guidance through this turbulent time has been invaluable, with his knowledge, skill and advice being greatly appreciated.

### Learning Resources and Guidance

- [ChatGPT](https://chatgpt.com/ "ChatGPT | Homepage")
- [Code Institute](https://codeinstitute.net/ "Code Institute")
- [MDN](https://developer.mozilla.org/en-US/ "MDN | Homepage")
- [Reddit](https://www.reddit.com/ "Reddit | Homepage")
- [Slack](https://slack.com/intl/en-gb/ "Slack")
- [Stack Overflow](https://stackoverflow.com/ "Stack Overflow")
- [W3 Schools](https://www.w3schools.com/ "W3 Schools")
- [YouTube](https://youtube.com/ "YouTube | Homepage")

### Code Attribution

The bag, checkout, and Stripe integration follow patterns established in the Code Institute Boutique Ado walkthrough project, which formed the structural basis for the e-commerce functionality. All code has been reviewed, understood, and adapted to fit the Gamers Guild project's specific requirements, models, and design. Custom implementations, including the board game discovery system, review and rating functionality, filtering and sorting system, favourites feature, self-referential shop category structure, and the automated test suite, were written independently.

### Image Credits:

Images were sourced from various websites, details are listed below.

- Ark Nova image - [Board Game Geek](https://boardgamegeek.com/image/6293412/ark-nova "Board Game Geek | Ark Nova")
- Azul image - [Board Game Geek](https://boardgamegeek.com/image/6973671/azul "Board Game Geek | Azul Image")
- Brass Birmingham image - [Board Game Geek](https://boardgamegeek.com/image/3490053/brass-birmingham "Board Game Geek | Brass Birmingham Image")
- Carcassonne image - [Board Game Geek](https://boardgamegeek.com/image/8621446/carcassonne "Board Game Geek | Carcassonne Image") 
- Catan image - [Board Game Geek](https://boardgamegeek.com/image/9156909/catan "Board Game Geek | Catan Image")
- D&D Official Dice Set image - [Element Games](https://elementgames.co.uk/vampire-counts/role-playing-games-books/rpg-dice/official-dice-set-dungeons-and-dragons-ddn-vat "Element Games | D&D Official Dice Set")
- Dungeon Mayhem image - [Board Game Geek](https://boardgamegeek.com/image/5324418/dungeon-mayhem-monster-madness "Board Game Geek | Dungeon Mayhem Image")
- Exploding Kittens image - [Board Game Geek]( https://boardgamegeek.com/image/2691976/exploding-kittens "Board Game Geek | Exploding Kittens")
- Flashpoint image - [Board Game Geek](https://boardgamegeek.com/image/1129370/flash-point-fire-rescue "Board Game Geek | Flashpoint Image")
- Gamers Guild Fav Icon and Logo - [Fav Icon](https://favicon.io/favicon-generator/ "Fav Icon | Generator")
- Gamers Guild Dice Tray images - [Gemini](https://gemini.google.com "Google Gemini | Homepage")
- Gamers Guild Hoody images - [Gemini](https://gemini.google.com "Google Gemini | Homepage")
- Gamers Guild T Shirt images - [Gemini](https://gemini.google.com "Google Gemini | Homepage")
- Gloomhaven image - [Board Game Geek](https://boardgamegeek.com/image/7546274/gloomhaven-second-edition "Board Game Geek | Gloomhaven Image")
- Gloomhaven Organiser image - [Folded Space](https://foldedspace.com/product/gloomhaven-second-edition "Folded Space | Gloomhaven Organiser")
- HeroQuest image - [Board Game Geek](https://boardgamegeek.com/image/338410/heroquest "Board Game Geek | HeroQuest Image")
- Lords of Waterdeep image - [Board Game Geek](https://boardgamegeek.com/image/9230112/lords-of-waterdeep "Board Game Geek | Lords of Waterdeep Image")
- MicroMacro image - [Hachette Boardgames](https://www.hachetteboardgames.co.uk/shop/eswmmfh-micromacro-crime-city-full-house-2289 " Hachette Boardgames | MicroMacro")
- One Deck Dungeon image - [Board Game Geek](https://boardgamegeek.com/image/3496794/one-deck-dungeon-forest-of-shadows "Board Game Geek | One Deck Dungeon Image")
- One Night Werewolf image - [Board Game Geek](https://boardgamegeek.com/image/8783294/one-night-ultimate-werewolf "Board Game Geek | One Night Werewolf Image")
- Pandemic image - [Board Game Geek](https://boardgamegeek.com/image/1534148/pandemic "Board Game Geek | Pandemic Image")
- Pandemic: In The Lab image - [Z-Man Games](https://www.zmangames.com/game/pandemic-in-the-lab/ "Z-Man Games | Pandemic: In The Lab")
- Pandemic: On The Brink image - [Z-Man Games](https://www.zmangames.com/game/pandemic-on-the-brink/ "Z-Man Games | Pandemic: On The Brink")
- Pandemic: State of Emergency image - [Z-Man Games](https://www.zmangames.com/game/pandemic-state-of-emergency/ "Z-Man Games | Pandemic: State of Emergency")
- Placeholder image - Created by [ChatGPT](https://chatgpt.com/ "ChatGPT | Homepage")
- Robinson Crusoe Deluxe Tokens image - [The Game Steward](https://www.thegamesteward.com/products/robinson-crusoe-resin-tokens-board-game-accessory "The Game Steward | Robinson Crusoe Resin Tokens")
- Robinson Crusoe image - [Board Game Geek](https://boardgamegeek.com/image/3165731/robinson-crusoe-adventures-on-the-cursed-island "Board Game Geek | Robinson Crusoe Image")
- Robinson Crusoe Organiser image - [Folded Space](https://foldedspace.com/product/robinson-crusoe "Folded Space | Robinson Crusoe Organiser")
- Robinson Crusoe Playmat image - [Portal Game](https://shopportalgames.com/products/robinson-crusoe-playmat "Portal Games | Robinson Crusoe Playmat")
- Terraforming Mars image - [Board Game Geek](https://boardgamegeek.com/image/3536616/terraforming-mars "Board Game Geek | Terraforming Mars Image")
- The Fox Experiment image - [Board Game Geek](https://boardgamegeek.com/image/7557488/the-fox-experiment "Board Game Geek | The Fox Experiment Image")
- Through the Ages image - [Board Game Geek](https://boardgamegeek.com/image/2663291/through-the-ages-a-new-story-of-civilization "Board Games Geek | Through the Ages Image")
- Tiny Epic Dungeons image - [Board Game Geek](https://boardgamegeek.com/image/6029065/tiny-epic-dungeons "Board Game Geek | Tiny Epic Dungeons Image")
- Tiny Epic Dungeons Playmat image - [Board Game Geek](https://boardgamegeek.com/image/6821417/tiny-epic-dungeons-official-game-mat "Board Game Geek | Tiny Epic Dungeons Playmat Image")
- Tiny Epic Tactics image - [Board Game Geek](https://boardgamegeek.com/image/4574827/tiny-epic-tactics "Board Game Geek | Tiny Epic Tactics Image")
- Tiny Epic Zombies image - [Board Game Geek](https://boardgamegeek.com/image/3937056/tiny-epic-zombies "Board Game Geek | Tiny Epic Zombies Image")
- Wingspan image - [Board Game Geek](https://boardgamegeek.com/image/4458123/wingspan "Board Game Geek | Wingspan Image")
- Zombicide image - [Board Game Geek](https://boardgamegeek.com/image/6091316/zombicide-2nd-edition "Board Game Geek | Zombicide Image")

### Content:

Content was sourced from various websites, details are listed below.

- Ark Nova information - [Board Game Geek](https://boardgamegeek.com/boardgame/342942/ark-nova "Board Game Geek | Ark Nova")
- Azul information - [Board Game Geek](https://boardgamegeek.com/boardgame/230802/azul "Board Game Geek | Azul")
- Brass Birmingham information - [Board Game Geek](https://boardgamegeek.com/boardgame/224517/brass-birmingham "Board Game Geek | Brass Birmingham")
- Carcassonne information - [Zatu](https://zatu.com/products/carcassonne-2015-new-edition?_pos=2&_psq=carcasso&_ss=e&_v=1.0 "Zatu | Carcassonne")
- Catan information - [Catan](https://www.catan.com/ "Catan | Homepage")
- Reviews and descriptions - [ChatGPT](https://chatgpt.com/ "ChatGPT | Homepage")
- D&D Official Dice Set information - [Magic Madhouse](https://magicmadhouse.co.uk/wizards-of-the-coast-d-d-official-dice-set "Magic Madhouse | D&D Official Dice Set")
- Dungeon Mayhem information - [Board Game Geek]( https://boardgamegeek.com/boardgame/295577/dungeon-mayhem-monster-madness "Board Game Geek | Dungeon Mayhem")
- Exploding Kittens information - [Board Game Geek](https://boardgamegeek.com/boardgame/172225/exploding-kittens "Board Game Geek | Exploding Kittens")
- Gamers Guild Dice Tray information - [Gemini](https://gemini.google.com "Google Gemini | Homepage")
- Gamers Guild Hoody information - [Gemini](https://gemini.google.com "Google Gemini | Homepage")
- Gamers Guild T Shirt information - [Gemini](https://gemini.google.com "Google Gemini | Homepage")
- Gloomhaven information - [Board Game Geek](https://boardgamegeek.com/boardgame/390478/gloomhaven-second-edition "Board Game Geek | Gloomhaven")
- Gloomhaven Organiser information - [Folded Space](https://foldedspace.com/product/gloomhaven-second-edition "Folded Space | Gloomhaven Organiser")
- Flash Point information - [Board Game Geek]( https://boardgamegeek.com/boardgame/100901/flash-point-fire-rescue "Board Game Geek | Flash Point")
- HeroQuest information - [Asmodee](https://www.asmodee.co.uk/collections/all-heroquest-games "Asmodee | HeroQuest")
- Lords of Waterdeep information - [Board Game Geek](https://boardgamegeek.com/boardgame/110327/lords-of-waterdeep "Board Game Geek | Lords of Waterdeep")
- MicroMacro information - [Zatu](https://zatu.com/products/micromacro-crime-city-full-house?_pos=3&_sid=e49eeb6f5&_ss=r "Zatu | MicroMacro")
- One Deck Dungeon information - [Board Game Geek](https://boardgamegeek.com/boardgame/224821/one-deck-dungeon-forest-of-shadows "Board Games Geek | One Deck Dungeon")
- One Night Werewolf information - [Board Game Geek]( https://boardgamegeek.com/boardgame/147949/one-night-ultimate-werewolf "Board Game Geek | One Night Werewolf")
- Pandemic information - [Zman Games](https://www.zmangames.com/game/pandemic/ "Zman Games | Pandemic")
- Pandemic: In The Lab information - [Z-Man Games](https://www.zmangames.com/game/pandemic-in-the-lab/ "Z-Man Games | Pandemic: In The Lab")
- Pandemic: On The Brink information - [Z-Man Games](https://www.zmangames.com/game/pandemic-on-the-brink/ "Z-Man Games | Pandemic: On The Brink")
- Pandemic: State of Emergency information - [Z-Man Games](https://www.zmangames.com/game/pandemic-state-of-emergency/ "Z-Man Games | Pandemic: State of Emergency")
- Robinson Crusoe Deluxe Tokens information - [The Game Steward](https://www.thegamesteward.com/products/robinson-crusoe-resin-tokens-board-game-accessory "The Game Steward | Robinson Crusoe Resin Tokens")
- Robinson Crusoe information - [Portal Games](https://shopportalgames.com/collections/robinson-crusoe/products/robinson-crusoe-2e "Portal Games | Robinson Crusoe")
- Robinson Crusoe Organiser information - [Folded Space](https://foldedspace.com/product/robinson-crusoe "Folded Space | Robinson Crusoe Organiser")
- Robinson Crusoe Playmat information - [Portal Game](https://shopportalgames.com/products/robinson-crusoe-playmat "Portal Games | Robinson Crusoe Playmat")
- Terraforming Mars information - [Board Game Geek]( https://boardgamegeek.com/boardgame/167791/terraforming-mars "Board Game Geek | Terraforming Mars")
- The Fox Experiment information - [Board Game Geek](https://boardgamegeek.com/boardgame/368432/the-fox-experiment "Board Game Geek | The Fox Experiment")
- Through the Ages information - [Board Game Geek](https://boardgamegeek.com/boardgame/182028/through-the-ages-a-new-story-of-civilization "Board Game Geek | Through the Ages")
- Tiny Epic Dungeons information - [Board Game Geek](https://boardgamegeek.com/boardgame/331787/tiny-epic-dungeons "Board Game Geek | Tiny Epic Dungeons")
- Tiny Epic Dungeons Playmat information - [Board Game Geek](https://boardgamegeek.com/boardgameaccessory/360513/tiny-epic-dungeons-official-game-mat "Board Game Geek | Tiny Epic Dungeons Playmat")
- Tiny Epic Tactics information - [Board Game Geek](https://boardgamegeek.com/boardgame/272409/tiny-epic-tactics "Board Game Geek | Tiny Epic Tactics")
- Tiny Epic Zombies information - [Board Game Geek](https://boardgamegeek.com/boardgame/244536/tiny-epic-zombies "Board Game Geek | Tiny Epic Zombies")
- Wingspan information - [Board Game Geek](https://boardgamegeek.com/boardgame/266192/wingspan "Board Games Geek | Wingspan")
- Zombicide information - [Zombicide](https://www.zombicide.com/2nd-edition/ "Zombicide | 2nd Edition")

### Visual Content

Wireframes were created using Canva
The colour scheme was generated using Coolors
The contrast grid was generated using Contrast Grid by Eightshapes
The Entity Relationship Diagram was created using dbdiagram.io

---------------------------------------------

[Back to contents](#contents)

---------------------------------------------