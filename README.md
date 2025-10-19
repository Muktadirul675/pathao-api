![GitHub Stars](https://img.shields.io/github/stars/Muktadirul675/pathao-api?style=social)  
![PyPI Version](https://img.shields.io/pypi/v/pathao-api)  

# PathaoAPI - Unofficial Python Wrapper for Pathao Merchant API

`pathao-api` is a lightweight Python SDK that allows developers to interact with Pathao's Merchant API, providing utilities for:

✅ Authentication  
✅ City / Zone / Area lookup  
✅ Delivery charge estimation  
✅ Store information retrieval
✅ Create Order

## Installation

```
pip install pathao-api
```

## Configuration

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


## Usage

```
from pathao_api import PathaoAPI

client = PathaoAPI()
```

Then you can call the methods using the `client` with necessery parameters.
### Available Methods
```
cities = client.get_city_list()
zones = client.get_zone_list(city_id:int)
areas = client.get_area_list(zone_id:int)
charge = client.get_delivery_charge(city_id:int, zone_id:int)
stores = client.get_stores()
order = client.create_order(order_id: str, recipient_name: str, recipient_phone: str, recipient_address: str, item_quantity: int, amount_to_collect: int, delivery_type: int = 48, item_type: int = 2, special_instruction: str = "", item_weight: float = 0.5, item_description: str = '')
```
**The return values are same as pathao's official docs**

## Contributing

Contributions are welcome! Submit an issue or PR.

---

## License

MIT License.

⭐ If you find this package helpful, consider giving a star!