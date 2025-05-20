from package.controllers.serialobjson import DataRecord
from package.models.produtos.estoque import Estoque
from time import sleep
import webbrowser
from time import sleep

class TelaAdm:
    def __init__(self, estoque: Estoque):
        self.clientes = DataRecord("package/controllers/db/database_clientes.json")
        self.produtos = DataRecord("package/controllers/db/database_produtos.json") 
        self.estoque = estoque

    def menu(self):
        while True:
            print("\n========MENU DO ADMINISTRADOR========")
            print("1. Mostrar clientes")
            print("2. Acessar estoque")
            print("3. Confirmar entrega para um cliente")
            print("4. Sair")

            escolha = input("Escolha: ")

            if escolha == "1":
                self.mostrar_clientes_html()
            elif escolha == "2":
                self.estoque.menu()
            elif escolha == "3":
                self.confirmar_entrega()
            elif escolha == "4":
                print("Saindo da área do administrador...")
                sleep(1)
                break
            else:
                print("Opção inválida.")
    
    def confirmar_entrega(self):
        print("\n=== CONFIRMAR ENTREGA ===")
        nome = input("Nome do cliente que deseja confirmar entrega: ").strip().title()
        clientes = self.clientes.read()
        for i, cliente in enumerate(clientes):
            if cliente['nome'] == nome:
                print(f"Entrega confirmada para {nome}!")
                del clientes[i]
                self.clientes.overwrite(clientes) 
                return
        print("Cliente não encontrado.")

    def mostrar_clientes_html(self):
            from package.controllers.serialobjson import DataRecord

            db_clientes = DataRecord("package/controllers/db/database_clientes.json")
            clientes = db_clientes.read()

            html_content = """
            <html>
            <head>
                <title>Clientes Cadastrados</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        padding: 20px;
                    }
                    h1 {
                        color: #333;
                        text-align: center;
                    }
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        background-color: white;
                        padding: 20px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                        border-radius: 10px;
                    }
                    th, td {
                        padding: 10px;
                        text-align: left;
                        border: 1px solid #ddd;
                    }
                    th {
                        background-color: #D98695;
                        color: white;
                    }
                    tr:nth-child(even) {
                        background-color: #e4b6bf;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Clientes Cadastrados</h1>
                    <table>
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Nome</th>
                                <th>Contato</th>
                                <th>Endereço</th>
                            </tr>
                        </thead>
                        <tbody>
            """

            if clientes:
                for idx, cliente in enumerate(clientes, start=1):
                    html_content += f"""
                    <tr>
                        <td>{idx}</td>
                        <td>{cliente.get('nome', '')}</td>
                        <td>{cliente.get('contato', '')}</td>
                        <td>{cliente.get('residencia', '')}</td>
                    </tr>
                    """
            else:
                html_content += "<tr><td colspan='4'>Nenhum cliente cadastrado.</td></tr>"

            html_content += """
                        </tbody>
                    </table>
                </div>
            </body>
            </html>
            """

            file_path = "clientes.html"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            print("Arquivo HTML gerado com sucesso: clientes.html")
            webbrowser.open(file_path)
