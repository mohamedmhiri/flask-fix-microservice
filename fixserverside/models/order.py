from marshmallow import Schema, fields


class Order(object):
  def __init__(self, label, email, password):
    self.label = label
    self.email = email
    self.password = password

  def __repr__(self):
    return '<Order(label={self.label!r})>'.format(self=self)


class OrderSchema(Schema):
  label = fields.Str()
  email = fields.Number()
  password = fields.Str()