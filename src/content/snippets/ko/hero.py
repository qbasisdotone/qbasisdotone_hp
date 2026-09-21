from synthesis import synthesize_qsvt, synthesize_state
from client import submit

# Ax = b 를 정규화 역행렬 f(x) = x / (x² + δ²) 로 푼다
qsvt, subnorm = synthesize_qsvt(A, f, block_encoding="sparse_lcu")
prep = synthesize_state(b)

circuit = ...  # prep 과 qsvt 연결, 측정 추가 (생략)
handle = submit(circuit, device="qasis.gpu-sim", shots=32768)
result = handle.result()
