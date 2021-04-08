## FINAL GROUP PROJECT_CS490
    Group 8
    Akshay Patel 
    Albert Wang 
    Marco Paparatto 
    Shayed Ahmed 

## Industry Mentor: Anita Anderson (Facebook)

## Music Game web app.


## Requirements
    1. npm install
    2. pip install -r requirements.txt
    3. pip install flask-socketio
    4.pip install flask-cors
    5.npm install socket.io-client --save
    6.pip install psycopg2-binary
    7.pip install Flask-SQLAlchemy==2.1
## Setup
    Run echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local in the project directory
## Clone the Repo:
    


## Run Application
    Run command in terminal (in your project directory): python app.py
    Run command in another terminal, cd into the project directory, and run npm run start
    Preview web page in browser '/'

## Deploy to Heroku
    Create a Heroku app: heroku create --buildpack heroku/python
    Add nodejs buildpack: heroku buildpacks:add --index 1 heroku/nodejs
    Push to Heroku: git push heroku main
## Heroku app link:
