"""Tests for the Calculator class."""

import pytest

from example.calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    """Create a Calculator instance for testing."""
    return Calculator()


class TestCalculator:
    """Test cases for Calculator."""

    def test_add(self, calculator: Calculator) -> None:
        """Test addition of two numbers."""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self, calculator: Calculator) -> None:
        """Test subtraction of two numbers."""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(1, 1) == 0
        assert calculator.subtract(0, 5) == -5

    def test_multiply(self, calculator: Calculator) -> None:
        """Test multiplication of two numbers."""
        assert calculator.multiply(2, 3) == 6
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(0, 100) == 0

    def test_divide(self, calculator: Calculator) -> None:
        """Test division of two numbers."""
        assert calculator.divide(6, 2) == 3
        assert calculator.divide(5, 2) == 2.5
        assert calculator.divide(-6, 2) == -3

    def test_divide_by_zero(self, calculator: Calculator) -> None:
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(5, 0)
