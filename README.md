# Our-Connected-Future
Connecting businesses and people with great ideas during a time of need.

# Now everything will run inside docker to handle ease of use with different packages and scalability

## To run Django Webserver
1. Install Docker: https://docs.docker.com/get-docker/
2. Make sure Docker is running on your machine.
3. Go to the root directory of the repository (where the .yml files are)
3. Run `docker-compose -f docker-compose.prod.yml logs -f`

Now docker will install python, postgresql etc in a container and then start the django webserver and the database.
The django webserver will be available at http://127.0.0.1:8000/ 

## Handy commands to run things with the created containers
#### stop all containers:
`docker kill $(docker ps -q)`

#### remove all containers
`docker rm $(docker ps -a -q)`

#### remove all docker images
`docker rmi $(docker images -q)`

#### remove all docker volumes
`docker volume ls -qf dangling=true | xargs  docker volume rm`

#### For docker to rebuild:
`docker-compose -f docker-compose.yml up --build -d`
 
#### See error messages in building container:
`docker-compose logs -f`

#### Can also specify the yml file
`docker-compose -f docker-compose.prod.yml logs -f`

#### Inspect a volume created
`docker volume inspect django-on-docker_postgres_data`

#### Access database
`docker-compose exec db psql --username=hello_django --dbname=hello_django_dev`

#### to run python scripts:
`docker-compose exec web python3 manage.py createsuperuser`
