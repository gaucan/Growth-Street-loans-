from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person = Table('person', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=64)),
    Column('buss_name', VARCHAR(length=64)),
    Column('address', VARCHAR(length=64)),
    Column('company_number', VARCHAR(length=64)),
    Column('buss_sector', VARCHAR(length=64)),
    Column('name', VARCHAR(length=64)),
    Column('phone', VARCHAR(length=64)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=64)),
    Column('buss_name', String(length=64)),
    Column('address', String(length=64)),
    Column('company_number', String(length=64)),
    Column('buss_sector', String(length=64)),
    Column('name', String(length=64)),
    Column('phone', String(length=64)),
)

loan = Table('loan', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('amount', VARCHAR(length=64)),
    Column('days', VARCHAR(length=64)),
    Column('reason', VARCHAR(length=64)),
    Column('person_id', INTEGER),
)

loan = Table('loan', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('amount', String(length=64)),
    Column('days', String(length=64)),
    Column('reason', String(length=64)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['person'].drop()
    post_meta.tables['user'].create()
    pre_meta.tables['loan'].columns['person_id'].drop()
    post_meta.tables['loan'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['person'].create()
    post_meta.tables['user'].drop()
    pre_meta.tables['loan'].columns['person_id'].create()
    post_meta.tables['loan'].columns['user_id'].drop()
