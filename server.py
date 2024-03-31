from flask import Flask, request, jsonify
app = Flask(__name__)

AR_tareas = []


# Devuelve la lista de tareas
@app.route("/tareas", methods=["GET"])
def get_tareas():
    return jsonify(AR_tareas), 200


# Ingresa una nueva tarea a la lista
@app.route("/tareas", methods=["POST"])
def post_tarea():
    AR_nueva_tarea = request.json
    AR_tareas.append(AR_nueva_tarea)
    return jsonify(AR_nueva_tarea), 200


# Actualiza los datos de una tarea, en caso de no proveer información 
# se mantiene la anterior
@app.route("/tareas", methods=["PUT"])
def put_tarea():

    AR_nombre_tarea = request.json["nombre"]
    AR_status_tarea = request.json["hecha"]

    for AR_tarea in AR_tareas:
        if AR_tarea["nombre"] == AR_nombre_tarea:
            AR_tarea["hecha"] = "si"
            return jsonify(
                {"message": "Tarea actualizada"}), 200
            
    return jsonify(
        {"message": "Tarea no encontrada"}), 404


# Elimina una tarea
@app.route("/tareas", methods=["DELETE"])
def delete_tarea():
    AR_nombre_tarea = request.json["nombre"]

    for AR_tarea in AR_tareas:
        if AR_tarea["nombre"] == AR_nombre_tarea:
            AR_tareas.remove(AR_tarea)
            return jsonify({"message": "Tarea eliminada"}), 200

    return jsonify({"message": "Tarea no encontrada"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
    