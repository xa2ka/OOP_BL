import json
import datetime
import Activity,Product,Reminders,User,UserAct,UserProd,Water
class SerializationError(Exception):
    pass

def serialize_instance(obj):
    if isinstance(obj, (Activity, Product, Reminders, User, UserAct, UserProd, Water)):
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

def serialize_to_json(obj):
    try:
        serialized = serialize_instance(obj)
        return json.dumps(serialized)
    except SerializationError as e:
        print(f"Serialization error: {str(e)}")
        return None

def deserialize_from_json(json_str, class_type):
    try:
        data = json.loads(json_str)
        return deserialize_instance(data, class_type)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {str(e)}")
        return None
    except SerializationError as e:
        print(f"Deserialization error: {str(e)}")
        return None

def save_to_file(obj, file_path):
    try:
        serialized = serialize_instance(obj)
        with open(file_path, 'w') as file:
            json.dump(serialized, file)
    except SerializationError as e:
        print(f"Serialization error: {str(e)}")
    except IOError as e:
        print(f"Error saving file: {str(e)}")

def load_from_file(file_path, class_type):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return deserialize_instance(data, class_type)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {str(e)}")
        return None
    except IOError as e:
        print(f"Error loading file: {str(e)}")
        return None
    except SerializationError as e:
        print(f"Deserialization error: {str(e)}")
        return None