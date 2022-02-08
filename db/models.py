import enum
from sqlalchemy import Integer, Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from db.database import Base


class Role(enum.Enum):
    admin = 'admin'
    manager = 'manager'


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(Enum(Role))


class DbLicense(Base):
    __tablename__ = "licenses"
    id = Column(Integer, primary_key=True, index=True)
    licence_type = Column(String)
    license_config_id = Column(
        Integer, ForeignKey("license_configs.id")
    )


class DbLicenseConfig(Base):
    __tablename__ = "license_configs"
    id = Column(Integer, primary_key=True, index=True)
    licence_type = Column(String)
    filled_form_id = Column(Integer, ForeignKey("filled_forms.id"))


class DbLicenseType(Base):
    __tablename__ = "license_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class DbProduct(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    license_id = Column(Integer, ForeignKey("licenses.id"))
    # license_type = relationship("DbLicenseType", backref="products")


class DbClient(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String)
    first_name = Column(String)
    email = Column(String)
    phone = Column(String)
    city = Column(String)
    country = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser", backref="manager_clients")


class DbForm(Base):
    __tablename__ = "forms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


class DbFormElement(Base):
    __tablename__ = "form_elements"
    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String)
    form_element_type_id = Column(
        Integer, ForeignKey("form_element_types.id")
    )
    form_id = Column(Integer, ForeignKey("forms.id"))


class DbFormElementType(Base):
    __tablename__ = "form_element_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class DbFormElementListValue(Base):
    __tablename__ = "form_element_list_values"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(String)
    form_element_id = Column(Integer, ForeignKey("form_elements.id"))


class DbFilledForm(Base):
    __tablename__ = "filled_forms"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    form_element_id = Column(Integer, ForeignKey("form_elements.id"))


class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3


class MyClass(Base):
    __tablename__ = "some_table"
    id = Column(Integer, primary_key=True)
    value = Column(Enum(MyEnum))
