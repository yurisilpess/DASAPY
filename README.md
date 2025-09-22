# Sistema DASA – Gerenciamento de Exames

Projeto desenvolvido para a disciplina da FIAP, inspirado nos exames mais comuns oferecidos pela DASA.  
O sistema é um script em Python que permite gerenciar pacientes e seus exames laboratoriais de forma simples via linha de comando.

---

## 📌 Funcionalidades

1. **Registrar Paciente**  
   - Cria um novo paciente com ID único sequencial.  

2. **Registrar Exame**  
   - Registra um exame para um paciente existente.  
   - Campos armazenados:  
     - Nome do exame  
     - Valor medido  
     - Unidade de medida  
     - Faixa de referência (mínimo e máximo, opcionais)  
     - Data e hora do registro  

3. **Listar Exames**  
   - Exibe todos os exames registrados para um paciente.  

4. **Filtrar Resultados Anormais**  
   - Lista apenas os exames que estão fora da faixa de referência.  

5. **Sair**  
   - Encerra o sistema.  

---

## Estrutura do Código

- `patients` (dicionário global): armazena pacientes e seus exames.  
- `patient_counter` e `test_counter`: controlam IDs únicos.  
- Funções principais:  
  - `clear_screen()` — limpa a tela.  
  - `register_patient(name)` — registra paciente.  
  - `record_test(patient_id, test_type, result, unit, ref_min, ref_max)` — registra exame.  
  - `list_tests(patient_id)` — retorna exames de um paciente.  
  - `abnormal_results(patient_id)` — retorna exames fora da faixa de referência.  
  - `format_test_record(record)` — formata exame para exibição.  
  - `run()` — loop principal com menu interativo (match/case).  

### Passos:
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/dasa-lab.git
   cd dasa-lab
