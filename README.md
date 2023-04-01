# Mongodb Flask and Go Application

### Creating mongodb cluster using docker compose
1. You can create mongoDb cluster by running docker-compose up
2. A MongoDB database named "stajdb" has been created
3. 2 collections named "ülkeler" and "iller" were created
4. In mongodb, user name "stajuser" password was created as "stajpassword" with test.sh script
5. ReplicaSet will be created with init scripts





### Python wep app with Flask
1. İmport necessary libraries into python application
2. Base image of docker container running for web application is python:3.8-slim-buster
3. The web application is running on port 4444 in a docker container.
4. Flask will print "Merhaba Python" in app /endpoint
5. When a request is made to the web application /staj path, it will return a random province data from the provinces collection(iller) in the stajdb database we created in MongoDB, also /allData endpoint used for get all collection(iller) data from database.


### USAGE
1. Clone the repo
2. Run `bash.sh` on your local.
3. MongoDB cluster is ready to use, Flask and Go applications endpoints is avaliable at your localhost.
