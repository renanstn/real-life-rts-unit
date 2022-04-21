# real-life-rts-unit

## TODO

- [x] Setup mosquitto (MQTT server)
- [ ] Programar ESP32 para receber instruções e executá-las
- [ ] Programar app para receber e tratar a imagem da webcam
- [ ] Programar app para identificar o robô
- [ ] Programar app para disparar comandos para o robô via MQTT

## Desenvolvimento

### Mosquitto

Resolver problema da falta de permissão para ler o arquivo de log:

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

## Referências

- Porque MQTT?: https://medium.com/mqtt-buddy/mqtt-vs-http-which-one-is-the-best-for-iot-c868169b3105
