with open_session("qasis.gpu-sim", seed=1234) as session:
    for i in range(12):
        # 목적 함수 1개 + parameter-shift 기울기 2개 = job 하나
        handle = submit(
            ansatz, device="qasis.gpu-sim",
            observable=[("Z", 1.0)],
            parameter_bindings=[{"theta": theta},
                                {"theta": theta + pi / 2},
                                {"theta": theta - pi / 2}],
            roles=["objective", "gradient", "gradient"],
            session=session,
        )
        r = handle.result()
        grad = (expval_of(r, binding_idx=1)
                - expval_of(r, binding_idx=2)) / 2
        theta -= 0.5 * grad

    curve = session.curve()  # 웹 세션 페이지와 같은 데이터
