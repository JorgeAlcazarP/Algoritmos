# Instalar pycryptodome en la terminal 
# pip install pycryptodome

# Luego importe DES3 para cifrado y md5 para clave
from Crypto.Cipher import DES3
from hashlib import md5

# Para seleccionar la operación de una opción dada
while True:
    import re
    def validar_password(password):
        if 8 <= len(password) <= 16:
            if re.search('[a-z]', password) and re.search('[A-Z]', password):
                if re.search('[0-9]', password):
                    if re.search('[!"#$%&()*+,-./:;?=@\^_`]', password):
                        return True
        return False

    print('Selecciona la operación a realizar:\n\t1- Cifrar\n\t2- Decifrar')
    operation = input('Selección: ')
    if operation not in ['1', '2']:
        break
        
    # Ruta de imagen / archivo para la operación
    file_path = input('Ruta de archivo: ')
    
    # Clave para realizar el algoritmo Triple DES
    key = input('TDES key: ')
    validar_password(key)
    if(validar_password(key))== True:
    # Codificar la clave dada a una clave ascii de 16 bytes con operación md5
        key_hash = md5(key.encode('ascii')).digest()

    # Ajuste la paridad de clave de la clave hash generada para la clave final Triple DES
        tdes_key = DES3.adjust_key_parity(key_hash)
    
    #  Cifrado con integración de clave Triple DES, MODE_EAX para confidencialidad y autenticación 
    # y nonce para generar un número aleatorio / pseudoaleatorio que se utiliza para el protocolo de autenticación
        cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    # Abrir y leer el archivo de la ruta dada
        with open(file_path, 'rb') as input_file:
            file_bytes = input_file.read()
        
            if operation == '1':
            # Realizar la operación de cifrado
                new_file_bytes = cipher.encrypt(file_bytes)
            else:
            # Realizar la operación de descifrado
                new_file_bytes = cipher.decrypt(file_bytes)
    
    # Escribir valores actualizados en el archivo de la ruta dada
        with open(file_path, 'wb') as output_file:
            output_file.write(new_file_bytes)
            print('Operación Exitosa!')
            break
    else:
         print("Tu contraseña debe integrar minúsculas, mayúsculas, números, caracteres especiales y mínimo deben ser 8 caracteres")