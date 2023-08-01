def test_hello_world(dut) -> None:
    dut.expect("Hello, World!")
