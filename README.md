# Dimerc_admin_portal

Welcome to the Dimerc Admin Portal! This portal is designed to manage users and explore photos using the JsonPlaceHolder API.

## Setup

### Prerequisites

- Python 3.x installed
- Git installed
- Code editor (e.g., Visual Studio Code)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ErizY/Dimerc_admin_portal.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Dimerc_admin_portal/flaskadmin/
    ```

3. Set up a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Generate Secret Key

To enhance security, generate a secret key for your Flask application:

1. Run the `generate_secret_key.py` script:

    ```bash
    python generate_secret_key.py
    ```

2. Copy the generated key.

3. Open `app.py` using your prefered editor and replace the existing `app.secret_key` with the new key.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the portal at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

3. Login with the default credentials:

    - Username: admin
    - Password: admin

## Portal Features

- **Manage Users:**
  - View a list of users.
  - Create new users.

- **Explore Photos:**
  - Browse through a directory of photos.

## Improvements

Here are some suggestions for future improvements:

- Implement user authentication with more secure methods (e.g., user database).
- Enhance the UI/UX of the portal for a more polished appearance.
- Implement error handling and feedback messages for a better user experience.
- Add logging to keep track of user actions and application events.

