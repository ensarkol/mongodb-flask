# Mongodb Flask Application

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





### Solved CI/CD part with Github Actions.
1. When the repo received new commit, new image is building in actions.
2. Pushing new image to docker hub



### USAGE
1. Clone the repo
2. Run `bash.sh` on your local.
3. MongoDB cluster is ready to use, Flask and Go applications endpoints is avaliable at your localhost.

![Screenshot from 2023-04-02 18-20-12](https://user-images.githubusercontent.com/97634177/229373794-85e76ccc-4c24-431d-8416-b26b8d2f19a5.png)

![Screenshot from 2023-04-02 18-22-51](https://user-images.githubusercontent.com/97634177/229373821-333e52e4-19a4-4312-82fd-613dd69278b1.png)
