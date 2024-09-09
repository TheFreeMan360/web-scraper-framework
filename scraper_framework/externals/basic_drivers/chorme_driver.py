from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import DEFAULT_EXECUTABLE_PATH, Service
from selenium.webdriver.chrome.webdriver import DEFAULT_KEEP_ALIVE, DEFAULT_PORT, DEFAULT_SERVICE_LOG_PATH

from scraper_framework.adapter.interface_driver import IDriver


class ChormeDriver(webdriver.Chrome, IDriver):
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

        # 更新 chorme options
        opt = {}

        # if chrome_options is not None:
        #     opt.update(chrome_options)

        super().__init__(
            executable_path,
            port,
            options,
            service_args,
            desired_capabilities,
            service_log_path,
            # chrome_options,
            opt,
            service,
            keep_alive)

    def __enter__(self) -> "ChormeDriver":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
