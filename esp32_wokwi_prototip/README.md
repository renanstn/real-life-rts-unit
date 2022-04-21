### Problema

Fazer testes na placa ESP32 é chato pra caralho, pois a cada alteração no
código você precisa esperar compilar, fazer o upload para a placa, pressionar o
botão de BOOT, para só ai perceber que o código que você fez não funciona.

### Solução

Para agilizar, eu descobri o maravilhoso site [wokwi](https://wokwi.com/), que
permite que você simule projetos IoT no próprio browser. Funciona que é uma
maravilha e tem até simulador de conexão wifi.

O `sketch` nessa pasta é o código criado lá, com os ajustes para funcionar na
network deles.
