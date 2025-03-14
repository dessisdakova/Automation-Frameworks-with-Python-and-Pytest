from pytest import mark


@mark.parametrize("tv_brand", [
    "Samsung",
    "Sony",
    "LG"
])
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")


def test_television_turns_on_json(tv_brand):
    print(f"{tv_brand} turns on as expected")


# pytest -s -v