from __future__ import annotations

import math
from http import HTTPStatus
from typing import Any, Dict

from flask import Flask, jsonify

app = Flask(__name__)


def build_response(number: int) -> Dict[str, Any]:
    factorial_value = math.factorial(number)
    parity_label = "par" if factorial_value % 2 == 0 else "impar"
    return {
        "numero": number,
        "factorial": factorial_value,
        "paridad_factorial": parity_label,
    }


@app.route("/factorial/<int:number>", methods=["GET"])
def factorial_endpoint(number: int):
    if number < 0:
        return (
            jsonify({
                "error": "El factorial solo está definido para enteros no negativos.",
            }),
            HTTPStatus.BAD_REQUEST,
        )

    response_body = build_response(number)
    return jsonify(response_body)


@app.route("/")
def root():
    return (
        "Servicio de cálculo de factorial. "
        "Utilice /factorial/<numero> para obtener el factorial y la paridad."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
