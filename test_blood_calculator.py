def test_check_HDL():
    from blood_calculator import check_HDL
    answer = check_HDL(85)
    expected = 'Normal'
    assert answer == expected
    answer = check_HDL(45)
    expected = 'Borderline Low'
    assert answer == expected
    answer = check_HDL(20)
    expected = 'Low'
    assert answer == expected

def test_check_LDL():
    from blood_calculator import check_LDL
    answer = check_LDL(120)
    expected = "Normal"
    assert answer == expected
    answer = check_LDL(150)
    expected = "Borderline high"
    assert answer == expected
    answer = check_LDL(180)
    expected = "High"
    assert answer == expected   
    answer = check_LDL(200)
    expected = "Very high"
    assert answer == expected 


def test_check_total_cholesterol():
    from blood_calculator import check_total_cholesterol
    answer = check_total_cholesterol(180)
    expected = "Normal"
    assert answer == expected
    answer = check_total_cholesterol(220)
    expected = "Borderline high"
    assert answer == expected
    answer = check_total_cholesterol(250)
    expected = "High"
    assert answer == expected   



