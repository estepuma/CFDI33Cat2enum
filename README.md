# CFDI33Cat2enum
Script de python para generar catálogos de CFDI 3.3 a java enums

Este Script genera los java enum de algunos catálogos del sat de CFDI 3.3. Los catálogos que genera son:

- Código postal
- Clave_prod_serv
- patente_anual
- municipio
- colonia
- clave_unidad
- forma_pago
- tipo_relacion
- regimen_fiscal
- impuesto

# Notas:
1. A los catálogos que genera les agrega un prefijo "C" por ejemplo para el catálogo clave unidad, genera un enum CClaveUnidad,
   con valores CC81("C81"), CC25("C25"), ...
2. Cada enum contiene un método String getValue() que obtiene el valor real.
3. El script en python se guía con los números de línea del archivo catCFDI.xsd, si se modifica el archivo habrá que actualizar el script
   con los nuevos números de línea.
4. Requiere python 2.7
