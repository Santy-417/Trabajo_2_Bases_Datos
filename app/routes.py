from fastapi import APIRouter, HTTPException
from app.models import CustomerCreate, Customer, EmployeeCreate, Employee, SupplierCreate, Supplier, ProductCreate, Product, OrderCreate, Order, DiscountCreate, Discount
from app.database import get_db_connection
from typing import List
import mysql.connector

router = APIRouter()

# Customer endpoints
@router.post("/customers/", response_model=Customer, tags=["Customers"])
def create_customer(customer: CustomerCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO customers (full_name, email, phone, address)
        VALUES (%s, %s, %s, %s)
        """
        values = (customer.full_name, customer.email, customer.phone, customer.address)
        
        cursor.execute(query, values)
        conn.commit()
        
        customer_id = cursor.lastrowid
        return Customer(customer_id=customer_id, **customer.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/customers/", response_model=List[Customer], tags=["Customers"])
def list_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM customers"
        cursor.execute(query)
        customers = cursor.fetchall()
        return [Customer(**customer) for customer in customers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/customers/bulk/", response_model=List[Customer], tags=["Customers"])
def create_customers_bulk(customers: List[CustomerCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO customers (full_name, email, phone, address)
        VALUES (%s, %s, %s, %s)
        """
        values = [(c.full_name, c.email, c.phone, c.address) for c in customers]
        
        cursor.executemany(query, values)
        conn.commit()
        
        # Fetch the last inserted id
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        # Calculate the ids of all inserted customers
        customer_ids = range(last_id - len(customers) + 1, last_id + 1)
        
        return [Customer(customer_id=cid, **c.dict()) for cid, c in zip(customer_ids, customers)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Employee endpoints
@router.post("/employees/", response_model=Employee, tags=["Employees"])
def create_employee(employee: EmployeeCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO employees (full_name, position, hire_date, salary)
        VALUES (%s, %s, %s, %s)
        """
        values = (employee.full_name, employee.position, employee.hire_date, employee.salary)
        
        cursor.execute(query, values)
        conn.commit()
        
        employee_id = cursor.lastrowid
        return Employee(employee_id=employee_id, **employee.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/employees/", response_model=List[Employee], tags=["Employees"])
def list_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM employees"
        cursor.execute(query)
        employees = cursor.fetchall()
        return [Employee(**employee) for employee in employees]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/employees/bulk/", response_model=List[Employee], tags=["Employees"])
def create_employees_bulk(employees: List[EmployeeCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO employees (full_name, position, hire_date, salary)
        VALUES (%s, %s, %s, %s)
        """
        values = [(e.full_name, e.position, e.hire_date, e.salary) for e in employees]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        employee_ids = range(last_id - len(employees) + 1, last_id + 1)
        
        return [Employee(employee_id=eid, **e.dict()) for eid, e in zip(employee_ids, employees)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Supplier endpoints
@router.post("/suppliers/", response_model=Supplier, tags=["Suppliers"])
def create_supplier(supplier: SupplierCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO suppliers (supplier_name, contact_email, contact_phone, address)
        VALUES (%s, %s, %s, %s)
        """
        values = (supplier.supplier_name, supplier.contact_email, supplier.contact_phone, supplier.address)
        
        cursor.execute(query, values)
        conn.commit()
        
        supplier_id = cursor.lastrowid
        return Supplier(supplier_id=supplier_id, **supplier.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/suppliers/", response_model=List[Supplier], tags=["Suppliers"])
def list_suppliers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM suppliers"
        cursor.execute(query)
        suppliers = cursor.fetchall()
        return [Supplier(**supplier) for supplier in suppliers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/suppliers/bulk/", response_model=List[Supplier], tags=["Suppliers"])
def create_suppliers_bulk(suppliers: List[SupplierCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO suppliers (supplier_name, contact_email, contact_phone, address)
        VALUES (%s, %s, %s, %s)
        """
        values = [(s.supplier_name, s.contact_email, s.contact_phone, s.address) for s in suppliers]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        supplier_ids = range(last_id - len(suppliers) + 1, last_id + 1)
        
        return [Supplier(supplier_id=sid, **s.dict()) for sid, s in zip(supplier_ids, suppliers)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Product endpoints
@router.post("/products/", response_model=Product, tags=["Products"])
def create_product(product: ProductCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        if product.supplier_id is not None:
            # Check if the supplier exists
            cursor.execute("SELECT supplier_id FROM suppliers WHERE supplier_id = %s", (product.supplier_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=400, detail=f"Supplier with id {product.supplier_id} does not exist")
        
        query = """
        INSERT INTO products (product_name, category, price, size, supplier_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (product.product_name, product.category, product.price, product.size, product.supplier_id)
        
        cursor.execute(query, values)
        conn.commit()
        
        product_id = cursor.lastrowid
        return Product(product_id=product_id, **product.dict())
    except mysql.connector.Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/products/", response_model=List[Product], tags=["Products"])
def list_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        return [Product(**product) for product in products]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/products/bulk/", response_model=List[Product], tags=["Products"])
def create_products_bulk(products: List[ProductCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO products (product_name, category, price, size, supplier_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = [(p.product_name, p.category, p.price, p.size, p.supplier_id) for p in products]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        product_ids = range(last_id - len(products) + 1, last_id + 1)
        
        return [Product(product_id=pid, **p.dict()) for pid, p in zip(product_ids, products)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Order endpoints
@router.post("/orders/", response_model=Order, tags=["Orders"])
def create_order(order: OrderCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO orders (customer_id, order_date, total_amount, employee_id)
        VALUES (%s, %s, %s, %s)
        """
        values = (order.customer_id, order.order_date, order.total_amount, order.employee_id)
        
        cursor.execute(query, values)
        conn.commit()
        
        order_id = cursor.lastrowid
        return Order(order_id=order_id, **order.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/orders/", response_model=List[Order], tags=["Orders"])
def list_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM orders"
        cursor.execute(query)
        orders = cursor.fetchall()
        return [Order(**order) for order in orders]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/orders/bulk/", response_model=List[Order], tags=["Orders"])
def create_orders_bulk(orders: List[OrderCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO orders (customer_id, order_date, total_amount, employee_id)
        VALUES (%s, %s, %s, %s)
        """
        values = [(o.customer_id, o.order_date, o.total_amount, o.employee_id) for o in orders]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        order_ids = range(last_id - len(orders) + 1, last_id + 1)
        
        return [Order(order_id=oid, **o.dict()) for oid, o in zip(order_ids, orders)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Discount endpoints
@router.post("/discounts/", response_model=Discount, tags=["Discounts"])
def create_discount(discount: DiscountCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO discounts (discount_name, discount_percent, product_id, order_id)
        VALUES (%s, %s, %s, %s)
        """
        values = (discount.discount_name, discount.discount_percent, discount.product_id, discount.order_id)
        
        cursor.execute(query, values)
        conn.commit()
        
        discount_id = cursor.lastrowid
        return Discount(discount_id=discount_id, **discount.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/discounts/", response_model=List[Discount], tags=["Discounts"])
def list_discounts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM discounts"
        cursor.execute(query)
        discounts = cursor.fetchall()
        return [Discount(**discount) for discount in discounts]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.post("/discounts/bulk/", response_model=List[Discount], tags=["Discounts"])
def create_discounts_bulk(discounts: List[DiscountCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO discounts (discount_name, discount_percent, product_id, order_id)
        VALUES (%s, %s, %s, %s)
        """
        values = [(d.discount_name, d.discount_percent, d.product_id, d.order_id) for d in discounts]
        
        cursor.executemany(query, values)
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        discount_ids = range(last_id - len(discounts) + 1, last_id + 1)
        
        return [Discount(discount_id=did, **d.dict()) for did, d in zip(discount_ids, discounts)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()