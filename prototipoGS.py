import tkinter as tk
from tkinter import messagebox

class CadastroSintomasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Selecione os seus sintomas")    # É o titulo da janela

        self.sintomas_selecionados = [] # Cria uma lista vazia para armazenar os sintomas selecionados

        button_width = 15 # Definine uma largura fixa para os botões, que pode ser chamada.

        # Estes são os botões de cada sintoma
        self.button_febre = tk.Button(root, text="Febre", width=button_width, command=self.toggle_febre) # O command=self.toggle_febre define que quando o botão for clicado, a função toggle_febre irá ser chamada
        self.button_dor_cabeca = tk.Button(root, text="Dor de Cabeça", width=button_width, command=self.toggle_dor_cabeca)
        self.button_dor_corpo = tk.Button(root, text="Dor no Corpo", width=button_width, command=self.toggle_dor_corpo)
        self.button_vomito = tk.Button(root, text="Vômito", width=button_width, command=self.toggle_vomito)
        self.button_tosse = tk.Button(root, text="Tosse", width=button_width, command=self.toggle_tosse)
        self.button_falta_ar = tk.Button(root, text="Falta de Ar", width=button_width, command=self.toggle_falta_ar)
        self.button_fadiga = tk.Button(root, text="Fadiga", width=button_width, command=self.toggle_fadiga)
        self.button_perda_olfato = tk.Button(root, text="Perda de Olfato", width=button_width, command=self.toggle_perda_olfato)
        self.button_perda_paladar = tk.Button(root, text="Perda de Paladar", width=button_width, command=self.toggle_perda_paladar)
        self.button_congestao_nasal = tk.Button(root, text="Congestão Nasal", width=button_width, command=self.toggle_congestao_nasal)
        self.button_dor_abdominal = tk.Button(root, text="Dor Abdominal", width=button_width, command=self.toggle_dor_abdominal)
        self.button_dor_ouvido = tk.Button(root, text="Dor de Ouvido", width=button_width, command=self.toggle_dor_ouvido)

        # Define o botão para enviar os sintomas
        self.button_enviar = tk.Button(root, text="Enviar", width=button_width, command=self.enviar_sintomas)

        # Define o botão para resetar todos os sintomas
        self.button_resetar = tk.Button(root, text="Resetar Sintomas", width=button_width, command=self.resetar_sintomas)

        # Define o botão para excluir o último sintoma adicionado
        self.button_excluir_ultimo = tk.Button(root, text="Excluir Último", width=button_width, command=self.excluir_ultimo_sintoma)

        # É o nome da seção que vai mostrar os sintomas selecionados antes de serem enviados
        self.label_sintomas_selecionados = tk.Label(root, text="Sintomas Selecionados:")

        # Define o widget (area branca) de saída para exibir a lista de sintomas
        self.text_lista_sintomas = tk.Text(root, height=10, width=40)

        # Configuração do layout usando grid
        self.button_febre.grid(row=0, column=0, padx=5, pady=5)
        self.button_dor_cabeca.grid(row=0, column=1, padx=5, pady=5)
        self.button_dor_corpo.grid(row=0, column=2, padx=5, pady=5)
        self.button_vomito.grid(row=0, column=3, padx=5, pady=5)
        self.button_tosse.grid(row=1, column=0, padx=5, pady=5)
        self.button_falta_ar.grid(row=1, column=1, padx=5, pady=5)
        self.button_fadiga.grid(row=1, column=2, padx=5, pady=5)
        self.button_perda_olfato.grid(row=2, column=0, padx=5, pady=5)
        self.button_perda_paladar.grid(row=2, column=1, padx=5, pady=5)
        self.button_congestao_nasal.grid(row=2, column=2, padx=5, pady=5)
        self.button_dor_abdominal.grid(row=2, column=3, padx=5, pady=5)
        self.button_dor_ouvido.grid(row=1, column=3, padx=5, pady=5)
        self.button_enviar.grid(row=4, column=0, columnspan=4, pady=10)
        self.button_resetar.grid(row=5, column=1, padx=5, pady=5)
        self.button_excluir_ultimo.grid(row=5, column=2, padx=5, pady=5)
        self.label_sintomas_selecionados.grid(row=6, column=0, columnspan=4)
        self.text_lista_sintomas.grid(row=7, column=0, columnspan=4)

    def toggle_febre(self):           # Define a função que foi chamada lá encima no botão
        self.toggle_sintoma("Febre")  # Essa função vai chamar outra função, que é a toggle_sintoma

    def toggle_dor_cabeca(self):
        self.toggle_sintoma("Dor de Cabeça")

    def toggle_dor_corpo(self):
        self.toggle_sintoma("Dor no Corpo")

    def toggle_vomito(self):
        self.toggle_sintoma("Vômito")

    def toggle_tosse(self):
        self.toggle_sintoma("Tosse")

    def toggle_falta_ar(self):
        self.toggle_sintoma("Falta de Ar")

    def toggle_fadiga(self):
        self.toggle_sintoma("Fadiga")

    def toggle_perda_olfato(self):
        self.toggle_sintoma("Perda de Olfato")

    def toggle_perda_paladar(self):
        self.toggle_sintoma("Perda de Paladar")

    def toggle_congestao_nasal(self):
        self.toggle_sintoma("Congestão Nasal")

    def toggle_dor_abdominal(self):
        self.toggle_sintoma("Dor Abdominal")

    def toggle_dor_ouvido(self):
        self.toggle_sintoma("Dor de Ouvido")

    def toggle_sintoma(self, sintoma):                  # Define a função toggle_sintoma 
        if sintoma in self.sintomas_selecionados:       # Se o sintoma estiver na lista de sintomas selecionados ele tira dela. Essa parte permite clicar mais de uma vez no botão para adicionar ou retirar
            self.sintomas_selecionados.remove(sintoma)  # Seria outra forma de retirar o sintoma caso tenha clicado errado nele, além do botão de tirar o ultimo sintoma adicionado
        else:                                           # Se o sintoma nao estiver na lista de sintomas selecionados, ele coloca nela
            self.sintomas_selecionados.append(sintoma)

        # Essa parte pega a lista recem atualizada com os sintomas escolhidos e mostra eles no widget label_sintomas_selecionados, que é responsavel por mostrar a lista antes de ser enviada
        self.label_sintomas_selecionados.config(text=f"Sintomas Selecionados: {', '.join(self.sintomas_selecionados)}")  # O .join transforma a lista em uma string, separados por virgulas, para mostrar no widget todos os sintomas em uma só linha

    def enviar_sintomas(self):                                                                         # Define a função enviar_sintomas, chamada pelo botão enviar, definido mais acima
        if not self.sintomas_selecionados:                                                             # Checa se a lista self_sintomas_selecionados está vazia (lista vazia em python é false em termos booleanos, entao esse if é true se a lista estiver vazia)
            messagebox.showwarning("Aviso", "Selecione pelo menos um sintoma para enviar ao médico.")  # Se estiver vazia, manda essa mensagem para o usuario.
            return                                                                                     # Encerra todo o processo iniciado pelo aperto do botao, para evitar que o código continue rodando
        
        self.text_lista_sintomas.config(state=tk.NORMAL)                                               # Muda o estado do text_lista_sintomas para normal. Só assim é possivel fazer alterações nesse widget
        self.text_lista_sintomas.delete(1.0, tk.END)                                                   # Essa parte deleta os sintomas escritos no widget. 1.0 representa linha 1 coluna 0, ele ele começa a deletar a partir disso
        self.text_lista_sintomas.insert(tk.END, "Encaminharemos para o médico:\n")                     # Essa parte insere a frase "Sintomas Selecionados:" no widget. O \n faz a quebra da linha, para que os sintomas apareçam embaixo da frase
        for sintoma in self.sintomas_selecionados:                                                     # Esse loop percorre a lista de sintomas selecionados, adicionando cada um deles ao widget. 
            self.text_lista_sintomas.insert(tk.END, f"{sintoma}\n")                                    # O \n faz a quebra de linha para que os sintomas apareçam um embaixo do outro
        self.text_lista_sintomas.config(state=tk.DISABLED)                                             # Muda o estado do text_lista_sintomas para disabled. Isso impede qualquer alteração no widget depois de clicar em enviar

    def resetar_sintomas(self):                                                 # Define a função resetar_sintomas, que é chamada pelo botão Resetar sintomas                                     
        self.sintomas_selecionados = []                                         # Ela redefine a lista self.sintomas_selecionados para uma lista vazia
        self.label_sintomas_selecionados.config(text="Sintomas Selecionados: ") # Atualiza o rótulo label_sintomas_selecionados, para que ele nao mostre nada tambem, deixando todo o widget limpo e coerente.

    def excluir_ultimo_sintoma(self):                                                                                        # Define a função excluir_ultimo_sintoma, que é chamada pelo botão excluir
        if self.sintomas_selecionados:                                                                                       # Checa se a lista está vazia, caso nao esteja ele executa o que estiver dentro do if
            self.sintomas_selecionados.pop()                                                                                 # o .pop() remove o ultimo elemento da lista self.sintomas_selecionados
            self.label_sintomas_selecionados.config(text=f"Sintomas Selecionados: {', '.join(self.sintomas_selecionados)}")  # Também tem a função de atualizar o rótulo label_sintomas_selecionados, para que ele mostre a lista atualizada

if __name__ == "__main__":          # Essa parte verifica se o script está sendo executado diretamente, já que nesse caso "__name__" vai ser definido como "__main__". Isso nao acontece quando o script é importado de outro script.
    root = tk.Tk()                  # Satisfazendo o primeiro if, essa parte cria uma janela do módulo tkinter. Essa janela é a interface grafica principal desse modulo
    app = CadastroSintomasApp(root) # Cria a instancia do CadastroSintomasApp definida no começo do código com o argumento root, que é o argumento definido acima, iniciando o aplicativo no formato tkinter
    root.mainloop()                 # Inicia o loop da interface do tkinter, que ficará rodando em segundo plano enquanto o script está sendo executado, respondendo aos eventos do usuario, até que a janela seja fechada. Ele tambem evita que o programa seja executado mais de uma vez
 
