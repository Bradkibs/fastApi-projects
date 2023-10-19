from enum import Enum
from uuid import uuid4

from sqlalchemy import BigInteger, Boolean, Column, Unicode, Enum as SQLAlchemyEnum, Sequence
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from core.database.mixins import TimestampMixin
from core.security.access_control import Allow, Everyone, RolePrincipal, UserPrincipal


class UserPermission(Enum):
    CREATE = "create"
    READ = "read"
    EDIT = "edit"
    DELETE = "delete"


sequence = Sequence('my_sequence', start=100_000_000_000)


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True, default=sequence, unique=True)
    uuid = Column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    password = Column(Unicode(255), nullable=False)
    phone_number = Column(Unicode(20), nullable=False)
    location = Column(Unicode(255), nullable=False, default='KENYA')
    role = Column(SQLAlchemyEnum('admin', 'user', 'customer_service', name='user_role_enum'), default='user', nullable=False)
    is_active = Column(Boolean, default=False)
    username = Column(Unicode(255), nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)

    tasks = relationship(
        "Task", back_populates="author", lazy="raise", passive_deletes=True
    )

    __mapper_args__ = {"eager_defaults": True}

    def __acl__(self):
        basic_permissions = [UserPermission.READ, UserPermission.CREATE]
        self_permissions = [
            UserPermission.READ,
            UserPermission.EDIT,
            UserPermission.CREATE,
        ]
        all_permissions = list(UserPermission)

        return [
            (Allow, Everyone, basic_permissions),
            (Allow, UserPrincipal(value=self.id), self_permissions),
            (Allow, RolePrincipal(value="admin"), all_permissions),
        ]
