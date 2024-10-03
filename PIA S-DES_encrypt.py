print("--------------S-DES---------------ENCRYPTION-------------S-DES---------------\n")
#Integrantes del equipo:                         Matrícula:
#Alejandra Cantú González                        1908866
#Victor Torres Cavazos                           1922988
#Daniel Gilberto Escobar Castañeda               1921830

with open(r"C:\Users\danie\OneDrive\Escritorio\5to semestre\CRIPTOGRAFÍA\PIA\victor.png", "rb") as image:
  f = image.read()
  b = bytearray(f)

#DE BYTES A BINARIO
encoded_b2 = "".join([format(n, '08b') for n in b])

#SEPARAMOS DE 8 EN 8
n = 8
binario = [encoded_b2[i:i+n] for i in range(0, len(encoded_b2), n)]

encdec = []
ki = []



while True:
    k = input("Ingrese una llave de 10 BITS: ")
    ki = []
    if len(k) == 10:
        for i in k:
            if i == '0':
                ki.append(i)
            elif i == '1':
                ki.append(i)
        if len(ki) != 10:
            print("Solo puedes ingresar 0 y 1")
        elif len(ki) == 10:
            break
    else:
        print("la llave debe tener un tamaño de 10 bits")
        print(k)
        continue


for i in binario:
    #print(i, 'esta es ', l)
    #Texto a cifrar
    m = i
    

    #Validamos que la llave sea de 10 bits y que sean 1's y 0's
    #Permutamos en P10 con 3 5 2 7 4 10 1 9 8 6
    def permut_3(m):
        p = [m[2], m[4], m[1], m[6], m[3], m[9], m[0], m[8], m[7], m[5]]
        return p


    P10k = permut_3(ki)
    

    # Dividimos P10 en LS1 y LS2
    LS1 = P10k[:5]
    LS2 = P10k[5:]


   

    # Permutando para mover 1 posicion a la izquierda
    def permut_4(m):
        p = [m[1], m[2], m[3], m[4], m[0]]
        return p


    LS1izq = permut_4(LS1)
    LS2izq = permut_4(LS2)


    

    # Tomamos 8 posiciones de los 10 bits de la llave principal
    def permut(m):
        p = [m[6], m[4], m[2], m[0], m[1], m[3], m[5], m[7]]
        return p


    
    LR = LS1izq + LS2izq
    sk1 = permut(LR)


 

    # Permutando para mover 2 posiciones a la izquierda
    def permut_5(m):
        p = [m[2], m[3], m[4], m[0], m[1]]
        return p


    LS1izq2 = permut_5(LS1)
    LS2izq2 = permut_5(LS2)
   

    LR2 = LS1izq2 + LS2izq2
    sk2 = permut(LR2)
    

    # 1  2  3  4  5  6  7  8
    # 1.Permutacion inicial con [0, 0, 1, 1, 1, 0, 1, 0]
    
    ip = permut(m)


   

    # 2. Entramos a nuestra funcion fk1
    # COMENZAMOS CON LA RONDA #1
    # Dividimos la la permutacion inicial en L y R

    def division(p):
        L = [p[0], p[1], p[2], p[3]]
        R = [p[4], p[5], p[6], p[7]]
        return L, R


    division(ip)
    L, R = division(ip)
    

    # Definimos la expansion del lado derecho 'R'
    ER = [R[3], R[2], R[1], R[0], R[3], R[2], R[1], R[0]]
    

    # Hacemos la suma xor con ER + sk1
    msk1 = []
    for i in range(8):
        if ER[i] == sk1[i]:
            msk1.append('0')
        elif ER[i] != sk1[i]:
            msk1.append('1')
    

    # Dividimos la suma xor de ER + sk1 en L1 y R1
    division(msk1)
    L1, R1 = division(msk1)


    

    # Definimos las s boxes
    def sboxe0(pos):
        dic = {'0000': '01', '0001': '00', '0010': '11', '0011': '10', '0100': '11', '0101': '10', '0110': '01',
               '0111': '00',
               '1000': '00', '1001': '10', '1010': '01', '1011': '11', '1100': '00', '1101': '01', '1110': '11',
               '1111': '10'}
        lado1 = pos[0] + pos[3]
        lado2 = pos[1] + pos[2]
        lado3 = lado1 + lado2
        for key in dic:
            if lado3 == key:
                res = dic[key]
        return res


    def sboxe1(pos):
        dic = {'0000': '00', '0001': '01', '0010': '10', '0011': '11', '0100': '10', '0101': '00', '0110': '01',
               '0111': '11',
               '1000': '11', '1001': '00', '1010': '01', '1011': '10', '1100': '10', '1101': '01', '1110': '00',
               '1111': '11'}
        lado1 = pos[0] + pos[3]
        lado2 = pos[1] + pos[2]
        lado3 = lado1 + lado2
        for key in dic:
            if lado3 == key:
                res = dic[key]
        return res


    s0L1 = sboxe0(L1)
    s1R1 = sboxe1(R1)

    

    # Unimos ambos resultados de las s-boxes para tener z
    z = s0L1 + s1R1
    

    # Nueva permutacion: 2 4 3 1
    ZP = [z[1], z[3], z[2], z[0]]
    

    # Hacemos la suma xor con L + ZP(que ZP fue la nueva permutacion)
    ZL = []
    for i in range(4):
        if str(L[i]) == ZP[i]:
            ZL.append('0')
        elif str(L[i]) != ZP[i]:
            ZL.append('1')
   

    # Unimos ZL(la suma xor) con R para obtener m prima
    m1 = ZL + R



    # Definimos la funcion para hacer el switch
    def permut_2(m):
        p = [m[4], m[5], m[6], m[7], m[0], m[1], m[2], m[3]]
        return p


    # Hacemos el switch de m prima o m1
    swm1 = permut_2(m1)
    

    # Dividimos el switch de m1 en parte izquierda(L2) y derecha(R2)
    L2, R2 = division(swm1)
   

    # Hacemos la expansion de R2
    ER2 = [R2[3], R2[2], R2[1], R2[0], R2[3], R2[2], R2[1], R2[0]]
    
    # Hacemos la suma xor para ER2 + sk2(nuestra segunda llave)

    msk2 = []
    for i in range(8):
        if ER2[i] == sk2[i]:
            msk2.append('0')
        elif ER2[i] != sk2[i]:
            msk2.append('1')
   

    # Dividimos la suma xor de ER2 + sk2
    division(msk2)
    Lmsk2, Rmsk2 = division(msk2)
    

    # Usamos las s boxes

    s0Lmsk2 = sboxe0(Lmsk2)
    s1Rmsk2 = sboxe1(Rmsk2)

    # Unimos los resultados de las s boxes
    z1 = s0Lmsk2 + s1Rmsk2

    

    # Nueva permutacion: 2 4 3 1
    ZP2 = [z1[1], z1[3], z1[2], z1[0]]
    

    # Hacemos la suma xor de ZP2 + L2
    ZL2 = []
    for i in range(4):
        if str(L2[i]) == ZP2[i]:
            ZL2.append('0')
        elif str(L2[i]) != ZP2[i]:
            ZL2.append('1')
    

    # Unimos la suma xor ZL2 y la R2
    m2 = ZL2 + R2
    
    # 1  2  3  4  5  6  7  8
    # Hacemos la permutacion inicial inversa para  [0, 0, 1, 0, 1, 0, 0, 1]
    ipi = [m2[3], m2[4], m2[2], m2[5], m2[1], m2[6], m2[0], m2[7]]
    
    encdec.append(ipi)


#de binario a byte
lst_binario = []
for i in encdec:
    for x in range(0,8):
        var = int(i[x])
        lst_binario.append(var)
for i in lst_binario:
    b_str = ''.join(str(e) for e in lst_binario)

n = 8
txt_sep = [b_str[i:i+n] for i in range(0, len(b_str), n)]

bytes = []
for i in txt_sep:
    bytes.append(int(i, 2))
print(bytes)
arr = bytearray(bytes)
#de byte a imagen

with open("encrypt.png", "wb") as f:
   f.write(arr)
   f.close()
   print("Imagen encriptada creada y guardada")
