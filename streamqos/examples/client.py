import grpc
from streamqos_pb2 import QoSRequest, QuantileMetrics, Protocol, StorageType, StorageFormat
from streamqos_pb2_grpc import StreamQoSStub

def make_request():
    channel = grpc.insecure_channel('localhost:50051')
    stub = StreamQoSStub(channel)
    request = QoSRequest(
        topic_name="high_priority_events",
        latency_ms=QuantileMetrics(p50=5, p95=10, p99=20),
        throughput_mb_per_sec=QuantileMetrics(p50=100, p95=200, p99=300),
        min_availability_percent=99.99,
        max_cost_per_gb=0.05,
        supported_protocols=[Protocol.KAFKA],
        preferred_storage=StorageType.NVME,
        az_failure_tolerance=2,
        storage_format=StorageFormat.JSON
    )
    response = stub.NegotiateQoS(request)
    print(response)

if __name__ == "__main__":
    make_request()
