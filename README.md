# Daria Reporter App

This test suite is related to the reporter software and tests all the automatable test scenarios.

1. Appium Framework: A popular tool for automating native and web app, used here to interact with the Reporter App.
2. Pytest Framework: Used for better test management and assertions.
3. Logging: For managing and storing logs during test execution.
   Follow the path below to see the logs: src/logs_config/logs.log
4. YAML: For managing input data in a structured way.
   To change the test input data, you can edit the yaml file in the following path: 
   src/device_data/input_data.yml
   src/device_data/data_device.yml

**Installation:**

    git clone https://github.com/farzane-shafiee/test-automate-appium-reporter.git

    cd appium_test
    
    create ENV and active it:

        for win: 
            python -m venv env

        for linux: 
            pip install virtualenv
            virtualenv --python=python3 venv
            source venv/bin/activate

    install dependencies:
        sudo apt-get install python-mysqldb
        pip install -r requirements.txt
        
        
    run tests:
        pytest