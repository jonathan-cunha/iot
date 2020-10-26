# Monitoramento de dispositivos IoT

Esse projeto tem como propósito a emulação de um Raspberry Pi para o monitoramento de eventos de teclado no dispositivo. 
O projeto utiliza GNS3 para emulação dos dispositivos envolvidos, Qemu para virtualização do Raspberry Pi OS e Docker container para implantação do broker de
mensagens. O broker utiliza o Eclipse Mosquitto.

A topologia da solução é dada da seguinte forma:

Raspberry -> Broker -> Receptor
