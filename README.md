# Sistema de Gestión de Recibos de Pizza

Este proyecto es un sistema básico para la gestión de recibos de pizza. Permite visualizar, agregar, actualizar, eliminar y guardar recibos de manera interactiva.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Créditos](#créditos)

---

## Características

- Visualización de todos los recibos.
- Búsqueda de detalles de un recibo por su ID.
- Agregar nuevos recibos al sistema.
- Actualizar la información de un recibo existente.
- Eliminar recibos del sistema.
- Guardar todos los recibos en un archivo de texto (`receipts.txt`) de manera estructurada.

---
## Main Technologies

- `Python`: Lenguaje principal para el desarrollo.
- `Estructura Modular`:
  - `models/models.py`: Define la clase `Receipt` para manejar recibos.
  - `utils/utils.py`: Contiene funciones auxiliares como `validate_unique_id`.
  - `database/data.py`: Proporciona datos iniciales de recibos.
  - `iu/menu.py`: Gestión del menú interactivo para el usuario.
- `Archivos de Texto`:
  - `receipts.txt`: Persistencia de datos estructurados de recibos.
- `Persistencia de Datos`: Los datos ingresados permanecen tras cerrar el programa.

