# Login Module Test Strategy & Matrix

## Overview
This document outlines the black-box test cases for the system login feature, utilizing **Equivalence Partitioning (EP)** and **Boundary Value Analysis (BVA)** to ensure robust validation.

## Test Case Matrix

| Test ID | Module | Test Scenario | EP / BVA Classification | Input Data | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_LOG_01** | Login | Valid username length boundary (minimum) | BVA (Valid) | Username: `abcde` (5 chars) | Login screen accepts input successfully | Pass |
| **TC_LOG_02** | Login | Invalid username too short | BVA (Invalid) | Username: `abcd` (4 chars) | Error: "Username must be at least 5 characters" | Pass |
| **TC_LOG_03** | Login | Valid username length boundary (maximum) | BVA (Valid) | Username: `abcdefghijklmno` (15 chars) | Login screen accepts input successfully | Pass |
| **TC_LOG_04** | Login | Invalid username too long | BVA (Invalid) | Username: `abcdefghijklmnop` (16 chars) | Error: "Username cannot exceed 15 characters" | Pass |
| **TC_LOG_05** | Login | Valid standard username | Equivalence Partitioning (Valid) | Username: `qa_engineer` | Accepted into system session | Pass |