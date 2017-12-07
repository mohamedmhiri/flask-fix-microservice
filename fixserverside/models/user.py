from marshmallow import Schema, fields


class User(object):
  def __init__(self, id, name, email, password):
    self.id = id
    self.name = name
    self.email = email
    self.password = password

  def __repr__(self):
    return '<User(name={self.name!r})>'.format(self=self)


class UserSchema(Schema):
  id = fields.Number()
  name = fields.Str()
  email = fields.Number()
  password = fields.Str()