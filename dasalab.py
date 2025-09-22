import sys
import os
from datetime import datetime

# Estruturas de dados em memória
patients = {}   # Dicionário: id_paciente -> {'nome': nome, 'exames': [registros_de_exame]}
patient_counter = 0
test_counter = 0

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def register_patient(name):
    """Registrar um novo paciente com ID único."""
    global patient_counter
    patient_counter += 1
    patient_id = patient_counter
    patients[patient_id] = {'nome': name, 'exames': []}
    return patient_id

def record_test(patient_id, test_type, result, unit, ref_min=None, ref_max=None):
    """Registrar um novo resultado de exame para um paciente existente."""
    global test_counter
    if patient_id not in patients:
        raise ValueError(f"ID do paciente {patient_id} não encontrado.")
    test_counter += 1
    test_id = test_counter
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    test_record = {
        'id': test_id,
        'tipo': test_type,
        'resultado': float(result),
        'unidade': unit,
        'ref_min': float(ref_min) if ref_min is not None else None,
        'ref_max': float(ref_max) if ref_max is not None else None,
        'data_hora': data_hora
    }
    patients[patient_id]['exames'].append(test_record)
    return test_id

def list_tests(patient_id):
    """Listar todos os exames para um determinado ID de paciente."""
    if patient_id not in patients:
        raise ValueError(f"ID do paciente {patient_id} não encontrado.")
    return patients[patient_id]['exames']

def abnormal_results(patient_id):
    """Retorna exames do paciente que estão fora da faixa de referência."""
    exames = list_tests(patient_id)
    return [
        rec for rec in exames
        if rec['ref_min'] is not None and rec['ref_max'] is not None
        and not (rec['ref_min'] <= rec['resultado'] <= rec['ref_max'])
    ]

def format_test_record(record):
    """Formatar um registro de exame em uma string legível."""
    ref_range = ""
    if record['ref_min'] is not None and record['ref_max'] is not None:
        ref_range = f" (Ref: {record['ref_min']}–{record['ref_max']} {record['unidade']})"
    return (f"Teste {record['id']}: {record['tipo']} = "
            f"{record['resultado']} {record['unidade']}{ref_range} "
            f"(Registrado em {record['data_hora']})")

def run():
    """Loop de interface de linha de comando para o sistema de laboratório."""
    while True:
        clear_screen()
        print("=== Sistema DASA – Gerenciamento de Exames ===\n")
        print("1 - Registrar Paciente")
        print("2 - Registrar Exame")
        print("3 - Listar Exames")
        print("4 - Filtrar Resultados Anormais")
        print("5 - Sair\n")
        cmd = input("Escolha uma opção (1-5): ").strip()

        match cmd:
            case '1':
                name = input("\nNome do paciente: ").strip()
                pid = register_patient(name)
                print(f"\nPaciente '{name}' registrado com ID {pid}")
                input("\nPressione Enter para continuar...")

            case '2':
                try:
                    pid = int(input("\nID do paciente: ").strip())
                    test_type = input("Tipo de exame: ").strip()
                    result = input("Valor do resultado: ").strip()
                    unit = input("Unidade: ").strip()
                    ref_min = input("Valor de referência mínimo (ou deixe em branco): ").strip()
                    ref_max = input("Valor de referência máximo (ou deixe em branco): ").strip()
                    ref_min = float(ref_min) if ref_min else None
                    ref_max = float(ref_max) if ref_max else None
                    tid = record_test(pid, test_type, result, unit, ref_min, ref_max)
                    print(f"\nExame ID {tid} registrado para paciente {pid}")
                except Exception as e:
                    print(f"\nErro: {e}")
                input("\nPressione Enter para continuar...")

            case '3':
                try:
                    pid = int(input("\nID do paciente: ").strip())
                    exames = list_tests(pid)
                    if not exames:
                        print("\nNenhum exame encontrado para este paciente.")
                    else:
                        print(f"\nExames do paciente {pid} ({patients[pid]['nome']}):\n")
                        for rec in exames:
                            print("  - " + format_test_record(rec))
                except Exception as e:
                    print(f"\nErro: {e}")
                input("\nPressione Enter para continuar...")

            case '4':
                try:
                    pid = int(input("\nID do paciente: ").strip())
                    anormais = abnormal_results(pid)
                    if not anormais:
                        print("\nNenhum exame fora da faixa de referência.")
                    else:
                        print(f"\nExames anormais do paciente {pid} ({patients[pid]['nome']}):\n")
                        for rec in anormais:
                            print("  - " + format_test_record(rec))
                except Exception as e:
                    print(f"\nErro: {e}")
                input("\nPressione Enter para continuar...")

            case '5':
                print("\nSaindo do sistema. Até logo!")
                break

            case _:
                print("\nComando inválido! Use apenas 1, 2, 3, 4 ou 5.")
                input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    run()
