
from hmac_token.hmac_token.generate import generate_digest

def test_generate_from_empty():
    signature = generate_digest({})
    assert isinstance(signature, str)
    assert len(signature) > 0

def test_generate_from_complex():
    signature = generate_digest({
        "id": "MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz",
        "zev": 123445,
        "name": "bob",
        "ls": ["asd", "ert", "dfgs"],
        "aaa": 12.45,
        "next": {
            "id": "LTAxMmMtMDllZGU5NDE2MDAzMDAwMDAwMDAtMDAwMC0wMDBi",
            "name": "luke",
            "zev": 5551,
            "aaa": 54.2,
            "new": False
        }
    })
    assert isinstance(signature, str)
    assert len(signature) > 0

def test_generate_same():
    signature_one = generate_digest({"id": 12345})
    signature_two = generate_digest({"id": 12345})
    assert signature_one == signature_two

def test_generate_different_from_similar():
    signature_one = generate_digest({
        "id": 12345,
        "name": "bob"
    })
    signature_two = generate_digest({
        "name": "bob",
        "id": 12345
    })
    assert signature_one != signature_two