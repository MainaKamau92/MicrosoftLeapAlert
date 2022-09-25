from typing import List, Tuple

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class ScrapLeap:

    def __init__(self) -> None:
        self.URL = "https://www.microsoft.com/en-us/leap/events/"
        self.event_tag = "section"
        self.event_class = "msleap-events-list"
        self.header_tag = "msleap-event__title"

    def _fetch_header_title(self, event_tag: Tag) -> str:
        return event_tag.find("h3", class_=self.header_tag).text

    @staticmethod
    def _fetch_entry_terms(event_tag: Tag) -> List[str]:
        terms_tag = event_tag.find("ul", class_="entry-terms")
        return [entry.text for entry in terms_tag.find_all("li")]

    def prepare_soup(self) -> BeautifulSoup:
        page = requests.get(self.URL)
        return BeautifulSoup(page.content, "html.parser")

    def _get_events(self) -> List[Tag]:
        soup = self.prepare_soup()
        events = soup.find_all(self.event_tag, class_=self.event_class)
        return events

    def parse_events(self) -> List[Tuple[str, List[str]]]:
        event_details = []
        events = self._get_events()
        for event in events:
            event_details.append(('title', self._fetch_header_title(event)))
            event_details.append(('terms', self._fetch_entry_terms(event)))
        return event_details


scrap_leap_instance = ScrapLeap()
