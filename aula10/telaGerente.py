import tkinter as tk
from conta import Conta
import json

def login():
    if input_titular.get() == "admin":
        if input_agência.get() == "1234":
            if input_CPF.get() == "5678":
                label_resposta.configure(text="Login realizado com sucesso!", fg="green")
        else:
            label_resposta.configure(text="Falha no login", fg="red")
    else:
        label_resposta.configure(text="Falha no login", fg="red")

def cadastrar():
    conta = conta(input_titular.get(), input_agência.get(), input_CPF.get)
    print(conta,extrato())
    print(conta.numero)

    with open ("clientes.json", "r") as clientes_arq:
        clientes = json.load(clientes_arq)
    
    clientes.append({
        "titular": conta.titular,
        "agencia": conta.agencia,
        "numero": conta.numero,
        "cpf": conta.cpf,
        "saldo": conta.saldo,
        "senha": conta.senha,
        "chavepix": conta.chavepix.senha
    })

    with open ("clientes.json", "w") as clientes_escrita:
        json.dump(clientes, clientes_escrita, indent=4)

    label_resposta.configure(text=f"conta: {conta.numero} titular: {conta.titular} cadastrado com sucesso", fg="green")

app = tk.Tk()
app.title("Tela GERENTE")
app.geometry("400x300")

# titular
label_titular = tk.Label(app, text="titular:")
label_titular.pack(pady=5)
input_titular = tk.Entry(app)
input_titular.pack()

# agência
label_agência = tk.Label(app, text="agência:")
label_agência.pack(pady=5)
input_agência = tk.Entry(app)
input_agência.pack()

# CPF
label_CPF = tk.Label(app, text="CPF:")
label_CPF.pack(pady=5)
input_CPF = tk.Entry(app)
input_CPF.pack()

# ENVIAR
botao = tk.Button(app, text="Enviar", command=cadastrar)
botao.pack(pady=10)

# RESPOSTA
label_resposta = tk.Label(app, text="")
label_resposta.pack(pady=5)

app.mainloop() # -> executar a tela em laço infinito