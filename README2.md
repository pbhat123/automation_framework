# Automation Framework

Selenium + Pytest automation framework (Edge, headed mode). Built to start
with one app (TERMINATOR) and scale to more apps without touching the core
engine.

## Setup

```
pip install -r requirements.txt
```

## Run all tests

```
pytest
```

## Run a specific app / folder

```
pytest apps/terminator/tests/integration
```

## Structure

```
automation_framework/
│
├── apps/
│   └── terminator/
│       ├── config/
│       │   └── terminator_config.py     # base_url, user id, password, test data
│       ├── pages/
│       │   └── PAGE_NAME_page.py        # generic POM template — copy per page
│       └── tests/
│           ├── integration/
│           │   └── test_FLOW_NAME.py    # generic test template — copy per flow
│           └── regression/
│
├── core/
│   ├── base_actions.py                  # all reusable Selenium actions
│   ├── driver_factory.py                # Edge driver setup (headed)
│   └── utils.py                         # timestamps, filenames, config loader
│
├── reports/      (auto-created)         # timestamped HTML report per run
├── logs/         (auto-created)         # timestamped log file per test
├── screenshots/  (auto-created)         # timestamped screenshot per failure
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Adding a new app

1. Create `apps/<new_app>/config/<new_app>_config.py`
2. Copy `PAGE_NAME_page.py` into `apps/<new_app>/pages/` per page, rename, fill in locators
3. Copy `test_FLOW_NAME.py` into `apps/<new_app>/tests/integration/` or `/regression/`, rename, fill in steps

No changes needed to anything in `core/`, `conftest.py`, or `pytest.ini`.

## Adding a new page (within an existing app)

1. Copy `PAGE_NAME_page.py`, rename it to `<page_name>_page.py`
2. Fill in real locators, delete unused element slots/methods

## Adding a new test (within an existing app)

1. Copy `test_FLOW_NAME.py`, rename it to `test_<flow_name>.py`
2. Import the relevant page(s), fill in real steps/asserts, delete unused sections
