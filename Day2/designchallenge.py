<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SmartStock - Inventory Management System</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,Helvetica,sans-serif;
}

body{
    background:#f5f7fb;
    color:#111827;
}

button,input,select,textarea{
    font-family:inherit;
}

button{
    cursor:pointer;
}

.hidden{
    display:none!important;
}

/* LOGIN */
.login-page{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#2563eb,#7c3aed);
}

.login-card{
    width:420px;
    max-width:92%;
    background:white;
    padding:40px;
    border-radius:20px;
    box-shadow:0 20px 60px rgba(0,0,0,.2);
}

.logo{
    display:flex;
    align-items:center;
    gap:12px;
    margin-bottom:30px;
}

.logo-icon{
    width:45px;
    height:45px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:#2563eb;
    color:white;
    border-radius:12px;
    font-size:22px;
    font-weight:bold;
}

.logo h2{
    font-size:21px;
}

.logo small{
    color:#6b7280;
}

.login-card h1{
    margin-bottom:8px;
}

.login-card>p{
    color:#6b7280;
    margin-bottom:25px;
}

.form-group{
    margin-bottom:16px;
}

label{
    display:block;
    font-size:13px;
    font-weight:bold;
    margin-bottom:7px;
}

input,select,textarea{
    width:100%;
    padding:12px;
    border:1px solid #dfe3ea;
    border-radius:8px;
    outline:none;
    background:white;
}

input:focus,select:focus,textarea:focus{
    border-color:#2563eb;
}

textarea{
    resize:vertical;
}

.primary-btn,
.secondary-btn,
.danger-btn{
    border:0;
    padding:11px 17px;
    border-radius:8px;
    font-weight:bold;
}

.primary-btn{
    background:#2563eb;
    color:white;
}

.primary-btn:hover{
    background:#1d4ed8;
}

.secondary-btn{
    background:#e5e7eb;
    color:#374151;
}

.danger-btn{
    background:#fee2e2;
    color:#dc2626;
}

.full{
    width:100%;
}

.login-demo{
    text-align:center;
    font-size:12px;
    color:#9ca3af;
    margin-top:18px;
}


/* APP */
.app{
    min-height:100vh;
    display:flex;
}

.sidebar{
    width:250px;
    position:fixed;
    left:0;
    top:0;
    bottom:0;
    background:#111827;
    color:white;
    z-index:100;
    display:flex;
    flex-direction:column;
}

.sidebar-logo{
    display:flex;
    gap:12px;
    align-items:center;
    padding:22px;
    border-bottom:1px solid #293241;
}

.sidebar-logo small{
    display:block;
    color:#9ca3af;
    font-size:11px;
    margin-top:3px;
}

.sidebar nav{
    padding:18px 12px;
}

.nav-item{
    width:100%;
    padding:13px;
    margin-bottom:5px;
    background:transparent;
    border:0;
    color:#9ca3af;
    text-align:left;
    border-radius:8px;
    font-size:14px;
}

.nav-item:hover{
    background:#1f2937;
    color:white;
}

.nav-item.active{
    background:#2563eb;
    color:white;
}

.sidebar-bottom{
    margin-top:auto;
    padding:15px;
    border-top:1px solid #293241;
}

.user{
    display:flex;
    align-items:center;
    gap:10px;
    margin-bottom:12px;
}

.avatar{
    width:38px;
    height:38px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    background:#dbeafe;
    color:#2563eb;
    font-weight:bold;
}

.user small{
    display:block;
    color:#9ca3af;
}

.logout{
    width:100%;
    border:0;
    background:transparent;
    color:#9ca3af;
    padding:10px;
    text-align:left;
}

.logout:hover{
    color:white;
}


/* MAIN */
.main{
    margin-left:250px;
    width:calc(100% - 250px);
}

.topbar{
    height:70px;
    background:white;
    border-bottom:1px solid #e5e7eb;
    display:flex;
    align-items:center;
    padding:0 30px;
    gap:20px;
    position:sticky;
    top:0;
    z-index:50;
}

.menu{
    display:none;
    border:0;
    background:none;
    font-size:22px;
}

.search{
    width:330px;
    background:#f3f4f6;
    padding:10px 14px;
    border-radius:8px;
    border:0;
}

.profile{
    margin-left:auto;
    display:flex;
    align-items:center;
    gap:10px;
}

.profile small{
    display:block;
    color:#6b7280;
    font-size:11px;
}

.content{
    padding:30px;
}

.page{
    display:none;
}

.page.active{
    display:block;
}

.page-header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:25px;
}

