from sqlmodel import Field, SQLModel, create_engine, Session, Relationship, select
from typing import Optional, List

# Base class for furniture
class Furniture(SQLModel):
    category: str
    warehouse_location: str  # Location: Fanling or Mongkok

# Chair model
class Chair(Furniture, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_no: str = Field(index=True, unique=True)
    stock_level: int
    price: float
    material: str
    width: float
    height: float
    depth: float
    has_armrests: bool
    max_weight: float
    has_sitting_pad: bool
    cart_items: List["CartItem"] = Relationship(back_populates="chair")

# Bed model
class Bed(Furniture, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_no: str = Field(index=True, unique=True)
    stock_level: int
    price: float
    material: str
    width: float
    height: float
    depth: float
    bed_size: str
    has_headboard: bool
    cart_items: List["CartItem"] = Relationship(back_populates="bed")

# Bookshelf model
class Bookshelf(Furniture, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_no: str = Field(index=True, unique=True)
    stock_level: int
    price: float
    material: str
    width: float
    height: float
    depth: float
    shelf_layers: int
    maximum_weight: float
    cart_items: List["CartItem"] = Relationship(back_populates="bookshelf")

# Shopping Cart Item model
class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: str  # e.g., user ID or session ID)
    product_type: str  # Chair, Bed or Bookshelf
    model_no: str  
    quantity: int = Field(ge=1)  # Quantity of the product in the cart
    chair_id: Optional[int] = Field(default=None, foreign_key="chair.id")
    bed_id: Optional[int] = Field(default=None, foreign_key="bed.id")
    bookshelf_id: Optional[int] = Field(default=None, foreign_key="bookshelf.id")
    chair: Optional[Chair] = Relationship(back_populates="cart_items")
    bed: Optional[Bed] = Relationship(back_populates="cart_items")
    bookshelf: Optional[Bookshelf] = Relationship(back_populates="cart_items")

# Create products list
products = [
    # Chair samples
    Chair(category="Wooden Chair", warehouse_location="FanLing", model_no="CH-001", stock_level=50, 
          price=299.0, material="Wood", width=45.0, height=85.0, depth=50.0, has_armrests=False, 
          max_weight=120.0, has_sitting_pad=True),
    Chair(category="Metal Chair", warehouse_location="Mongkok", model_no="CH-002", stock_level=30, 
          price=349.0, material="Metal", width=50.0, height=90.0, depth=55.0, has_armrests=True, 
          max_weight=150.0, has_sitting_pad=True),
    Chair(category="Plastic Chair", warehouse_location="FanLing", model_no="CH-003", stock_level=20, 
          price=199.0, material="Plastic", width=40.0, height=80.0, depth=45.0, has_armrests=False, 
          max_weight=100.0, has_sitting_pad=False),
    Chair(category="Ergonomic Chair", warehouse_location="Mongkok", model_no="CH-004", stock_level=25, 
          price=499.0, material="Mesh", width=48.0, height=95.0, depth=52.0, has_armrests=True, 
          max_weight=130.0, has_sitting_pad=True),
    Chair(category="Folding Chair", warehouse_location="FanLing", model_no="CH-005", stock_level=40, 
          price=149.0, material="Aluminum", width=42.0, height=78.0, depth=48.0, has_armrests=False, 
          max_weight=110.0, has_sitting_pad=False),

    # Bed samples
    Bed(category="Wooden Bed - Double", warehouse_location="FanLing", model_no="BD-001", stock_level=10, 
        price=1999.0, material="Wood", width=200.0, height=40.0, depth=160.0, bed_size="Double", 
        has_headboard=True),
    Bed(category="Metal Bed - Double", warehouse_location="Mongkok", model_no="BD-002", stock_level=15, 
        price=1499.0, material="Metal", width=180.0, height=35.0, depth=150.0, bed_size="Double", 
        has_headboard=False),
    Bed(category="Wooden Bed - Single", warehouse_location="FanLing", model_no="BD-003", stock_level=8, 
        price=999.0, material="Wood", width=150.0, height=30.0, depth=120.0, bed_size="Single", 
        has_headboard=True),
    Bed(category="Upholstered Bed - Queen", warehouse_location="Mongkok", model_no="BD-004", stock_level=12, 
        price=2499.0, material="Fabric", width=210.0, height=45.0, depth=170.0, bed_size="Queen", 
        has_headboard=True),
    Bed(category="Metal Bed - Single", warehouse_location="FanLing", model_no="BD-005", stock_level=20, 
        price=799.0, material="Metal", width=140.0, height=32.0, depth=110.0, bed_size="Single", 
        has_headboard=False),

    # Bookshelf samples
    Bookshelf(category="Wooden Book Shelf - Small Size", warehouse_location="FanLing", model_no="BS-001", 
              stock_level=25, price=599.0, material="Wood", width=80.0, height=180.0, depth=30.0, 
              shelf_layers=5, maximum_weight=25.0),
    Bookshelf(category="Metal Book Shelf", warehouse_location="Mongkok", model_no="BS-002", stock_level=30, 
              price=499.0, material="Metal", width=70.0, height=160.0, depth=25.0, shelf_layers=4, 
              maximum_weight=20.0),
    Bookshelf(category="Wooden Book Shelf - Big Size", warehouse_location="FanLing", model_no="BS-003", 
              stock_level=15, price=799.0, material="Wood", width=90.0, height=200.0, depth=35.0, 
              shelf_layers=6, maximum_weight=30.0),
    Bookshelf(category="Corner Bookshelf", warehouse_location="Mongkok", model_no="BS-004", stock_level=18, 
              price=649.0, material="Wood", width=60.0, height=170.0, depth=40.0, shelf_layers=4, 
              maximum_weight=22.0),
    Bookshelf(category="Tall Metal Bookshelf", warehouse_location="FanLing", model_no="BS-005", stock_level=22, 
              price=699.0, material="Metal", width=75.0, height=190.0, depth=30.0, shelf_layers=5, 
              maximum_weight=28.0),
]

# Create SQLite engine
engine = create_engine("sqlite:///furniture.db")

# Create all tables
SQLModel.metadata.create_all(engine)

# Insert furniture products
def insert_furniture(products):
    valid_locations = {"FanLing", "Mongkok"}
    with Session(engine) as session:
        for product in products:
            # Validate warehouse_location
            if product.warehouse_location not in valid_locations:
                raise ValueError(f"Invalid warehouse_location: {product.warehouse_location}. Must be one of {valid_locations}")
            
            # Check if the item already exists using a query
            existing = None
            if isinstance(product, Chair):
                existing = session.exec(
                    select(Chair).where(Chair.model_no == product.model_no)
                ).first()
            elif isinstance(product, Bed):
                existing = session.exec(
                    select(Bed).where(Bed.model_no == product.model_no)
                ).first()
            elif isinstance(product, Bookshelf):
                existing = session.exec(
                    select(Bookshelf).where(Bookshelf.model_no == product.model_no)
                ).first()
            
            # Only add if it doesn't exist
            if not existing:
                session.add(product)
        
        # Commit all changes at once
        session.commit()

# Insert shopping cart items
def insert_cart_items(cart_items):
    with Session(engine) as session:
        for item in cart_items:
            # Validate product_type
            valid_product_types = {"Chair", "Bed", "Bookshelf"}
            if item.product_type not in valid_product_types:
                raise ValueError(f"Invalid product_type: {item.product_type}. Must be one of {valid_product_types}")
            
            # Check if the product exists and get its ID
            product = None
            if item.product_type == "Chair":
                product = session.exec(
                    select(Chair).where(Chair.model_no == item.model_no)
                ).first()
                if product:
                    item.chair_id = product.id
            elif item.product_type == "Bed":
                product = session.exec(
                    select(Bed).where(Bed.model_no == item.model_no)
                ).first()
                if product:
                    item.bed_id = product.id
            elif item.product_type == "Bookshelf":
                product = session.exec(
                    select(Bookshelf).where(Bookshelf.model_no == item.model_no)
                ).first()
                if product:
                    item.bookshelf_id = product.id
            
            if not product:
                raise ValueError(f"Product with model_no {item.model_no} and type {item.product_type} does not exist")
            
            # Check stock availability
            if product.stock_level < item.quantity:
                raise ValueError(f"Insufficient stock for {item.product_type} {item.model_no}. Available: {product.stock_level}, Requested: {item.quantity}")
            
            # Check if the cart item already exists for this cart_id and product
            existing_item = session.exec(
                select(CartItem).where(
                    CartItem.cart_id == item.cart_id,
                    CartItem.product_type == item.product_type,
                    CartItem.model_no == item.model_no
                )
            ).first()
            
            if existing_item:
                # Update quantity if item exists
                existing_item.quantity += item.quantity
            else:
                # Add new cart item
                session.add(item)
        
        session.commit()

# List shopping cart contents
def list_cart_contents(cart_id: str):
    with Session(engine) as session:
        # Fetch all cart items for the given cart_id
        cart_items = session.exec(
            select(CartItem).where(CartItem.cart_id == cart_id)
        ).all()
        
        if not cart_items:
            print(f"No items found in cart {cart_id}")
            return
        
        print(f"\nShopping Cart Contents for {cart_id}:")
        print("-" * 40)
        print(f"{'Item':<20} {'Quantity':<10} {'Unit Price':<12} {'Total Price':<12}")
        print("-" * 40)
        
        total_cart_price = 0.0
        
        for item in cart_items:
            product = None
            unit_price = 0.0
            item_name = f"{item.product_type} {item.model_no}"
            
            # Fetch product details based on product_type
            if item.product_type == "Chair":
                product = session.exec(
                    select(Chair).where(Chair.model_no == item.model_no)
                ).first()
            elif item.product_type == "Bed":
                product = session.exec(
                    select(Bed).where(Bed.model_no == item.model_no)
                ).first()
            elif item.product_type == "Bookshelf":
                product = session.exec(
                    select(Bookshelf).where(Bookshelf.model_no == item.model_no)
                ).first()
            
            if product:
                unit_price = product.price
            else:
                print(f"Warning: Product {item.product_type} {item.model_no} not found")
                continue
            
            # Calculate total price for this item
            total_item_price = item.quantity * unit_price
            total_cart_price += total_item_price
            
            # Print item details
            print(f"{item_name:<20} {item.quantity:<10} ${unit_price:<11.2f} ${total_item_price:<11.2f}")
        
        print("-" * 40)
        print(f"{'Total':<20} {'':<10} {'':<12} ${total_cart_price:.2f}")
        print("-" * 40)

# Example shopping cart items
cart_items = [
    CartItem(cart_id="user_001", product_type="Chair", model_no="CH-001", quantity=2),
    CartItem(cart_id="user_001", product_type="Bed", model_no="BD-002", quantity=1),
    CartItem(cart_id="user_002", product_type="Bookshelf", model_no="BS-003", quantity=1),
    CartItem(cart_id="user_002", product_type="Chair", model_no="CH-004", quantity=3),
]

# Insert products and cart items
insert_furniture(products)
insert_cart_items(cart_items)

# List contents of example carts
list_cart_contents("user_001")
list_cart_contents("user_002")