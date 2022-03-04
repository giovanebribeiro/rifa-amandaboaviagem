import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

mail=st.secrets["email"]

def send(to, number, to_name):

	sender = 'noreply@boaviagemribeiro.com'
	sender_title = "Não responder"

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] =  Header("[RIFA] Obrigada por participar", 'utf-8')
	msg['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
	msg['To'] = to

	# Create the body of the message (a plain-text and an HTML version).
	text = f"Olá {to_name},\n\nMuito obrigada por contribuir com a literatura (e a cultura nacional)! O número que você reservou foi o {number}. Para concluir a reserva da rifa, você pode transferir os R$10 para o seguinte PIX, no nome de Amanda Pessoa Neves Boaviagem Ribeiro. A chave PIX é o e-mail amanda.pessoa.mrc@gmail.com.\n\nGuarde este e-mail! Ele é o seu comprovante de reserva. \n\nDATA DA RIFA: 31 de Julho de 2022. O horário será anunciado em uma live no Instagram. Siga para não percer nenhum detalhe: https://instagram.com/pagina90_"
	with open("template-email.html", 'r') as t:
		html = t.read()
		html = html.replace("#NUM#", str(number))
		html = html.replace("#NAME#", to_name)
		t.close()

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# Create server object with SSL option
	server = smtplib.SMTP_SSL(mail.host, mail.port)

	# Perform operations via server
	server.login(mail.username, mail.password)
	server.sendmail(sender, [to], msg.as_string())
	server.quit()