.page-header h1{
    font-size:28px;
    margin-bottom:5px;
}

.page-header p{
    color:#6b7280;
    font-size:14px;
}


/* STATS */
.stats{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:15px;
    margin-bottom:20px;
}

.stat{
    background:white;
    border:1px solid #e5e7eb;
    padding:20px;
    border-radius:12px;
}

.stat-title{
    color:#6b7280;
    font-size:12px;
}

.stat-value{
    font-size:25px;
    font-weight:bold;
    margin:8px 0;
}

.green-text{
    color:#16a34a;
}

.red-text{
    color:#dc2626;
}

.orange-text{
    color:#d97706;
}


/* PANELS */
.grid{
    display:grid;
    grid-template-columns:2fr 1fr;
    gap:20px;
    margin-bottom:20px;
}

.panel{
    background:white;
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:20px;
}

.panel h3{
    margin-bottom:5px;
}

.panel p{
    color:#6b7280;
    font-size:12px;
}

.panel-head{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;
}


/* TABLE */
.toolbar{
    display:flex;
    gap:10px;
    margin-bottom:20px;
}

.table-search{
    width:280px;
}

.table-container{
    overflow-x:auto;
}

table{
    width:100%;
    border-collapse:collapse;
}

th{
    background:#f9fafb;
    color:#6b7280;
    font-size:11px;
    padding:13px;
    text-align:left;
}

td{
    padding:14px 13px;
    border-bottom:1px solid #f0f0f0;
    font-size:13px;
}

.badge{
    display:inline-block;
    padding:5px 9px;
    border-radius:20px;
    font-size:10px;
    font-weight:bold;
}

.in{
    background:#dcfce7;
    color:#15803d;
}

.low{
    background:#fef3c7;
    color:#b45309;
}

.out{
    background:#fee2e2;
    color:#b91c1c;
}

.action{
    border:0;
    padding:6px 9px;
    border-radius:6px;
    background:#eff6ff;
    color:#2563eb;
    font-size:11px;
    margin-right:4px;
}


/* ACTIVITY */
.activity{
    display:flex;
    align-items:center;
    gap:12px;
    padding:13px 0;
    border-bottom:1px solid #f1f1f1;
}

.activity-icon{
    width:32px;
    height:32px;
    background:#eff6ff;
    color:#2563eb;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
}

.activity strong{
    display:block;
    font-size:12px;
}

.activity small{
    color:#6b7280;
    font-size:10px;
}


/* SUPPLIERS */
.cards{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:18px;
}

.supplier-card,
.low-card{
    background:white;
    border:1px solid #e5e7eb;
    padding:20px;
    border-radius:12px;
}

.supplier-card h3,
.low-card h3{
    margin-bottom:6px;
}

.supplier-card p,
.low-card p{
    color:#6b7280;
    font-size:12px;
    margin-bottom:10px;
}

.supplier-info{
    line-height:2;
    font-size:12px;
}


/* SETTINGS */
.settings{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
}


/* MODAL */
.modal{
    display:none;
    position:fixed;
    inset:0;
    background:rgba(0,0,0,.5);
    z-index:500;
    justify-content:center;
    align-items:center;
    padding:20px;
}

.modal.show{
    display:flex;
}

.modal-box{
    background:white;
    width:700px;
    max-width:100%;
    max-height:90vh;
    overflow:auto;
    padding:25px;
    border-radius:15px;
}

.modal-header{
    display:flex;
    justify-content:space-between;
    margin-bottom:20px;
}

.close{
    border:0;
    background:#f3f4f6;
    width:32px;
    height:32px;
    border-radius:7px;
    font-size:20px;
}

.form-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:15px;
}

.modal-buttons{
    display:flex;
    justify-content:flex-end;
    gap:10px;
    margin-top:20px;
}


/* TOAST */
.toast{
    position:fixed;
    right:25px;
    bottom:25px;
    background:#111827;
    color:white;
    padding:15px 20px;
    border-radius:9px;
    transform:translateY(100px);
    opacity:0;
    transition:.3s;
    z-index:1000;
}

.toast.show{
    transform:translateY(0);
    opacity:1;
}


/* RESPONSIVE */
@media(max-width:1200px){

    .stats{
        grid-template-columns:repeat(3,1fr);
    }

    .cards{
        grid-template-columns:repeat(2,1fr);
    }

}

@media(max-width:900px){

    .sidebar{
        transform:translateX(-100%);
        transition:.3s;
    }

    .sidebar.open{
        transform:translateX(0);
    }

    .main{
        margin-left:0;
        width:100%;
    }

    .menu{
        display:block;
    }

    .grid{
        grid-template-columns:1fr;
    }

    .settings{
        grid-template-columns:1fr;
    }

}

