# Plivo Messagin API Demo
## System Requirements
- Python 3 + pip
- An internet browser to view the application
## Installation and Deployment
1. Download/unzip the repository in the directory of your choice and navigate to the `plivo_app/` directory in terminal
2. Add configuration file to the `conf/` directory (see directions below)
3. Create a virtual environment with python 3 in the application directory
    - `python3 -m venv venv`
4. Activate the virtual environment
    - `. venv/bin/activate`
5. Install dependencies from the requirements.txt file with pip
    - `pip install -r requirements.txt`
6. Set app.py as the flask application
    - `export FLASK_APP=app.py`
7. Run the flask application with the command `flask run`. If successfull, your application will be available at http://127.0.0.1:5000/ for testing.
```
(venv) Matthews-MBP:plivo_app mbehn$ flask run
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

### Configuration File:
1. Create a file called configuration.conf in the root directory of the application folder
2. Copy the configuration template below and paste it into the file
2. Replace the placholder values with your Plivo auth_id, auth_token, and src_number (the number you have rented from Plivo)
```
[plivo]
auth_id = $auth_id_placeholder
auth_token = $auth_token_placeholder
src_number = $src_number_placeholder
```