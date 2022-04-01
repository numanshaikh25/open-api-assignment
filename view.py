from model import Entry, db
from schema import EntrySchema
from flask import Flask, jsonify, request

def get(id=None):
    """
    GET Entry
    """
    try:

        entry = Entry.query.filter().all()
        entry_schema =  EntrySchema(many=True)
        return entry_schema.jsonify(entry)
 
    except Exception as e:
        jsonify({"error":"There was an error"})
        

def post():
    
    """
    ADD Entry
    """
    data = request.get_json()
    try:
        new_entry = Entry(**data)
        entry_schema = EntrySchema()
        db.session.add(new_entry)
        db.session.commit()
        return entry_schema.jsonify(new_entry)
    except Exception as e:
        print(e)
        jsonify({"error":"There was an error"})        


def put(id):
    """
    UPDATE Entry 
    """
    try:
            
        data = request.get_json()
        entry = Entry.query.filter_by(id=id).first()
        entry = Entry.query.filter_by(id=id)
        entry.update(data)
        db.session.commit()
                
        return jsonify(data)
    except Exception as e:
        jsonify({"error":"There was an error"})
        


def delete(id):
    """
    DELETE Entry 
    """
    try:
        print(id)
        entry = Entry.query.filter_by(id=id).first()
        print(entry)
        db.session.delete(entry)
        db.session.commit()  
        return jsonify({"success":"Entry successfully deleted"})
    except Exception as e:
        jsonify({"error":"There was an error"})