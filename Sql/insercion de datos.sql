insert into categorias(idcategoria, nombre, descripcion)values
(001, 'tuberia', 'Todo tipo de tubos sin ninguna excepcion'),
(002, 'herramientas', 'todo tipo de herramientas elaboradas'),
(003, 'materiales gramados ', 'todo tipo de materiales gramados');


insert into productos(idproducto, idcategoria, codigodebarras, nombre, preciounitariodecompra, pesoenkg, unidadesenbodega, preciounitarioventa)Values
(001, 001, null, 'tubo pvc 1/2', 20000, null, 12, 21000),
(002, 002, null, 'martillo', 10000, null, 10, 11000),
(003, 003, null, 'arena', 30000, 10000, null, 40000),
(004, 001, NULL, 'tubo PVC 3/4', 25000, NULL, 8, 27000),
(005, 002, NULL, 'destornillador', 8000, NULL, 15, 9500),
(006, 003, NULL, 'cemento', 35000, 25000, NULL, 45000);

insert into clientes(idcliente, nombre, apellido, direccion) values
(001, 'daniel', 'bocachica', 'calle 122 #23'),
(002, 'pedro', 'sanchez', 'av ferrocarril #23 A 23'),
(003, 'ermerindo', 'picua', 'calle 32 #34 V 3');

insert into pedidos(idpedido, idcliente, fechaderealizacion, personaquerecibe, direcciondestino) values
(001, 001, '11/08/2021', 'daniel bocachica', 'calle 32 #34 V 3'),
(002, 003, '11/08/2022', 'dan hica', 'calle 34 #34 V 3'),
(003, 002, '11/08/2023', 'niel chica', 'calle 35 #34 V 3');

insert into productosdelpedido(idpedido, idproducto, cantidadunidadesrequeridas, cantidadunidadesdespachadas)values

(003, 003, 1000, 300);
INSERT INTO usuarios (nombre, contraseña) VALUES
    ('admin', '12345'),
    ('user1', 'password1');
INSERT INTO productos (idCategoria, codigoDeBarras, nombre, precioUnitarioDeCompra, pesoEnKg, unidadesEnBodega, precioUnitarioVenta, CantidadMinStock)
VALUES 
    (1, 111111, 'Producto 1', 100, 1, 50, 150, 10),
    (2, 222222, 'Producto 2', 200, 2, 60, 250, 15),
    (3, 333333, 'Producto 3', 300, 3, 70, 350, 20),
    (1, 444444, 'Producto 4', 400, 4, 80, 450, 25),
    (2, 555555, 'Producto 5', 500, 5, 90, 550, 30),
    (3, 666666, 'Producto 6', 600, 6, 100, 650, 35),
    (1, 777777, 'Producto 7', 700, 7, 110, 750, 40),
    (2, 888888, 'Producto 8', 800, 8, 120, 850, 45),
    (3, 999999, 'Producto 9', 900, 9, 130, 950, 50),
    (1, 123456, 'Producto 10', 1000, 10, 140, 1050, 55),
    (2, 234567, 'Producto 11', 1100, 11, 150, 1150, 60),
    (3, 345678, 'Producto 12', 1200, 12, 160, 1250, 65),
    (1, 456789, 'Producto 13', 1300, 13, 170, 1350, 70),
    (2, 567890, 'Producto 14', 1400, 14, 180, 1450, 75),
    (3, 678901, 'Producto 15', 1500, 15, 190, 1550, 80),
    (1, 789012, 'Producto 16', 1600, 16, 200, 1650, 85),
    (2, 890123, 'Producto 17', 1700, 17, 210, 1750, 90),
    (3, 901234, 'Producto 18', 1800, 18, 220, 1850, 95),
    (1, 112233, 'Producto 19', 1900, 19, 230, 1950, 100),
    (2, 223344, 'Producto 20', 2000, 20, 240, 2050, 105),
    (3, 334455, 'Producto 21', 2100, 21, 250, 2150, 110),
    (1, 445566, 'Producto 22', 2200, 22, 260, 2250, 115),
    (2, 556677, 'Producto 23', 2300, 23, 270, 2350, 120),
    (3, 667788, 'Producto 24', 2400, 24, 280, 2450, 125),
    (1, 778899, 'Producto 25', 2500, 25, 290, 2550, 130),
    (2, 889900, 'Producto 26', 2600, 26, 300, 2650, 135),
    (3, 990011, 'Producto 27', 2700, 27, 310, 2750, 140),
    (1, 100112, 'Producto 28', 2800, 28, 320, 2850, 145),
    (2, 111223, 'Producto 29', 2900, 29, 330, 2950, 150),
    (3, 122334, 'Producto 30', 3000, 30, 340, 3050, 155);