@media(max-width:600px){

    .content{
        padding:18px;
    }

    .topbar{
        padding:0 18px;
    }

    .topbar .search{
        display:none;
    }

    .stats{
        grid-template-columns:1fr;
    }

    .cards{
        grid-template-columns:1fr;
    }

    .page-header{
        flex-direction:column;
        align-items:flex-start;
        gap:15px;
    }

    .toolbar{
        flex-direction:column;
    }

    .table-search{
        width:100%;
    }

    .form-grid{
        grid-template-columns:1fr;
    }
}
</style>
</head>


<body>

<!-- =====================================================
     LOGIN PAGE
===================================================== -->

<div id="loginPage" class="login-page">

<div class="login-card">

<div class="logo">
    <div class="logo-icon">S</div>
    <div>
        <h2>SmartStock</h2>
        <small>Inventory Management</small>
    </div>
</div>

<h1>Welcome Back 👋</h1>
<p>Sign in to manage your inventory.</p>

<form id="loginForm">

<div class="form-group">
<label>Email</label>
<input type="email" id="email"
placeholder="admin@smartstock.com" required>
</div>

<div class="form-group">
<label>Password</label>
<input type="password" id="password"
placeholder="Enter password" required>
</div>

<button class="primary-btn full">
Login
</button>

</form>

<div class="login-demo">
Demo: Use any email and password
</div>

</div>
</div>


<!-- =====================================================
     APPLICATION
===================================================== -->

<div id="app" class="app hidden">


<!-- SIDEBAR -->

<aside class="sidebar">

<div class="sidebar-logo">

<div class="logo-icon">S</div>

<div>
<strong>SmartStock</strong>
<small>Inventory System</small>
</div>

</div>


<nav>

<button class="nav-item active"
onclick="showPage('dashboard',this)">
🏠 Dashboard
</button>

<button class="nav-item"
onclick="showPage('products',this)">
📦 Products
</button>

<button class="nav-item"
onclick="showPage('suppliers',this)">
🏢 Suppliers
</button>

<button class="nav-item"
onclick="showPage('stock',this)">
🔄 Stock Movement
</button>

<button class="nav-item"
onclick="showPage('lowstock',this)">
⚠️ Low Stock
</button>

<button class="nav-item"
onclick="showPage('reports',this)">
📊 Reports
</button>

<button class="nav-item"
onclick="showPage('settings',this)">
⚙️ Settings
</button>

</nav>


<div class="sidebar-bottom">

<div class="user">

<div class="avatar">AD</div>

<div>
<strong>Admin</strong>
<small>Administrator</small>
</div>

</div>

<button class="logout"
onclick="logout()">
⇥ Logout
</button>

</div>

</aside>


<!-- MAIN -->

<main class="main">

<header class="topbar">

<button class="menu"
onclick="toggleSidebar()">
☰
</button>

<input
class="search"
id="globalSearch"
placeholder="Search products..."
>

<div class="profile">

<div class="avatar">AD</div>

<div>
<strong>Admin</strong>
<small>Administrator</small>
</div>

</div>

</header>


<div class="content">


<!-- =====================================================
     DASHBOARD
===================================================== -->

<section id="dashboard" class="page active">

<div class="page-header">

<div>
<h1>Dashboard</h1>
<p>Here's what's happening with your inventory today.</p>
</div>

<button class="primary-btn"
onclick="openProductModal()">
+ Add Product
</button>

</div>


<div class="stats">

<div class="stat">
<div class="stat-title">Total Products</div>
<div class="stat-value" id="totalProducts">0</div>
<div class="green-text">↑ 8.2% this month</div>
</div>

<div class="stat">
<div class="stat-title">Total Stock</div>
<div class="stat-value" id="totalStock">0</div>
<div class="green-text">↑ 5.4% this month</div>
</div>

<div class="stat">
<div class="stat-title">Low Stock</div>
<div class="stat-value orange-text" id="lowStock">0</div>
<div class="red-text">Needs attention</div>
</div>

<div class="stat">
<div class="stat-title">Out of Stock</div>
<div class="stat-value red-text" id="outStock">0</div>
<div class="red-text">Requires action</div>
</div>

<div class="stat">
<div class="stat-title">Inventory Value</div>
<div class="stat-value" id="inventoryValue">₹0</div>
<div class="green-text">↑ 12.3% this month</div>
</div>

</div>


