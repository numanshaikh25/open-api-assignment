from flask_marshmallow import Marshmallow
ma = Marshmallow()

class EntrySchema(ma.Schema):
    """
    Schema
    """
    class Meta:
        fields = (
        'id', 
        'checked', 
        'name', 
        'type', 
        'age',
        'description',
        'date',
        )