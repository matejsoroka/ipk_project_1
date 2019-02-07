import json
import socket

KEY = "dd8daa3e80e4dc491a5b60ca768c2461"
city = "Bardejov"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('api.openweathermap.org', 80)

client_socket.connect(server_address)

req = 'GET /data/2.5/weather?q={}&APPID={} HTTP/1.0\r\n\r\n'.format(city, KEY).encode('UTF-8')

client_socket.send(req)

response = ''
while True:
    recv = client_socket.recv(1024)
    if not recv:
        break
    response += recv.decode('UTF-8')

client_socket.close()

weather = json.loads(response.split("\r\n\r\n")[-1])

print(weather['name'])
print(weather['weather'][0]['description'])
print("temp: {0:.1f}°C".format(float(weather['main']['temp']) - 273.15))
print("humidity: {}%".format(weather['main']['humidity']))
print("pressure: {}hPa".format(weather['main']['pressure']))
print("wind-speed: {}km/h".format(weather['wind']['speed']))
print("wind-deg: {}".format(weather['wind']['deg']))
