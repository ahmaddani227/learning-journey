# copy dictonary

kartun = {
    'up': 'upin',
    'ip': 'ipin',
    'ad': 'adit',
    'sp': 'sopo',
    'jrw': 'jarwo',
}

cartoon = kartun.copy()

print(f"kartun: {kartun} \n")
print(f"cartoon: {cartoon} \n")

kartun['ad'] = 'dani' 
print(f"kartun: {kartun} \n")
print(f"cartoon: {cartoon} \n")


# pop dictonary (berdasarkan key)
dataUpin = cartoon.pop('up')
print(f"Data Upin = {dataUpin} \n")
print(f"Cartoon = {cartoon} \n")

# popitem dictonary (yang terakhir)
dataTerakhir = cartoon.popitem()
print(f"Data Terakhir = {dataTerakhir} \n")
print(f"Cartoon = {cartoon} \n")