<div class="grid">

<div class="panel">

<div class="panel-head">
<div>
<h3>Inventory Overview</h3>
<p>Stock movement over the last 7 months</p>
</div>
</div>

<canvas id="inventoryChart"></canvas>

</div>


<div class="panel">

<div class="panel-head">
<h3>Stock Distribution</h3>
</div>

<canvas id="categoryChart"></canvas>

</div>

</div>


<div class="grid">

<div class="panel">

<div class="panel-head">
<h3>Low Stock Products</h3>

<button class="secondary-btn"
onclick="showPage('lowstock')">
View All
</button>

</div>

<div id="dashboardLowStock"></div>

</div>


<div class="panel">

<div class="panel-head">
<h3>Recent Activity</h3>
</div>

<div id="recentActivity"></div>

</div>

</div>

</section>


<!-- =====================================================
     PRODUCTS
===================================================== -->

<section id="products" class="page">

<div class="page-header">

<div>
<h1>Products</h1>
<p>Manage your inventory products.</p>
</div>

<button class="primary-btn"
onclick="openProductModal()">
+ Add Product
</button>

</div>


<div class="panel">

<div class="toolbar">

<input
class="table-search"
id="productSearch"
placeholder="Search products..."
oninput="renderProducts()"
>

<select id="categoryFilter"
onchange="renderProducts()">

<option value="all">All Categories</option>
<option>Electronics</option>
<option>Accessories</option>
<option>Office</option>

</select>

<select id="statusFilter"
onchange="renderProducts()">

<option value="all">All Status</option>
<option>In Stock</option>
<option>Low Stock</option>
<option>Out of Stock</option>

</select>

</div>


<div class="table-container">

<table>

<thead>
<tr>
<th>Product</th>
<th>SKU</th>
<th>Category</th>
<th>Price</th>
<th>Stock</th>
<th>Status</th>
<th>Actions</th>
</tr>
</thead>

<tbody id="productTable"></tbody>

</table>

</div>

</div>

</section>


<!-- =====================================================
     SUPPLIERS
===================================================== -->

<section id="suppliers" class="page">

<div class="page-header">

<div>
<h1>Suppliers</h1>
<p>Manage suppliers and vendors.</p>
</div>

<button class="primary-btn">
+ Add Supplier
</button>

</div>

<div class="cards" id="supplierCards"></div>

</section>


<!-- =====================================================
     STOCK MOVEMENT
===================================================== -->

<section id="stock" class="page">

<div class="page-header">

<div>
<h1>Stock Movement</h1>
<p>Track inventory coming in and going out.</p>
</div>

<div>

<button class="secondary-btn"
onclick="openStockModal('out')">
− Stock Out
</button>

<button class="primary-btn"
onclick="openStockModal('in')">
+ Stock In
</button>

</div>

</div>


<div class="panel">

<div class="table-container">

<table>

<thead>
<tr>
<th>Date</th>
<th>Product</th>
<th>Type</th>
<th>Quantity</th>
<th>User</th>
<th>Reference</th>
</tr>
</thead>

<tbody id="movementTable"></tbody>

</table>

</div>

</div>

</section>


<!-- =====================================================
     LOW STOCK
===================================================== -->

<section id="lowstock" class="page">

<div class="page-header">

<div>
<h1>Low Stock</h1>
<p>Products that require your attention.</p>
</div>

</div>

<div class="cards" id="lowStockCards"></div>

</section>


<!-- =====================================================
     REPORTS
===================================================== -->

<section id="reports" class="page">

<div class="page-header">

<div>
<h1>Reports</h1>
<p>Analyze your inventory performance.</p>
</div>

<div>
<button class="secondary-btn"
onclick="exportCSV()">
Export CSV
</button>

<button class="primary-btn"
onclick="window.print()">
Export PDF
</button>
</div>

</div>


<div class="stats">

<div class="stat">
<div class="stat-title">Inventory Value</div>
<div class="stat-value" id="reportValue">₹0</div>
</div>

<div class="stat">
<div class="stat-title">Products</div>
<div class="stat-value" id="reportProducts">0</div>
</div>

<div class="stat">
<div class="stat-title">Low Stock</div>
<div class="stat-value orange-text" id="reportLow">0</div>
</div>

</div>


<div class="panel">

<h3>Inventory Performance</h3>

<br>

<canvas id="reportChart"></canvas>

</div>

</section>


<!-- =====================================================
     SETTINGS
===================================================== -->

<section id="settings" class="page">

<div class="page-header">

<div>
<h1>Settings</h1>
<p>Manage your account and inventory preferences.</p>
</div>

