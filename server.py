from flask import Flask, request, jsonify
app = Flask(__name__)

PORT = 8081

tareas = []


# Devuelve la lista de tareas
@app.route("/tareas", methods=["GET"])
def get_tareas():
    return jsonify(tareas), 200


# Ingresa una nueva tarea a la lista
@app.route("/tareas", methods=["POST"])
def post_tarea():
    nueva_tarea = request.json
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 200


# Actualiza los datos de una tarea, en caso de no proveer información 
# se mantiene la anterior
@app.route("/tareas", methods=["PUT"])
def put_tarea():

    nombre = request.json["nombre"]
    hecha = request.json["hecha"]

    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tarea["hecha"] = hecha
            return jsonify(
                {"message": "Tarea actualizada"}), 200
            
    return jsonify(
        {"message": "Tarea no encontrada"}), 404


# Elimina una tarea
@app.route("/tareas", methods=["DELETE"])
def delete_tarea():
    nombre = request.json["nombre"]

    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tareas.remove(tarea)
            return jsonify({"message": "Tarea eliminada"}), 200

    return jsonify({"message": "Tarea no encontrada"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
    