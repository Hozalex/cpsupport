from abc import ABC, abstractmethod


class ApiService(ABC):

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def get(self):
        pass
