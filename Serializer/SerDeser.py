import sqlite3
import json

class SerializationError(Exception):
    pass

def serialize_instance(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    else:
        raise SerializationError("Object is not serializable")

def deserialize_instance(data, class_type):
    if not isinstance(data, dict):
        raise SerializationError("Invalid data format, expected a dictionary")
    
    try:
        return class_type.from_dict(data)
    except Exception as e:
        raise SerializationError(f"Failed to deserialize object: {str(e)}")

def serialize_to_sqlite(obj, conn, table_name):
    try:
        serialized = serialize_instance(obj)
        columns = ', '.join(serialized.keys())
        values = ', '.join(['?' for _ in serialized.values()])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        conn.execute(sql, tuple(serialized.values()))
    except SerializationError as e:
        print(f"Serialization error: {str(e)}")

def deserialize_from_sqlite(conn, table_name, class_type, row_id):
    try:
        sql = f"SELECT * FROM {table_name} WHERE id = ?"
        cursor = conn.execute(sql, (row_id,))
        data = cursor.fetchone()
        if data:
            deserialized = deserialize_instance(dict(zip(cursor.description, data)), class_type)
            return deserialized
        else:
            return None
    except sqlite3.Error as e:
        print(f"Database error: {str(e)}")
        return None
    except SerializationError as e:
        print(f"Deserialization error: {str(e)}")
        return None

# Usage example
conn = sqlite3.connect('example.db')
conn.execute('''CREATE TABLE IF NOT EXISTS mytable
                 (id INTEGER PRIMARY KEY, data TEXT)''')

# Serialize and save an object to the database
my_obj = SomeClass(...)
serialize_to_sqlite(my_obj, conn, 'mytable')

# Deserialize an object from the database
deserialized_obj = deserialize_from_sqlite(conn, 'mytable', SomeClass, 1)