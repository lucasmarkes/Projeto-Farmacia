import numpy as np
opcao = 0
i = 0

def calculo_idade(data_nasc):
    from datetime import datetime, date
    data_nasc = data_nasc.replace("-", " ")
    data_nasc = datetime.strptime(data_nasc, '%d %m %Y')
    data_atual = date.today()
    return data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))

while i == 0:
    try:
        print('-=> Sistema de farmácia! <=-')
        print('1 - Cliente')
        print('2 - Funcionário')
        print('3 - Medicamentos')
        print('-1 - Finalizar')
        escolha = int(input('Digite a opção escolhida: '))
        print('-=-'*10)

        if escolha == -1:
            print('Programa finalizado!')
            break

        if escolha == 1:
            print('1 - Cadastro')
            print('2 - Edição de dados')
            print('3 - Remoção de cliente')
            print('4 - Busca')
            print('5 - Listar')
            print('-1 Para finalizar')
            escolha_clientes = int(input('Digite a opção escolhida: '))

            if escolha_clientes == 1:
                manipulador = open('clientes.txt', 'a', encoding='utf8')
                print('Você escolheu a opção de cadastro!')
                CPF = input('Digite o CPF: ')
                CPF = CPF + '\n'
                str(CPF)
                nome = input('Digite o Nome: ')
                nome = nome + '\n'
                data_nasc = input('Digite sua data de nascimento no formato DD-MM-YYYY: ')
                data_nasc2 = data_nasc + '\n'
                idade_calculada = calculo_idade(data_nasc)
                idade_calculada = str(idade_calculada) + '\n'
                manipulador.write(CPF)
                manipulador.write(nome)
                manipulador.write(data_nasc2)
                manipulador.write(idade_calculada)
                manipulador.close()
                print('Cadastro efetuado com sucesso!')

            if escolha_clientes == 2:
                print('Você escolheu a opção de edição!')
                manipulador2 = open('clientes.txt', 'r', encoding='utf8')
                texto = manipulador2.read()
                split = texto.split()
                cpf_edit = split.index(input('Digite o CPF que deseja localizar para editar: '))
                nome_edit = split.index(input('Digite o nome corespondente ao CPF: '))
                manipulador2.close()

                print('1 - Alterar Nome')
                print('2 - Alterar data de nascimento')
                print('3 - Alterar CPF')
                print('0 - Sair')
                editar = int(input('Digite a opção escolhida: '))

                if editar == 1:
                    split.pop(nome_edit)
                    nome_alterado = input('Digite o nome de sua escolha: ')
                    split.insert(nome_edit, nome_alterado)
                    str(split)
                    texto2 = '\n'.join(split)
                    edit = open('clientes.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('O nome foi alterado!')

                if editar == 2:
                    data_edit = nome_edit + 1
                    idade_edit = data_edit + 1
                    split.pop(data_edit)
                    data_alterada = input('Digite a data correta (no formato DD-MM-YYYY): ')
                    split.insert(data_edit, data_alterada)
                    split.pop(idade_edit)
                    idade_calculada = calculo_idade(data_alterada)
                    idade_calculada = str(idade_calculada) + '\n'
                    split.insert(idade_edit, idade_calculada)
                    str(split)
                    texto2 = '\n'.join(split)
                    edit = open('clientes.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('A data foi alterada!')

                if editar == 3:
                    split.pop(cpf_edit)
                    cpf_alterado = input('Digite o CPF da sua escolha: ')
                    split.insert(cpf_edit, cpf_alterado)
                    str(split)
                    texto2 = '\n'.join(split)
                    edit = open('clientes.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('O CPF foi alterado!')

            if escolha_clientes == 3:
                print('Você escolheu a opção de remoção!')
                manipulador2=open('clientes.txt', 'r', encoding='utf8')
                texto=manipulador2.read()
                split=texto.split()
                cpf_remove=split.index(input('Digite o CPF que deseja localizar para remover: '))
                nome_remove=cpf_remove+1
                data_remove=cpf_remove+2
                idade_remove=cpf_remove+3
                split.pop(idade_remove)
                split.pop(data_remove)
                split.pop(nome_remove)
                split.pop(cpf_remove)

                print(split)
                texto='\n'.join(split)
                manipulador2.close()
                remove=open('clientes.txt', 'w', encoding='utf8')
                remove.write(texto)
                remove.close()
                print('Usuário removido com sucesso!')

            if escolha_clientes == 4:
                print('Você escolheu a opção de busca!')
                print('1 - Buscar usuário por CPF')
                print('2 - Buscar Usuário por Nome')
                print('0 - Sair')
                escolha = int(input('Digite a opção da sua escolha: '))

                if escolha == 1:
                    manipulador2=open('clientes.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    manipulador2.close()
                    cpf_edit=split.index(input('Digite o CPF a ser buscado: '))
                    idade_edit = cpf_edit + 4
                    print(split[cpf_edit:idade_edit])

                if escolha == 2:
                    manipulador2=open('clientes.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    manipulador2.close()
                    nome_edit =split.index(input('Digite o nome a ser buscado: '))
                    idade_edit=nome_edit + 3
                    cpf_edit = nome_edit - 1
                    print(split[cpf_edit:idade_edit])

            if escolha_clientes == 5:
                print('Você escolheu a opção de listar clientes!')
                manipulador2=open('clientes.txt', 'r', encoding='utf8')
                texto = manipulador2.read()
                print(texto)
                manipulador2.close()

        if escolha == 2:
            print('1 - Cadastro')
            print('2 - Edição de dados')
            print('3 - Remoção de funcionário')
            print('4 - Busca')
            print('5 - Listar')
            print('-1 Para finalizar')
            escolha_funcionarios = int(input('Digite a opção escolhida: '))

            if escolha_funcionarios == 1:
                manipulador = open('funcionarios.txt', 'a', encoding='utf8')
                matricula = input('Digite a matrícula: ')
                nome_fun = input('Digite o nome: ')
                data_nasc = input('Digite sua data de nascimento no formato DD-MM-YYYY: ')
                admissao = input('Digite sua data de admissão no formato DD-MM-YYYY: ')
                idade_calculada=calculo_idade(data_nasc)
                matricula = matricula + '\n'
                nome_fun += '\n'
                data_nasc+= '\n'
                admissao += '\n'
                idade_calculada=str(idade_calculada)+'\n'

                manipulador.write(matricula)
                manipulador.write(nome_fun)
                manipulador.write(data_nasc)
                manipulador.write(admissao)
                manipulador.write(idade_calculada)
                manipulador.write('\n')
                manipulador.close()
                print('Cadastro efetuado com sucesso!')

            if escolha_funcionarios == 2:
                print('Você escolheu a opção de edição! ')
                manipulador2=open('funcionarios.txt', 'r', encoding='utf8')
                texto = manipulador2.read()
                split = texto.split()
                matricula_edit = split.index(input('Digite a matricula que deseja localizar para editar: '))
                nome_fun_edit = split.index(input('Digite o nome corespondente aa matricula: '))
                manipulador2.close()

                print('1 - Editar Nome')
                print('2 - Editar Matrícula')
                print('3 - Editar data de nascimento')
                print('4 - Editar data de admissão')
                print('0 - Sair')
                escolha_edit_fun = int(input('Digite a opção escolhida: '))

                if escolha_edit_fun == 1:
                    split.pop(nome_fun_edit)
                    nome_alterado=input('Digite o nome de sua escolha: ')
                    split.insert(nome_fun_edit, nome_alterado)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('funcionarios.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('Nome alterado com sucesso!')

                if escolha_edit_fun == 2:
                    split.pop(matricula_edit)
                    nova_matricula = input('Digite a matricula da sua escolha: ')
                    split.insert(matricula_edit, nova_matricula)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('funcionarios.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('Matrícula alterada com sucesso!')

                if escolha_edit_fun == 3:
                    nova_data_fun = input('Digite a nova data no formato DD-MM-YYYY: ')
                    data_edit = nome_fun_edit +1
                    idade_edit = nome_fun_edit +3
                    split.pop(data_edit)
                    split.insert(data_edit, nova_data_fun)
                    split.pop(idade_edit)
                    idade_calculada=calculo_idade(nova_data_fun)
                    idade_calculada=str(idade_calculada)+'\n'
                    split.insert(idade_edit, idade_calculada)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('funcionarios.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()

                if escolha_edit_fun == 4:
                    nova_admissao_fun = input('Digite a nova data de admissão no formato DD-MM-YYYY: ')
                    data_edit=nome_fun_edit+2
                    split.pop(data_edit)
                    split.insert(data_edit, nova_admissao_fun)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('funcionarios.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()

            if escolha_funcionarios == 3:
                print('Você escolheu a opção de remoção!')
                manipulador2=open('funcionarios.txt', 'r', encoding='utf8')
                texto=manipulador2.read()
                split=texto.split()
                matricula_remove=split.index(input('Digite a matricula que deseja localizar para remover: '))
                nome_remove=matricula_remove+1
                data_remove=matricula_remove+2
                admissao_remove = matricula_remove+3
                idade_remove=matricula_remove+4

                split.pop(idade_remove)
                split.pop(admissao_remove)
                split.pop(data_remove)
                split.pop(nome_remove)
                split.pop(matricula_remove)

                texto='\n'.join(split)
                manipulador2.close()
                remove=open('funcionarios.txt', 'w', encoding='utf8')
                remove.write(texto)
                remove.close()
                print('Usuário removido com sucesso!')

            if escolha_funcionarios == 4:
                print('Você escolheu a opção de busca!')
                print('1 - Buscar por matrícula')
                print('2 - Buscar por nome')
                opcao = int(input('Digite a opção escolhida: '))

                if opcao == 1:
                    manipulador2=open('funcionarios.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    manipulador2.close()
                    matricula=split.index(input('Digite a matrícula ser buscado: '))
                    idade_edit= matricula+4
                    print(split[matricula:idade_edit])

                if opcao == 2:
                    manipulador2=open('funcionarios.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    manipulador2.close()
                    nome_edit=split.index(input('Digite o nome a ser buscado: '))
                    idade_edit=nome_edit+3
                    matricula=nome_edit-1
                    print(split[matricula:idade_edit])

            if escolha_funcionarios == 5:
                print('Você escolheu a opção de listar funcionarios!')
                manipulador2=open('funcionarios.txt', 'r', encoding='utf8')
                texto=manipulador2.read()
                print(texto)
                manipulador2.close()

        if escolha == 3:
            print('Você selecionou a opção de medicamentos! ')
            print('1 - Cadastrar Medicamento')
            print('2 - Editar medicamento')
            print('3 - Remover medicamento')
            print('4 - Buscar medicamento por nome')
            print('5 - Listar medicamentos')
            print('-1 - Para Finalizar')
            opcao = int(input('Digite a opção escolhida: '))

            if opcao == 1:
                print('Você selecionou a opção de cadastrar medicamento')
                manipulador = open('medicamentos.txt', 'a', encoding='utf8')
                nome_med = input('Digite o nome do medicamento: ')
                nome_med = nome_med + '\n'
                laboratorio = input('Digite o nome do laboratório: ')
                laboratorio = laboratorio +  '\n'
                valor = input('Valor do produto: ')
                valor = valor + '\n'
                generico = input('Digite genérico caso o produto for genérico: ')
                generico = generico +'\n'
                quantidade = input('Quantidade do medicamento: ')
                quantidade = quantidade + '\n'
                manipulador.write(nome_med)
                manipulador.write(laboratorio)
                manipulador.write(generico)
                manipulador.write(valor)
                manipulador.write(quantidade)
                manipulador.close()
                print('Medicamento registrado com sucesso!')

            if opcao == 2:
                print('Você escolheu a opção de edição!') #opção escolhida
                print('1 - Alterar nome de medicamento')
                print('2 - Alterar nome de laboratorio')
                print('3 - Alterar preço')
                print('4 - Alterar quantidade')
                print('5 - Alterar tipo(Genérico ou original')
                escolha = int(input('Digite a opção de sua escolha: '))

                if escolha == 1:
                    manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    medicamento=split.index(input('Digite o nome do medicamento que deseja localizar para editar: '))
                    manipulador2.close()
                    split.pop(medicamento)
                    nome_alterado=input('Digite o nome de sua escolha: ')
                    split.insert(medicamento, nome_alterado)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('medicamentos.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('O Nome do medicamento foi alterado!')

                if escolha == 2:
                    manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    medicamento=split.index(input('Digite o nome do medicamento que deseja localizar para editar: '))
                    lab = medicamento + 2
                    manipulador2.close()

                    split.pop(lab)
                    lab_alterado=input('Digite o nome do laboratorio de sua escolha: ')
                    split.insert(lab, lab_alterado)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('medicamentos.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('O Nome do laboratório foi alterado!')

                if escolha == 3:
                    manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    valor=split.index(input('Digite o nome do medicamento que deseja localizar para editar: '))
                    lab=valor+3
                    manipulador2.close()

                    split.pop(lab)
                    valor_alterado=input('Digite o novo valor: ')
                    split.insert(lab, valor_alterado)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('medicamentos.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('O Valor do medicamento foi alterado!')

                if escolha == 4:
                    manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    quantidade=split.index(input('Digite o nome do medicamento que deseja localizar para editar: '))
                    lab=quantidade+4
                    manipulador2.close()

                    split.pop(lab)
                    valor_alterado=input('Digite a nova quantidade de medicamentos: ')
                    split.insert(lab, valor_alterado)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('medicamentos.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('A Quantidade de medicamentos foi alterada!')

                if escolha == 5:
                    manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                    texto=manipulador2.read()
                    split=texto.split()
                    quantidade=split.index(input('Digite o nome do medicamento que deseja localizar para editar: '))
                    generico=quantidade+2
                    manipulador2.close()

                    split.pop(generico)
                    valor_alterado=input('Digite (original) se o remédio tiver essa classificação: ')
                    split.insert(generico, valor_alterado)
                    str(split)
                    texto2='\n'.join(split)
                    edit=open('medicamentos.txt', 'w', encoding='utf8')
                    edit.write(texto2)
                    edit.close()
                    print('O tipo do remédio foi alterado foi alterado!')


            if opcao == 3:
                print('Você escolheu a opção de remoção!')
                manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                texto=manipulador2.read()
                split=texto.split()
                medicamento_remove=split.index(input('Digite o nome do medicamento que deseja localizar para remover: '))
                lab_remove = medicamento_remove + 2
                valor_remove = medicamento_remove + 3
                qtd_remove = medicamento_remove + 4

                split.pop(qtd_remove)
                split.pop(valor_remove)
                split.pop(lab_remove)
                split.pop(medicamento_remove)
                texto='\n'.join(split)
                manipulador2.close()
                remove=open('medicamentos.txt', 'w', encoding='utf8')
                remove.write(texto)
                remove.close()
                print('Medicamento removido com sucesso!')

            if opcao == 4:
                print('Você escolheu a opção de buscar medicamento por nome!')
                manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                texto=manipulador2.read()
                split=texto.split()
                medicamento_localizar = split.index(input('Digite o nome do medicamento que deseja buscar: '))
                qtd_locate = medicamento_localizar + 5
                print(split[medicamento_localizar:qtd_locate])
                manipulador2.close()

            if opcao == 5:
                manipulador2=open('medicamentos.txt', 'r', encoding='utf8')
                print('Você escolheu a opção de listar medicamentos')
                print('Deseja listar todos os medicamentos? ')
                print('1 - Sim')
                print('0 - Não')
                opcao = int(input('Digite sua escolha de opção: '))

                if opcao == 1:
                    texto=manipulador2.read()
                    split = texto.split()
                    caminho = split[::]
                    print(caminho)
                    manipulador2.close()
    except ValueError:
        print('-=> Digite um dos valores e da forma indicada! <=-')
        print('')