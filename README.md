# Python Flask API CRUD  
## Development version  
python v3.7.3    

# Requirements
`pip install mysql-connector-python`  
`pip install -U flask-cors`  

# Configure
open `index.py` and edit `setLocalhost`, `Database`, `setUsername`, `setPassword`, `setTableName` and `PORT`    
<img src="assets/img/migrate.png" width="30%">   

open `controller/Users.py` and edit `setLocalhost`, `Database`, `setUsername`, `setPassword`, `setTableName` and `PORT`    
<img src="assets/img/users.png" width="30%">   

# Operations  

* Create  
* Read    
* Update    
* Delete   

# Usage  
```
FLASK_APP=index.py flask run 
```
```
migrate - http://127.0.0.1:5000/migrate
```
```
Create [POST] - http://127.0.0.1:5000/users/create {name:john, address: philippines}
```
```
Read [GET] - http://127.0.0.1:5000/users
```
```
Update [POST] - http://127.0.0.1:5000/users/1/update {name:john, address: philippines}
```
```  
Delete [GET] - http://127.0.0.1:5000/users/1/delete
```
  
# Postman
## Home  
<img src="assets/img/home.png" width="30%">   

## Create  
<img src="assets/img/create.png" width="30%">   

## Read  
<img src="assets/img/read.png" width="30%">   

## Update  
<img src="assets/img/update.png" width="30%">   

## Delete  
<img src="assets/img/delete.png" width="30%">   

Use Postman to Test API Request
[Postman](https://www.getpostman.com/)  
