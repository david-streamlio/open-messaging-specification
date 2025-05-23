from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import List

app = FastAPI()

class Protocol(str, Enum):
    kafka = "KAFKA"
    pulsar = "PULSAR"
    mqtt = "MQTT"
    websockets = "WEBSOCKETS"

class StorageType(str, Enum):
    object_storage = "OBJECT_STORAGE"
    attached_storage = "ATTACHED_STORAGE"
    ephemeral = "EPHEMERAL"
    nvme = "NVME"

class StorageFormat(str, Enum):
    json = "JSON"
    avro = "AVRO"
    bytes = "BYTES"
    lakehouse = "LAKEHOUSE"

class QuantileMetrics(BaseModel):
    p50: float
    p95: float
    p99: float

class QoSRequest(BaseModel):
    topic_name: str
    latency_ms: QuantileMetrics
    throughput_mb_per_sec: QuantileMetrics
    min_availability_percent: float
    max_cost_per_gb: float
    supported_protocols: List[Protocol]
    preferred_storage: StorageType
    az_failure_tolerance: int
    storage_format: StorageFormat

@app.post("/qos/request")
def qos_request(req: QoSRequest):
    return {
        "message": f"Received QoS request for topic '{req.topic_name}'",
        "status": "PENDING"
    }