</div>


<div class="settings">

<div class="panel">

<h3>Account Settings</h3>

<br>

<div class="form-group">
<label>Full Name</label>
<input value="Admin">
</div>

<div class="form-group">
<label>Email</label>
<input value="admin@smartstock.com">
</div>

<div class="form-group">
<label>Password</label>
<input type="password" value="password">
</div>

<button class="primary-btn"
onclick="toast('Account settings saved!')">
Save Changes
</button>

</div>


<div class="panel">

<h3>Business Settings</h3>

<br>

<div class="form-group">
<label>Business Name</label>
<input value="SmartStock Store">
</div>

<div class="form-group">

<label>Currency</label>

<select>
<option>Indian Rupee ₹</option>
<option>US Dollar $</option>
<option>Euro €</option>
</select>

</div>

<div class="form-group">
<label>Minimum Stock Level</label>
<input type="number" value="10">
</div>

<button class="primary-btn"
onclick="toast('Business settings saved!')">
Save Settings
</button>

</div>

</div>

</section>


</div>
</main>
</div>


<!-- =====================================================
     ADD PRODUCT MODAL
===================================================== -->

<div id="productModal" class="modal">

<div class="modal-box">

<div class="modal-header">

<h2>Add Product</h2>

<button class="close"
onclick="closeModal('productModal')">
×
</button>

</div>


<form id="productForm">

<div class="form-grid">

<div class="form-group">
<label>Product Name</label>
<input id="pName" required>
</div>

<div class="form-group">
<label>SKU</label>
<input id="pSku" required>
</div>

<div class="form-group">
<label>Category</label>
<select id="pCategory">
<option>Electronics</option>
<option>Accessories</option>
<option>Office</option>
</select>
</div>

<div class="form-group">
<label>Brand</label>
<input id="pBrand">
</div>

<div class="form-group">
<label>Purchase Price</label>
<input type="number" id="pPurchase" required>
</div>

<div class="form-group">
<label>Selling Price</label>
<input type="number" id="pSelling" required>
</div>

<div class="form-group">
<label>Current Stock</label>
<input type="number" id="pStock" required>
</div>

<div class="form-group">
<label>Minimum Stock</label>
<input type="number" id="pMin" value="10" required>
</div>

</div>

<div class="form-group">
<label>Description</label>
<textarea id="pDescription"></textarea>
</div>

<div class="modal-buttons">

<button type="button"
class="secondary-btn"
onclick="closeModal('productModal')">
Cancel
</button>

<button class="primary-btn">
Save Product
</button>

</div>

</form>

</div>
</div>


<!-- =====================================================
     STOCK MODAL
===================================================== -->

<div id="stockModal" class="modal">

<div class="modal-box">

<div class="modal-header">

<h2 id="stockTitle">Stock In</h2>

<button class="close"
onclick="closeModal('stockModal')">
×
</button>

</div>


<form id="stockForm">

<input type="hidden" id="movementType">

<div class="form-group">

<label>Product</label>

<select id="movementProduct"></select>

</div>

<div class="form-group">

<label>Quantity</label>

<input
type="number"
id="movementQuantity"
min="1"
required
>

</div>

<div class="form-group">

<label>Reference Number</label>

<input id="reference">

</div>

<div class="form-group">

<label>Notes</label>

<textarea id="notes"></textarea>

</div>

<div class="modal-buttons">

<button type="button"
class="secondary-btn"
onclick="closeModal('stockModal')">
Cancel
</button>

<button class="primary-btn">
Confirm
</button>

</div>

</form>

</div>
</div>


<div id="toast" class="toast">
Success
</div>


<!-- =====================================================
     JAVASCRIPT
===================================================== -->

<script>

/* ================= DATA ================= */

let products = [

{
id:1,
name:"Wireless Mouse",
sku:"WM001",
category:"Electronics",
brand:"Logitech",
purchase:500,
price:799,
stock:120,
min:20
},

{
id:2,
name:"Keyboard",
sku:"KB002",
category:"Electronics",
brand:"HP",
purchase:850,
price:1299,
stock:18,
min:25
},

{
id:3,
name:"USB Cable",
sku:"UC003",
category:"Accessories",
brand:"Anker",
purchase:150,
price:299,
stock:0,
min:20
},

{
id:4,
name:"Laptop Stand",
sku:"LS004",
category:"Accessories",
brand:"Portronics",
purchase:700,
price:1199,
stock:35,
min:15
},

{
id:5,
name:"Webcam",
sku:"WC005",
category:"Electronics",
brand:"Logitech",
purchase:1800,
price:2499,
stock:8,
min:15
},

{
id:6,
name:"Notebook",
sku:"NB006",
category:"Office",
brand:"Classmate",
purchase:50,
price:80,
stock:200,
min:30
}

];


