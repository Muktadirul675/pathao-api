![GitHub Stars](https://img.shields.io/github/stars/Muktadirul675/pathao-api?style=social)  
![PyPI Version](https://img.shields.io/pypi/v/pathao-api)  

# PathaoAPI - Unofficial Python Wrapper for Pathao Merchant API

`pathao-api` is a lightweight Python SDK that allows developers to interact with Pathao's Merchant API, providing utilities for:

✅ Authentication  
✅ City / Zone / Area lookup  
✅ Delivery charge estimation  
✅ Store information retrieval

---

## Installation

```
pip install pathao-api
```

---

Configuration

You can configure credentials via a .env file or pass them directly during initialization.

✅ Option 1: Using .env
```
PATHAO_BASE_URL=https://api.pathao.com
PATHAO_STORE_ID=12345
PATHAO_CLIENT_ID=your_client_id
PATHAO_CLIENT_SECRET=your_client_secret
PATHAO_USERNAME=merchant@you.com
PATHAO_PASSWORD=yourpassword
```
✅ Option 2: Initialize with Arguments

```
from pathao_api import PathaoAPI

client = PathaoAPI(
    base_url="https://api.pathao.com",
    store_id="12345",
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="merchant@you.com",
    password="yourpassword"
)
```

---

Usage

```
from pathao_api import PathaoAPI

client = PathaoAPI()

cities = client.get_city_list()
zones = client.get_zone_list(city_id=1)
areas = client.get_area_list(zone_id=5)
charge = client.get_delivery_charge(city_id=1, zone_id=5)
stores = client.get_stores()
```

---

Available Methods

Method	Description

```
get_city_list()	# Retrieve available cities
get_zone_list(city_id)	# Retrieve zones within a city
get_area_list(zone_id)	# Retrieve areas within a zone
get_delivery_charge(city_id, zone_id)	# Get delivery charge estimation
get_stores()	# Retrieve Pathao store information
```

---

Error Handling

Missing credentials - ValueError

Missing method parameters - Exception



---

Contributing

Contributions are welcome! Submit an issue or PR.


---

License

MIT License.


---

⭐ If you find this package helpful, consider giving a star!