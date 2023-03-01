This repo contains the core pieces of my fully-functional and live website, compfolks.com

**How to find everything in the repo:**

**app_bb:** contains the HTML templates

**commands:** contains the python scraping scripts and z-score scripts

**css:** contains the CSS

**favicon:** contains the logo information for browsers

**js:** contains the javascript

**forms.py:** contains user forms

**models.py:** contains the database structure

**views.py:** renders pages and contains the model simulation scripts

**DESCRIPTION**

This project is a fully-functional, live website (CompFolks.com) that enables users to build a custom computer model to predict the outcome of baseball games, with no coding required by the user. The user can take advantage of a clean interface, make choices of what they want to include in the model, and then run their very own baseball model. CompFolks.com was built using the Django framework and is hosted on Heroku.

I spent months learning and practicing the skills to build a full-stack website from scratch. On the backend, I write and maintain Python scraping scripts to import batter/pitcher/team statistics. The scraping scripts run daily, and I continuously refactor and optimize these scripts. The first version that ran correctly for some scripts took ~30 minutes to run and more memory than the allotted servers could handle. After a series of optimizations, no script takes longer than 6 minutes to run, and all are well within memory limits.

When writing these scripts, I had to debug many errors along the way. For example, the first time I wrote the fielding scripts, I forgot to allow designated hitters to have blank fielding stats, and it took time to find the issue and fix it. Pitchers having infinite ERA's and strikeout/walk ratios with a zero denominator (pitchers who have not walked a batter) offered similar challenges.

After the statistics have been updated, the z-score computation scripts run automatically with Heroku scheduling. For every batter/pitcher/team, the scripts compute the z-score in each statistic ahead of time; in other words, before anyone even clicks to run a model. This turns the load on the hosting servers at runtime (especially during peak moments) from impossibly burdensome to entirely bearable.

One of the most important scripts is the matchup-scraper. It runs automatically every five minutes and imports matchups to the website database, so that when users run their model, each matchup that has lineups posted online can be simulated. The result of the simulation is passed back to the front end, and ultimately, using dynamically generated HTML and JavaScript, the user can view their custom model results for the day’s games. The matchup import script is so important that I created two versions of it which operate on different lineup-posting websites but produce identical results. This was done so that even if the default scraper's website changes its HTML, the other can run in its stead with only minimal downtime of switching the backup to be the default scraper.  

Ultimately, when the user clicks submit, their input is processed on the backend and passed to the model simulation. The model code was originally written without modularity, which meant that it could only produce a result for the day’s matchups. I wanted to develop a new webpage that simulates any matchup using an advanced single-game mode that would allow the user to custom select every batter in the lineup and custom assign innings to individual pitchers. I wanted to reuse already-written simulation code, so I refactored the code to make it highly modular. This improved readability and maintainability, while also allowing me to use already-written blocks of code for the new webpage.

Administratively, I observe website analytics, monitor load on servers, and schedule automated scripts. I develop new software in a separate testing environment. Before implementing updates, I test the functionality and user interface with feedback from real users. The testing environment also has its own test database, so that anything running in testing does not affect what the user sees in production. For repeat users, I use cookies to keep all of their input saved for the next time they use the site. I use pickle for conversions for non-JSON-compliant objects.

On the front end, I constructed and tested a user-friendly experience using HTML, CSS, and JavaScript. For example, it took several JavaScript iterations of a "loading circle" before I found one that achieved desired functionality. I needed to implement a “loading circle” because in testing, users repeatedly hit the submit button, causing their request to be reset and take even longer. When I implemented the loading circle, I did not want the circle to remain in place of the submit button if the user clicked “back” on their browser. The button needed to properly reset (back to a regular submit button) when users clicked the "back" button on the browser; otherwise, the user would be forced to refresh the page if they wanted to run their model again. My first attempt of a loading circle worked on Google Chrome, but it broke down on other browsers. Using virtual machines for testing, I eventually found a solution that worked across multiple browsers.

It also took a long series of trial-and-error / user testing until I achieved a clean, friendly interface which worked across multiple screen sizes and browser types. This was especially challenging for the webpage which took in user input (“workshop”). I needed to balance my mission to give power-users as much choice as possible, while avoiding intimidating novice users. One area where I achieved this was by using default selections in the "general" tab, which allows more experienced users to fine-tune their model, while allowing novice users to simply skip ahead. Furthermore, I spent a lot of time developing and testing the webpages so that they would be enjoyable to use on both small and large screens.

To further ease of use, I used JavaScript to form a built-in running calculator. The calculator informs the user of the current total and implicitly instructs them to ensure all of their categories sum to 100. I spent a significant amount of time writing methods to catch possible user input errors on the front end, and to indicate how to rectify the errors clearly and immediately. I also crafted instructive error messages from the back end; I know from experience how frustrating poorly-worded error messages can be, and I wanted to make sure no one felt that way when using CompFolks.com.

Over several months, I have collected a dedicated fanbase that provides constructive input and eagerly awaits new features. I plan on continuing to learn, improve, and expand. The future is bright at CompFolks.com
