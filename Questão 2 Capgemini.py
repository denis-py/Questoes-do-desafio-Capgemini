contl = 0
contu = 0
conts = 0

alphabetlower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
             , 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabetupper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

password = input(f'Digite a sua senha abaxixo: \n'
      f'Critérios para uma senha forte: \n'
      f'A senha deverá possuir no mínimo 6 caracteres\n'
      f'Contém no mínimo 1 digito\n'
      f'Contém no mínimo 1 letra em maiúsculo\n'
      f'Contém no mínimo 1 letra em minúsculo\n'
      f'Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+\n'
      f'Digite a sua senha aqui: ')

for j in range(0, len(password)):
    for i in range(0, len(alphabetlower)):
        if password[j] == alphabetlower[i]:
            contl = contl + 1


for j in range(0, len(password)):
    for i in range(0, len(alphabetupper)):
        if password[j] == alphabetupper[i]:
            contu = contu + 1

for j in range(0, len(password)):
    for i in range(0, len(special)):
        if password[j] == special[i]:
            conts = conts + 1


print('Sua senha contém {0} caracteres'.format(len(password)))
0,

if contl == 0:
    print('Sua senha necessita de pelo menos um caractere minúsculo')
if contu == 0:
    print('Sua senha necessita de pelo menos um caractere maiúsculo')
if conts == 0:
    print('Sua senha necessita de pelo menos um caratcere especial')
if len(password) < 6:
    print('Suá senha devará haver pelo menos 6 caracteres')
if len(password) == 0:
    print('Suá senha devará conter pelo menos 1 dígito')

