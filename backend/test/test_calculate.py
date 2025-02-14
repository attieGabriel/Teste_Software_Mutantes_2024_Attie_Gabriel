import sys
import os

# Caminho absoluto para o arquivo calculate.py
calculate_path = 'C:\\Users\\Gabriel\\Programacao\\VSCODE\\BMI-Calculator\\backend'

# Adicionar o caminho ao sys.path
sys.path.insert(0, calculate_path)

from calculate import calculate_bmi, get_bmi_category
import pytest


def test_calculate_bmi():
    assert calculate_bmi(160.0, 54.0) == 21.093749999999996


def test_calculate_bmi_zero_and_negative_values():
    assert calculate_bmi(0.0, 0.0) == 0
    assert calculate_bmi(-1.0, 0.0) == 0
    assert calculate_bmi(0.0, -1.0) == 0
    assert calculate_bmi(150.0, 0.0) == 0
    assert calculate_bmi(0.0, 150.0) == 0


def test_invalid_input_type():
    with pytest.raises(TypeError):
        calculate_bmi('160', 54)

    with pytest.raises(TypeError):
        calculate_bmi(160, '54')

    with pytest.raises(TypeError):
        calculate_bmi('160', '54')

    with pytest.raises(TypeError):
        calculate_bmi('a', 55)

    with pytest.raises(TypeError):
        calculate_bmi(55, 'a')

    with pytest.raises(TypeError):
        calculate_bmi('a', 'a')


def test_category():
    assert get_bmi_category(0.0) == 'Inhuman'
    assert get_bmi_category(16.0) == 'Underweight'
    assert get_bmi_category(21.1) == 'Normal Weight'
    assert get_bmi_category(28.0) == 'Overweight'
    assert get_bmi_category(31.0) == 'Obesity'


def test_invalid_category_input():
    with pytest.raises(TypeError):
        get_bmi_category('16.0')
        
def test_mutante():
    assert calculate_bmi(1.0, 150.0) == 1500000

