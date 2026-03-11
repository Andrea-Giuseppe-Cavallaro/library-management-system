from src.models.base import SerializerMixin, db


class CatalogueModel(db.Model, SerializerMixin):
    __tablename__ = "catalogues"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default="Main Catalogue")

    books = db.relationship("BookModel", back_populates="catalogue", lazy="select")

    def update_from_dict(self, data: dict) -> None:
        self.name = data["name"]
        self.books = data["books"]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "books": self._get_ids_from_relation("books"),
        }
