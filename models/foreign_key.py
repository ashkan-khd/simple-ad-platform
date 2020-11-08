from models import BaseModel


class ForeignKey:
    __model: BaseModel = None
    __id: int = -1

    def __init__(self, id, model) -> None:
        self.__model = model
        self.__id = id

    def object(self) -> BaseModel:
        for obj in self.__model.get_objects():
            if obj.get_id() == self.__id:
                return obj

