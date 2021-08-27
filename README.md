# ML-blockchain-voting
Here is example of a voting application that verifies a voter using a machine learning model and sends voting results to the blockchain 
## Requirements for project
To use this project you need:
+ install ML model(this model, which verify face of voters) -- https://github.com/efffna/verification_person
you should setup this model at __$PROJECT_HOME__ directory. 
+ Then you need to do : __export PROJECT_HOME=/path/to/model__
+ __pip3 install -r requirements.txt__
+ You need to setup ssl cert, because brovser does not allowed js video stream without https connection
+ To serve this app I used nginx-gunicorn binding 

+ blockchain(in work)
