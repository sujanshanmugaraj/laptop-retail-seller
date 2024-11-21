
### **Key Features of the System**

1. **Product Management:**
   - The system allows for the management of products with fields like:
     - **Product Name:** The name of the product.
     - **Price:** The price of the product.
     - **Image:** An image associated with the product.
     - **Features:** Detailed specifications of the product, including brand, model, processor, RAM, weight, and other features.

2. **Customer Management:**
   - Customers are linked to the **User model** via a one-to-one relationship, meaning each user can have one customer profile.
   - The profile stores:
     - **Customer Name**
     - **Email Address**
     - **Phone Number** (with validation for a 10-digit phone number).

3. **Order Management:**
   - Orders are created when a customer makes a purchase, and each order includes:
     - **Order Date**
     - **Order Status** (whether it's complete or not)
     - **Total Amount**
     - A list of products added to the order, tracked by the **OrderItem** model.
   - There are properties to calculate:
     - **Total Cart Value:** The sum of the prices of all products in the cart.
     - **Total Cart Items:** The total number of items in the cart.

4. **Review Management:**
   - Customers can leave reviews for products they have purchased.
   - Reviews include:
     - **Content:** The review text.
     - **Datetime:** The timestamp when the review was created.

5. **Checkout Details:**
   - After placing an order, customers provide their **checkout information**:
     - **Shipping Address**
     - **Phone Number**
     - **City, State, Zip Code**
     - **Payment Information** (which could be credit card details or other payment methods).

6. **Discounts and Order Updates:**
   - The system uses **Django signals** to apply dynamic discounts:
     - If an item in an order has a quantity greater than 3, a 20% discount is applied to the total order amount.

7. **Customer Contact:**
   - A **Contact** model allows customers to submit inquiries or support requests, which are stored with the customer's name, email, phone number, and description of the issue.

---


### **How the System Works:**

1. **Admin or User Interface**:
   - Admins or users can add products, manage customer orders, view reviews, and handle customer inquiries.
   - Customers can browse products, add items to their cart, and complete purchases.
   
2. **Order Process**:
   - When a customer places an order, the system generates an `Order` record, calculates the total amount, and associates it with the customer and the items in the order (`OrderItem` model).
   - At checkout, the system collects the customer's shipping details and processes the payment information.

3. **Dynamic Discounts**:
   - The system listens for changes in the `OrderItem` model and applies a discount if any product in the order exceeds 3 units.
   
4. **Reviews and Feedback**:
   - After a purchase, customers can leave reviews for products, providing valuable feedback for other customers and the business.

---

### **Use Cases for This System:**
This system is ideal for an **e-commerce platform** that:
- Sells physical or digital products (e.g., electronics, clothing, etc.).
- Tracks customer purchases, order status, and shipping information.
- Allows customers to provide feedback through reviews.
- Provides a mechanism to offer discounts based on order conditions (e.g., bulk purchases).

---

