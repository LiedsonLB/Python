from tkinter import *

class CaixaEletronico:
    def __init__(self):
        self.conta = 1000
        self.machinesaque = 1000
        self.saques = 0
        self.notas_disponiveis = {100: 10, 50: 10, 20: 10, 10: 10, 5: 10, 2: 10}

        self.app = Tk()
        self.app.title("Caixa Eletrônico")
        self.app.geometry("600x400")
        self.app.configure(background="#f2f2f2")

        self.current_frame = None
        self.show_service_frame()

    def saque(self, quantidade):
        if quantidade > self.conta:
            return "Saldo insuficiente"
        if quantidade > self.machinesaque:
            return "Limite de saque da máquina atingido"
        
        self.conta -= quantidade
        self.machinesaque -= quantidade
        self.saques += 1

        result = f"Saque realizado com sucesso!\nSeu saldo restante é de R${self.conta}"
        notas_retiradas = {}

        for nota in sorted(self.notas_disponiveis.keys(), reverse=True):
            while quantidade >= nota and self.notas_disponiveis[nota] > 0:
                quantidade -= nota
                self.notas_disponiveis[nota] -= 1
                if nota in notas_retiradas:
                    notas_retiradas[nota] += 1
                else:
                    notas_retiradas[nota] = 1

        if notas_retiradas:
            result += "\nNotas retiradas:"
            for nota, quantidade in notas_retiradas.items():
                result += f"\n{quantidade} nota(s) de R${nota}"

        return result

    def show_saque_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.app, bg="#f2f2f2")
        self.current_frame.pack(fill="both", expand=True)

        label_instruction = Label(self.current_frame, text="Informe o valor a ser sacado:", background="#f2f2f2", font=("Helvetica", 12))
        label_instruction.place(x=150, y=100, width=300, height=30)

        quantidade_entry = Entry(self.current_frame, font=("Helvetica", 12))
        quantidade_entry.place(x=200, y=140, width=200, height=30)

        button_confirm = Button(self.current_frame, background="#161616", foreground="white", text="Confirmar", font=("Helvetica", 12), command=lambda: self.realizar_saque(quantidade_entry.get()))
        button_confirm.place(x=250, y=180, width=100, height=30)

        button_voltar = Button(self.current_frame, background="#161616", foreground="white", text="Voltar", font=("Helvetica", 12), command=self.show_service_frame)
        button_voltar.place(x=10, y=10, width=80, height=30)

    def realizar_saque(self, quantidade):
        quantidade = int(quantidade)
        if quantidade > 0:
            if quantidade <= self.conta and quantidade <= self.machinesaque:
                resultado = self.saque(quantidade)
                self.show_result_frame(resultado)
            else:
                resultado = "Valor de saque inválido"
                self.show_result_frame(resultado)

    def show_service_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.app, bg="#f2f2f2")
        self.current_frame.pack(fill="both", expand=True)

        label_welcome = Label(self.current_frame, text="Bem-vindo ao Caixa Eletrônico", background="#f2f2f2", foreground="darkblue", font=("Helvetica", 16))
        label_welcome.place(x=100, y=50, width=400, height=30)

        label_instruction = Label(self.current_frame, text="Digite o nome de usuário:", background="#f2f2f2", font=("Helvetica", 12))
        label_instruction.place(x=200, y=100, width=200, height=30)

        user = Entry(self.current_frame, font=("Helvetica", 12))
        user.place(x=200, y=140, width=200, height=30)

        button_confirm = Button(self.current_frame, background="#161616", foreground="white", text="Confirmar", font=("Helvetica", 12), command=self.show_saque_frame)
        button_confirm.place(x=250, y=180, width=100, height=30)

        result_label = Label(self.current_frame, background="#f2f2f2", foreground="darkblue", font=("Helvetica", 12))
        result_label.place(x=100, y=250, width=400, height=60)

    def show_result_frame(self, result):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = Frame(self.app, bg="#f2f2f2")
        self.current_frame.pack(fill="both", expand=True)

        result_label = Label(self.current_frame, text=result, background="#f2f2f2", foreground="darkblue", font=("Helvetica", 12))
        result_label.place(x=100, y=150, width=400, height=100)

        button_voltar = Button(self.current_frame, background="#161616", foreground="white", text="Voltar", font=("Helvetica", 12), command=self.show_service_frame)
        button_voltar.place(x=10, y=10, width=80, height=30)

    def run(self):
        self.app.mainloop()

caixa = CaixaEletronico()
caixa.run()
