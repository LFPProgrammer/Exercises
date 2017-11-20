#C = (5 * (F-32) / 9).
#FAHRENHEIT PARA CELSIUS

fahrenheit = float(input("Informe a temperatura em FAHRENNHEIT:\n"))

celsius = (5*(fahrenheit-32)/9)
print("A temperatura em CELSIUS é:", "%.2f" % celsius)
