# 🛒 Spesa — Smart Local Shopping Platform

**Spesa** is a Django-based full-stack web application designed to streamline the shopping experience between local shopkeepers and their customers. The platform enables product listing, real-time cart management, checkout with order tracking, and user authentication. Shopkeepers can showcase their products, and customers can browse, add to cart, and place orders smoothly.

---

## 🧩 App Breakdown

Spesa is organized into several modular Django apps, each handling a specific feature:

### `home`
Landing page and public-facing views of the platform. It includes:
- Homepage UI
- About/Contact pages
- Navigation and footer templates

### `listing`
Handles the product listing logic:
- Add/Edit/Delete products
- Display product catalog
- Filter/search functionality

### `cart`
Manages user shopping carts:
- Add to cart
- Update quantity
- Cart summary

### `checkout`
Processes the checkout flow:
- Address form
- Payment integration (dummy/real)
- Order confirmation and summary

### `create`
Allows shopkeepers to create and manage their store inventory:
- Product upload form
- Price, description, image management

### `details`
Handles individual product and order detail views:
- Product description page
- Order tracking/status updates

### `userauths`
User authentication and account management:
- Signup/Login/Logout
- Password reset/change
- Profile management

---

## 🔧 Tech Stack

- **Backend:** Django 5+
- **Frontend:** HTML5, CSS3, JavaScript (with optional Tailwind or Bootstrap)
- **Database:** SQLite (default), can scale to PostgreSQL
- **Others:** Django Templates, Static Files, Custom Middleware (if added)

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/spesa.git
   cd spesa
