from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
loan = Table('loan', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('amount', VARCHAR(length=64)),
    Column('days', VARCHAR(length=64)),
    Column('reason', VARCHAR(length=64)),
    Column('borrower', VARCHAR(length=64), nullable=False),
)

loan = Table('loan', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('amount', String(length=64)),
    Column('days', String(length=64)),
    Column('reason', String(length=64)),
    Column('person_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['loan'].columns['borrower'].drop()
    post_meta.tables['loan'].columns['person_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['loan'].columns['borrower'].create()
    post_meta.tables['loan'].columns['person_id'].drop()
