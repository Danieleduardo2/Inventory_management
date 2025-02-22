CREATE TABLE categorias(
idCategoria serial primary key,
nombre varchar(50) not null,
descripcion varchar(200)
);

CREATE TABLE productos(
idProducto serial primary key,
idCategoria int not null,
codigoDeBarras int,
nombre varchar(100) not null,
precioUnitarioDeCompra int not null, 
pesoEnKg int,
unidadesEnBodega int,
precioUnitarioVenta int not null,
CantidadMinStock int,
foreign key(idCategoria) references categorias(idCategoria)
);


CREATE TABLE clientes (
idCliente int primary key,
nombre varchar(30) not null,
apellido varchar(30) not null,
direccion varchar(100)
);           

CREATE TABLE pedidos(
idPedido serial primary key,
idCliente int,
fecha_registro_ Date DEFAULT CURRENT_DATE,
hora_registro TIME DEFAULT CURRENT_TIME,
apellidoPersonaQueRecibe varchar(30),
nombrePersonaQueRecibe varchar(30),
direccionDestino varchar(100), 	
foreign key (idCliente) references clientes(idCliente)
);

CREATE TABLE productosDelPedido(
idPedido int,
idProducto int,
cantidadUnidadesRequeridas int,
cantidadUnidadesDespachadas int not null,
primary key(idProducto, idPedido),
foreign key(idProducto) references productos(idProducto),
foreign key(idPedido) references pedidos(idPedido)
);

Create table usuarios(
idUsuario serial primary key,
nombre varchar(50),
contraseña varchar(30)
)
