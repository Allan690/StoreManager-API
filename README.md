[![Build Status](https://travis-ci.com/Allan690/StoreManager-API.svg?branch=develop)](https://travis-ci.com/Allan690/StoreManager-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/4d3b5c08dcfcee62cac2/maintainability)](https://codeclimate.com/github/Allan690/StoreManager-API/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Allan690/StoreManager-API/badge.svg?branch=develop)](https://coveralls.io/github/Allan690/StoreManager-API?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8add588aea5f4eeb941b7f166cc7bdf9)](https://www.codacy.com/app/Allan690/StoreManager-API?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Allan690/StoreManager-API&amp;utm_campaign=Badge_Grade)


# Store Manager API
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.
## Required Features
1.  Store attendant can search and add products to buyer’s cart.
2. Store attendant can see his/her sale records but can’t modify them.
3. App should show available products, quantity and price.
4. Store owner can see sales and can filter by attendants.
5. Store owner can add, modify and delete products.


## Optional Features
1. Store owner can give admin rights to a store attendant.
2.  Products should have categories.
3.  Store attendants should be able to add products to specific categories.



## Getting Started

1) Clone the repository by doing: `git clone https://github.com/Allan690/StoreManager-API.git`

2) Create a virtual environment: `virtualenv env`

3) Activate the virtual environment: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows.

4) Install the requirements : `pip install -r requirements.txt`

## Running tests
You can either do: `pytest app\tests` or `nosetests app\tests`

### Prerequisites

- python 3.6

- virtual environment

## Running it on machine
- source `.env`

- `flask run`

## ENDPOINTS
| Endpoint                                | FUNCTIONALITY |
| ----------------------------------------|:-------------:|
| POST /api/v1/auth/register                 | This will register  the user       |
| POST /api/v1/auth/login                    | This will login a registered user  |
| POST /api/v1/auth/logout                   | This will log out a logged in user |
| POST /api/v1/auth/reset-password           | This will reset the password       | 
| POST  /api/v1/products                     | This will add a product       |
| POST  /api/v1/sales                        | This will add a sale         | 
| GET  /api/v1/products                          | This will get all products      |
| GET  /api/v1/products/productId                | retrieve a single product by id   |
| GET  /api/v1/sales                             | retrieve all sale records |
| GET  /api/v1/sales/salesId                 | retrieves a single sale record      | 
| PUT  /api/v1/products                 | This will modify a product | 
| PUT  /api/v1/sales                | This will modify a sales record  | 
| DELETE  /api/v1/products/productId             | Deletes a product by its id    | 
| DELETE  /api/v1/sales/salesId                 | Deletes a sales record by id  | 

      
       
       


## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pip](https://pypi.python.org/pypi/pip) - Dependency Management

 

## Authors

* **Allan Mogusu** 



## License

This project is licensed under the MIT License

