# ContactBook

Un libro de contactos básico en Python.  
Almacena nombres, apellidos y números de teléfono en una lista de diccionarios.  
Incluye opciones para:

- Agregar nuevos contactos
- Buscar por nombre o apellido (búsqueda parcial)
- Listar todos los contactos ordenados alfabéticamente (por apellido y luego por nombre)
- Guardar y cargar contactos automáticamente desde un archivo JSON

## Características

- Persistencia: guarda y carga contactos en `contactos.json`
- Búsqueda flexible (parcial, no sensible a mayúsculas)
- Ordenamiento automático por apellido y nombre
- Menú interactivo simple
- Usa solo Python estándar (sin dependencias externas)

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/camilobaezam/ContactBook.git
2. Entra al directorio: cd ContactBook

## Uso

Ejecuta el programa: python ContactBook.py

Menú principal:
Opciones:
1. Agregar contacto
2. Buscar contacto
3. Listar contactos (ordenados)
4. Salir
Elige una opción:

## Ejemplos de uso
Agregar un contacto

1. Opción 1
2. Ingresa:
Nombre: Juan
Apellido: Pérez
Teléfono: +56912345678

Mensaje: "Contacto 'Juan Pérez' agregado exitosamente."

Buscar contactos

Opción 2
Ingresa: "Pérez" o "juan" o "per"
Muestra todos los contactos que coincidan (parcialmente)

Listar contactos ordenados

Opción 3
Ejemplo de salida
--- Lista de contactos (ordenados) ---
 1. Avedaño, Mario - +56911111111
 2. Avedaño, Policarpo - +56922222222
 3. Bodoque, Juan - +56933333333

Total de contactos: 3

Al salir

Al elegir opción 4, guarda automáticamente en contactos.json

## Ideas para mejorar el proyecto (futuras versiones)

- Editar contactos existentes
- Eliminar contactos
- Buscar por teléfono
- Exportar a CSV
- Interfaz gráfica con tkinter
- Validación de formato de teléfono
- Agrupar por inicial de apellido

## Autor

Camilo Baeza
