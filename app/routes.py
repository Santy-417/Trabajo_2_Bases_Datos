from fastapi import APIRouter, HTTPException
from app.models import CustomerCreate, Customer, EmployeeCreate, Employee, SupplierCreate, Supplier, ProductCreate, Product, OrderCreate, Order, DiscountCreate, Discount
from app.database import get_db_connection
from typing import List
import mysql.connector
from datetime import date

router = APIRouter()

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
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        
        customer_ids = range(last_id - len(customers) + 1, last_id + 1)
        
        return [Customer(customer_id=cid, **c.dict()) for cid, c in zip(customer_ids, customers)]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


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


@router.post("/products/", response_model=Product, tags=["Products"])
def create_product(product: ProductCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if product.supplier_id is not None:
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

@router.get("/Query1/", tags=["Query1: Get customer info by id"])
def get_customer_by_id(customer_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = f"SELECT * FROM customers WHERE customer_id = {customer_id}"
        cursor.execute(query)
        customers = cursor.fetchall()
        return [Customer(**customer) for customer in customers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query2/", tags=["Query2: Get employees with out orders"])
def get_employees_without_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = f"SELECT employees.* from employees LEFT join orders on employees.employee_id = orders.employee_id where orders.order_id IS NULL"
        cursor.execute(query)
        employees = cursor.fetchall()
        return [Employee(**employee) for employee in employees]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query3/", tags=["Query3: Get customers with out orders"])
def get_customers_without_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = f"SELECT customers.* FROM orders RIGHT join customers on customers.customer_id = orders.customer_id where orders.order_id IS NULL"
        cursor.execute(query)
        customers = cursor.fetchall()
        return [Customer(**customer) for customer in customers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query4/", tags=["Query4: Get MAX discount"])
def get_max_discount():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = f"SELECT MAX(discounts.discount_percent) FROM discounts"
        cursor.execute(query)
        discount = cursor.fetchone()
        return discount
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query5/", tags=["Query5: Get MIN discount"])
def get_min_discount():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = f"SELECT MIN(discounts.discount_percent) FROM discounts"
        cursor.execute(query)
        discount = cursor.fetchone()
        return discount
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query6/", tags=["Query6: Get average discount"])
def get_average_discount():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = f"SELECT AVG(discounts.discount_percent) FROM discounts"
        cursor.execute(query)
        discount = cursor.fetchone()
        return discount
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query7/", tags=["Query7: Get Orders before a date"])
def get_orders_before_date(date: date):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = f"SELECT * FROM orders WHERE order_date <= '{date}'"
        cursor.execute(query)
        orders = cursor.fetchall()
        return [Order(**order) for order in orders]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query8/", tags=["Query8: Get Orders after a date"])
def get_orders_after_date(date: date):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = f"SELECT * FROM orders WHERE order_date >= '{date}'"
        cursor.execute(query)
        orders = cursor.fetchall()
        return [Order(**order) for order in orders]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query9/", tags=["Query9: Get Orders between two dates"])
def get_orders_between_dates(start_date: date, end_date: date):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        query = f"SELECT * FROM orders WHERE order_date BETWEEN '{start_date}' AND '{end_date}'"
        cursor.execute(query)
        orders = cursor.fetchall()
        return [Order(**order) for order in orders]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.get("/Query10/", tags=["Query10: Get total orders by customer"])
def get_total_orders_by_customer(customer_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        SELECT customers.full_name, COUNT(orders.order_id) AS total_orders
        FROM customers
        LEFT JOIN orders ON customers.customer_id = orders.customer_id
        WHERE customers.customer_id = %s
        GROUP BY customers.full_name
        """
        cursor.execute(query, (customer_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.get("/Query11/", tags=["Query11: Get employees with total sales"])
def get_employees_with_total_sales():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        SELECT employees.full_name, SUM(orders.total_amount) AS total_sales
        FROM employees
        LEFT JOIN orders ON employees.employee_id = orders.employee_id
        GROUP BY employees.full_name
        """
        cursor.execute(query)
        employees_sales = cursor.fetchall()
        return employees_sales
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.get("/Query12/", tags=["Query12: Get products with discounts"])
def get_products_with_discounts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        SELECT products.product_name, discounts.discount_name, discounts.discount_percent
        FROM products
        LEFT JOIN discounts ON products.product_id = discounts.product_id
        """
        cursor.execute(query)
        products_discounts = cursor.fetchall()
        return products_discounts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.get("/Query13/", tags=["Query13: Get average order amount by employee"])
def get_average_order_amount_by_employee(employee_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        SELECT employees.full_name, AVG(orders.total_amount) AS average_order_amount
        FROM employees
        INNER JOIN orders ON employees.employee_id = orders.employee_id
        WHERE employees.employee_id = %s
        GROUP BY employees.full_name
        """
        cursor.execute(query, (employee_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.get("/Query14/{customer_id}/", tags=["Query14: Get customers with their last order date by ID"])
def get_customers_with_last_order(customer_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT customers.full_name, MAX(orders.order_date) AS last_order_date
        FROM customers
        LEFT JOIN orders ON customers.customer_id = orders.customer_id
        WHERE customers.customer_id = %s
        GROUP BY customers.full_name
        """
        cursor.execute(query, (customer_id,))
        customers_last_order = cursor.fetchall()
        return customers_last_order
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/Query15/", tags=["Query15: Get total products by supplier"])
def get_total_products_by_supplier():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
        SELECT suppliers.supplier_name, COUNT(products.product_id) AS total_products
        FROM suppliers
        LEFT JOIN products ON suppliers.supplier_id = products.supplier_id
        GROUP BY suppliers.supplier_id, suppliers.supplier_name
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()