# NAMA : Abizar Algifari Arham
# NIM  : 25241092

# Latihan Aritmatika, Aplikasi Konversi Suhu
# Buatlah program konversi suhu dengan output sebagai berikut:

# Suhu anda adalah
# Suhu anda dalam fahrenheit
# Suhu anda dalam reamur
# Suhu anda dalam kelvin

Celcius = float(input(" Masukkan suhu anda dalam celcius : "))

fahrenheit = (Celcius * 9/5) + 32
reamur = Celcius * 4/5
kelvin = Celcius + 273.15

print("____ HASILNYA ADALAH ____")
print("Suhu anda adalah : ", Celcius, "°C")
print("Suhu anda dalam Fahrenheit : ", fahrenheit, "°F")
print("Suhu anda dalam Reamur : ", reamur, "°R")
print("Suhu anda dalam Kelvin : ", kelvin, "°K")
