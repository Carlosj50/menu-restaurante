from menus import *
from colorama import init, Fore, Back, Style


# Inicializar colorama
init(autoreset=True)

def imprimir_menu(nombre_menu, lista_platos):
    print(f"\n{Fore.CYAN}Menú de {nombre_menu}:{Style.RESET_ALL}")
    for i, plato in enumerate(lista_platos, start=1):
        print(f"{Fore.YELLOW}{i}- {plato}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}V- Volver al menú principal{Style.RESET_ALL}")
    print(f"{Fore.RED}F- Finalizar pedido{Style.RESET_ALL}")

def mostrar_nombres_menus(menus_dict):
    print(f"\n{Fore.MAGENTA}Nombres de Menús:{Style.RESET_ALL}")
    for i, nombre in enumerate(menus_dict.keys(), start=1):
        print(f"{Fore.YELLOW}{i}- {nombre}{Style.RESET_ALL}")

def convertir_a_diccionario(nombres, listas_platos):
    return {nombre: platos for nombre, platos in zip(nombres, listas_platos)}

# Crear el diccionario dinámicamente
menus_dict = convertir_a_diccionario(nombres_menus, [
    menu_pastas,
    menu_carnes,
    menu_pescados,
    menu_vegetariano,
    menu_postres,
    menu_bebidas
])

def tomar_comanda():
    comanda = []

    while True:
        # Mostrar el menú principal
        mostrar_nombres_menus(menus_dict)

        # Solicitar al usuario que seleccione un menú
        try:
            seleccion_menu = int(input(f"\n{Fore.CYAN}Selecciona un tipo de plato por su número: {Style.RESET_ALL}"))
            if 1 <= seleccion_menu <= len(menus_dict):
                nombre_menu = list(menus_dict.keys())[seleccion_menu - 1]
                lista_platos = menus_dict[nombre_menu]

                # Mostrar el menú seleccionado
                while True:
                    imprimir_menu(nombre_menu, lista_platos)
                    opcion = input(f"\n{Fore.CYAN}Selecciona un plato por su número o una opción (V, F): {Style.RESET_ALL}").strip().upper()

                    if opcion == "V":
                        # Volver al menú principal
                        break
                    elif opcion == "F":
                        # Finalizar el pedido
                        print(f"\n{Fore.GREEN}✅ Comanda finalizada.{Style.RESET_ALL}")
                        print(f"{Fore.MAGENTA}Resumen del pedido:{Style.RESET_ALL}")
                        for i, plato in enumerate(comanda, start=1):
                            print(f"{Fore.YELLOW}{i}- {plato}{Style.RESET_ALL}")
                        return
                    else:
                        # Intentar seleccionar un plato por número
                        try:
                            seleccion_plato = int(opcion)
                            if 1 <= seleccion_plato <= len(lista_platos):
                                plato_seleccionado = lista_platos[seleccion_plato - 1]
                                comanda.append(f"{plato_seleccionado} (Menú de {nombre_menu})")
                                print(f"{Fore.GREEN}📝 Has añadido: {plato_seleccionado}{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}Número inválido. Elige un número del 1 al {len(lista_platos)}.{Style.RESET_ALL}")
                        except ValueError:
                            print(f"{Fore.RED}Entrada inválida. Por favor, ingresa un número o una opción válida (V, F).{Style.RESET_ALL}")

        except ValueError:
            print(f"{Fore.RED}Entrada inválida. Por favor, ingresa un número válido.{Style.RESET_ALL}")
