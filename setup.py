# Get the value of environment variables from the user

token_value = input('Enter the value of the application token: ')
chat_id_value = input('Enter chat id value: ')

file_env = open('.env', 'w', encoding='utf-8')
file_env.write('TOKEN={}\n'.format(token_value))
file_env.write('CHAT_ID={}\n'.format(chat_id_value))
file_env.close()

print('Setup script completed successfully')