from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import DEFAULT_EXECUTABLE_PATH
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import DEFAULT

from scraper_framework.adapter.xx_website.interface_xx_page_actions import IXXPageActions
from scraper_framework.externals.basic_drivers.chorme_driver import ChormeDriver


class XXPageChormeDriver(ChormeDriver, IXXPageActions):
    def __init__(self,
                 executable_path=...,
                 port=...,
                 options: Options = None,
                 service_args=None,
                 desired_capabilities=None,
                 service_log_path=...,
                 chrome_options=None,
                 service: Service = None,
                 keep_alive=...
                 ) -> None:
        super().__init__(
            executable_path,
            port,
            options,
            service_args,
            desired_capabilities,
            service_log_path,
            chrome_options,
            service,
            keep_alive)
