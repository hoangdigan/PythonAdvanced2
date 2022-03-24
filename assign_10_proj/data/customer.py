import sqlalchemy as sa
from .modelbase import ModelBase

class Customer(ModelBase):
    __tablename__ = 'Customer'

    id = sa.Column('Id', sa.Integer, primary_key=True, autoincrement=True)
    company_name = sa.Column('CompanyName', sa.String, nullable=False)
    contact_name = sa.Column('ContactName', sa.String, nullable=False)
    contact_title = sa.Column('ContactTitle', sa.String)

    __table_args__ = (
        sa.Index('my_index', 'CompanyName', 'ContactName'),
    )

    def __repr__(self):
        return f'<Customer {self.id} ({self.company_name_name} {self.contact_name}) {self.contact_title}>'