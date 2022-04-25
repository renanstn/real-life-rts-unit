# real-life-rts-unit

## TODO

- [x] Setup mosquitto (MQTT server)
- [ ] Programar ESP32 para receber instruções e executá-las
- [ ] Programar app para receber e tratar a imagem da webcam
- [ ] Programar app para identificar o robô e sua direção
  - [ ] Usando a imagem de um objeto semicircular e [este](https://stackoverflow.com/questions/59363937/opencv-detecting-an-object-and-its-rotation) método?
  - [ ] Usando 2 ou 3 imagens para identificação e deduzir o ângulo entre elas?
- [x] Programar app para disparar comandos para o robô via MQTT

## Desenvolvimento

### Mosquitto

Se deixar que o mosquitto crie o arquivo de `log` dentro do Docker, vai ficar dando erro de permissão toda hora ao tentar visualizá-lo. Para evitar isso:

```sh
cd log
sudo touch mosquitto.log
sudo chmod o+w mosquitto.log
sudo chown 1883:1883 mosquitto.log
```

Testando `pub`:

```
docker-compose run --rm mqtt sh
mosquitto_pub -h 192.168.15.8 -p 1883 -t "test" -m 1
```

testando `sub`

```
docker-compose run --rm mqtt sh
mosquitto_sub -h 192.168.15.8 -p 1883 -t "test"
```

### Python app

Formatar código com `black`:

```
docker-compose run --rm app black .
```

## Referências

- Porque MQTT?: https://medium.com/mqtt-buddy/mqtt-vs-http-which-one-is-the-best-for-iot-c868169b3105
