from marshmallow import Schema, fields


class User(object):
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

  def __repr__(self):
    return '<User(name={self.name!r})>'.format(self=self)


class UserSchema(Schema):
  name = fields.Str()
  email = fields.Number()
  password = fields.Str()