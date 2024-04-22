
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import angular

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    # Render the order form
    return render_template('order_form.html')

# Define the POST route to create an order
@app.route('/create_order', methods=['POST'])
def create_order():
    # Get the form data
    customer_name = request.form.get('customer_name')
    product_name = request.form.get('product_name')
    quantity = request.form.get('quantity')

    # Create an order
    order = Order(customer_name, product_name, quantity)

    # Save the order to the database

    # Redirect to the confirmation page
    return redirect(url_for('order_confirmation', order_id=order.id))

# Define the GET route to retrieve a list of orders
@app.route('/orders')
def get_orders():
    # Get a list of orders from the database
    orders = Order.query.all()

    # Render the orders page
    return render_template('orders.html', orders=orders)

# Define the order confirmation route
@app.route('/order_confirmation')
def order_confirmation():
    # Get the order ID from the query string
    order_id = request.args.get('order_id')

    # Get the order from the database
    order = Order.query.get(order_id)

    # Render the order confirmation page
    return render_template('order_confirmation.html', order=order)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
