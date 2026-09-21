with open_session("qasis.gpu-sim", seed=1234) as session:
    for i in range(12):
        # one objective + two parameter-shift gradients = one job
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

    curve = session.curve()  # same data as the web session page
