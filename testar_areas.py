from database import init_db, add_area, get_all_areas, get_area_by_id, update_areas, delete_areas

def testar_areas():
    print('Iniciando teste das funções de áreas')

    print("\n1 Inicializando o BD...")
    init_db()

    print("Areas encontradas")
    areas = get_all_areas()
    if areas:
        print("Áreas encontradas")
        for area in areas:
            print(f"Nome: {area['nome']}, Descrição: {area['descricao']}")

    