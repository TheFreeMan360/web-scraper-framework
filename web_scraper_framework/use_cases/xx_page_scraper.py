from scraper_framework.use_cases.scraper import Scraper

from scraper_framework.adapter.interface_driver import IDriver
from scraper_framework.adapter.xx_website.interface_xx_page_parsing_functions import IXXPageParsingFunctions
from scraper_framework.adapter.interface_writer import IWriter

from scraper_framework.externals.xx_website.xx_page_chorme_driver import XXPageChormeDriver
from scraper_framework.externals.xx_website.xx_page_parser import XXPageParser


class XXPageScraper(Scraper):
    def __init__(self) -> None:
        super().__init__()
        self.__driver: IDriver = XXPageChormeDriver
        self.__parser: IXXPageParsingFunctions = XXPageParser

    def scrape(self, id: str) -> None:
        url = "{id}"

        self.__driver.get(url=url)
        text: str = self.__driver.xxx()
        data: dict = self.__parser.parse(text)
        self.write_to_csv(data)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__driver.close()

    # def parse(self):
    #     play_load = {"user-agent": generate_user_agent()}
    #     url = ""
    #     res = requests.get(url, headers=play_load)

    # def to_dataframe(self):
    #     return pd.DataFrame(self.__data)

    # def write_to_csv(self, data: dict):
    #     csv_writer: Writer = CSVWriter()
    #     return csv_writer.write(data)

    # def to_excel(self):
    #     pd.DataFrame(self.__data).to_excel()

    # def save_redis(self): pass

    # def save_mysql(self): pass
