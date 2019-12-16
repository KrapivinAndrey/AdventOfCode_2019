import day_16


def test_get_pattern():
    assert day_16.get_pattern(1) == [0, 1, 0, -1]
    assert day_16.get_pattern(2) == [0, 0, 1, 1, 0, 0, -1, -1]


def test_apply_pattern():
    assert day_16.apply_pattern('12345678', day_16.get_pattern(1)) == '4'
    assert day_16.apply_pattern('12345678', day_16.get_pattern(2)) == '8'
    assert day_16.apply_pattern('12345678', day_16.get_pattern(3)) == '2'
    assert day_16.apply_pattern('12345678', day_16.get_pattern(4)) == '2'
    assert day_16.apply_pattern('12345678', day_16.get_pattern(5)) == '6'
    assert day_16.apply_pattern('12345678', day_16.get_pattern(6)) == '1'
    assert day_16.apply_pattern('12345678', day_16.get_pattern(7)) == '5'
    assert day_16.apply_pattern('12345678', day_16.get_pattern(8)) == '8'


def test_phase():
    assert day_16.phase('12345678') == '48226158'
    assert day_16.phase('48226158') == '34040438'
    assert day_16.phase('34040438') == '03415518'
    assert day_16.phase('03415518') == '01029498'


def test_run_phase():
    assert day_16.run_phase('80871224585914546619083218645595', 100)[:8:] == '24176176'
    assert day_16.run_phase('19617804207202209144916044189917', 100)[:8:] == '73745418'
    assert day_16.run_phase('69317163492948606335995924319873', 100)[:8:] == '52432133'
