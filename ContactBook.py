import json
import os

def cargar_contactos(archivo='contactos.json'):
    """Carga los contactos desde un archivo JSON."""
    if os.path.exists(archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            print("Error al cargar contactos. Iniciando con lista vacía.")
    return []

def guardar_contactos(contactos, archivo='contactos.json'):
    """Guarda los contactos en un archivo JSON."""
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(contactos, f, ensure_ascii=False, indent=4)
        print("Contactos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar contactos: {e}")

def agregar_contacto(contactos):
    """Agrega un nuevo contacto."""
    print("\n--- Agregar nuevo contacto ---")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    telefono = input("Teléfono: ").strip()
    
    if not nombre or not apellido:
        print("Nombre y apellido son obligatorios.")
        return
    
    nuevo_contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    }
    
    contactos.append(nuevo_contacto)
    print(f"Contacto '{nombre} {apellido}' agregado exitosamente.")

def buscar_contacto(contactos):
    """Busca contactos por nombre o apellido (búsqueda parcial)."""
    print("\n--- Buscar contacto ---")
    termino = input("Ingresa nombre o apellido a buscar (parcial o completo): ").strip().lower()
    
    if not termino:
        print("Debes ingresar algo para buscar.")
        return
    
    resultados = []
    for contacto in contactos:
        if (termino in contacto["nombre"].lower() or 
            termino in contacto["apellido"].lower()):
            resultados.append(contacto)
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} contacto(s):")
        for i, c in enumerate(resultados, 1):
            print(f"{i}. {c['nombre']} {c['apellido']} - {c['telefono']}")
    else:
        print("No se encontraron contactos.")

def listar_contactos(contactos):
    """Lista todos los contactos ordenados alfabéticamente por apellido y luego nombre."""
    if not contactos:
        print("No hay contactos registrados.")
        return
    
    # Ordenar: primero por apellido, luego por nombre
    contactos_ordenados = sorted(contactos, key=lambda x: (x["apellido"].lower(), x["nombre"].lower()))
    
    print("\n--- Lista de contactos (ordenados) ---")
    for i, c in enumerate(contactos_ordenados, 1):
        print(f"{i:2d}. {c['apellido']}, {c['nombre']} - {c['telefono']}")
    print(f"Total de contactos: {len(contactos_ordenados)}")

def main():
    contactos = cargar_contactos()
    print("=== ContactBook - Libro de Contactos ===\n")
    
    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos (ordenados)")
        print("4. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == '1':
            agregar_contacto(contactos)
        elif opcion == '2':
            buscar_contacto(contactos)
        elif opcion == '3':
            listar_contactos(contactos)
        elif opcion == '4':
            guardar_contactos(contactos)
            print("¡Gracias por usar ContactBook! Hasta luego.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
