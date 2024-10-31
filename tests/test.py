from mypackage import myModule
def test_topn():
    assert myModule.top_n([8,3,5,4,6], 3) == [8,6,5], 'incorrect'