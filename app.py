import json
from datetime import datetime

class EcoMetrics:
    def __init__(self):
        self.registros = []
        self.custo_m3 = 6.50  # Valor médio estimado por m³ em R$

    def adicionar_registro(self, setor: str, consumo_potavel_m3: float, agua_reuso_m3: float):
        if consumo_potavel_m3 < 0 or agua_reuso_m3 < 0:
            raise ValueError("Os volumes não podem ser negativos.")
        
        total_utilizado = consumo_potavel_m3 + agua_reuso_m3
        percentual_reuso = (agua_reuso_m3 / total_utilizado * 100) if total_utilizado > 0 else 0
        economia_financeira = agua_reuso_m3 * self.custo_m3

        registro = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "setor": setor,
            "consumo_potavel_m3": round(consumo_potavel_m3, 2),
            "agua_reuso_m3": round(agua_reuso_m3, 2),
            "eficiencia_reuso_pct": round(percentual_reuso, 2),
            "economia_estimada_brl": round(economia_financeira, 2)
        }
        self.registros.append(registro)
        return registro

    def gerar_relatorio_geral(self):
        total_reuso = sum(r["agua_reuso_m3"] for r in self.registros)
        total_economia = sum(r["economia_estimada_brl"] for r in self.registros)
        
        return {
            "total_operacoes": len(self.registros),
            "volume_total_reutilizado_m3": round(total_reuso, 2),
            "economia_financeira_total_brl": round(total_economia, 2),
            "detalhamento": self.registros
        }

if __name__ == "__main__":
    sistema = EcoMetrics()
    sistema.adicionar_registro("Irrigação Setor A", 12.5, 35.0)
    sistema.adicionar_registro("Limpeza Operacional", 5.0, 18.2)
    
    relatorio = sistema.gerar_relatorio_geral()
    print(json.dumps(relatorio, indent=4, ensure_ascii=False))
