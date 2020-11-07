class BaseModel:
    _id: int = -1

    def __init__(self, objects: list) -> None:
        self._id = (objects[-1]._id + 1 if len(objects) != 0 else 1)
