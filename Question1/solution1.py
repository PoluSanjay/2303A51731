from flask import Flask, request, jsonify

app = Flask(__name__)

# Employee Class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.id = emp_id
        self.name = name
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "salary": self.salary
        }

# Store employees in a list
employees = []

# Add Employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json

    emp = Employee(
        data['id'],
        data['name'],
        data['salary']
    )

    employees.append(emp)

    return jsonify({
        "message": "Employee Added"
    }), 201


# Get All Employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify([emp.to_dict() for emp in employees])


# Update Employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json

    for emp in employees:
        if emp.id == id:
            emp.name = data.get('name', emp.name)
            emp.salary = data.get('salary', emp.salary)

            return jsonify({
                "message": "Employee Updated",
                "employee": emp.to_dict()
            })

    return jsonify({
        "error": "Employee Not Found"
    }), 404


# Delete Employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees

    employees = [emp for emp in employees if emp.id != id]

    return jsonify({
        "message": "Employee Deleted"
    })


if __name__ == '__main__':
    app.run(debug=True)