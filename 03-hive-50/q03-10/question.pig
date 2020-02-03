-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

datos = LOAD 'data.tsv' USING PigStorage('\t') 
    AS (letra:CHARARRAY, 
        fecha:CHARARRAY,
        cantidad:INT);
DUMP datos;

ordenar_datos = ORDER datos BY cantidad;
DUMP ordenar_datos;
ordenar_datos2 = FOREACH  ordenar_datos GENERATE cantidad ; 
DUMP ordenar_datos2;

ordenar_datos3 = LIMIT ordenar_datos2 5;
DUMP ordenar_datos3;

STORE ordenar_datos3 INTO 'output' using PigStorage('\t');