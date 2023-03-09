from math import ceil


class PhotoAlbum():
    PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_ON_PAGE))

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {self.photos[page].index(label) + 1}"

        return "No more free slots"

    def display(self):
        result = ['-----------']
        for row in self.photos:
            result.append(("[] " * len(row)).rstrip())
            result.append('-----------')

        return "\n".join(result)

