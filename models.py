from tortoise import fields
from tortoise.models import Model


class Users(Model):
    """Users schema"""

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=64)
    gender = fields.CharField(max_length=10)
    status = fields.CharField(max_length=10)

    class Meta:
        table = "user"

    def __str__(self) -> str:
        return self.name


class Posts(Model):
    """Posts schema"""

    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    title = fields.CharField(max_length=256)
    body = fields.TextField()

    class Meta:
        table = "post"

    def __str__(self) -> str:
        return self.title


class Comments(Model):
    """Comments schema"""

    id = fields.IntField(pk=True)
    post_id = fields.IntField()
    name = fields.CharField(max_length=64)
    email = fields.CharField(max_length=64)
    body = fields.TextField()

    class Meta:
        table = "comment"

    def __str__(self) -> str:
        return self.name


class Todos(Model):
    """Comments schema"""

    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    title = fields.CharField(max_length=256)
    due_on = fields.DatetimeField()
    status = fields.CharField(max_length=10)

    class Meta:
        table = "todo"

    def __str__(self) -> str:
        return self.title
