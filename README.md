## <font size="7">**Clients DB**</font>

​### <font color="gree"> API for registering clients, using python and Flask-SQLAlchemy </font> Saves a movie

## <font size="6">Base URL /api </font>

## <font size="6">Routes</font>

​
​

### <font color="gree"> POST </font> Saves a client in the db

​

```json
/clients
```

<font color="caramel"> _Request_ </font>
​

```json
{
  "name": "Julia",
  "email": "jugf@gmail.com",
  "phone": "(12)13212-1234"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Julia",
  "email": "jugf@gmail.com",
  "phone": "(12)13212-1234",
  "creation_date": "Mon, 01 Nov 2021 23:53:13 GMT",
  "last_visit": "Mon, 01 Nov 2021 23:53:13 GMT",
  "visits": 1
}
```

​

### <font color="purple"> GET </font> Returns a list of the clients

​

```json
/clients
```

<font color="yellow"> _Response_ </font>
​

```json
{
 {
    "name": "Julia",
    "email": "jugf@gmail.com",
    "phone": "(12)13212-1234",
    "creation_date": "Mon, 01 Nov 2021 23:53:13 GMT",
    "last_visit": "Tue, 02 Nov 2021 22:14:46 GMT",
    "visits": 13
  },
  {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Mon, 27 Sep 2021 22:42:05 GMT",
    "last_visit": "Mon, 27 Sep 2021 22:42:36 GMT",
    "visits": 2
  }
}
```

​

### <font color="orange"> PATCH </font> Updates a specific client information

​

```json
/clients
```

​
<font color="caramel"> Request </font>
​

```json
{
  "email": "ju98@gmail.com"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "name": "Julia",
  "email": "jugf@gmail.com",
  "phone": "(12)13212-1234",
  "creation_date": "Mon, 01 Nov 2021 23:53:13 GMT",
  "last_visit": "Tue, 02 Nov 2021 23:08:07 GMT",
  "visits": 15
}
```

### <font color="red"> DELETE </font> Delete a specific client

​

```json
/clients
```

​
<font color="caramel"> Request </font>
​

```json
{
  "email": "ju98@gmail.com"
}
```

<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```

​
