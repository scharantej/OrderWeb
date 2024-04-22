## Flask Order System Application Design

**HTML Files**

- **order_form.html**: Contains the order form with input fields for customer information, product selection, and quantity.
- **order_confirmation.html**: Displays a confirmation message along with the order details once the form is submitted.

**Routes**

- **index**: The main route that displays the order form.
- **create_order**: A POST route that receives the form data, creates an order, and redirects to the confirmation page.
- **orders**: A GET route that retrieves a list of existing orders and displays them.

**Structure**

```
myapp
├── app.py
├── templates
│   ├── order_form.html
│   └── order_confirmation.html
```