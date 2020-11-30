# Start of the Skeleton Code

reply = s.recv(5)
if reply == 'valid':
	print 'Username and password valid'
	ss = s.recv(4096)
	'''
	Part-2:TODO: Please printout the number of unread message once a new client login
	'''
	start_new_thread(receiveThread, (s,))
	message = ""
	while True :	
		message = raw_input("Choose an option (type the number): \n 1. Logout \n 2. Send messages \n 3. Group Configuration \n 4. Offline message \n")		
		try :
			s.sendall(message)
			if message == str(1):
				break
				
			if message == str(2):
				while True:
					message = raw_input("Choose an option (type the number): \n 1. Private messages \n 2. Broadcast messages \n 3. Group messages \n")
					try :
						'''
						Part-2:TODO: Send option to server
						'''
						if message == str(1):
							pmsg = raw_input("Enter your private message\n")
							try :
								'''
								Part-2:TODO: Send private message
								'''
							except socket.error:
								print 'Private Message Send failed'
								sys.exit()
							rcv_id = raw_input("Enter the recevier ID:\n")
							try :
								'''
								Part-2:TODO: Send private message
								'''
								break
							except socket.error:
								print 'rcv_id Send failed'
								sys.exit()
						if message == str(2):
							bmsg = raw_input("Enter your broadcast message\n")
							try :
								'''
								Part-2:TODO: Send broadcast message
								'''
								break
							except socket.error:
								print 'Broadcast Message Send failed'
								sys.exit()
						if message == str(3):
							gmsg = raw_input("Enter your group message\n")
							try :
								'''
								Part-2:TODO: Send group message
								'''
							except socket.error:
								print 'Group Message Send failed'
								sys.exit()
							g_id = raw_input("Enter the Group ID:\n")
							try :
								'''
								Part-2:TODO: Send group message
								'''
								break
							except socket.error:
								print 'g_id Send failed'
								sys.exit()
					except socket.error:
						print 'Message Send failed'
						sys.exit() 
					
			if message == str(3):
				option = raw_input("Do you want to: 1. Join Group 2. Quit Group: \n")
				if option == str(1):
					group = raw_input("Enter the Group you want to join: ")
					try :
						'''
						Part-2:TODO: Join a particular group
						'''
					except socket.error:
						print 'group info sent failed'
						sys.exit()
				elif option == str(2):
					group = raw_input("Enter the Group you want to quit: ")
					try :
						'''
						Part-2:TODO: Quit a particular group
						'''
					except socket.error:
						print 'group info sent failed'
						sys.exit()
				else:
					print 'Option not valid'
			
			if message == str(4):
				while not os.getpgrp() == os.tcgetpgrp(sys.stdout.fileno()):
					pass
				option = raw_input("Do you want to: 1. View all offline messages; 2. View only from a particular Group\n")
				if option == str(1):					
					try :
						'''
						Part-2:TODO: View all offline messages
						'''
					except socket.error:
						print 'msg Send failed'
						sys.exit()
				elif option == str(2):
					group = raw_input("Enter the group you want to view the messages from: ")
					try :
						'''
						Part-2:TODO: View only from a particular group
						'''
					except socket.error:
						print 'group Send failed'
						sys.exit()
				else:
					print 'Option not valid'
		except socket.error:
			print 'Send failed'
			sys.exit()
		
else:
	print 'Invalid username or password'

# End of the Skeleton Code

