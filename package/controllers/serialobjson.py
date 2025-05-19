import json
import os
from typing import List, Dict, Any

class DataRecord:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.__models: List[Dict[str, Any]] = []
        self.read()

    def read(self) -> List[Dict[str, Any]]:
        try:
            if not os.path.exists(self.filepath) or os.path.getsize(self.filepath) == 0:
                self.__models = []
                self._save_file()
                return self.__models

            with open(self.filepath, 'r', encoding='utf-8') as fjson:
                self.__models = json.load(fjson)
                return self.__models

        except json.JSONDecodeError:
            print(f"[ERRO] JSON inválido em {self.filepath}. Inicializando com lista vazia.")
            self.__models = []
            self._save_file()
            return self.__models

        except Exception as e:
            print(f"[ERRO] Falha ao ler {self.filepath}: {str(e)}")
            self.__models = []
            return self.__models

    def add(self, data: Dict[str, Any]) -> bool:
        try:
            self.__models.append(data)
            return self._save_file()
        except Exception as e:
            print(f"[ERRO] Falha ao adicionar registro: {str(e)}")
            return False

    def overwrite(self, new_data: List[Dict[str, Any]]) -> bool:
        #Esse aqui vai substituir todos os dados do arquivo
        try:
            self.__models = new_data
            return self._save_file()
        except Exception as e:
            print(f"[ERRO] Falha ao sobrescrever dados: {str(e)}")
            return False

    def _save_file(self) -> bool:
        try:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            
            with open(self.filepath, 'w', encoding='utf-8') as fjson:
                json.dump(self.__models, fjson, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"[ERRO] Sem permissão para escrever em {self.filepath}")
            return False
        except Exception as e:
            print(f"[ERRO] Falha ao salvar arquivo: {str(e)}")
            return False

    def get_all(self) -> List[Dict[str, Any]]:
        return self.__models.copy()  

    def remove(self, condition: callable) -> bool:
        try:
            initial_count = len(self.__models)
            self.__models = [item for item in self.__models if not condition(item)]
            if len(self.__models) < initial_count:
                return self._save_file()
            return False  
        except Exception as e:
            print(f"[ERRO] Falha ao remover registros: {str(e)}")
            return False