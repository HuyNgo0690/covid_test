from typing import List, Dict

from sqlalchemy import inspect


class BaseMode:
    def set_data(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def serialize(self) -> Dict:
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(list_items: List) -> List[Dict]:
        return [data.serialize() for data in list_items]
