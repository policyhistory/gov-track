from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, \
                       Boolean, \
                       BigInteger, SmallInteger, \
                       String

Base = declarative_base()

class TLD(Base):
  __tablename__ = 'TLD'
  id = Column(SmallInteger, primary_key=True)
  tld = Column(String(8))
  def __repr__(self):
    return "<TLD(id='%d', tld='%s')>" % (self.id, self.tld)

class Domain(Base):
  __tablename__ = 'Domain'
  id = Column(BigInteger, primary_key=True)
  url = Column(String(64), nullable=False)
  ssl = Column(Boolean, nullable=False, default=False)
  tld_id = Column(SmallInteger, ForeignKey('TLD.id'))

class Resource(Base):
  __tablename__ = 'Resource'
  id = Column(BigInteger, primary_key=True)
  name = Column(String(1024), nullable=False)
  parent = Column(BigInteger, nullable=True, default=0)
  domain_id = Column(BigInteger, ForeignKey('Domain.id'), nullable=False)
