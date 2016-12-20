# Project Plan

## 1. Team
604998 Susanna Nevalainen
546807 Rohan Krishnakumar
464840 Nazia Hussain

## 2. Goal
In this project we will be building an online game store for JavaScript games. The game store will be a marketplace where players can buy games and developers can sell their games on the platform.

### Planned Features:
    - Registration
            As a developer: add games to their inventory, see list of game sales
            As a player: buy games, play games, see game high scores and record their score to it
    - Authentication
            Login, logout, Email validation
    - Basic player functionalities
    - Buy games
    - Payment
    - Play games
    - Security restrictions
    - Search 
    - Basic developer functionalities:
    - Add a game (URL)
    - set price for the game
    - remove/modify game
    - Basic game inventory and sales statistics
    - Security restrictions
    - Game/service interaction:
    - postMessage to the parent window containing the current score after game 
    - ranking list 
    - player score history
    - Messages from service to the game
    - Additional features:
    		- Social media sharing
    		- Third party login (Gmail)
    - Responsive UI for mobile


## 3. Plans

### 3.1. Technology 
We will use Django for the backend and for the front end HTML5, CSS3, JQuery and Javascript. For the database we will use SQLite.  

### 3.2. Pages
The platform will have multiple pages. For the basic functionality we have discussed the following important views in our web-application:

    1. Home Page (To display all the games available)
    2. Game Page (A page where the game can be played/bought)
    3. User/Developer Dashboard (User can see bought games, Developer can see added games)
    4. Sign-up (To register new player/developer)
    5. Log-in (For sign in)

### 3.3. Models	
We plan to have the following models:

#### 3.3.1. User 
It will store the user details and will have a flag which will tell apart whether the user is a player or a developer. We will check the flag and provide appropriate functionality to the user.
Fields:
	* Id
	* Name
	* Last Name
	* Email
	* Password
	* Developer Flag


#### 3.3.2. Game
The Game model will store all the games added by developers to the marketplace. It will also store the price set by the developer.
Fields:
	* Id
	* Developer Id (from User model)
	* Title
	* Source (Link to the HTML file)
	* Price (set by developer)
	* Category (Game category to facilitate searching)
	
#### 3.3.3. PlayerGame
This model is to keep track of which user has purchased what games. When a player purchases a game, it will be added to this table against the username of the player. This will also keep track of the game state and the score of the player.
Fields:
	* Game Id (from Game model)
	* Player Id (From User model)
	* PurchasedOn Timestamp (When the game was purchased)
	* PurchasePrice (Price at which game was purchased, used in statistics)
	* State
	
#### 3.3.4. ScoreBoard
This model will keep track of the score submission from games. Whe a player is playing a game and a score is submitted, it will add a new entry in this table. 
Fields:
	* Timestamp (Time at which the score is submitted)
	* Game Id (from Game model, game which submitted the score)
	* Player Id (from User model, player playing the game)
	* Score 


### 3.4. Implementation of Features
Following sections describe the plans for implementing each feature:

#### 3.4.1. Authentication
We plan to use the Django Authentication system to implement authentication service for the users and developers. The Login view will be for input and a session will be created when a user logs in. Based on the user type (player or developer), he will be directed to appropriate dashboard (player or developer). We will also include email verification process. 

#### 3.4.2. Developer Functions
The developer functions will be accessed from the developer dashboard view. To add new games, we will create a new view which will add the game link and its price to the Game model. We will also provide the functionality to update the price of the game. The sales statistics can be shown on the dashboard and can be gathered from the PlayerGame model. 

#### 3.4.3. Player Functions
A player can see the games bought by him from the player dashboard view. To play the game, we will create a Game view. Upon navigating to the Game view, we will confirm if he has bought the game (from PlayerGame model) and then load the iframe.
If the player has not bought the game, then a "Buy" option will be presented. When the player buys the game, an entry will be created in the PlayerGame table. The recommended mock payment service will be used. 
A player can find the games from the Home view, where games will be able to be searched based on category and text input.

#### 3.4.4. Game/Service Integration
The integration between the game and service will be done using message transfer between the iFrame and the parent window. The messages will be used as described in the project requirements.

#### 3.4.5. Security
We will make the application try to prevent SQL Injections, XSS, CSRF attacks.

#### 3.4.6. Extra features
The extra features we plan to implement are:
    Social media sharing
    Third party login (Gmail)
    Responsive UI for mobile
    If time permits, we will try to implement other features. 


### 3.4. Priorities
We will be focusing on the basic features and goals first. We start with the models, views and Heroku deployment. With time, additional features could be supported. If we have extra time, we can also consider features outside the original plan.


## 4. Process and Time Schedule
So far, we have decided to collaborate over email. Moreover, we will be meeting in the campus every alternate day to discuss about the current status of the project and take appropriate actions. We will distribute work equally amongst the team members.


### Following is the rough timeline for the project:

    Due Date	Feature Completion
    08-01-2016	Heroku deployment, Basic HTML Views, Models, and Authentication
    15-01-2016	Developer and Player Functionality
    30-01-2016	Payment Functionality + Save Load features
    10-02-2016	Home View and Searching games
    15-02-2016	Final touch up and bug fixes

### Following diagram outlines a rough division of work:
    ![alt text] https://git.niksula.hut.fi/files/note/3289/Screen_Shot_2016-12-16_at_4.04.10.png


## 5. Testing
We will use the example game provided to test the game service. The UI will be tested using different browsers (Chrome/Firefox/IE) on different platforms (Mobile/Tablets/Desktops).

## 6. Risk Analysis
In the worst case we will not have time to finish even basic features but it is not likely if we start according to the plan and stick to it. The consequences would be lower grade than expected.
Another risk is that we are implementing same features without knowing that someone else is doing the same. As we have divided the tasks beforehand, this is not very likely but in case schedule will change this is a possible risk. Consequences would be lost time in the development.