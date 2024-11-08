# E-Commerce Web App

This is a **Django-based eCommerce application** with a user-friendly interface designed for selling both digital and non-digital products. The app includes the following features:

### Features

- **Homepage**: Displays a range of products categorized as digital and non-digital items. Users can browse through these products, view details, and add them to their cart.

- **Add to Cart**: Allows users to add products to their cart with a single click. Users can also update the quantity of items directly from the cart interface.

- **Cart Management**: In-cart quantity adjustments enable users to increase or decrease item quantities before proceeding to checkout, offering flexibility and control over their order.

- **Checkout Process**: For non-digital products, users are required to enter both an address and email to ensure proper delivery. For digital products, only an email is required for electronic delivery.

Built with Django for backend functionality, the app utilizes HTML, CSS, and JavaScript for a seamless and responsive frontend experience. This setup ensures a smooth shopping experience from product selection to checkout.

---

## Prerequisites

1. **Python**: Ensure Python is installed (version 3.6+). [Download from Python.org](https://www.python.org/downloads/).

2. **Virtual Environment (recommended)**: To avoid dependency conflicts, create a virtual environment.

### Create a Virtual Environment

- **For Linux/macOS:**
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

- **For Windows:**
  ```bash
  python -m venv env
  .\env\Scripts\activate
  ```

---

## Install Dependencies

1. **Make sure pip is up to date**:
   ```bash
   pip install --upgrade pip
   ```

2. **Install the required packages** from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## Database Setup

1. **Apply initial migrations** to set up the database:
   ```bash
   python manage.py migrate
   ```

---

## Create a Superuser (Optional)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

---

## Run the Development Server

Start the local development server:

```bash
python manage.py runserver
```

---

**A folder has been created to integrate a payment system using a dummy gateway. This integration is currently incomplete, and any help or suggestions to implement this feature would be greatly appreciated!**
