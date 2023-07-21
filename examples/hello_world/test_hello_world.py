from pytest_embedded_idf import IdfDut

def test_hello_world(dut: IdfDut) -> None:
    dut.expect("Hello, World!")
