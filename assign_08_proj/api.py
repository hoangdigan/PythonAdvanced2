from student import *

# route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'Students': Student.get_all_students()})

# route to get student by id
@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    return_value = Student.get_student(id)
    return jsonify(return_value)

# route to add new student
@app.route('/students', methods=['POST'])
def add_student():
    request_data = request.get_json()
    Student.add_student(request_data["name"], request_data["birthday"], request_data["sex"])
    response = Response("Student added", 201, mimetype='application/json')
    return response


# route to update student with PUT method
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    request_data = request.get_json()
    Student.update_student(id, request_data['name'], request_data['birthday'],request_data['sex'])
    response = Response("Student Updated", status=200, mimetype='application/json')
    return response

# route to delete student using the DELETE method
@app.route('/students/<int:id>', methods=['DELETE'])
def remove_student(id):
    Student.delete_student(id)
    response = Response("Student Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)