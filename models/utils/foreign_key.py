from models.utils import BaseModel


class ForeignKey:
    __model: BaseModel = None
    __id: int = -1

    def __init__(self, id: int, model: BaseModel) -> None:
        self.__model = model
        self.__id = id

    def object(self) -> BaseModel:
        return self.__model.get_objects().get(self.__id, self.__model.__call__())
