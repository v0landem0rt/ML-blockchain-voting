# ML-blockchain-voting
Here is example of a voting application that verifies a voter face, using js video capture and machine learning model, then sends voting results to the blockchain.  This is a django app vith registration and frontend.  
## Requirements for project
To use this project you need:
+ install postgres and django framevork
+ install ML model(this model, which verify face of voters) -- https://github.com/efffna/verification_person
you should setup this model at __$PROJECT_HOME__ directory. 
+ Then you need to do : __export PROJECT_HOME=/path__
+ __pip3 install -r requirements.txt__
+ You need to setup ssl cert, because brovser does not allowed js video stream without https connection
+ To serve this app I used nginx-gunicorn binding(__restart.sh__ used for apply changes to app config, it used after __python3 manage.py migrate__ command). Folder with nginx and gunicorn configs contains default nginx sites-avaliable server config(with https), gunicorn socket and service config.

+ blockchain(in work)
