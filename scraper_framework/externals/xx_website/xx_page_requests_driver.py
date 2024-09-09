from scraper_framework.externals.basic_drivers.requests_driver import RequestsDriver
from scraper_framework.adapter.xx_website.interface_xx_page_actions import IXXPageActions


class XXPageRequestsDriver(RequestsDriver, IXXPageActions):
    def __init__(self) -> None:
        super().__init__()
