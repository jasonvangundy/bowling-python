from robber import expect


def test_slicing():
    a_list = [1, 2, 3, 4]
    expect(a_list[1:]).to.eq([2, 3, 4])
