# Online-Shopping-REST-API

#### DESCRIPTION

 -    Built a REST Api in Python.
 -    A RESTful Api built for serving as a Backend for a Shopping Cart.
 -    Customer object has one required field; [string]Name.
 -    Has an API for a customer to make a purchase 
 -    Tracks the number of purchases made by a customer. 
 -    Returns the cost of the purchase.
 -    Cost is $100 minus a loyalty discount.


#### REQUIREMENTS

 - Python 3.8.10
 - Flask 
 - pip
 - Firecamp
 - Postman

#### INSTALLATION INSTRUCTIONS
-   Clone or download the repo. into any fresh temporary folder.
-   Cd into that root folder you just cloned locally.
-   Open terminal in the current folder and create a virtual enevironment

    ```
    python3 -m venv env
    ```
-   Activate the environment
    ```
    source /path-to-the-folder/env/bin/activate
    ```
- Install pip3
    ```
    sudo apt install python3-pip
    ```
- Install python3
    ```
    sudo apt install python3
    ```
- Install Flask
   ```
    pip3 install Flask
    ```
- Execute app.py file which will start a server.
   ```
    python3 app.py
    ```
    
    App should now be running on **localhost:5000**
         
### Dependencies 
 - Dependencies are
    import json
    from flask import Flask, jsonify, request


### For Testing (Firecamp)
- Firecamp extension can be used for testing !
- You can now fire up postman and then perform several operations on the REST API.

## Available API Routes

### [Customer Routes](#1-Customer-routes)
| Routes        | Description           | 
| ------------- |:-------------:|
| [`GET/customers/<name>`](#a-get-a-customer's-purchase-count)    |Get a customer's purchase count|
| [`POST/new/`](#b-sign-up-a-new-customer)     | Sign up a new customer |     
| [`PUT/purchases/<name>`](#c-put-customer-purchase-count)    |Put customer purchase|
| [`DELETE/customers/<name>`](#d-delete-a-customer) |Delete a customer from database |

## 1. Customer Routes

### A. Get customer.
Send Get request to fetch the list of Orders in JSON format..
```
Method: GET 
URL: /customers/<name>
Produces: application/json
```
  #### Example 1  :
  - **Request** : /customers/alice
  - **Response**: 200 OK
  
````json
{
    "alice": 4
}
````
#### Example 2 :
  - **Request** : /customers/billy
  - **Response**: 400 BAD REQUEST
  
````json
{
    "error": "data not found"
}
````
----

### B. Create a new customer
     
```
Method: POST
URL: /new/<name>
Produces: application/json
```
#### Parameters :
| Field        | Type           |Required  |Description |
| ------------- |:-------------:|:-------:|:-----:|
| name   | String |Required    | Name of the customer |

#### Example 1:
- **Request:**  `/new/bazooka`

- **Response:** 200 OK
````json
{
    "bazooka": 0
}
````  
#### Example 2:
- **Request:**  `/new/alice`

- **Response:** 422 Invalid input
````json
{
    "error": "customer already exists or name is invalid"
}
````  
----

### C. Customer Purchase

```
Method: PUT
URL: /purchases/<name>
Produces: application/json
```
#### Example 1 :
- **Request:**  `/purchases/bazooka`

- **Response:**
````json
{
    "bazooka": 1,
    "price": 99
}
````   
#### Example 2 :
- **Request:**  `/purchases/pepper`

- **Response:** 422 Invalid name
````json
{
    "error": "Enter a valid name"
}
```` 
----

### D. Delete a particular customer
  ```
Method: DELETE
URL: /customers/<name>
Produces: application/json
```
#### Example 1 :
- **Request:**  `/customers/alice`

- **Response:**
````json
{
    "deleted": "alice"
}

````  
#### Example 2 :
- **Request:**  `/customers/alice`

- **Response:** 400 Bad Request
````json
{
    "error": "data not found"
}
````  
