import tkinter as tk

def imc():
    quilos = float(quilos_entry.get())
    altura = float(altura_entry.get())**2
    imc = quilos/altura
    imc2 = round(imc,2)
    resultado_label.config(text = f"Seu IMC é igual a = {imc2:}")

    if imc2 < 18.5:
        print('Abaixo do peso')
    elif imc2 >= 18.5 and imc2 <= 24.9:
        print('Peso normal')
    elif imc2 >= 25.0 and imc2 <= 29.9:
        print('Pré obesidade')
    elif imc2 >= 30.0 and imc2 <= 34.9:
        print('Obesidade grau 1')
    elif imc2 >= 35.0 and imc2 <= 39.9:
        print('Obesidade grau 2')
    elif imc2 > 39.9:
        print('Obesidade grau 3')
    else:
        print('ERRO')


janela = tk.Tk()
janela.title(' Calculadora de Massa Corpórea - IMC ')
janela.geometry('500x130')
janela.resizable(0,0)
janela.configure(bg = '#B0C4DE')

label_quilos = tk.Label(janela, text = 'Digite seu peso (Em KG):' ,font = ('Verdana' , '8' , 'bold'), bg ='#D3D3D3', fg='#000000')
label_quilos.pack()
quilos_entry = tk.Entry(janela)
quilos_entry.pack()

label_altura = tk.Label(janela, text = 'Digite sua altura (Em MTS):', anchor='nw' ,font = ('Verdana' , '8' , 'bold'), bg ='#D3D3D3', fg='#000000')
label_altura.pack()
altura_entry = tk.Entry(janela)
altura_entry.pack()

btn = tk.Button(janela, text = 'Calcule seu IMC' , command= imc)
btn.pack()

resultado_label = tk.Label(janela, text ='')
resultado_label.pack()

janela.mainloop()


