from model.Editora import Editora

class EditoraDAO:

    def __init__(self):
        self.__editoras: list[Editora] = []

    def listar(self) -> list[Editora]:
        return self.__editoras

    def adicionar(self, editora: Editora) -> None:
        self.__editoras.append(editora)

    def remover(self, editora_id: str) -> bool:
        encontrado = False
        for e in self.__editoras:
            if (e.id == editora_id):
                index = self.__editoras.index(e)
                self.__editoras.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, editoras_id) -> Editora:
        edi = None
        for e in self.__editoras:
            if (e.id == editoras_id):
                edi = e
                break
        return edi
   
    def ultimo_id(self) -> int:
        index = len(self.__editoras) -1
        if (index == -1):
            id = 0
        else:
            id = self.__editoras[index].id
        return id