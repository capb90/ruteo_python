# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
Nombre: Carlos Andrés Portillo B.
"""
def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    global recorrido_min
    try:
        for llave in distancias:
            if not((distancias[llave]==0 and llave[0]==llave[1] and min(distancias.values())>=0) or (distancias[llave]!=0 and llave[0]!=llave[1] and min(distancias.values())>=0)):
                return "Por favor revisar los datos de entrada."
            else:
                continue
        ruta_tem=[]
        km=[]
        valores_min=[]
        nueva_ruta=[]
        a=0
        while a==0:
            tamaño=len(ruta_inicial)
            for i in range(1,tamaño-1):  
                for j in range(i+1,tamaño-1):  
                    lista_aux=ruta_inicial[:]
                    var_aux=lista_aux[i]
                    lista_aux[i]=lista_aux[j]
                    lista_aux[j]=var_aux
                    ruta_tem.append(lista_aux)
                    suma=0
                    for m in range(0,len(lista_aux)-1):
                        dato=lista_aux[m]
                        dato1=lista_aux[m+1]
                        clave=(dato,dato1)
                        suma+=distancias[clave]
                    km.append(suma)
                    
            recorrido_min=min(km)
            posicion=km.index(recorrido_min)
            nueva_ruta=ruta_tem[posicion]
            valores_min.append(recorrido_min)
            valor_final=len(valores_min)
            if valor_final>2 and valores_min[-1]==valores_min[valor_final-2]:
                break
            else:
                ruta_inicial=nueva_ruta
        ruta='-'.join(nueva_ruta)
        distancia=recorrido_min
        return {'ruta':ruta,'distancia':distancia} 
    
    except:
            return "Por favor revisar los datos de entrada."

        
ruta_inicial=['H', 'B', 'E', 'A', 'C', 'D', 'H']
distancias={('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'):0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

print(ruteo(distancias, ruta_inicial))
       
ruta_inicial=['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']
distancias={('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}
        
print(ruteo(distancias, ruta_inicial))        
        
ruta_inicial=['H', 'B', 'E', 'A', 'C', 'D', 'H']
distancias={('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'):0, ('A', 'B'):10, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 10}
    
print(ruteo(distancias, ruta_inicial))   


    

     
                
        