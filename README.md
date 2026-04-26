# API Automation Framework (Playwright + Pytest)

## Overview

This project is a **Python-based API automation framework** built using:

* Playwright (API testing)
* Pytest (test runner)
* Pytest-HTML (reporting)

It follows a **layered architecture**:

```
Tests → API Layer (POM) → API Client → Playwright Context
```

---

## Project Structure

```
api-automation/
│
├── tests/              # Test cases (CRUD + validations)
├── api/                # API layer (UsersAPI - endpoints)
├── utils/              # Helpers (API client, validators, test data)
├── config/             # Configuration (base URL)
├── conftest.py         # Pytest fixtures (API context)
└── requirements.txt
```

---

## Prerequisites

* Python 3.8+
* pip (Python package manager)

---

## Setup Instructions

### Clone the repository

```
git clone <your-repo-url>
cd api-automation
```


###  Install dependencies

```
pip install -r requirements.txt
```

---


## How to Run Tests

### Run tests

```
pytest -v
```


### Run with console logs

```
pytest -s -v
```

## Generate HTML Report

### Run tests with report

```
pytest -v --html=report.html 
```

### Open report

* Open `report.html` in browser

## Features

* CRUD API test coverage
* Dynamic test data generation
* Reusable API client
* POM (Page Object Model for APIs)
* Response validation utilities
* HTML reporting


## Sample Test Flow

1. Create user (POST)
2. Fetch user (GET)
3. Update user (PUT)
4. Delete user (DELETE)

## Tech Stack

* Python
* Pytest
* Playwright
* Pytest-HTML

