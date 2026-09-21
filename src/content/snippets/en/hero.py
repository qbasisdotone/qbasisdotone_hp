from synthesis import synthesize_qsvt, synthesize_state
from client import submit

# Solve Ax = b with the regularized inverse f(x) = x / (x² + δ²)
qsvt, subnorm = synthesize_qsvt(A, f, block_encoding="sparse_lcu")
prep = synthesize_state(b)

circuit = ...  # join prep and qsvt, add measurements (omitted)
handle = submit(circuit, device="qasis.gpu-sim", shots=32768)
result = handle.result()
