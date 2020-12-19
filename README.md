# Github-Trends

## Context:
The project in shortest explanation possible is a REST microservice, that generates 
a list of trending languages collated from 100 trending repositories in the last 30
days on Github. For each on the list of languages, comes the number of repositories 
using the Language and the repository + repository details of each. 

## Concept:
Using datetime module to get 30 days before (to pass into github's api parameters), 
then using the requests module, data is fetched from api.github.com/search; this data 
is then used as json(Python's dictionary) and is passed to a serializer; which 
manipulates the data and returns a json format containing the list of languages, 
the number of repositories using each language and also each of the repository/project 
and its details, using a language.
       
## Installation
```shell script
# create and setup a virtual environment
$ python3 -m venv GithubTrends
# Move Into the folder
$ cd GithubTrends/
# activate the environment
$ source bin/activate
# make a dir for the project and move into it
$ mkdir GithubTrends && cd GithubTrends/
# clone the project
$ git clone https://github.com/adewolejosh/github-trends.git
# install all dependencies
$ pip install -r requirements.txt

# You're done with the installation!
```

## How to Run
```shell script
# run the app
# remember to set environment variable e.g SECRET_KEY, DEBUG by adding a .env file
$ python3 manage.py runserver

# check it out at localhost:8000/api/trends/
```

## Endpoint
 Development:
- `localhost:8000/api/trends/ `
    - returns an object of items, which consists of the following : 
        - list of Languages, from the 100 trending repositories
        - a language, number of repositories using it, the repositories using it`


## Trade-Offs
- As specified, no need for databases or cache, so the commands 
`$ python3 manage.py makemigrations && python3 manage.py migrate` can be ignored when
running the app.
- Since the app has only one required endpoint, swagger ui or postman or any major
documentation wasn't taken into consideration.
- Github's API permits about 60 unauthenticated requests per hour, so I didn't worry
about getting an API key and all other details for an authenticated request. Though I
enforced a rate-limiting on the API.
- The sorting algo in serializers could be a lot shorter but I later realized some
repositories return "null" as the language, so I had to take that into consideration.
Would look into reducing it though.
 
 
## Author
- Joshua Adewole
 [Github](https://github.com/adewolejosh)
 [Twitter](https://twitter.com/adewole_josh/) 

Inspired and in total thanks to The team at Gemography for the coding challenge!
