import linecache
import re
import os


# Eliminar ya que java solo admite hasta 65535
def cps():
    init_line = 232
    last_line = 96009 #last_line - 1
    cache = dict()

    f = open('CCodigoPostal.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_CodigoPostal", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CCodigoPostal {\n"""

    postfix = """\nprivate final String text;

    private CCodigoPostal(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing c_CodigoPostal ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        cp_line = linecache.getline('catCFDI.xsd', counter)
        cp = re.findall(r'"([^"]*)"', cp_line)

        if cp[0] in cache:
            cache[cp[0]] = cache[cp[0]] + 1
        else:
            cache[cp[0]] = 1
            if counter == (last_line-1):
                f.write('C' + cp[0] + '("' + cp[0] + '");')
                print '    finish in line ' + str(counter)
            else:
                f.write('C' + cp[0] + '("' + cp[0] + '"),')


    f.write(postfix)
    f.close()

# Eliminar ya que java solo admite hasta 65535
def clave_prod_serv():
    init_line = 96333
    last_line = 149172 #last_line - 1
    cache = dict()

    f = open('CClaveProdServ.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_ClaveProdServ", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CClaveProdServ {\n"""

    postfix = """\nprivate final String text;

    private CClaveProdServ(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing c_ClaveProdServ ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        clave_line = linecache.getline('catCFDI.xsd', counter)
        clave_prod_serv = re.findall(r'"([^"]*)"', clave_line)

        if clave_prod_serv[0] in cache:
            cache[clave_prod_serv[0]] = cache[clave_prod_serv[0]] + 1
        else:
            cache[clave_prod_serv[0]] = 1
            if counter == (last_line - 1):
                f.write('C' + clave_prod_serv[0] + '("' + clave_prod_serv[0] + '");')
                print '    finish in line ' + str(counter)
            else:
                f.write('C' + clave_prod_serv[0] + '("' + clave_prod_serv[0] + '"),')

    f.write(postfix)
    f.close()


def patente_anual():
    init_line = 163308
    #last_line = 166419 #last_line - 1
    last_line = 163311
    f = open('CPatenteAnual.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_PatenteAduanal", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CPatenteAnual {\n"""

    postfix = """\nprivate final String text;

    private CPatenteAnual(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing c_PatenteAduanal ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        patente_line = linecache.getline('catCFDI.xsd', counter)
        patente_anual = re.findall(r'"([^"]*)"', patente_line)
        if counter == (last_line - 1):
            f.write('C' + patente_anual[0] + '("' + patente_anual[0] + '");')
            print '    finish in line ' + str(counter)
        else:
            f.write('C' + patente_anual[0] + '("' + patente_anual[0] + '"),')

    f.write(postfix)
    f.close()


def municipio():
    init_line = 162679
    last_line = 163249 #last_line - 1
    f = open('CMunicipio.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_Municipio", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CMunicipio {\n"""

    postfix = """\nprivate final String text;

    private CMunicipio(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing CMunicipio ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        municipio_line = linecache.getline('catCFDI.xsd', counter)
        municipio = re.findall(r'"([^"]*)"', municipio_line)
        if counter == (last_line - 1):
            f.write('C' + municipio[0] + '("' + municipio[0] + '");')
            print '    finish in line ' + str(counter)
        else:
            f.write('C' + municipio[0] + '("' + municipio[0] + '"),')

    f.write(postfix)
    f.close()

# Eliminar ya que java solo admite hasta 65535
def colonia():
    init_line = 152604
    last_line = 162603 #last_line - 1
    cache = dict()

    f = open('CColonia.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_Colonia", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CColonia {\n"""

    postfix = """\nprivate final String text;

    private CColonia(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing c_Colonia ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        colonia_line = linecache.getline('catCFDI.xsd', counter)
        colonia = re.findall(r'"([^"]*)"', colonia_line)

        if colonia[0] in cache:
            cache[colonia[0]] = cache[colonia[0]] + 1
        else:
            cache[colonia[0]] = 1
            if counter == (last_line - 1):
                f.write('C' + colonia[0] + '("' + colonia[0] + '");')
                print '    finish in line ' + str(counter)
            else:
                f.write('C' + colonia[0] + '("' + colonia[0] + '"),')

    f.write(postfix)
    f.close()



def clave_unidad():
    init_line = 149177
    last_line = 152483 #last_line - 1
    cache = dict()

    f = open('CClaveUnidad.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_ClaveUnidad", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CClaveUnidad {\n"""

    postfix = """\nprivate final String text;

    private CClaveUnidad(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing c_ClaveUnidad ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        clave_unidad_line = linecache.getline('catCFDI.xsd', counter)
        clave_unidad = re.findall(r'"([^"]*)"', clave_unidad_line)

        if clave_unidad[0] in cache:
            cache[clave_unidad[0]] = cache[clave_unidad[0]] + 1
        else:
            cache[clave_unidad[0]] = 1
            if counter == (last_line - 1):
                f.write('C' + clave_unidad[0] + '("' + clave_unidad[0] + '");')
                print '    finish in line ' + str(counter)
            else:
                f.write('C' + clave_unidad[0] + '("' + clave_unidad[0] + '"),')

    f.write(postfix)
    f.close()

def forma_pago():
    init_line = 6
    last_line = 26 #last_line + 1
    f = open('CFormaPago.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_FormaPago", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CFormaPago {\n"""

    postfix = """\nprivate final String text;

    private CFormaPago(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing c_FormaPago ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        forma_pago_line = linecache.getline('catCFDI.xsd', counter)
        forma_pago = re.findall(r'"([^"]*)"', forma_pago_line)
        if counter == (last_line - 1):
            f.write('C' + forma_pago[0] + '("' + forma_pago[0] + '");')
            print '    finish in line ' + str(counter)
        else:
            f.write('C' + forma_pago[0] + '("' + forma_pago[0] + '"),')

    f.write(postfix)
    f.close()


def tipo_relacion():
    init_line = 96014
    last_line = 96020 #last_line - 1
    cache = dict()

    f = open('CTipoRelacion.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_TipoRelacion", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CTipoRelacion {\n"""

    postfix = """\nprivate final String text;

    private CTipoRelacion(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing CTipoRelacion ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        tipo_relacion_line = linecache.getline('catCFDI.xsd', counter)
        tipo_relacion = re.findall(r'"([^"]*)"', tipo_relacion_line)

        if tipo_relacion[0] in cache:
            cache[tipo_relacion[0]] = cache[tipo_relacion[0]] + 1
        else:
            cache[tipo_relacion[0]] = 1
            if counter == (last_line - 1):
                f.write('C' + tipo_relacion[0] + '("' + tipo_relacion[0] + '");')
                print '    finish in line ' + str(counter)
            else:
                f.write('C' + tipo_relacion[0] + '("' + tipo_relacion[0] + '"),')

    f.write(postfix)
    f.close()


def impuesto():
    init_line = 96014
    last_line = 96020 #last_line - 1
    cache = dict()

    f = open('CImpuesto.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_Impuesto", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CImpuesto {\n"""

    postfix = """\nprivate final String text;

    private CImpuesto(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing CImpuesto ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        impuesto_line = linecache.getline('catCFDI.xsd', counter)
        impuesto = re.findall(r'"([^"]*)"', impuesto_line)

        if impuesto[0] in cache:
            cache[impuesto[0]] = cache[impuesto[0]] + 1
        else:
            cache[impuesto[0]] = 1
            if counter == (last_line - 1):
                f.write('C' + impuesto[0] + '("' + impuesto[0] + '");')
                print '    finish in line ' + str(counter)
            else:
                f.write('C' + impuesto[0] + '("' + impuesto[0] + '"),')

    f.write(postfix)
    f.close()


def regimen_fiscal():
    init_line = 96025
    last_line = 96046 #last_line - 1
    cache = dict()

    f = open('CRegimenFiscal.java', 'a')

    prefix = """
                package mx.gob.sat.v33;
                import javax.xml.bind.annotation.XmlEnum;
                import javax.xml.bind.annotation.XmlType;

                @XmlType(name = "c_RegimenFiscal", namespace = "http://www.sat.gob.mx/sitio_internet/cfd/catalogos")
                @XmlEnum
                public enum CRegimenFiscal {\n"""

    postfix = """\nprivate final String text;

    private CRegimenFiscal(final String text) {
        this.text = text;
    }

    public String getValue() {
        return text;
    }

    @Override
    public String toString() {
        return text;
    }
    }"""

    f.write(prefix)
    print "processing CRegimenFiscal ..."
    print "    Init in line " + str(init_line)
    for counter in range(init_line, last_line): #Number lines in xml file
        regimen_fiscal_line = linecache.getline('catCFDI.xsd', counter)
        regimen_fiscal = re.findall(r'"([^"]*)"', regimen_fiscal_line)

        if regimen_fiscal[0] in cache:
            cache[regimen_fiscal[0]] = cache[regimen_fiscal[0]] + 1
        else:
            cache[regimen_fiscal[0]] = 1
            if counter == (last_line - 1):
                f.write('C' + regimen_fiscal[0] + '("' + regimen_fiscal[0] + '");')
                print '    finish in line ' + str(counter)
            else:
                f.write('C' + regimen_fiscal[0] + '("' + regimen_fiscal[0] + '"),')

    f.write(postfix)
    f.close()


try:
    os.remove("CCodigoPostal.java")
    print ("File CCodigoPostal.java removed!!")
except OSError:
    print ("File CCodigoPostal.java doesn't exist")

try:
    os.remove("CClaveProdServ.java")
    print ("File CClaveProdServ.java removed!!")
except OSError:
    print ("File CClaveProdServ.java doesn't exist")

try:
    os.remove("CPatenteAnual.java")
    print ("File CPatenteAnual.java removed!!")
except OSError:
    print ("File CPatenteAnual.java doesn't exist")

try:
    os.remove("CMunicipio.java")
    print ("File CMunicipio.java removed!!")
except OSError:
    print ("File CMunicipio.java doesn't exist")

try:
    os.remove("CColonia.java")
    print ("File CColonia.java removed!!")
except OSError:
    print ("File CColonia.java doesn't exist")

try:
    os.remove("CClaveUnidad.java")
    print ("File CClaveUnidad.java removed!!")
except OSError:
    print ("File CClaveUnidad.java doesn't exist")

try:
    os.remove("CFormaPago.java")
    print ("File CFormaPago.java removed!!")
except OSError:
    print ("File CFormaPago.java doesn't exist")

try:
    os.remove("CTipoRelacion.java")
    print ("File CTipoRelacion.java removed!!")
except OSError:
    print ("File CTipoRelacion.java doesn't exist")

try:
    os.remove("CRegimenFiscal.java")
    print ("File CRegimenFiscal.java removed!!")
except OSError:
    print ("File CRegimenFiscal.java doesn't exist")

try:
    os.remove("CImpuesto.java")
    print ("File CImpuesto.java removed!!")
except OSError:
    print ("File CImpuesto.java doesn't exist\n")


cps()
clave_prod_serv()
patente_anual()
municipio()
colonia()
clave_unidad()
forma_pago()
tipo_relacion()
regimen_fiscal()
impuesto()
