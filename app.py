from flask import Flask, jsonify
from prisma import Prisma

app = Flask(__name__)

@app.route("/student", methods=["GET"])
async def list_students():
    prisma = Prisma()
    await prisma.connect()
    
    student = await prisma.student.find_first()
    student_dict = student.model_dump()
    
    return jsonify(student_dict), 200



if __name__ == "__main__":
    app.run(debug=True)