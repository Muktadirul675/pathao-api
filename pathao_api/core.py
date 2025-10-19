from . import constants, routes, controllers

class PathaoAPI:
    REQUIRED_CONSTANTS = [
        "PATHAO_BASE_URL",
        "PATHAO_STORE_ID",
        "PATHAO_CLIENT_ID",
        "PATHAO_CLIENT_SECRET",
        "PATHAO_USERNAME",
        "PATHAO_PASSWORD",
    ]

    def __init__(self, 
                 base_url=None,
                 store_id=None,
                 client_id=None,
                 client_secret=None,
                 username=None,
                 password=None):
        """
        Initialize PathaoAPI with optional overrides.
        Overrides module-level constants if provided.
        Raises ValueError if any required value is missing.
        """

        if base_url is not None:
            constants.PATHAO_BASE_URL = base_url
        if store_id is not None:
            constants.PATHAO_STORE_ID = store_id
        if client_id is not None:
            constants.PATHAO_CLIENT_ID = client_id
        if client_secret is not None:
            constants.PATHAO_CLIENT_SECRET = client_secret
        if username is not None:
            constants.PATHAO_USERNAME = username
        if password is not None:
            constants.PATHAO_PASSWORD = password

        for var_name in self.REQUIRED_CONSTANTS:
            if getattr(constants, var_name) in (None, ""):
                raise ValueError(f"{var_name} is not set. Provide it via .env or as a constructor argument.")

        self.base_url = constants.PATHAO_BASE_URL
        self.store_id = constants.PATHAO_STORE_ID
        self.client_id = constants.PATHAO_CLIENT_ID
        self.client_secret = constants.PATHAO_CLIENT_SECRET
        self.username = constants.PATHAO_USERNAME
        self.password = constants.PATHAO_PASSWORD
        self.refresh_token = None
        self.access_token = None
        self.routes : routes.PathaoRoutes = routes.PathaoRoutes(self.base_url)
        data = controllers.issue_access_token(self.routes.ISSUE_TOKEN, args={
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "password",
            "username": self.username,
            "password": self.password
        })
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']

    def get_city_list(self):
        res = controllers.get_city_list(self.routes.CITY_LIST, token=self.access_token)
        return res
    
    def get_zone_list(self, city_id=None):
        if not city_id:
            raise Exception("Must provide a city id")
        res = controllers.get_zone_list(self.routes.ZONE_LIST(city_id),token=self.access_token)
        return res
    
    def get_area_list(self, zone_id=None):
        if not zone_id:
            raise Exception("Must provide a zone id")
        res = controllers.get_area_list(self.routes.AREA_LIST(zone_id),token=self.access_token)
        return res

    def get_delivery_charge(self,city_id, zone_id, item_type:int=2,delivery_type:int=48, item_weight:float=0.5):
        if not zone_id or not city_id:
            raise Exception("Both zone id and city id is required")
        res = controllers.get_price_plan(self.routes.PRICE_PLAN,payload={
            "store_id" : self.store_id,
            "item_type": item_type,
            "delivery_type" : delivery_type,
            "item_weight" : f"{item_weight}",
            "recipient_city": city_id,
            "recipient_zone": zone_id
        },token=self.access_token)
        return res

    def get_stores(self):
        res = controllers.get_stores_info(self.routes.STORES_INFO, token=self.access_token)
        return res
    
    def create_order(self, order_id:str,recipient_name:str,recipient_phone:str,recipient_address:str, item_quantity:int, amount_to_collect:int, delivery_type:int=48, item_type:int=2, special_instruction:str="",item_weight:float=0.5,item_description:str=''):
        payload = {
            "store_id": self.store_id,
            "merchant_order_id": order_id,
            "recipient_name": recipient_name,
            "recipient_phone": recipient_phone,
            "recipient_address": recipient_address,
            "delivery_type": delivery_type,
            "item_type": item_type,
            "special_instruction": special_instruction,
            "item_quantity": item_quantity,
            "item_weight": f"{item_weight}",
            "item_description": item_description,
            "amount_to_collect": amount_to_collect
        }
        res = controllers.create_order(self.routes.CREATE_ORDER, token=self.access_token, payload=payload)
        return res
