# Gestisce i dati dei libri nel database.


from typing import List


class Book:

    def __init__(
        self,
        id: int,
        title: str,
        authors: List[str],
        language: List[str],
        first_publish_year: int,
        ebook_access: str,
    ):
        self.id = id
        self.title = title
        self.authors = authors
        self.language = language
        self.first_publish_year = first_publish_year
        self.ebook_access = ebook_access

    def is_available(self) -> bool:
        return self.ebook_access != "no_ebook"

    def __str__(self) -> str:
        authors = ", ".join(self.authors)
        languages = ", ".join(self.language)
        return f"{self.title} ({self.first_publish_year}) - {authors} [{languages}]"
