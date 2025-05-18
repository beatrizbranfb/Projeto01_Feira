import json
import os

class DataRecord:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__models = []
        self.read()

    def read(self):
        if not os.path.exists(self.filepath) or os.path.getsize(self.filepath) == 0:
            print(f"[INFO] Criando arquivo vazio: {self.filepath}")
            with open(self.filepath, 'w', encoding='utf-8') as fjson:
                json.dump([], fjson)

        try:
            with open(self.filepath, 'r', encoding='utf-8') as fjson:
                self.__models = json.load(fjson)
        except json.JSONDecodeError:
            print(f"[ERRO] JSON inválido em {self.filepath}. Substituindo por lista vazia.")
            self.__models = []
            with open(self.filepath, 'w', encoding='utf-8') as fjson:
                json.dump(self.__models, fjson)

        return self.__models

    def write(self, data):
        self.__models.append(data)
        with open(self.filepath, 'w', encoding='utf-8') as fjson:
            json.dump(self.__models, fjson, indent=4)

    def overwrite(self, new_data):
        self.__models = new_data
        with open(self.filepath, 'w', encoding='utf-8') as fjson:
            json.dump(self.__models, fjson, indent=4)

