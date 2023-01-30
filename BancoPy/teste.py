from BancoPy.models.cliente import Cliente
from BancoPy.models.conta import Conta


victor: Cliente = Cliente('Victor G. Hermogenes', 'victorltrgh@gmail.com', '177.679.807-40', '01/07/1997')

# print(victor)

contaf: Conta = Conta(victor)

# print(contaf)