let suppliers = [

{
name:"TechWorld Supplies",
contact:"Rajesh Kumar",
phone:"+91 98765 43210",
email:"techworld@example.com",
products:25,
orders:48
},

{
name:"Digital Hub",
contact:"Priya Sharma",
phone:"+91 99887 66554",
email:"digitalhub@example.com",
products:18,
orders:35
},

{
name:"Office Mart",
contact:"Arun Kumar",
phone:"+91 91234 56789",
email:"officemart@example.com",
products:12,
orders:21
}

];


let movements = [

{
date:"26 Aug 2026",
product:"Wireless Mouse",
type:"Stock In",
quantity:50,
user:"Admin",
reference:"PO-1024"
},

{
date:"25 Aug 2026",
product:"Keyboard",
type:"Stock Out",
quantity:12,
user:"Staff",
reference:"SO-882"
},

{
date:"24 Aug 2026",
product:"Laptop Stand",
type:"Stock In",
quantity:30,
user:"Admin",
reference:"PO-1023"
}

];


/* ================= LOGIN ================= */

document.getElementById("loginForm")
.addEventListener("submit",function(e){

e.preventDefault();

document.getElementById("loginPage")
.classList.add("hidden");

document.getElementById("app")
.classList.remove("hidden");

initialize();

toast("Login successful!");

});


function logout(){

document.getElementById("app")
.classList.add("hidden");

document.getElementById("loginPage")
.classList.remove("hidden");

}


/* ================= NAVIGATION ================= */

function showPage(id,button){

document.querySelectorAll(".page")
.forEach(p=>p.classList.remove("active"));

document.getElementById(id)
.classList.add("active");


document.querySelectorAll(".nav-item")
.forEach(n=>n.classList.remove("active"));

if(button)
button.classList.add("active");


if(id==="dashboard")
updateDashboard();

if(id==="products")
renderProducts();

if(id==="suppliers")
renderSuppliers();

if(id==="stock")
renderMovements();

if(id==="lowstock")
renderLowStock();

if(id==="reports")
renderReports();


document.querySelector(".sidebar")
.classList.remove("open");

}


/* ================= SIDEBAR ================= */

function toggleSidebar(){

document.querySelector(".sidebar")
.classList.toggle("open");

}


/* ================= STATUS ================= */

function status(product){

if(product.stock===0)
return "Out of Stock";

if(product.stock<=product.min)
return "Low Stock";

return "In Stock";

}


function badgeClass(s){

if(s==="In Stock")
return "in";

if(s==="Low Stock")
return "low";

return "out";

}


/* ================= DASHBOARD ================= */

function updateDashboard(){

let totalProducts=products.length;

let totalStock=products.reduce(
(a,p)=>a+p.stock,0);

let low=products.filter(
p=>p.stock>0 && p.stock<=p.min).length;

let out=products.filter(
p=>p.stock===0).length;

let value=products.reduce(
(a,p)=>a+(p.stock*p.price),0);


document.getElementById("totalProducts")
.textContent=totalProducts;

document.getElementById("totalStock")
.textContent=totalStock.toLocaleString();

document.getElementById("lowStock")
.textContent=low;

document.getElementById("outStock")
.textContent=out;

document.getElementById("inventoryValue")
.textContent="₹"+value.toLocaleString();


renderDashboardLowStock();

renderActivity();

drawCharts();

}


/* ================= LOW STOCK DASHBOARD ================= */

function renderDashboardLowStock(){

let box=document.getElementById(
"dashboardLowStock");

let list=products.filter(
p=>p.stock<=p.min).slice(0,4);


box.innerHTML=list.map(p=>`

<div class="activity">

<div class="activity-icon">⚠</div>

<div>
<strong>${p.name}</strong>
<small>${p.stock} units remaining</small>
</div>

<span class="badge ${badgeClass(status(p))}">
${status(p)}
</span>

</div>

`).join("");

}


/* ================= ACTIVITY ================= */

function renderActivity(){

let box=document.getElementById(
"recentActivity");

box.innerHTML=movements.slice(0,5)
.map(m=>`

<div class="activity">

<div class="activity-icon">
${m.type==="Stock In" ? "+" : "-"}
</div>

<div>
<strong>${m.type}: ${m.product}</strong>
<small>${m.quantity} units • ${m.date}</small>
</div>

</div>

`).join("");

}


