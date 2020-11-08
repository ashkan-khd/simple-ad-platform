from models.utils import BaseModel


class ForeignKey:
    __model: BaseModel = None
    __id: int = -1

    def __init__(self, id, model) -> None:
        self.__model = model
        self.__id = id

    def object(self) -> BaseModel:
        return self.__model.get_objects()[self.__id]
