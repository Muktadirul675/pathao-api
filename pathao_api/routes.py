from .constants import PATHAO_BASE_URL

def route(url: str, base_url: str = None):
    """
    Join base_url and url safely, removing extra slashes.
    """
    base = base_url or PATHAO_BASE_URL

    if not base:
        raise ValueError("Base URL is not set. Provide base_url or set PATHAO_BASE_URL.")

    base = base.rstrip("/")
    url = url.lstrip("/")
    url_prefix = "aladdin/api/v1"
    return f"{base}/{url_prefix}/{url}"


class PathaoRoutes:
    """
    Holds all Pathao API routes for a given base URL.
    Each instance has its own routes.
    """

    def __init__(self, base_url: str = None):
        self.base_url = base_url or PATHAO_BASE_URL
        if not self.base_url:
            raise ValueError("Base URL is not set. Provide base_url or set PATHAO_BASE_URL.")

        # Initialize routes
        self.ISSUE_TOKEN = route("issue-token", self.base_url)
        self.REFRESH_TOKEN = route("refresh-token", self.base_url)
        self.CITY_LIST = route('city-list', self.base_url)
        self.ZONE_LIST = lambda city_id : route(f'/cities/{city_id}/zone-list', self.base_url)
        self.AREA_LIST = lambda zone_id : route(f'/zones/{zone_id}/area-list', self.base_url)
        self.PRICE_PLAN = route("merchant/price-plan",self.base_url)
        self.CREATE_ORDER = route("orders",self.base_url)
        self.STORES_INFO = route('stores', self.base_url)