/* ================= PRODUCTS ================= */

function renderProducts(){

let search=
(document.getElementById("productSearch")?.value||"")
.toLowerCase();

let category=
document.getElementById("categoryFilter")?.value||"all";

let filterStatus=
document.getElementById("statusFilter")?.value||"all";


let list=products.filter(p=>{

let searchMatch=
p.name.toLowerCase().includes(search)||
p.sku.toLowerCase().includes(search);

let categoryMatch=
category==="all"||p.category===category;

let statusMatch=
filterStatus==="all"||
status(p)===filterStatus;

return searchMatch &&
categoryMatch &&
statusMatch;

});


document.getElementById("productTable")
.innerHTML=list.map(p=>`

<tr>

<td>
<strong>${p.name}</strong><br>
<small>${p.brand}</small>
</td>

<td>${p.sku}</td>

<td>${p.category}</td>

<td>₹${p.price.toLocaleString()}</td>

<td>${p.stock}</td>

<td>
<span class="badge ${badgeClass(status(p))}">
${status(p)}
</span>
</td>

<td>

<button class="action"
onclick="viewProduct(${p.id})">
View
</button>

<button class="action"
onclick="deleteProduct(${p.id})">
Delete
</button>

</td>

</tr>

`).join("");

}


/* ================= VIEW PRODUCT ================= */

function viewProduct(id){

let p=products.find(x=>x.id===id);

alert(
"PRODUCT DETAILS\n\n"+
"Product: "+p.name+"\n"+
"SKU: "+p.sku+"\n"+
"Category: "+p.category+"\n"+
"Brand: "+p.brand+"\n"+
"Stock: "+p.stock+"\n"+
"Selling Price: ₹"+p.price+"\n"+
"Minimum Stock: "+p.min
);

}


/* ================= DELETE ================= */

function deleteProduct(id){

let p=products.find(x=>x.id===id);

if(confirm("Delete "+p.name+"?")){

products=products.filter(
x=>x.id!==id);

renderProducts();
updateDashboard();

toast("Product deleted!");

}

}


/* ================= ADD PRODUCT ================= */

function openProductModal(){

document.getElementById("productModal")
.classList.add("show");

}


document.getElementById("productForm")
.addEventListener("submit",function(e){

e.preventDefault();


let p={

id:Date.now(),

name:document.getElementById("pName").value,

sku:document.getElementById("pSku").value,

category:document.getElementById("pCategory").value,

brand:document.getElementById("pBrand").value,

purchase:Number(
document.getElementById("pPurchase").value),

price:Number(
document.getElementById("pSelling").value),

stock:Number(
document.getElementById("pStock").value),

min:Number(
document.getElementById("pMin").value)

};


products.push(p);

closeModal("productModal");

this.reset();

renderProducts();
updateDashboard();

toast("Product added successfully!");

});


/* ================= SUPPLIERS ================= */

function renderSuppliers(){

document.getElementById("supplierCards")
.innerHTML=suppliers.map(s=>`

<div class="supplier-card">

<h3>${s.name}</h3>

<p>${s.contact}</p>

<div class="supplier-info">

<div>📞 ${s.phone}</div>

<div>✉ ${s.email}</div>

<div>📦 Products: ${s.products}</div>

<div>🛒 Orders: ${s.orders}</div>

</div>

<br>

<button class="secondary-btn">
View Supplier
</button>

</div>

`).join("");

}


/* ================= STOCK MOVEMENT ================= */

function renderMovements(){

document.getElementById("movementTable")
.innerHTML=movements.map(m=>`

<tr>

<td>${m.date}</td>

<td>${m.product}</td>

<td>
<span class="badge ${
m.type==="Stock In"?"in":"out"
}">
${m.type}
</span>
</td>

<td>
${m.type==="Stock In"?"+":"-"}${m.quantity}
</td>

<td>${m.user}</td>

<td>${m.reference}</td>

</tr>

`).join("");

}


/* ================= STOCK MODAL ================= */

function openStockModal(type){

document.getElementById("stockModal")
.classList.add("show");

document.getElementById("movementType")
.value=type;

document.getElementById("stockTitle")
.textContent=
type==="in"?"Stock In":"Stock Out";


document.getElementById("movementProduct")
.innerHTML=products.map(p=>`

<option value="${p.id}">
${p.name} — Stock: ${p.stock}
</option>

`).join("");

}


