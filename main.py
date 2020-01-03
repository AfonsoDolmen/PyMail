from email.parser import Parser
import imaplib, smtplib, email
import os, time

main = '''
  (((((.........................(((((   
  ((((((((....................(((((((  
  ((((((((((.................((((((((  
  ((((.((((((((..........((((((((((((  
  ((((....((((((((.....((((((((.(((((  
  ((((......(((((((((((((((.....(((((  
  ((((........(((((((((((.......(((((  
  ((((...........(((((..........(((((  
  ((((..........................(((((  
  ((((..........................(((((  
  ((((..........................(((((  
  ((((..........................(((((
'''

def enviarEmail(smtp, user, servidor_email_SMTP, servidor_email_IMAP):
	os.system('cls')
	para = input('\nPara: ')
	msg = input('\nMenssagem: ')

	try:
		print('\nEnviando email...')
		smtp.sendmail(user, para, msg)
		time.sleep(2)
		print('\nEmail enviado com sucesso.')
		time.sleep(1)
		escolherAcao(servidor_email_SMTP, servidor_email_IMAP)
	except:
		print('\nFalha ao enviar o email.')
		time.sleep(2)
		os.system('cls')
		escolherAcao(servidor_email_SMTP, servidor_email_IMAP)

def conectarServidorSMTP_TSL(servidor_email_SMTP, servidor_email_IMAP):
	os.system('cls')
	smtp = smtplib.SMTP(servidor_email_SMTP)
	smtp.starttls()

	try:
		user = str(input("Digite seu e-mail: "))
		passwd = str(input("Digite a senha do seu e-mail: "))
		smtp.login(user, passwd)
		print('\nConectando ao seu email...')
		time.sleep(2)
		enviarEmail(smtp, user, servidor_email_SMTP, servidor_email_IMAP)
	except:
		print('Falha no login, tente novamente!')
		time.sleep(2)
		os.system('cls')
		escolherAcao(servidor_email_IMAP, servidor_email_SMTP)

def conectarServidorSMTP(servidor_email_SMTP, servidor_email_IMAP):
	os.system('cls')
	smtp = smtplib.SMTP_SSL(servidor_email_SMTP)

	try:
		user = str(input("Digite seu e-mail: "))
		passwd = str(input("Digite a senha do seu e-mail: "))
		smtp.login(user, passwd)
		print('\nConectando ao seu email...')
		time.sleep(2)
		enviarEmail(smtp, user, servidor_email_SMTP, servidor_email_IMAP)
	except:
		print('Falha no login, tente novamente!')
		os.system('cls')
		escolherAcao(servidor_email_IMAP, servidor_email_SMTP)

def abrirInbox(imap, servidor_email_IMAP, servidor_email_SMTP):
	imap.select('inbox')
	typ, data = imap.search(None, 'ALL')

	os.system('cls')

	for msg in data[0].split():
		typ, data = imap.fetch(msg, '(RFC822)')
		
		menssagem = email.message_from_bytes(data[0][1])

		de = menssagem['From']
		para = menssagem['To']
		assunto = menssagem['Subject']
		data = menssagem['Date']

		print('Data: ' + data)
		print('De: ' + de)
		try:
			print('Para: ' + para)
		except:
			print("Para: ouve um erro.")
		print('Assunto: ' + assunto)
		print('+----------------------------------------------------+')
		continue
	escolherAcao(servidor_email_IMAP, servidor_email_SMTP)

def conectarServidorIMAP(servidor_email_IMAP, servidor_email_SMTP):
	imap = imaplib.IMAP4_SSL(servidor_email_IMAP)

	try:
		os.system("cls")
		user = str(input("Digite o seu e-mail: "))
		passwd = str(input("Digite a senha do seu e-mail: "))
		imap.login(user, passwd)
		print('\nConectando usuario e senha.\n')
	except:
		print('\nUsuario ou senha incorretos!')
		exit()

	abrirInbox(imap, servidor_email_IMAP, servidor_email_SMTP)

def escolherAcao(servidor_email_IMAP, servidor_email_SMTP):
	print('\n1 - Verificar caixa de entrada.')
	print('')
	print('2 - Enviar email.')
	print('')
	escolha = str(input('Escolha sua acao: '))
	if escolha == '1':
		conectarServidorIMAP(servidor_email_IMAP, servidor_email_SMTP)
	elif escolha == '2':
		if servidor_email_SMTP == "smtp.office365.com":
			conectarServidorSMTP_TSL(servidor_email_SMTP, servidor_email_IMAP)
		else:
			conectarServidorSMTP(servidor_email_IMAP, servidor_email_SMTP)

def inicio(servidor_email_IMAP, servidor_email_SMTP):
	os.system('cls')
	print('\n')
	print(main)

	print('PyMail!\n')
	print('Programa escrito por Afonso!\n')
	escolherAcao(servidor_email_SMTP, servidor_email_IMAP)

def escolherEmail():
	servidor_email_IMAP = ""
	servidor_email_SMTP = ""

	print('\nEscolha seu email desejado: ')
	print('\n1- Gmail')
	print("")
	print('2- Outlook')
	print("")
	escolher_servidor = str(input('Escolha o servidor de email que deseja conectar: '))
	if escolher_servidor == "1":
		servidor_email_IMAP = "imap.gmail.com"
		servidor_email_SMTP = "smtp.gmail.com"
		inicio(servidor_email_SMTP, servidor_email_IMAP)

	elif escolher_servidor == "2":
		servidor_email_IMAP = "imap-mail.outlook.com"
		servidor_email_SMTP = "smtp.office365.com"
		inicio(servidor_email_SMTP, servidor_email_IMAP)
	else:
		print('\nPor favor, escolha as opcoes acima.')
		time.sleep(1)
		os.system('cls')
		escolherEmail()

escolherEmail()
