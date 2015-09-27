# On My Way

A web and mobile application that algorithmically generates a tourism route from a given city and interests.

## Development

### Environment

```shell
$ pyvenv venv/
$ source venv/bin/activate
```

```shell
$ deactivate
```

### Dependencies

```shell
$ pip install -r requirements.txt
```

### WSGI

```shell
$ gunicorn wsgi:api
```

## Deployment

### API Keys

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
