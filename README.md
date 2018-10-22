[![Build Status](https://travis-ci.com/Allan690/StoreManager-API.svg?branch=develop)](https://travis-ci.com/Allan690/StoreManager-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/8c940897901ce84ceeb6/maintainability)](https://codeclimate.com/github/Allan690/StoreManager-API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Allan690/StoreManager-API/badge.svg?branch=develop)](https://coveralls.io/github/Allan690/StoreManager-API?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8add588aea5f4eeb941b7f166cc7bdf9)](https://www.codacy.com/app/Allan690/StoreManager-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Allan690/StoreManager-API&amp;utm_campaign=Badge_Grade)
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/3b5f48196e4b3a68d97c)

# Store Manager-API
Store Manager API is a flask RESTful API that implements token based authentication with endpoints that enable the user
to:
- register and login to the store
- add, modify and delete products from the store
- view sale records 
- add sale records

## Example request with response
```
curl --request POST \
  --url https://store-manager-api-app-v1.herokuapp.com/api/v1/auth/register \
  --header 'Content-Type: application/json' \
  --data '{
  "email": "testuser999@gmail.com",
  "password": "testuserpass"
}'

Response body
{
"message": "User registered successfully"
}

Response code 
{
201
}
Response header
{
"connection":"keep-alive"
"content-length" :"48"
"content-type": "application/json"
"date": "Sat, 20 Oct 2018 12:37:59 GMT"
"server": "gunicorn/19.9.0"
"via": "1.1 vegur"
}

```
## Getting Started

1) Clone the repository by doing: `git clone https://github.com/Allan690/StoreManager-API.git`

2) Create a virtual environment: `virtualenv env`

3) Activate the virtual environment: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows.

4) Install the requirements : `pip install -r requirements.txt`

## Running tests
You can either do: `pytest app\tests` or `nosetests app\tests`

### Prerequisites

-   python 3.6
-   virtual environment

## Running it on machine
- Create a .env file to store your environment variables: `touch .env`
- In the `.env` file add this line: `export SECRET=<your-secret-key-here`
- On terminal do: `source .env`
- Run the application: `flask run`
- The api endpoints can be consumed using postman.

## Endpoints
| Endpoint                                   | FUNCTIONALITY                      |
| ----------------------------------------   |:----------------------------------:|
| POST /api/v1/auth/register                 | This will register  the user       |
| POST /api/v1/auth/login                    | This will login a registered user  |
| POST /api/v1/auth/logout                   | This will log out a logged in user |
| POST /api/v1/auth/reset-password           | This will reset the password       | 
| POST  /api/v1/products                     | This will add a product            |
| POST  /api/v1/sales                        | This will add a sale               | 
| GET  /api/v1/products                      | This will get all products         |
| GET  /api/v1/products/productId            | retrieve a single product by id    |
| GET  /api/v1/sales                         | retrieve all sale records          |
| GET  /api/v1/sales/salesId                 | retrieves a single sale record     | 
| PUT  /api/v1/products                      | This will modify a product         | 
| PUT  /api/v1/sales                         | This will modify a sales record    | 
| DELETE  /api/v1/products/productId         | Deletes a product by its id        | 
| DELETE  /api/v1/sales/salesId              | Deletes a sales record by id       | 

## Heroku application
https://store-manager-api-app-v1.herokuapp.com/

## API documentation
https://documenter.getpostman.com/view/4671755/RWguwwQQ#intro
- *Note*: if using the above documentation for running the application on your local machine, just replace the heroku app
link with your localhost e.g `localhost:5000/api/v1/auth/register` for the registration endpoint

## Built With
* [Flask](http://flask.pocoo.org/) -  The web framework used
* [Pip](https://pypi.python.org/pypi/pip) -  Dependency Management

## Authors
* **Allan Mogusu** 

## License

This project is licensed under the MIT License

