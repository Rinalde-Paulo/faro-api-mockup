# main.py (VERSÃO LIMPA - SEM CHAVE)
from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="FARO API Mockup (Módulo 5 - Risco Climático)",
    description="Simulação de fachada da API.",
    version="2.0.0"
)

# Endpoint (NÃO MAIS PROTEGIDO AQUI)
@app.get("/api/v1/assessment/risk")
async def get_risk_assessment():
    """
    Endpoint principal que simula o resultado da avaliação de risco climático.
    O API Gateway faz a proteção.
    """

    simulated_data = {
        "status": "success",
        "timestamp": "2025-11-14T18:30:00Z",
        "location_id": "LOC-12345",
        "climatic_risk_score": 7.8,
        "risk_level": "High",
        "primary_threat": "Flooding",
        "details": {
            "drought_probability": 0.15,
            "flood_probability": 0.65,
            "fire_probability": 0.20,
            "mitigation_suggestions": [
                "Implementar sistemas de drenagem reforçados.",
                "Revisar o plano de contingência para eventos extremos."
            ]
        }
    }

    return simulated_data
