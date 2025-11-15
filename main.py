# main.py (COMPLETO E 100% CORRIGIDO)
from fastapi import FastAPI, Header, HTTPException, Depends
from typing import Optional

app = FastAPI(
    title="FARO API Mockup (Módulo 5 - Risco Climático)",
    description="Simulação de fachada da API protegida por API Key (para demonstração).",
    version="1.0.0"
)

# Chave de API de Simulação (CORRETA)
SIMULATED_API_KEY = "AIzaSyB5_RgL9ZUKGbxFrwkL6T0b8g9_Q2MGcuo"

# Função de Validação da Chave
def verify_api_key(x_api_key: Optional[str] = Header(None, alias="X-API-Key")):
    """Verifica a chave de API fornecida no cabeçalho X-API-Key."""
    if not x_api_key or x_api_key != SIMULATED_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Acesso não autorizado. Chave de API inválida ou ausente no cabeçalho X-API-Key."
        )

# Endpoint Protegido (CORRIGIDO)
@app.get("/api/v1/assessment/risk")
async def get_risk_assessment(is_authorized: bool = Depends(verify_api_key)):
    """
    Endpoint principal que simula o resultado da avaliação de risco climático.
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
