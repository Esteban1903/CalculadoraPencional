import unittest


class ParametrosPension:
    def __init__(self):
        self.edad = None
        self.salario_actual = None
        self.semanas_laboradas = None
        self.ahorro_pensional_a_hoy = None
        self.rentabilidad_promedio = None
        self.tasa_administracion = None
        self.edad_pension_total = None


class PensionTest(unittest.TestCase):

    @staticmethod
    def testAhorroPensionalAHoyMenorACero():
        """
        Prueba para validar el comportamiento cuando el ahorro pensional a hoy es menor a cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 99
        parametros.salario_actual = 2000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = -2
        parametros.rentabilidad_promedio = 6
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"


    @staticmethod
    def testSemanasLaboradasMenoresACero():
        """
        Prueba para validar el comportamiento cuando las semanas laboradas son menores a cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 78
        parametros.salario_actual = 0
        parametros.semanas_laboradas = -20
        parametros.ahorro_pensional_a_hoy = 0
        parametros.rentabilidad_promedio = 0
        parametros.tasa_administracion = 0
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"

    @staticmethod
    def testEdadMenorIgualACero():
        """
        Prueba para validar el comportamiento cuando la edad es menor o igual a cero.
        """
        parametros = ParametrosPension()
        parametros.edad = -10
        parametros.salario_actual = 0
        parametros.semanas_laboradas = 0
        parametros.ahorro_pensional_a_hoy = 0
        parametros.rentabilidad_promedio = 0
        parametros.tasa_administracion = 0
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"

    @staticmethod
    def testEdadCero():
        """
        Prueba para validar el comportamiento cuando la edad es exactamente cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 0
        parametros.salario_actual = 0
        parametros.semanas_laboradas = 0
        parametros.ahorro_pensional_a_hoy = 0
        parametros.rentabilidad_promedio = 0
        parametros.tasa_administracion = 0
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "s"
        hereda_pension = "n"

    @staticmethod
    def testEdadMayorACientoVeinte():
        """
        Prueba para validar el comportamiento cuando la edad es mayor a 120 años.
        """
        parametros = ParametrosPension()
        parametros.edad = 122
        parametros.salario_actual = 2000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 30000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "M"
        estado_civil = "c"
        hereda_pension = "n"

    @staticmethod
    def testTasaMenorACero():
        """
        Prueba para validar el comportamiento cuando la tasa de administración es menor a cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = 2500000
        parametros.semanas_laboradas = 1000
        parametros.ahorro_pensional_a_hoy = 20000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = -3
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"

    @staticmethod
    def testTasaMayorATres():
        """
        Prueba para validar el comportamiento cuando la tasa de administración es mayor a 3%.
        """
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = 5000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 20000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 5
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"

    @staticmethod
    def testSalarioActualMenorACero():
        """
        Prueba para validar el comportamiento cuando el salario actual es menor a cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = -3000000
        parametros.semanas_laboradas = 0
        parametros.ahorro_pensional_a_hoy = 0
        parametros.rentabilidad_promedio = 0
        parametros.tasa_administracion = 0
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"

    @staticmethod
    def testSalarioActualCero():
        """
        Prueba para validar el comportamiento cuando el salario actual es exactamente cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 76
        parametros.salario_actual = 0
        parametros.semanas_laboradas = 0
        parametros.ahorro_pensional_a_hoy = 0
        parametros.rentabilidad_promedio = 0
        parametros.tasa_administracion = 0
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 0

    @staticmethod
    def testRentabilidadPromedioMenorACero():
        """
        Prueba para validar el comportamiento cuando la rentabilidad promedio es menor a cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = 15000000
        parametros.semanas_laboradas = 1100
        parametros.ahorro_pensional_a_hoy = 400000000
        parametros.rentabilidad_promedio = -2
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 415000000.0

    @staticmethod
    def testRentabilidadPromedioCero():
        """
        Prueba para validar el comportamiento cuando la rentabilidad promedio es exactamente cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = 10000000
        parametros.semanas_laboradas = 1290
        parametros.ahorro_pensional_a_hoy = 130000000
        parametros.rentabilidad_promedio = 0
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 140000000.0

    @staticmethod
    def testSemanasLaboradasCero():
        """
        Prueba para validar el comportamiento cuando las semanas laboradas son exactamente cero.
        """
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = 0
        parametros.semanas_laboradas = 0
        parametros.ahorro_pensional_a_hoy = 0
        parametros.rentabilidad_promedio = 0
        parametros.tasa_administracion = 0
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 0

    @staticmethod
    def testEdadPensionMayorLegal():
        """
        Prueba para validar el comportamiento cuando la edad de pensión es mayor que la legal.
        """
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = 2000000
        parametros.semanas_laboradas = 1400
        parametros.ahorro_pensional_a_hoy = 20000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 80
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 43935653.751799814

    @staticmethod
    def testHeredaPension():
        parametros = ParametrosPension()
        parametros.edad = 65
        sexo = "f"
        estado_civil = "c"
        parametros.salario_actual = 14000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 200000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "s"
        valor_ahorrado = 214000000.0

    @staticmethod
    def testAhorroPensionalEsperado_PrimerCaso():
        parametros = ParametrosPension()
        parametros.edad = 70
        parametros.salario_actual = 3000000
        parametros.semanas_laboradas = 1260
        parametros.ahorro_pensional_a_hoy = 11000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "m"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 14000000.0

    @staticmethod
    def testAhorroPensionalEsperado_SegundoCaso():
        parametros = ParametrosPension()
        parametros.edad = 64
        parametros.salario_actual = 4000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 125000000
        parametros.rentabilidad_promedio = 2
        parametros.tasa_administracion = 1
        parametros.edad_pension_total = 65
        sexo = "m"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 132920000.0

    @staticmethod
    def testAhorroPensionalEsperado_TercerCaso():
        parametros = ParametrosPension()
        parametros.edad = 72
        parametros.salario_actual = 2000000
        parametros.semanas_laboradas = 1290
        parametros.ahorro_pensional_a_hoy = 21000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "f"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 23000000.0

    @staticmethod
    def testAhorroPensionalEsperado_CuartoCaso():
        parametros = ParametrosPension()
        parametros.edad = 65
        parametros.salario_actual = 9000000
        parametros.semanas_laboradas = 1302
        parametros.ahorro_pensional_a_hoy = 12000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 1
        parametros.edad_pension_total = 65
        sexo = "m"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 21000000.0

    @staticmethod
    def testAhorroPensionalEsperado_QuintoCaso():
        parametros = ParametrosPension()
        parametros.edad = 40
        parametros.salario_actual = 4000000
        parametros.semanas_laboradas = 1300
        parametros.ahorro_pensional_a_hoy = 15000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 1
        parametros.edad_pension_total = 65
        sexo = "m"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 102729598.50517015

    @staticmethod
    def testAhorroPensionalEsperado_SextoCaso():
        parametros = ParametrosPension()
        parametros.edad = 75
        parametros.salario_actual = 2500000
        parametros.semanas_laboradas = 1350
        parametros.ahorro_pensional_a_hoy = 80000000
        parametros.rentabilidad_promedio = 1
        parametros.tasa_administracion = 2
        parametros.edad_pension_total = 65
        sexo = "m"
        estado_civil = "c"
        hereda_pension = "n"
        valor_ahorrado = 82500000.0

