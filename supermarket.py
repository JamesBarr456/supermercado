"""
Un supermercado maneja el catálogo de los productos que vende. De cada producto se conoce su nombre,
 precio, y si el mismo es parte del programa Precios Cuidados o no. Por defecto, el producto no es parte 
 del programa, a menos que se especifique lo contrario.

Para ayudar a los clientes, el supermercado quiere realizar descuentos en productos de Primera Necesidad.
 Es por eso que al calcular el precio de un producto de Primera Necesidad, se aplica un descuento del 10%.
  Es decir:


precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9
El supermercado, del cual se conoce el nombre y la dirección, desea conocer la cantidad total de productos
 que comercializa y la suma total de los precios de los mismos."""
class supermarket():
    def __init__(self):
        self.name = "Los chinos de la San Martin"
        self.direccion = "San Martin 455"

class producto:
     def __init__(self,name,price,precioCuidado = False):
         self.name = name
         self.price = price
         self.descuento = precioCuidado
     
     def valorDePrecio(self):
         if self.descuento:
             self.price = self.price * 0.9
             return self.price
        
class catalogo():
     def __init__(self) -> None:
        self.productos = []
    
     def agregar_Producto(self,nombre,precioBase,pCuidados):
         p = producto(name=nombre, price=precioBase, precioCuidado=pCuidados)
         p.valorDePrecio()
         self.productos.append(p)
         print("Producto agregado al catalogo exitosamente")
     
     def mostrarCatalogo(self):
         for x in self.productos:
             print(f"Nombre:\t{x.name}")
             print(f"Precio:\t{x.price}$")
        
     def cantidadProductos(self):  
        valor = 0
        for i in self.productos:
            valor += 1
        print(f"En el supermercado tenemos un valor de {valor} cant/ de productos")

     def sumaPrecios(self):
        valor=0
        for x in self.productos:
            valor = valor + x.price
        print(f"El valor total de todos los productos disponible es:\t{valor}")

print(f"Bienvenido al programa de '{supermarket().name}'")
print(f"Nos encontramos en {supermarket().direccion}")
print("----------------------------------------------")  
x = catalogo()
print("----------------------------------------------")
x.agregar_Producto("Cocacola", 90,False)
x.agregar_Producto("Manteca", 100,True)
x.agregar_Producto("leche",80,True)
x.agregar_Producto("Pan",60,False)
print("----------------------------------------------")
x.mostrarCatalogo()
print("----------------------------------------------")
x.cantidadProductos()
x.sumaPrecios()