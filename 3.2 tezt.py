# x = 1
# y = 999
# z = "0,2"
# print("Let's count together: {}, then goes {}, and then {}".format(x, y, z))
#
# str1 = 999
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"Должно быть {expected_result}, а у вас {actual_result}, непорядок..."
