Poker Game Backend

A Python-based poker game project implementing core card, deck, player, and game logic, with a Flask backend and Prisma database integration.

Overview

This project explores the backend logic behind a poker game, including card and deck management, player state, game state, turns, betting, and poker-hand evaluation.

The project is structured into separate components for the game engine and backend application.

Features

* Card and deck management
* Deck shuffling and card dealing
* Human and computer player objects
* Player cards, bets, and game state
* Community card management
* Turn management between players
* Poker-hand evaluation logic
* Command-line game functionality
* Flask backend
* Prisma database integration
* JWT and password-hashing components

Technologies

* Python
* Flask
* Prisma
* SQLite/PostgreSQL-compatible database tooling
* JWT
* bcrypt
* Pipenv

Project Structure

poker-game-backend/
├── app/              # Flask application and backend components
├── game/             # Poker game logic
│   ├── card.py
│   ├── deck.py
│   ├── game.py
│   ├── player.py
│   └── cli.py
├── prisma/           # Database schema
├── app.py             # Flask entry point
└── main.py            # Application entry point

Key Concepts

Game Logic

The game package contains the core poker logic, including:

* Creating and shuffling a deck
* Dealing cards to players
* Managing players
* Managing turns
* Tracking the pot and bets
* Managing community cards
* Evaluating poker hands

Backend

The Flask application provides the backend layer and integrates with Prisma for database access.

Running the Project

1. Clone the repository

git clone https://github.com/Yasmine101-101/poker-game-backend.git
cd poker-game-backend

2. Install Python dependencies

pipenv install
pipenv shell

3. Install JavaScript/Prisma dependencies

npm install

4. Run the application

python main.py

What I Learned

This project strengthened my understanding of:

* Object-oriented programming in Python
* Designing game logic and managing application state
* Working with classes and object relationships
* Backend application structure
* Flask development
* Database integration with Prisma
* Authentication concepts
* Building command-line applications
