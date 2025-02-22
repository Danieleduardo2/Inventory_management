select *
from productosdelpedido;
--Mostrar Lista
SELECT * FROM MostrarProductosOrdenados(4);
SELECT * FROM MostrarProductosDelPedidoOrdenados(5);
SELECT * FROM MostrarPedidosOrdenados(4);
SELECT * FROM MostrarClientesOrdenados(4);
--Calcular ganancias_______________________________________________________________

SELECT * FROM calcularGananciasPorFecha('01/01/2000', '31/12/2024');
-----------------------------------------------------------------------
SELECT * FROM buscarDato(2,'a');

--Productos
SELECT insertarProducto(
    2,            -- idCategoria
    null,   -- codigoDeBarras
    'perno elastico', -- nombre
    100000,         -- precioUnitarioDeCompra
    null,            -- pesoEnKg
    50,           -- unidadesEnBodega
    1500,          -- precioUnitarioVenta
	10
);
SELECT borrarProducto(11);
SELECT actualizar_producto('cantidadminstock', '10', 12);

--Hacer pedido
select * from buscar_producto_por_nombre('p');
SELECT insertarPedidoConCliente(
    0, -- Indica que se debe insertar un nuevo cliente
    'pedo', -- Apellido de la persona que recibe
    'Mae', -- Nombre de la persona que recibe
    'Av. nunca Viva 456' -- Dirección de destino
);

SELECT insertarProductoDelPedido(
    1, -- idPedido
    13, -- idProducto
    49, -- cantidadUnidadesRequeridas
    49 -- cantidadUnidadesDespachadas
);
select * from sacandoPedidoPDF(3);


--alter table pedidos
--drop column fecha_registro 

--Alter table productos
--add column CantidadMinStock int;

--ALTER TABLE pedidos
--ADD COLUMN fecha_registro_ Date DEFAULT CURRENT_DATE;

SELECT tgname AS trigger_name,
       tgrelid::regclass AS table_name,
       tgtype AS trigger_type,
       tgdeferrable AS deferrable,
       tginitdeferred AS init_deferred,
       proname AS function_name
FROM pg_trigger
JOIN pg_proc ON pg_trigger.tgfoid = pg_proc.oid
ORDER BY table_name, trigger_name;

