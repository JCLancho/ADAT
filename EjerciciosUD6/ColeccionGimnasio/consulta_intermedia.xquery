xquery version "3.1";
declare option exist:serialize "method=xml media-type=text/xml omit-xml-declaration=no indent=yes";
<cuotas>
    {for $socio_actividad in collection("/db/gimnasio")/USO_GIMNASIO/fila_uso
        let $socio := collection("/db/gimnasio")/SOCIOS_GIM/fila_socios[COD=$socio_actividad/CODSOCIO/text()]
        let $actividad := collection("/db/gimnasio")/ACTIVIDADES_GIM/fila_actividades[@cod = $socio_actividad/CODACTIV/text()]
    return
        <datos>
            <COD>{$socio_actividad/CODSOCIO/text()}</COD>
            <NOMBRESOCIO>{$socio/NOMBRE/text()}</NOMBRESOCIO>
            <CODACTIV>{$socio_actividad/CODACTIV/text()}</CODACTIV>
            <NOMBREACTIVIDAD>{$actividad/NOMBRE/text()}</NOMBREACTIVIDAD>
            <horas>{xs:integer($socio_actividad/HORAFINAL/text() - $socio_actividad/HORAINICIO/text())}</horas>
            <tipoact>{$actividad/@tipo/data()}</tipoact>
            {if ($actividad/@tipo/data() = 1) then(
                <cuota_adicional>0</cuota_adicional>
            ) else(
                if ($actividad/@tipo/data() = 2) then(
                    <cuota_adicional>2</cuota_adicional>
                )else(
                    <cuota_adicional>4</cuota_adicional>
                    )
                )
            }
        </datos>
    }
</cuotas>