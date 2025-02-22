CREATE OR REPLACE FUNCTION calcularGananciasPorFecha(diaInicio date, diaFinal date)
RETURNS TABLE (
    nombre_producto varchar(100),
    ventas bigint,
    gastos bigint,
    ganancias bigint
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        pr.nombre,
        sum(pd.cantidadunidadesdespachadas * pr.preciounitarioventa) as ventas,
        sum(pd.cantidadunidadesdespachadas * pr.preciounitariodecompra) as gastos,
        sum(pd.cantidadunidadesdespachadas * pr.preciounitarioventa) - sum(pd.cantidadunidadesdespachadas * pr.preciounitariodecompra) as ganancias
    FROM
        productos pr
        JOIN productosdelpedido pd ON pr.idproducto = pd.idproducto
        JOIN pedidos pe ON pd.idpedido = pe.idpedido
    WHERE
        pe.fecha_registro_ BETWEEN diaInicio AND diaFinal 
    GROUP BY
        pr.nombre
    
    UNION ALL

    SELECT
        'Total' as nombre_producto,
        sum(pd.cantidadunidadesdespachadas * pr.preciounitarioventa) as ventas,
        sum(pd.cantidadunidadesdespachadas * pr.preciounitariodecompra) as gastos,
        sum(pd.cantidadunidadesdespachadas * pr.preciounitarioventa) - sum(pd.cantidadunidadesdespachadas * pr.preciounitariodecompra) as ganancias
    FROM
        productos pr
        JOIN productosdelpedido pd ON pr.idproducto = pd.idproducto
        JOIN pedidos pe ON pd.idpedido = pe.idpedido
    WHERE
        pe.fecha_registro_ BETWEEN diaInicio AND diaFinal;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION MostrarProductosOrdenados(opcion int)
RETURNS TABLE (
    idProducto int,
    idCategoria int,
    codigoDeBarras int,
    nombre varchar(100),
    precioUnitarioDeCompra int,
    pesoEnKg int,
    unidadesEnBodega int,
	precioUnitarioVenta int,
	cantidadminstock int
) AS $$
BEGIN
    IF opcion = 1 THEN
        RETURN QUERY
        SELECT *
        FROM productos
        ORDER BY nombre;
    ELSIF opcion = 2 THEN
        RETURN QUERY
        SELECT *
        FROM productos
        ORDER BY precioUnitarioDeCompra;
    ELSIF opcion = 3 THEN
        RETURN QUERY
        SELECT *
        FROM productos
        ORDER BY unidadesEnBodega;
    ELSE
        RETURN QUERY
        SELECT *
        FROM productos
		ORDER BY precioUnitarioVenta;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION MostrarProductosDelPedidoOrdenados(opcion int)
RETURNS TABLE (
    idPedido int,
    idProducto int,
    cantidadUnidadesRequeridas int,
    cantidadUnidadesDespachadas int
) AS $$
BEGIN
    IF opcion = 1 THEN
        RETURN QUERY
        SELECT *
        FROM productosDelPedido
        ORDER BY idPedido;
    ELSIF opcion = 2 THEN
        RETURN QUERY
        SELECT *
        FROM productosDelPedido
        ORDER BY idProducto;
    ELSIF opcion = 3 THEN
        RETURN QUERY
        SELECT *
        FROM productosDelPedido
        ORDER BY cantidadUnidadesRequeridas;
    ELSIF opcion = 4 THEN
        RETURN QUERY
        SELECT *
        FROM productosDelPedido
        ORDER BY cantidadUnidadesDespachadas;
    ELSE
        RETURN QUERY
        SELECT *
        FROM productosDelPedido
		ORDER BY cantidadunidadesdespachadas;
    END IF;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION MostrarPedidosOrdenados(opcion int)
RETURNS TABLE (
    idPedido int,
    idCliente int,
	direccionDestino varchar(100),
	hora_registro time,
	personaQueRecibe varchar(30),
	apellidopersonaquerecibe varchar(30),
    fechaDeRealizacion date
) AS $$
BEGIN
    IF opcion = 1 THEN
        RETURN QUERY
        SELECT *
        FROM pedidos
        ORDER BY idPedido;
    ELSIF opcion = 2 THEN
        RETURN QUERY
        SELECT *
        FROM pedidos
        ORDER BY idCliente;
    ELSIF opcion = 3 THEN
        RETURN QUERY
        SELECT *
        FROM pedidos
        ORDER BY fechaDeRealizacion;
    ELSIF opcion = 4 THEN
        RETURN QUERY
        SELECT *
        FROM pedidos
        ORDER BY nombrepersonaquerecibe;
    ELSIF opcion = 5 THEN
        RETURN QUERY
        SELECT *
        FROM pedidos
        ORDER BY direccionDestino;
    ELSE
        RETURN QUERY
        SELECT *
        FROM pedidos;
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION MostrarClientesOrdenados(opcion int)
RETURNS TABLE (
    idCliente int,
    nombre varchar(30),
    apellido varchar(30),
    direccion varchar(100)
) AS $$
BEGIN
    IF opcion = 1 THEN
        RETURN QUERY
        SELECT *
        FROM clientes
        ORDER BY idCliente;
    ELSIF opcion = 2 THEN
        RETURN QUERY
        SELECT *
        FROM clientes
        ORDER BY nombre;
    ELSIF opcion = 3 THEN
        RETURN QUERY
        SELECT *
        FROM clientes
        ORDER BY apellido;
    ELSIF opcion = 4 THEN
        RETURN QUERY
        SELECT *
        FROM clientes
        ORDER BY direccion;
    ELSE
        RETURN QUERY
        SELECT *
        FROM clientes;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION buscarDato(tabla int, criterioBusqueda varchar)
RETURNS TABLE (
    id int,
    nombre varchar(100),
    descripcion varchar(200),
    precio int,
    cantidad int
) AS $$
BEGIN
    IF tabla = 1 THEN
        RETURN QUERY
        SELECT c.idCategoria as id, c.nombre, c.descripcion, NULL::int as precio, NULL::int as cantidad
        FROM categorias c
        WHERE c.nombre ILIKE '%' || criterioBusqueda || '%' 
           OR c.descripcion ILIKE '%' || criterioBusqueda || '%';
    ELSIF tabla = 2 THEN
        RETURN QUERY
        SELECT p.idProducto as id, p.nombre, NULL::varchar as descripcion, p.precioUnitarioDeCompra as precio, NULL::int as cantidad
        FROM productos p
        WHERE p.nombre ILIKE '%' || criterioBusqueda || '%';
    ELSIF tabla = 3 THEN
        RETURN QUERY
        SELECT c.idCliente as id, c.nombre, NULL::varchar as descripcion, NULL::int as precio, NULL::int as cantidad
        FROM clientes c
        WHERE c.nombre ILIKE '%' || criterioBusqueda || '%' 
           OR c.apellido ILIKE '%' || criterioBusqueda || '%';
    ELSIF tabla = 4 THEN
        RETURN QUERY
        SELECT pd.idPedido as id, pd.idProducto::varchar as nombre, NULL::varchar as descripcion, NULL::int as precio, pd.cantidadUnidadesDespachadas as cantidad
        FROM productosDelPedido pd
        WHERE pd.idProducto::varchar ILIKE '%' || criterioBusqueda || '%';
    ELSIF tabla = 5 THEN
        RETURN QUERY
        SELECT u.idUsuario as id, u.nombre, NULL::varchar as descripcion, NULL::int as precio, NULL::int as cantidad
        FROM usuarios u
        WHERE u.nombre ILIKE '%' || criterioBusqueda || '%';
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION insertarProducto(
    idCategoria int,
    codigoDeBarras int,
    nombre varchar,
    precioUnitarioDeCompra int,
    pesoEnKg int,
    unidadesEnBodega int,
    precioUnitarioVenta int,
	cantidadminstock int
) RETURNS void AS $$
BEGIN
    INSERT INTO productos (
        idCategoria, codigoDeBarras, nombre, precioUnitarioDeCompra,
        pesoEnKg, unidadesEnBodega, precioUnitarioVenta, cantidadminstock
    ) VALUES (
        idCategoria, codigoDeBarras, nombre, precioUnitarioDeCompra,
        pesoEnKg, unidadesEnBodega, precioUnitarioVenta, cantidadminstock
    );
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION borrarProducto(
    idProductoParam int
) RETURNS void AS $$
BEGIN
    DELETE FROM productos
    WHERE idProducto = idProductoParam;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION ActualizarUP(
    idproducto_ int,
    nuevoValor int,
    columna text
) RETURNS void AS $$
DECLARE
    valorAntiguo int;
BEGIN
    -- Obtener el valor antiguo según la columna especificada
    IF columna = 'pesoenkg' THEN
        SELECT pesoenkg INTO valorAntiguo
        FROM productos
        WHERE idproducto = idproducto_;
    ELSE
        SELECT unidadesenbodega INTO valorAntiguo
        FROM productos
        WHERE idproducto = idproducto_;
    END IF;

    -- Actualizar la columna según el valor antiguo y el nuevo valor
    IF columna = 'pesoenkg' THEN
        UPDATE productos
        SET pesoenkg = valorAntiguo + nuevoValor
        WHERE idproducto = idproducto_;
    ELSE
        UPDATE productos
        SET unidadesenbodega = valorAntiguo + nuevoValor
        WHERE idproducto = idproducto_;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION actualizar_producto(
    columna text,
    nuevo_valor text,
    id_producto int
) RETURNS void AS $$
DECLARE
    valor_anterior int;
BEGIN
    -- Convertir el nombre de la columna a minúsculas
    columna := lower(columna);

    -- Obtener el valor anterior y actualizar para las columnas pesoEnKg y unidadesEnBodega
    IF columna = 'pesoenkg' THEN
        SELECT pesoenkg INTO valor_anterior
        FROM productos
        WHERE idproducto = id_producto;
        
        UPDATE productos
        SET pesoenkg = valor_anterior + nuevo_valor::int
        WHERE idproducto = id_producto;
        
    ELSIF columna = 'unidadesenbodega' THEN
        SELECT unidadesenbodega INTO valor_anterior
        FROM productos
        WHERE idproducto = id_producto;
        
        UPDATE productos
        SET unidadesenbodega = valor_anterior + nuevo_valor::int
        WHERE idproducto = id_producto;
    
    ELSE
        -- Convertir el nuevo valor al tipo de datos correcto según la columna
        IF columna IN ('idcategoria', 'codigodebarras', 'cantidadminstock', 'unidadesenbodega') THEN
            EXECUTE format('UPDATE productos SET %I = $1::int WHERE idProducto = $2', columna)
            USING nuevo_valor, id_producto;
        ELSIF columna IN ('preciounitariodecompra', 'preciounitarioventa', 'pesoenkg') THEN
            EXECUTE format('UPDATE productos SET %I = $1::numeric WHERE idProducto = $2', columna)
            USING nuevo_valor, id_producto;
        ELSE
            EXECUTE format('UPDATE productos SET %I = $1 WHERE idProducto = $2', columna)
            USING nuevo_valor, id_producto;
        END IF;
    END IF;
END;
$$ LANGUAGE plpgsql;





CREATE OR REPLACE FUNCTION insertarPedidoConCliente(
    p_insertaCliente INT,
    p_apellidoPersonaQueRecibe VARCHAR(30),
    p_nombrePersonaQueRecibe VARCHAR(30),
    p_direccionDestino VARCHAR(100)
) RETURNS INT AS $$
DECLARE
    nuevoIdCliente INT;
    nuevoIdPedido INT;
BEGIN
    IF p_insertaCliente = 1 THEN
        -- Insertar nuevo cliente
        INSERT INTO clientes(nombre, apellido, direccion)
        VALUES (p_nombrePersonaQueRecibe, p_apellidoPersonaQueRecibe, p_direccionDestino)
        RETURNING idCliente INTO nuevoIdCliente;
    ELSE
        -- Buscar cliente existente por nombre y apellido
        SELECT idCliente INTO nuevoIdCliente
        FROM clientes
        WHERE nombre = p_nombrePersonaQueRecibe AND apellido = p_apellidoPersonaQueRecibe
        LIMIT 1;

        
        END IF;
    

    -- Insertar nuevo pedido
    INSERT INTO pedidos(
        idCliente, 
        apellidoPersonaQueRecibe, 
        nombrePersonaQueRecibe, 
        direccionDestino
    ) VALUES (
        nuevoIdCliente, 
        p_apellidoPersonaQueRecibe, 
        p_nombrePersonaQueRecibe, 
        p_direccionDestino
    )
    RETURNING idPedido INTO nuevoIdPedido;

    -- Retornar el id del nuevo pedido
    RETURN nuevoIdPedido;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION insertarProductoDelPedido(
    p_idPedido INT,
    p_idProducto INT,
    p_cantidadUnidadesRequeridas INT,
    p_cantidadUnidadesDespachadas INT
) RETURNS VOID AS $$
BEGIN
    -- Verificar si el pedido y el producto existen
    IF EXISTS (SELECT 1 FROM pedidos WHERE idPedido = p_idPedido) THEN
        IF EXISTS (SELECT 1 FROM productos WHERE idProducto = p_idProducto) THEN
            -- Insertar en productosDelPedido
            INSERT INTO productosDelPedido(
                idPedido,
                idProducto,
                cantidadUnidadesRequeridas,
                cantidadUnidadesDespachadas
            ) VALUES (
                p_idPedido,
                p_idProducto,
                p_cantidadUnidadesRequeridas,
                p_cantidadUnidadesDespachadas
            );
        ELSE
            RAISE EXCEPTION 'Producto con id % no existe', p_idProducto;
        END IF;
    ELSE
        RAISE EXCEPTION 'Pedido con id % no existe', p_idPedido;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION buscar_producto_por_nombre(nombre_producto VARCHAR)
RETURNS TABLE (
    idProducto INT,
    idCategoria INT,
    codigoDeBarras INT,
    nombre VARCHAR,
    precioUnitarioDeCompra INT,
    pesoEnKg INT,
    unidadesEnBodega INT,
    precioUnitarioVenta INT,
    CantidadMinStock INT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.idProducto,
        p.idCategoria,
        p.codigoDeBarras,
        p.nombre,
        p.precioUnitarioDeCompra,
        p.pesoEnKg,
        p.unidadesEnBodega,
        p.precioUnitarioVenta,
        p.CantidadMinStock
    FROM
        productos p
    WHERE
        p.nombre ILIKE '%' || nombre_producto || '%';
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION sacandoPedidoPDF(
    idPedidoInput int
)
RETURNS TABLE (
    idPedido int,
    idCliente int,
    nombreProducto varchar(100),
    precioPorUnidad int,
    cantidadUnidadesDespachadas int,
    montoTotalPorProducto int,
    nombrePersonaQueRecibe varchar(30),
    apellidoPersonaQueRecibe varchar(30),
    direccion varchar(100),
    horaRegistro time,
    fechaRegistro date
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        pe.idPedido,
        pe.idCliente,
        pr.nombre AS nombreProducto,
        pr.precioUnitarioVenta AS precioPorUnidad,
        pdp.cantidadUnidadesDespachadas,
        pdp.cantidadUnidadesDespachadas * pr.precioUnitarioVenta AS montoTotalPorProducto,
        pe.nombrePersonaQueRecibe,
        pe.apellidoPersonaQueRecibe,
        pe.direccionDestino,
        pe.hora_registro,
        pe.fecha_registro_
    FROM
        pedidos pe
        INNER JOIN productosDelPedido pdp ON pe.idPedido = pdp.idPedido
        INNER JOIN productos pr ON pdp.idProducto = pr.idProducto
    WHERE
        pe.idPedido = idPedidoInput;
END;
$$ LANGUAGE plpgsql;


