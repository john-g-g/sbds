# coding=utf-8

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import Boolean
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import BigInteger

#from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import JSON

from ..import Base
from ...enums import operation_types_enum
from ...field_handlers import amount_field
from ...field_handlers import amount_symbol_field
from ...field_handlers import comment_body_field
from .base import BaseOperation
from .base import BaseVirtualOperation

class EscrowApproveOperation(Base, BaseOperation):
    """
    
    
    Steem Blockchain Example
    ======================
    {
      "who": "on0tole",
      "approve": true,
      "from": "xtar",
      "agent": "on0tole",
      "to": "testz",
      "escrow_id": 59102208
    }

    

    """
    
    __tablename__ = 'sbds_op_escrow_approves'
    __operation_type__ = 'escrow_approve_operation'
    
    _from = Column('from', Unicode(50), index=True) # name:from
    to = Column(String(50), index=True) # steem_type:account_name_type
    agent = Column(String(50), index=True) # steem_type:account_name_type
    who = Column(String(50), index=True) # steem_type:account_name_type
    escrow_id = Column(Integer) # steem_type:uint32_t
    approve = Column(Boolean) # steem_type:bool
    operation_type = Column(
        operation_types_enum,
        nullable=False,
        index=True,
        default='escrow_approve_operation')
    
    _fields = dict(
        _from=lambda x: x.get('from'),
        to=lambda x: x.get('to'),
        agent=lambda x: x.get('agent'),
        who=lambda x: x.get('who'),
        escrow_id=lambda x: x.get('escrow_id'),
        approve=lambda x: x.get('approve'),
    )


