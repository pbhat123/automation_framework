automation_framework/
│
├── apps/
│   └── terminator/
│       ├── config/
│       │   └── terminator_config.py     # base_url, user id, password, test data
│       │
│       ├── pages/
│       │   ├── login_page.py            # POM: locators + actions for that page
│       │   ├── dashboard_page.py
│       │   └── some_popup.py            # only if popup is complex/reused
│       │
│       └── tests/
│           ├── integration/
│           │   └── test_integration_flow.py
│           └── regression/
│               └── test_regression_flow.py
│
├── core/
│   ├── base_actions.py                  # reusable Selenium actions (click, type, select, upload, etc.)
│   ├── driver_factory.py                # Edge driver setup (headed for now)
│   └── utils.py                         # timestamp, common helpers, dir creation
│
├── reports/
│   └── terminator/
│       └── <timestamp>_terminator_<testname>_report.html
│
├── logs/
│   └── terminator/
│       └── <timestamp>_terminator_<testname>.log
│
├── screenshots/
│   └── terminator/
│       └── <timestamp>_terminator_<testname>_FAILURE.png
│
├── conftest.py                          # pytest hooks: report/log/screenshot wiring
├── pytest.ini
└── requirements.txt
