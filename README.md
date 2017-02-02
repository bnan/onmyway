# On My Way

![onmyway](http://i.imgur.com/FPowMwU.png)

Developed at Porto Summer of Code 2015, a 48h hackathon set in Porto, On My Way is a web and mobile application that algorithmically generates a tourism route for a given city and interests.

## Technologies

### Server

- Python
- Falcon
- SQLite
- Foursquare's APIs
- Google Maps' APIs

### Client

- HTML, CSS, JavaScript
- Material Design Lite
- Google Maps' JavaScript API
- PhoneGap

## Development

### Dependencies

```
$ pip install -r requirements.txt
```

### Run

```
$ gunicorn wsgi:api
```

## Deployment

Obtain API keys for Foursquare and Google Maps and store them in:

- `config/foursquare.json`

  ```json
  {
      "client_id": "VSO0H2M52WG0BFUJJNR0VN23IXMDE2KH0D21L0PCJ03DOHPP",
      "client_secret": "W1PQXRGKFIAJCZ0DCOSA2EBGB0G1CZ3GTQKHF3SF3VWWUDZJ"
  }
  ```

- `config/googlemaps.json`

  ```json
  {
      "key": "AIzaSyBfyM6agboTt7jx_z-zZe0FVaFBTkCreXo"
  }
  ```
