# T1 Redes de Computadores
Comunicação UDP em Python.

1. As máquinas utilizadas devem estar em uma mesma rede local e com Python3 instalado.
2. Deve-se baixar um arquivo em cada máquina, por exemplo client.py na máquina 1 e server.py na máquina 2.
3. Abra o terminal em ambas as máquinas e configure seus IPs.
4. 1. Na máquina que tiver o arquivo server.py baixado, deve-se digitar no terminal: python3 server.py (ip da máquina) (porta na qual o servidor está funcionando)
      Exemplo: $ python3 server.py 192.168.1.6 8080
4. 2. Na máquina que tiver o arquivo client.py baixado, deve-se digitar no terminal: python3 client.py (ip da máquina com server.py baixado) (porta na qual o servidor está funcionando)
      Exemplo: $ python3 client.py 192.168.1.6 8080
