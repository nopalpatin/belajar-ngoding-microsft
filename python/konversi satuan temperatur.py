#konversi satuan temperatur

#input suhu

#input suhu celcius
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu adalah", celcius, "celcius")

#input suhu fahrenheit
fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
print("Suhu adalah", fahrenheit, "fahrenheit")

#input suhu kelvin
kelvin = float(input("Masukkan suhu dalam kelvin: "))
print("Suhu adalah", kelvin, "kelvin")

#input suhu reamur
reamur = float(input("Masukkan suhu dalam reamur: "))
print("Suhu adalah", reamur, "reamur")

#konversi suhu dari celcius

#konversi suhu celcius ke fahrenheit
fahrenheit = (celcius * 9/5) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

#konversi suhu celcius ke kelvin
kelvin = celcius + 273.15
print("Suhu dalam kelvin adalah", kelvin, "kelvin")

#konversi suhu celcius ke reamur
reamur = celcius * 4/5
print("Suhu dalam reamur adalah", reamur, "reamur")

#konversi suhu dari fahrenheit

#konversi suhu fahrenheit ke celcius
celcius = (fahrenheit - 32) * 5/9
print("Suhu dalam celcius adalah", celcius, "celcius")

#konversi suhu fahrenheit ke kelvin
kelvin = (fahrenheit + 459.67) * 5/9
print("Suhu dalam kelvin adalah", kelvin, "kelvin")

#konversi suhu fahrenheit ke reamur
reamur = (fahrenheit - 32) * 4/9
print("Suhu dalam reamur adalah", reamur, "reamur")

#konversi suhu dari kelvin

#konversi suhu kelvin ke celcius
celcius = kelvin - 273.15
print("Suhu dalam celcius adalah", celcius, "celcius")

#konversi suhu kelvin ke fahrenheit
fahrenheit = kelvin * 9/5 - 459.67
print("Suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

#konversi suhu kelvin ke reamur
reamur = (kelvin - 273.15) * 4/5
print("Suhu dalam reamur adalah", reamur, "reamur")

#konversi suhu dari reamur

#konversi suhu reamur ke celcius
celcius = reamur * 5/4
print("Suhu dalam celcius adalah", celcius, "celcius")

#konversi suhu reamur ke fahrenheit
fahrenheit = reamur * 9/4 + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

#konversi suhu reamur ke kelvin
kelvin = reamur * 5/4 + 273.15
print("Suhu dalam kelvin adalah", kelvin, "kelvin")



