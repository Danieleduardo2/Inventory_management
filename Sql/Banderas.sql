CREATE OR REPLACE FUNCTION modificarCantidadInventario()
RETURNS TRIGGER AS $$
DECLARE
unidadesenbodega_aux int;
BEGIN
    select unidadesenbodega into unidadesenbodega_aux
	from productos
	where idproducto = NEW.idproducto;
	
	
    IF unidadesenbodega_aux IS NOT NULL THEN
        UPDATE productos
        SET unidadesenbodega = unidadesenbodega - new.cantidadunidadesdespachadas 
        WHERE idproducto = NEW.idproducto;
    ELSE
        UPDATE productos
        SET pesoenkg = pesoenkg - new.cantidadunidadesdespachadas
        WHERE  idproducto = NEW.idproducto;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER modificarCantidadInventario_
AFTER INSERT ON productosdelpedido
FOR EACH ROW
EXECUTE FUNCTION modificarCantidadInventario();


CREATE OR REPLACE FUNCTION actualizar_productos_escaseados() 
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT unidadesEnBodega FROM productos WHERE idProducto = NEW.idProducto) IS NOT NULL THEN
        IF (SELECT unidadesEnBodega FROM productos WHERE idProducto = NEW.idProducto) < 
           (SELECT CantidadMinStock FROM productos WHERE idProducto = NEW.idProducto) THEN
            INSERT INTO productosEscaseados(idProducto, nombre, CantidadEnStock)
            VALUES (
                NEW.idProducto, 
                (SELECT nombre FROM productos WHERE idProducto = NEW.idProducto), 
                (SELECT unidadesEnBodega FROM productos WHERE idProducto = NEW.idProducto)
            )
            ON CONFLICT (idProducto) DO UPDATE 
            SET CantidadEnStock = EXCLUDED.CantidadEnStock;
        END IF;
    ELSE
        IF (SELECT pesoEnKg FROM productos WHERE idProducto = NEW.idProducto) < 
           (SELECT CantidadMinStock FROM productos WHERE idProducto = NEW.idProducto) THEN
            INSERT INTO productosEscaseados(idProducto, nombre, CantidadEnStock)
            VALUES (
                NEW.idProducto, 
                (SELECT nombre FROM productos WHERE idProducto = NEW.idProducto), 
                (SELECT pesoEnKg FROM productos WHERE idProducto = NEW.idProducto)
            )
            ON CONFLICT (idProducto) DO UPDATE 
            SET CantidadEnStock = EXCLUDED.CantidadEnStock;
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
--no esta implementado
CREATE TRIGGER trigger_actualizar_productos_escaseados
AFTER INSERT ON productosDelPedido
FOR EACH ROW
EXECUTE FUNCTION actualizar_productos_escaseados();

CREATE OR REPLACE FUNCTION modificarCantidadInventarioUpdate()
RETURNS TRIGGER AS $$
DECLARE
    unidadesenbodega_aux int;
BEGIN
    -- Obtener unidades en bodega del producto relacionado
    SELECT unidadesenbodega INTO unidadesenbodega_aux
    FROM productos
    WHERE idproducto = NEW.idproducto;

    -- Verificar si unidadesenbodega_aux no es nulo
    IF unidadesenbodega_aux IS NOT NULL THEN
        -- Actualizar unidades en bodega restando cantidadunidadesdespachadas.new
        UPDATE productos
        SET unidadesenbodega = unidadesenbodega - (NEW.cantidadunidadesdespachadas-old.cantidadunidadesdespachadas)
        WHERE idproducto = NEW.idproducto;
    ELSE
        -- En caso de que unidadesenbodega_aux sea nulo, actualizar pesoenkg
        UPDATE productos
        SET pesoenkg = pesoenkg - (NEW.cantidadunidadesdespachadas-old.cantidadunidadesdespachadas)
        WHERE idproducto = NEW.idproducto;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER modificarCantidadInventarioUpdate_
AFTER UPDATE ON productosdelpedido
FOR EACH ROW
EXECUTE FUNCTION modificarCantidadInventarioUpdate();


CREATE OR REPLACE FUNCTION actualizar_cantidades()
RETURNS TRIGGER AS $$
BEGIN
    -- Buscar si ya existe una fila con el mismo idPedido e idProducto
    IF EXISTS (
        SELECT 1
        FROM productosDelPedido
        WHERE idPedido = NEW.idPedido
          AND idProducto = NEW.idProducto
    ) THEN
        -- Actualizar las cantidades requeridas y despachadas
        UPDATE productosDelPedido
        SET cantidadUnidadesRequeridas = cantidadUnidadesRequeridas + NEW.cantidadUnidadesRequeridas,
            cantidadUnidadesDespachadas = cantidadUnidadesDespachadas + NEW.cantidadUnidadesDespachadas
        WHERE idPedido = NEW.idPedido
          AND idProducto = NEW.idProducto;
        
        RETURN NULL;  -- No insertar nueva fila, ya existe una
    ELSE
        -- Si no existe, insertar la nueva fila
        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;
DROP trigger trigger_actualizar_cantidades ON productosdelpedido;

CREATE TRIGGER trigger_actualizar_cantidades
BEFORE INSERT ON productosDelPedido
FOR EACH ROW
EXECUTE FUNCTION actualizar_cantidades();


