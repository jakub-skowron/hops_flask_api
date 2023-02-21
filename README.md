# HOPS FLASK API

# v.1.0

## The root endpoint

`https://hopsflaskapi-production.up.railway.app`

### Pagination and something other

Data is paginated default to 20 hops per 1 page. To get data from other page you can use parameter `?page` and set chosen value.You can change pagination by use special parameter `?per_page`.

### Parameters

If you want to get all hops from the database you need to use:

`$ curl https://hopsflaskapi-production.up.railway.app/hops`

To get and filter hops you can use some url parameters which you can find below:

`$ curl https://hopsflaskapi-production.up.railway.app/hops?<parameter>=<value>`

| Parameter       | Description |
| :-----------|:-------------:|
| name     | returns hops by name
| used_for      | returns hops by purpose of use (aroma, bittering, all purpose) |
| beer_style | returns hops by use in specific beer styles |
| origin | returns hops by origin country |
***
Important!

You don't need to use complete value of parameter. For example you can use `.../hops?name=cit` instead `.../hops?name=Citra` and in your response you get all hops in the database where name value contains "cit"`.

Value of parameters are not case senstivie (for example `.../hops?name=CiTrA` = `.../hops?name=citra`).

***
You can also join parameters:

`$ curl https://hopsflaskapi-production.up.railway.app/hops?<parameter1>=<value1>&<parameter2>=<value2>&<parameter3>=<value3>`

If you want to get one type of hop you can filtering it by id and use syntax as follow:

`$ curl https://hopsflaskapi-production.up.railway.app/hops/<id>`

### Random hop

If you want to get random hop:

`$ curl https://hopsflaskapi-production.up.railway.app/hops/random`

### Rate limits

Rate limit is set to 10 requests per 1 minute.
You can check what the rate limit is and how many requests are remaining by looking at the rate limit headers sent in the response.

### Response example

- Request:

`$ curl https://hopsflaskapi-production.up.railway.app/hops/1`

- Response:

```json
{
    "alpha": "8.0-11.0%",
    "aroma": "Citrus,Floral,Tropical Fruit",
    "beta": "6.0-7.0%",
    "description": "Floral, tropical, and citrus (lemon, orange and grapefruit) characteristics",
    "id": 1,
    "name": "Amarillo®",
    "origin": "American",
    "substitutions": "Cascade, Centennial",
    "typical_beer_styles": "American Amber,American Pale Ale,India Pale Ale,Porter,Stout",
    "used_for": "Aroma"
}
```

### What I want to add in v.1.1 and later?

Priority:

- More filtering options,
- Improvement of data quality.
