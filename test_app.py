import unittest
from app import EcoMetrics

class TestEcoMetrics(unittest.TestCase):
    def setUp(self):
        self.sistema = EcoMetrics()

    def test_calculo_economia_e_eficiencia(self):
        res = self.sistema.adicionar_registro("Teste", 10.0, 10.0)
        self.assertEqual(res["eficiencia_reuso_pct"], 50.0)
        self.assertEqual(res["economia_estimada_brl"], 65.0)

    def test_valor_negativo_erro(self):
        with self.assertRaises(ValueError):
            self.sistema.adicionar_registro("Erro", -5.0, 10.0)

if __name__ == "__main__":
    unittest.main()
