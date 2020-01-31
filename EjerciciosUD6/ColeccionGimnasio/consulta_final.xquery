xquery version "3.1";
declare option exist:serialize "method=xml media-type=text/xml omit-xml-declaration=no indent=yes";
<cuota_final>
    {for $socio in collection("/db/gimnasio")/SOCIOS_GIM/fila_socios
        let $suma_cuotas := sum(collection("/db/gimnasio")/cuotas/datos[COD=$socio/COD/text()]/cuota_adicional)
    return
        <datos>
            <COD>{$socio/COD/text()}</COD>
            <NOMBRESOCIO>{$socio/NOMBRE/text()}</NOMBRESOCIO>
            <CUOTA_FIJA>{$socio/CUOTA_FIJA/text()}</CUOTA_FIJA>
            <suma_cuota_adic>{$suma_cuotas}</suma_cuota_adic>
            <cuota_total>{$suma_cuotas + $socio/CUOTA_FIJA/text()}</cuota_total>
        </datos>
    }
</cuota_final>