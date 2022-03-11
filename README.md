# Hangman Game

Hangman game is a simple guessing Python terminal game that user guesses a number each time. There is a hint that tells the user if the number guessed is too big or too small from the target. The user keeps guessing until guesses a correct number or until reaches the maximum attempts allowed.


## User Experience UX

 ### User Stories

 * As a first time user, I want the game to be easily accessible.
 * As a first time user, I want to know how to play the game.
 * As a game user, I want to know the game result.
 * As a game user, I want to be able to continuesly play the game as I wish.

[Back to top](#hangman-game)

 ### Site Owner Stories

 The purpose of the site is to provide an easy and fun guessing game for everyone to enjoy.

## Existing Features

The game is built using Python only.

* There is a welcome message on the start screen.
* It asks user if the user would like to play game or not.
* The game exits if the user enters 'no'.
* It asks for user's name afterwards if the user enters 'yes.
* It gives user hints about the range of numbers to be entered.
* It prints one piece of Hangman body graphics on each time user enters a wrong number.
* It displays a win message if the user wins the game.
* It displays a lost message if the user loses the game.
* It asks user to play again or not. The game restarts if the answer is 'yes'. The game exits if the answser is 'no'.


[Back to top](#hangman-game)

## Technologies Used

* [GitHub]() - to host the files and the content of the game.
* [GitPod]() - to edit the code and push the code to GitHub page.
* [Python]() - to create the code for the game.

[Back to top](#hangman-game)

## Testing

## Libraries

The ```random``` module is imported to generate a random number for the project.

## Deployment

### Deploy the project to Heroku

  1. Log in to my personal Heroku account page, select ```Create new app```, give a name to the new app, choose a ```region``` from the drop down list to```Europe```. Then click ```Create app```.
  
  2. Go to the ```Settings``` tab afterwards, click ```Add buildpack``` button on the right side of the ```Buildpacks section```, first select ```python``` and add it, then select ```nodejs``` and add it.


  3. Go to the ```Deploy``` tab, click ```GitHub``` in the ```Deployment method``` section, search for the repo on GitHub, click ```Connect```. 
  4. In the ```Manual deploy```section, seclect ```main``` and then click ```Deploy Branch``` button, the app was successfully deployed after a while. 
  5. Click the ```View``` button on the bottom of the page or the ```Open app``` button on the top right corner to view the programme.





## Credit

* I watched Python tutorials by [Corey Schafer](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU) on [YouTube]() to learn more about Python.

* The Hangman graphics are from [Shaun Halverson](https://www.youtube.com/watch?v=pFvSb7cb_Us) on [YouTube]().
  
* I watched Python mini projects by [Tech With Tim](https://www.youtube.com/watch?v=DLn3jOsNRVE&t=1515s) on [YouTube]() to gain the extra knowledge for building the Hangman game.

[Back to top](#hangman-game)

## Acknowledgement

* Whilst I have tried to deviate as much as possible, there might be some similarities in the code as the project was influenced by the code along Love Sandwiches project at [Code Institute]().

* I relied upon the support from Code Institue [online tutors](),  mentor [Precious Ijege](),  project lead [David Bowers](), Slack community and my families. Great thanks to all those who support my learning journey. 
  
* I use W3schools, YouTube and stack overflow for general references throughout the project. I watched the tutorial videos on Youtube to gain extra knowledge about Python.

* The [Hangman Game]() application is intended for education purpose of completing the Portfolio Project 3 for the Diploma of Full Stack Software Development course at [Code Institue](https://codeinstitute.net/).

[Back to top](#hangman-game)