document.getElementById("stockForm")
.addEventListener("submit",function(e){

e.preventDefault();


let type=
document.getElementById("movementType").value;

let id=
Number(document.getElementById("movementProduct").value);

let qty=
Number(document.getElementById("movementQuantity").value);

let p=products.find(x=>x.id===id);


if(type==="out" && qty>p.stock){

toast("Not enough stock!");

return;

}


if(type==="in")
p.stock+=qty;
else
p.stock-=qty;


movements.unshift({

date:"26 Aug 2026",

product:p.name,

type:type==="in"?"Stock In":"Stock Out",

quantity:qty,

user:"Admin",

reference:
document.getElementById("reference").value||
"N/A"

});


closeModal("stockModal");

this.reset();

renderMovements();
updateDashboard();

toast(
type==="in"
?"Stock added successfully!"
:"Stock removed successfully!"
);

});


/* ================= LOW STOCK ================= */

function renderLowStock(){

let list=products.filter(
p=>p.stock<=p.min);


document.getElementById("lowStockCards")
.innerHTML=list.map(p=>`

<div class="low-card">

<h3>${p.name}</h3>

<p>SKU: ${p.sku}</p>

<h2>${p.stock} units</h2>

<p>Minimum: ${p.min}</p>

<br>

<button class="primary-btn"
onclick="openStockModal('in')">
Reorder
</button>

</div>

`).join("");


if(list.length===0){

document.getElementById("lowStockCards")
.innerHTML=
"<div class='panel'><h3>All stock levels are healthy 🎉</h3></div>";

}

}


/* ================= REPORTS ================= */

function renderReports(){

let value=products.reduce(
(a,p)=>a+(p.stock*p.price),0);

let low=products.filter(
p=>p.stock<=p.min).length;


document.getElementById("reportValue")
.textContent="₹"+value.toLocaleString();

document.getElementById("reportProducts")
.textContent=products.length;

document.getElementById("reportLow")
.textContent=low;


if(window.reportChart)
window.reportChart.destroy();


window.reportChart=new Chart(
document.getElementById("reportChart"),
{

type:"bar",

data:{

labels:[
"Mon","Tue","Wed",
"Thu","Fri","Sat","Sun"
],

datasets:[

{
label:"Stock In",
data:[120,150,80,180,130,200,160]
},

{
label:"Stock Out",
data:[70,90,100,120,80,110,90]
}

]

},

options:{
responsive:true
}

});

}


/* ================= CHARTS ================= */

function drawCharts(){

if(window.inventoryChart)
window.inventoryChart.destroy();

if(window.categoryChart)
window.categoryChart.destroy();


window.inventoryChart=new Chart(
document.getElementById("inventoryChart"),
{

type:"line",

data:{

labels:[
"Feb","Mar","Apr",
"May","Jun","Jul","Aug"
],

datasets:[{

label:"Inventory",

data:[
12000,
13500,
12800,
15000,
16200,
17500,
18450
],

borderWidth:3,
tension:.4

}]

},

options:{
responsive:true
}

});


let categories={};

products.forEach(p=>{

categories[p.category]=
(categories[p.category]||0)+p.stock;

});


window.categoryChart=new Chart(
document.getElementById("categoryChart"),
{

type:"doughnut",

data:{

labels:Object.keys(categories),

datasets:[{

data:Object.values(categories)

}]

},

options:{
responsive:true
}

});

}


/* ================= SEARCH ================= */

document.getElementById("globalSearch")
.addEventListener("input",function(){

showPage("products");

document.getElementById("productSearch")
.value=this.value;

renderProducts();

});


/* ================= MODAL ================= */

function closeModal(id){

document.getElementById(id)
.classList.remove("show");

}


/* ================= TOAST ================= */

function toast(message){

let t=document.getElementById("toast");

t.textContent="✓ "+message;

t.classList.add("show");

setTimeout(()=>{
t.classList.remove("show");
},2500);

}


/* ================= CSV ================= */

function exportCSV(){

let csv=
"Product,SKU,Category,Price,Stock,Status\n";

products.forEach(p=>{

csv+=
`${p.name},${p.sku},${p.category},${p.price},${p.stock},${status(p)}\n`;

});


let blob=new Blob(
[csv],
{type:"text/csv"}
);

let url=URL.createObjectURL(blob);

let a=document.createElement("a");

a.href=url;
a.download="smartstock-inventory.csv";

a.click();

URL.revokeObjectURL(url);

toast("CSV exported!");

}


/* ================= INITIALIZE ================= */

function initialize(){

updateDashboard();

renderProducts();

renderSuppliers();

renderMovements();

renderLowStock();

}

</script>

</body>
</html>
