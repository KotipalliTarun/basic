{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b78a01bd-9afa-4b3f-b8cc-8b6f8548a489",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "May I ask you for your name?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " Tarun\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tarun, we are going to play a game. I am thinking of a number between 1 and 200\n",
      "Go ahead. Guess!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  100\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  150\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too high\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  120\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too low\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  148\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The guess of the number that you have entered is too high\n",
      "Try Again!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Guess:  132\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nope. The number I was thinking of was 130\n",
      "Do you want to play again?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " no\n"
     ]
    }
   ],
   "source": [
    "import random #bring in the random number\n",
    "import time\n",
    "number=random.randint(1, 200) #pick the number between 1 and 200\n",
    "\n",
    "def intro():\n",
    "    print(\"May I ask you for your name?\")\n",
    "    name=input() #asks for the name\n",
    "    print(name + \", we are going to play a game. I am thinking of a number between 1 and 200\")\n",
    "    time.sleep(.5)\n",
    "    print(\"Go ahead. Guess!\")\n",
    "\n",
    "def pick():\n",
    "    guessesTaken = 0\n",
    "    while guessesTaken < 6: #if the number of guesses is less than 6\n",
    "        time.sleep(.25)\n",
    "        enter=input(\"Guess: \") #inserts the place to enter guess\n",
    "        try: #check if a numbera was entered\n",
    "            guess = int(enter) #stores the guess as an integer instead of a string    \n",
    "\n",
    "            if guess<=200 and guess>=1: #if they are in range\n",
    "                guessesTaken=guessesTaken+1 #adds one guess each time the player is wrong\n",
    "                if guessesTaken<6:\n",
    "                    if guess<number:\n",
    "                        print(\"The guess of the number that you have entered is too low\")\n",
    "                    if guess>number:\n",
    "                        print(\"The guess of the number that you have entered is too high\")\n",
    "                    if guess != number:\n",
    "                        time.sleep(.5)\n",
    "                        print(\"Try Again!\")\n",
    "                if guess==number:\n",
    "                    break #if the guess is right, then we are going to jump out of the while block\n",
    "            if guess>200 or guess<1: #if they aren't in the range\n",
    "                print(\"Silly Goose! That number isn't in the range!\")\n",
    "                time.sleep(.25)\n",
    "                print(\"Please enter a number between 1 and 200\")\n",
    "\n",
    "        except: #if a number wasn't entered\n",
    "            print(\"I don't think that \"+enter+\" is a number. Sorry\")\n",
    "            \n",
    "    if guess == number:\n",
    "        guessesTaken = str(guessesTaken)\n",
    "        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')\n",
    "\n",
    "    if guess != number:\n",
    "        print('Nope. The number I was thinking of was ' + str(number))\n",
    "\n",
    "playagain=\"yes\"\n",
    "while playagain==\"yes\" or playagain==\"y\" or playagain==\"Yes\":\n",
    "    intro()\n",
    "    pick()\n",
    "    print(\"Do you want to play again?\")\n",
    "    playagain=input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19dc923b-5f03-4962-9d77-f683bc5c8540",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
