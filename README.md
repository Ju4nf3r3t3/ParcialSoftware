# ParcialS

Este repositorio contiene un microservicio sencillo construido con Flask que calcula el factorial de un número enviado en la URL.

## Cómo ejecutar el servicio

1. Crear y activar un entorno virtual de Python (opcional pero recomendado).
2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:

   ```bash
   python app.py
   ```

4. Realizar una petición GET a `http://localhost:8000/factorial/<numero>`.

### Ejemplo de respuesta

```
GET http://localhost:8000/factorial/5

{
  "numero": 5,
  "factorial": 120,
  "paridad_factorial": "par"
}
```

Para números negativos el servicio devuelve un mensaje de error con estado HTTP 400.

## Extensión para integrar un servicio de historial

Si este microservicio tuviera que comunicarse con otro servicio encargado de almacenar el historial de cálculos en una base de datos externa, realizaría las siguientes modificaciones:

1. **Inyección de configuración**: agregaría variables de entorno o un archivo de configuración para almacenar la URL base del servicio de historial y credenciales si fueran necesarias.
2. **Cliente HTTP dedicado**: implementaría un módulo específico (por ejemplo, `history_client.py`) que encapsule las llamadas HTTP al servicio externo, lo que permitiría manejar timeouts, reintentos y registro de errores de forma aislada.
3. **Lógica asincrónica u operaciones en segundo plano**: dependiendo de los requisitos de rendimiento, usaría tareas asincrónicas (con Celery, RQ o similares) o hilos para evitar que la respuesta al cliente final se bloquee mientras se guarda el historial.
4. **Manejo de fallos y observabilidad**: integraría circuit breakers o backoff exponencial para tolerar errores temporales del servicio externo, además de métricas y logs para supervisar los intentos de almacenamiento.
5. **Contratos claros**: definiría el formato del payload enviado al servicio de historial (por ejemplo, número, factorial, marca de tiempo y resultado de la paridad) y validaría las respuestas para asegurar la integridad de la operación.

Con estas medidas, el microservicio seguiría respondiendo rápidamente a los usuarios, mientras que la persistencia del historial quedaría delegada de forma robusta al servicio especializado.
