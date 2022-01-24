import streamlit as st
import pandas as pd
import os
import pymongo

# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])

st.title('Rifa literária entre amigos')

st.markdown(
    "Olá! Obrigada por querer ajudar a tornar este sonho realidade. Comprando essa rifa você estará ajudando a transformar meus livros em audiobooks, "
    "fazendo com que suas mensagens de esperança e amor cheguem a mais pessoas. O prêmio será os livros de 1 a 5 de Anne de Green Gables, da [Editora Pedra Azul]() "
    ". Afinal de contas, quem passa uma mensagem positiva, apesar das adversidades, é Anne. Que o(a) ganhador(a) possa aprender boas lições com essa ruivinha como eu aprendi."
    "A você, desejo uma BOAVIAGEM na leitura, e a todos boa sorte!")
 
def read_picked_numbers():
    db = client.test
    items = db.my_collection.find()
    items = list(items)  # make hashable for st.cache
    return [item['PICKED_NUMBER'] for item in items]

def write_new_number(name, email, num):
    db = client.test
    db.my_collection.insert_one({"NAME": name, "EMAIL": email, "PICKED_NUMBER": num, "PAYED": False})

def remaining_numbers():
    TOTAL_NUMBERS = 2000
    return list(
        set(range(1, TOTAL_NUMBERS + 1)) -
        set(read_picked_numbers()))

def nums_you_picked(your_email):
    db = client.test
    items = db.my_collection.find()
    items = list(items)  # make hashable for st.cache
    nums = [
        item['PICKED_NUMBER'] for item in items
        if item['EMAIL'].lower() == your_email.lower()]
    return nums
    

name = st.text_input(
    "São só 3 passos! Primeiro, por favor digite seu nome, para "
    "que possamos te identificar:")

if len(name) > 0:
    email = st.text_input("Agora, preciso do seu melhor e-mail:")

    if len(email) > 0:
        vocativo = f"Perfeito, {name}!"
        you_picked = nums_you_picked(name)
        if len(you_picked) > 0:
            st.subheader(
                "{} Você **já pegou** os números: **{}**. Se quiser "
                "pegar ainda outros, prossiga "
                "adiante.".format(
                    vocativo,
                    str(you_picked).replace("[", "").replace("]", "")
                    )
                )
        else:
            st.subheader(
                "{} Pronto, agora qual número você gostaria "
                "de pegar para a Rifa?".format(vocativo))

        option = st.selectbox(
            f"Selecione um número dentre os {len(remaining_numbers())} "
            "que não foram selecionados ainda.",
            tuple(["Nenhum"] + remaining_numbers()))
        st.write('Valor selecionado:', option)

        if option != "Nenhum":
            if st.button('Confirmar'):
                write_new_number(name, email, int(option))
                st.markdown(
                    f"**Muito obrigada por contrubuir com a literatura (e a cultura nacional), {name}!"
                    "Para concluir a reserva da rifa, você pode **transferir os R$10 para "
                    "o seguinte PIX**, no nome de **Amanda Pessoa Neves Boaviagem Ribeiro**:")

                st.subheader("amanda.pessoa.mrc@gmail.com")

                st.markdown(
                    "Para escolher um novo valor, por favor "
                    "**recarregue** a página.")
            else:
                st.markdown(
                    "**Calma! Você pode voltar e escolher outro número, se "
                    "quiser. Sua escolha só vai se efetivar após clicar "
                    "em *Confirmar*.**")
