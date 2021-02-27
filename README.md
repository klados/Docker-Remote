# Docker Remote 


## setup:
* install dependencies: `pip install -r requirements.txt`
* start mysql: ` sudo systemctl start mysql`
* run server: `unicorn -w 2 --reload -b localhost:5000 "main:app"`  