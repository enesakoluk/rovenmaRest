# RovenmaREST
## 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
## Start
```sh
cd compose
docker compose up
```

## Accounts
```sh
curl --location --request POST 'http://localhost:8550/accounts/register/' \
--form 'username="username"' \
--form 'password="password"' \
--form 'password2="password"' \
--form 'email="email"' \
--form 'first_name="first_name"' \
--form 'last_name="last_name"'
```
## Tokens
```sh
curl --location --request POST 'http://localhost:8550/accounts/api/token/' \
--form 'username="username"' \
--form 'password="password"'
```

- Token Geçerliklik suresi 1 saat / 3600 s
- Refresh Token Geçerlilik Süresi 1 gün


## Product CRUD
 
Create
  ```sh
    curl --location --request POST 'http://localhost:8550/product/' \
    --header 'Authorization: Bearer [TOKEN]' \
    --header 'Content-Type: application/json' \
    --data-raw '{
     "name":"name",
     "categoryId":"categoryId",
     "stockInformation":stockInformation[int],
     "barcodeNumber":"barcodeNumber"
    }'
  ```
- Read

```sh
    curl --location --request GET 'http://localhost:8550/product/' \
    --header 'Authorization: Bearer [TOKEN]'}'
```
- Get
```sh
    curl --location --request GET 'http://localhost:8550/product/1' \
    --header 'Authorization: Bearer [TOKEN]'}'
```
- Update
```sh
    curl --location --request PATCH 'http://localhost:8550/product/1' \
    --header 'Authorization: Bearer [TOKEN]' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    
    "name": "test",
    "categoryId": "test",
    "stockInformation": 10,
    "barcodeNumber": "test"
    
}'
```
- Delete
```sh
   curl --location --request DELETE 'http://localhost:8550/product/1' \
    --header 'Authorization: Bearer [TOKEN]' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    
    "name": "test",
    "categoryId": "test",
    "stockInformation": 10,
    "barcodeNumber": "test"
    
}'
```
# Query
| Plugin | README |
| ------ | ------ |
| name | contains |
| id | contains |
| barcodeNumber | contains |
| stockInformation | contains |
| created_at_gt | gt year |
| created_at_lt | lt year |

```sh
   curl --location --request GET 'http://localhost:8550/product/?name=test' \
    --header 'Authorization: Bearer [TOKEN]' \
    --header 'Content-Type: application/json' \
    
```

