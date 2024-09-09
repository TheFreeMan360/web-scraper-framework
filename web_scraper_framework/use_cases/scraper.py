import abc


class Scraper(object):

    @abc.abstractmethod
    def scrape(self, url: str) -> None: pass

    def __enter__(self) -> "Scraper":
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: pass
