package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class CalculatorTest {
    @Test
    void divideWorks() {
        assertEquals(5, new Calculator().divide(10, 2));
    }
}
