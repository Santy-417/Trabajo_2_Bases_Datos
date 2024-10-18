from pydantic import BaseModel, Field, EmailStr
from datetime import date
from typing import Optional

class CustomerCreate(BaseModel):
    full_name: str = Field(..., description="Nombre completo del cliente (campo requerido)")
    email: EmailStr = Field(..., description="Correo electrónico del cliente (campo requerido)")
    phone: Optional[str] = Field(None, description="Número de teléfono del cliente")
    address: str = Field(..., description="Dirección del cliente (campo requerido)")

class Customer(CustomerCreate):
    customer_id: int

class EmployeeCreate(BaseModel):
    full_name: str = Field(..., description="Nombre completo del empleado (campo requerido)")
    position: str = Field(..., description="Cargo del empleado (campo requerido)")
    hire_date: date = Field(..., description="Fecha de contratación del empleado (campo requerido)")
    salary: float = Field(..., description="Salario del empleado (campo requerido)")

class Employee(EmployeeCreate):
    employee_id: int

class SupplierCreate(BaseModel):
    supplier_name: str = Field(..., description="Nombre del proveedor (campo requerido)")
    contact_email: Optional[EmailStr] = Field(None, description="Correo electrónico de contacto del proveedor")
    contact_phone: Optional[str] = Field(None, description="Número de teléfono de contacto del proveedor")
    address: Optional[str] = Field(None, description="Dirección del proveedor")

class Supplier(SupplierCreate):
    supplier_id: int

class ProductCreate(BaseModel):
    product_name: str = Field(..., description="Product name (required)")
    category: str = Field(..., description="Product category (required)")
    price: float = Field(..., description="Product price (required)")
    size: str = Field(..., description="Product size (required)")
    supplier_id: Optional[int] = Field(None, description="Supplier ID (optional)")

class Product(ProductCreate):
    product_id: int

class OrderCreate(BaseModel):
    customer_id: int = Field(..., description="ID del cliente que realiza el pedido (campo requerido)")
    order_date: date = Field(..., description="Fecha del pedido (campo requerido)")
    total_amount: float = Field(..., description="Monto total del pedido (campo requerido)")
    employee_id: int = Field(..., description="ID del empleado que procesa el pedido (campo requerido)")

class Order(OrderCreate):
    order_id: int

class DiscountCreate(BaseModel):
    discount_name: str = Field(..., description="Nombre del descuento (campo requerido)")
    discount_percent: float = Field(..., description="Porcentaje de descuento (campo requerido)")
    product_id: Optional[int] = Field(None, description="ID del producto al que se aplica el descuento")
    order_id: Optional[int] = Field(None, description="ID del pedido al que se aplica el descuento")

class Discount(DiscountCreate):
    discount_id: int
