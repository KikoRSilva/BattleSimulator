
"""
Francisco Silva 97433
"""
#################################################################################################
#---------------------------------------# TAD POSICAO #-----------------------------------------#
#################################################################################################
# O TAD posicao eh usado para representar uma posicao (x, y) de um labirinto arbitrariamente    #
#               grande, sendo x e y dois valores inteiros nao negativos.                        #
#################################################################################################

# CONSTRUTOR:
def cria_posicao(x, y):

    '''
        cria posicao(x,y) recebe os valores correspondentes as coordenadas de uma
        posicao e devolve a posicao correspondente. O construtor verifica a validade
        dos seus argumentos, gerando um ValueError com a mensagem 'cria posicao:
        argumentos invalidos' caso os seus argumentos nao sejam validos.

        N --> Posicao
    '''

    # verifica a validade
    if  isinstance(x, int) and isinstance(y, int) and  x >= 0 and y >= 0:
        return x,y
    raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(p):

    '''
        cria copia posicao(p) recebe uma posicao e devolve uma copia nova da posicao.

        Posicao --> Posicao
    '''

    # cria uma copia da posicao num tuplo!
    return pos[0], pos[1]


# SELETORES:
def obter_pos_x(p):

    '''
        obter_pos_x(p) devolve a componente x da posicao p.

        Posicao --> N
    '''

    # componente x
    return p[0]

def obter_pos_y(p):

    '''
        obter_pos_y(p) devolve a componente y da posicao p.

        Posicao --> N
    '''

    # componente y
    return p[1]


# RECONHECEDOR:
def eh_posicao(arg):

    '''
        eh_posicao(arg) devolve True caso o seu argumento seja um TAD posicao e
        False caso contrario.

        Universal --> Booleano
    '''

    # verifica a validade dos argumentos
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], (int)) \
           and isinstance(arg[1], int) and arg[0] >= 0 and arg[1] >= 0


# TESTE:
def posicoes_iguais(p1, p2):

    '''
        posicoes_iguais(p1, p2) devolve True apenas se p1 e p2 sao posicoes iguais

        Posicao x Posicao --> Booleano
    '''

    # verifica a validade dos argumentos
    return p1 == p2


# TRANSFORMADOR:
def posicao_para_str(p):

    '''
        posicao_para_str(p) devolve a cadeia de caracteres '(x, y)' que representa o
        seu argumento, sendo os valores x e y as coordenadas de p.

        Posicao --> Str
    '''

    # converte a posicao para uma string
    return str(p)


# FUNCOES ALTO NIVEL:
def obter_posicoes_adjacentes(p):

    '''
        obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes a posicao
        p de acordo com a ordem de leitura de um labirinto.

        Posicao --> Tuplo de Posicoes
    '''

    return tuple((cria_posicao(adj[0], adj[1]) for adj in ((obter_pos_x(p)+dx, obter_pos_y(p)+dy) \
            for dx, dy in ((0, -1), (-1, 0), (1, 0), (0, 1))) if (adj[0] >= 0 and adj[1] >= 0)))



#####################################################################################################
#------------------------------------------#TAD UNIDADE #-------------------------------------------#
#####################################################################################################
# O TAD unidade eh usado para representar as unidades de combate no simulador de batalhas presentes #
# num labirinto. Cada unidade eh caracterizada pela sua posicao, forca de ataque, pontos de vida e  #
# exercito. A forca de ataque e os pontos de vida sao valores inteiros positivos e o exercito eh    #
#                           qualquer cadeia de caracteres nao vazia.                                #
#####################################################################################################

# CONSTRUTOR:
def cria_unidade(p, v, f, strg):

    '''
        cria unidade(p, v, f, str) recebe uma posicao p, dois valores inteiros maiores
        que 0 correspondentes a vida e forca da unidade, e uma cadeia de caracteres
        nao vazia correspondente ao exercito da unidade; e devolve a unidade correspondente.
        O construtor verifica a validade dos seus argumentos, gerando um ValueError com a
        mensagem 'cria unidade: argumentos invalidos' caso os seus argumentos nao sejam validos.

        Posicao x N x N x Str --> Unidade
    '''

    # verifica a validade dos argumentos
    if not eh_posicao(p) or not isinstance(v, int) or not isinstance(f, int) or v <= 0 or f <= 0\
            or not isinstance(strg, str) or len(strg) == 0:
        raise ValueError('cria_unidade: argumentos invalidos')

    # devolve a unidade numa lista
    return {'pos': p, 'side': strg, 'life': v, 'pow': f}

def cria_copia_unidade(u):

    '''
        cria copia unidade(u) recebe uma unidade u e devolve uma nova copia da unidade.

        Unidade --> Unidade
    '''

    # devolve uma copia da unidade
    return {'pos': cria_copia_posicao(u['pos']), 'side': u['side'], 'life': u['life'], 'pow': u['pow']}


# SELETORES:
def obter_posicao(u):

    '''
        obter posicao(u) devolve a posicao da unidade u

        Unidade --> Posicao
    '''

    # devolve a posicao da unidade
    return u['pos']

def obter_exercito(u):

    '''
        obter_exercito(u) devolve a cadeia de carateres correspondente ao exercito da unidade

        Unidade --> Str
    '''

    #devolve o nome do exercito da unidade
    return u['side']

def obter_forca(u):

    '''
        obter_forca(u) devolve o valor corresponde a forca de ataque da unidade

        Unidade --> N
    '''

    # devolve o valor da forca da unidade
    return u['pow']

def obter_vida(u):

    '''
        obter_vida(u) devolve o valor corresponde aos pontos de vida da unidade

        Unidade --> N
    '''

    #devolve o valor da vida da unidade
    return u['life']


# MODIFICADORES:
def muda_posicao(u,p):

    '''
        muda posicao(u, p) modifica destrutivamente a unidade u alterando a sua
        posicao com o novo valor p, e devolve a propria unidade.

        Unidade x Posicao --> Unidade
    '''

    # substitui a posicao da unidade pela posicao dada
    u['pos'] = p
    #retorna a unidade ja alterada
    return u

def remove_vida(u, v):

    '''
        remove vida(u, v) modifica destrutivamente a unidade u alterando os seus
        pontos de vida subtraindo o valor v, e devolve a propria unidade.

        Unidade x N --> Unidade
    '''

    # subtrai a vida o valor dado
    u['life'] = u['life'] - v
    # devolve a unidade ja modificada
    return u


# RECONHECEDOR:
def eh_unidade(u):

    '''
        eh_unidade(arg) devolve True caso o seu argumento seja um TAD unidade e
        False caso contrario.

        Universal --> Booleano

    '''

    # verifca a validade dos argumentos
    return isinstance(u, dict) and len(u) == 4 and \
            tuple(sorted(u.keys())) == ('life', 'pos', 'pow', 'side') and \
            isinstance(u['side'], str) and len(u['side']) >= 1 and \
            type(u['pow']) == int and u['pow'] >= 0 and \
            type(u['life']) == int and u['life'] >= 0 and \
            eh_posicao(u['pos'])


# TESTE:
def unidades_iguais(u1, u2):

    '''
        unidades_iguais(u1, u2) devolve True apenas se u1 e u2 sao unidades iguais.

        Unidade x Unidade --> Booleano
    '''
    # verifica a validade dos argumentos
    return u1['life'] == u2['life'] and \
           u1['side'] == u2['side'] and \
           u1['pow'] == u2['pow'] and \
           posicoes_iguais(u1['pos'], u2['pos'])


# TRANSFORMADORES:
def unidade_para_char(u):

    '''
        unidade_para_char(u) devolve a cadeia de caracteres dum unico elemento,
        correspondente ao primeiro caracter em maiuscula do exercito da unidade
        passada por argumento.

        Unidade --> Str
    '''

    # devolve apenas a primeira letra do exercito da unidade em maiusculas
    return u['side'].upper()[0]

def unidade_para_str(u):

    '''
        unidade_para str(u) devolve a cadeia de caracteres que representa a unidade

        Unidade --> Str
    '''

    return '{}[{}, {}]@{}'.format(unidade_para_char(u),
                                    obter_vida(u), obter_forca(u),
                                    posicao_para_str(obter_posicao(u)))


# FUNCOES DE ALTO NIVEL:
def unidade_ataca(u1,u2):

    '''
        unidade_ataca(u1, u2) modifica destrutivamente a unidade u2 retirando o valor de
        pontos de vida correspondente a forca de ataque da unidade u1. A funcao devolve
        True se a unidade u2 for destruıda ou False caso contrario.

        Unidade x Unidade --> Booleano
    '''

    # a unidade ao atacar, subtrai a vida a forca, guarda a vida resultante e, no final, compara com 0
    # caso a vida da unidade for maior devolve false
    return obter_vida(remove_vida(u2, obter_forca(u1))) <= 0

def ordenar_unidades(t):

    '''
        ordenar_unidades(t) devolve um tuplo contendo as mesmas unidades do tuplo
        fornecido como argumento, ordenadas de acordo com a ordem de leitura do labirinto.

        Tuplo Unidades --> Tuplo Unidades
    '''

    return tuple(sorted(t, key= lambda x: (obter_pos_y(obter_posicao(x)), obter_pos_x(obter_posicao(x)))))


#####################################################################################################
#-------------------------------------------#TAD MAPA #---------------------------------------------#
#####################################################################################################
#                       O TAD mapa e usado para representar um labirinto                            #
#                       e as unidades que se encontram dentro do labirinto                          #
#####################################################################################################


# FUNCOES AUX:
def dimensao_x(d):

    '''
        Esta funcao recebe uma dimensao e devolve a dimensao x.

        Dimensao --> N
    '''

    # devolve a componente x da dimensao do labirinto
    return d[0]

def dimensao_y(d):

    '''
        Esta funcao recebe uma dimensao e devolve a dimensao Y.

        Dimensao --> N
    '''

    # devolve a componente y da dimensao do labirinto
    return d[1]


# CONSTRUTOR:
def cria_mapa(dim, walls, army1, army2):

    '''
        cria_mapa(d, w, e1, e2) recebe um tuplo d de 2 valores inteiros correspondentes as dimensoes Nx e Ny do labirinto,
        um tuplo w de 0 ou mais posicoes correspondentes as paredes que nao sao dos limites exteriores do labirinto,
        um tuplo e1 de 1 ou mais unidades do mesmo exercito, e um tuplo e2 de um ou mais unidades de um outro exercito;
        e devolve o mapa que representa internamente o labirinto e as unidades presentes.
        O construtor verifica a validade dos seus argumentos, gerando uma mensagem de erro caso os seus argumentos
        nao sejam validos.

        Tuplo Dimensoes × Tuplo Paredes Interiores × Tuplo Exercito 1 × Tuplo Exercito 2 --> Mapa
    '''

    if isinstance(dim, tuple) and len(dim) == 2 and all((type(x) == int) and (x >= 3) for x in dim) and \
            isinstance(walls, tuple) and all(eh_posicao(p) for p in walls) and \
            isinstance(army1, tuple) and len(army1) >= 1 and all(eh_unidade(p) for p in army1) and \
            isinstance(army2, tuple) and len(army2) >= 1 and all(eh_unidade(p) for p in army2):

        nx, ny = dim

        mapa = {'maze': [[0]*ny for _ in range(nx)],
                'army1': {},
                'army2': {},
                'dim': dim}

        # Cria labirinto com paredes exteriores
        for x in range(nx):
            mapa['maze'][x][0], mapa['maze'][x][-1] = 1, 1

        for x in (0, -1):
            for y in range(ny):
                mapa['maze'][x][y] = 1

        for w in walls:
            x, y = obter_pos_x(w), obter_pos_y(w)
            if (not (0 <= x < nx and 0 <= y < ny)) or mapa['maze'][x][y] == 1:
                raise ValueError('cria_mapa: argumentos invalidos')
            mapa['maze'][obter_pos_x(w)][obter_pos_y(w)] = 1

        mapa['maze'] = tuple(map(tuple, mapa['maze']))

        # cria exercito 1
        mapa['army_names'] = {}
        army_name = obter_exercito(army1[0])
        for unit in army1:
            pos = obter_posicao(unit)
            x, y = obter_pos_x(pos), obter_pos_y(pos)
            if not (0 <= x < nx and 0 <= y < ny and not mapa['maze'][x][y] and
                    posicao_para_str(pos) not in mapa['army1'] and
                    obter_exercito(unit) == army_name):
                raise ValueError('cria_mapa: argumentos invalidos')
            mapa['army1'][posicao_para_str(pos)] = unit

        mapa['army_names'][army_name] = 'army1'

        # cria exercito 2
        army_name = obter_exercito(army2[0])
        if army_name in mapa['army_names']:
            raise ValueError('cria_mapa: argumentos invalidos')

        for unit in army2:
            pos = obter_posicao(unit)
            x, y = obter_pos_x(pos), obter_pos_y(pos)
            if not (0 <= x < nx and 0 <= y < ny and not mapa['maze'][x][y] and
                    posicao_para_str(pos) not in mapa['army1'] and
                    posicao_para_str(pos) not in mapa['army2'] and
                    obter_exercito(unit) == army_name):
                raise ValueError('cria_mapa: argumentos invalidos')
            mapa['army2'][posicao_para_str(pos)] = unit

        mapa['army_names'][army_name] = 'army2'

        return mapa

    raise ValueError('cria_mapa: argumentos invalidos')


def cria_copia_mapa(mapa):

    '''
        cria_copia_mapa(m) recebe um mapa e devolve uma nova copia do mapa.

        Mapa --> Mapa
    '''

    new_mapa = dict(zip(('maze', 'dim'), (mapa['maze'], mapa['dim'])))
    new_mapa['army_names'] = mapa['army_names'].copy()
    for side in ('army1', 'army2'):
        new_mapa[side] = dict((k, cria_copia_unidade(v)) for k, v in mapa[side].items())

    return new_mapa


# SELETORES:
def obter_tamanho(m):

    '''
        obter_tamanho(m) devolve um tuplo de dois valores inteiros correspondendo
        o primeiro deles a dimensao Nx e o segundo a dimensao Ny do mapa.

        Mapa --> Tuplo
    '''

    # devolve o tamanho do labirinto em tuplo, usando funcoes auxiliares que criei.
    return  m['dim']

def obter_nome_exercitos(m):

    '''
        obter_nome_exercitos devolve um tuplo ordenado com duas cadeias de
        caracteres correspondendo aos nomes dos exercitos do mapa

        Mapa --> Tuplo
    '''

    # ordena os nomes dos exercitos das unidades
    return tuple(sorted(m['army_names'].keys()))

def obter_unidades_exercito(m, e):

    '''
        obter_unidades_exercito devolve um tuplo contendo as unidades do mapa pertencentes ao exercito
        indicado pela cadeia de caracteres e, ordenadas em ordem de leitura do labirinto.

        Mapa x Str --> Tuplo Unidades
    '''

    # se o nome do exercito for igual ao nome dado, devolve o tuplo das unidades do exercito com esse nome.
    side = m['army_names'][e]
    return ordenar_unidades(tuple(m[side].values()))

def obter_todas_unidades(mapa):

    '''
        obter_todas_unidades(m) devolve um tuplo contendo todas as unidades do mapa,
        ordenadas em ordem de leitura do labirinto.

        Mapa ---> Tuplo Unidades
    '''
    # devolve todas as unidades ordenadas pela ordem de leitura do labirinto
    return ordenar_unidades(tuple(mapa['army1'].values()) + tuple(mapa['army2'].values()))

def obter_unidade(m, p):

    '''
        obter_unidade(m, p) devolve a unidade do mapa que se encontra na posicao p.

        Mapa x Posicao --> Unidade
    '''

    pos = posicao_para_str(p)
    if pos in m['army1']:
        return m['army1'][p]
    else:
        return m['army2'][p]


# MODIFICADORES:
def eliminar_unidade(m, u):

    '''
        eliminar_unidade(m, u) modifica destrutivamente o mapa m eliminando a unidade u do mapa e
        deixando livre a posicao onde se encontrava a unidade. Devolve o proprio mapa.

        Mapa x Unidade --> Mapa
    '''

    pos = posicao_para_str(obter_posicao(u))
    if pos in m['army1']:
        del m['army1'][pos]
    else:
        del m['army2'][pos]

    return m

def mover_unidade(m, u ,p):

    '''
        mover unidade(m, u, p) modifica destrutivamente o mapa m e a unidade u alterando a posicao da unidade
        no mapa para a nova posicao p e deixando livre a posicao onde se encontrava. Devolve o proprio mapa.

        Mapa x Unidade x Posicao --> Mapa
    '''

    side = m['army_names'][obter_exercito(u)]
    del m[side][posicao_para_str(obter_posicao(u))]
    unit = muda_posicao(u, p)
    mapa[side][posicao_para_str(p)] = unit

    return m


# RECONHECEDORES:
def eh_posicao_unidade(m, p):

    '''
        eh_posicao_unidade(m, p) devolve True apenas no caso da posicao p do mapa
        estar ocupada por uma unidade.

        Mapa x Posicao --> Booleano
    '''

    return posicao_para_str(p) in m['army1'] or posicao_para_str(p) in m['army2']

def eh_posicao_corredor(m, p):

    '''
        eh_posicao_corredor(m, p) devolve True apenas no caso da posicao p do mapa corresponder a um corredor
        no labirinto (independentemente de estar ou nao ocupado por uma unidade).

        Mapa x Posicao --> Booleano
    '''

    return m['maze'][obter_pos_x(p)][obter_pos_y(p)] == 0

def eh_posicao_parede(m, p):

    '''
        eh_posicao_parede(m, p) devolve True apenas no caso da posicao p do mapa
        corresponder a uma parede do labirinto.

        Mapa x Posicao --> Booleano
    '''

    return m['maze'][obter_pos_x(po)][obter_pos_y(po)] == 1


# TESTES:
def mapas_iguais(m1, m2):

    '''
        mapas_iguais(m1, m2) devolve True apenas se m1 e m2 forem mapas iguais.

        Mapa x Mapa --> Booleano
    '''

    return sorted(m1['army1'].keys()) == sorted(m2['army1'].keys()) and \
           sorted(m1['army2'].keys()) == sorted(m2['army2'].keys()) and \
           all(unidades_iguais(m1['army1'][k], m2['army1'][k]) for k in m1['army1']) and \
           all(unidades_iguais(m1['army2'][k], m2['army2'][k]) for k in m1['army2']) and \
           m1['maze'] == m2['maze']


# TRANSFORMADOR:
def mapa_para_str(m):
    string = ''
    max_x, max_y = obter_tamanho(m)
    for y in range(max_y):
        for x in range(max_x):
            pos = cria_posicao(x, y)

            if eh_posicao_unidade(m, pos):
                string += unidade_para_char(obter_unidade(m, pos))
            elif eh_posicao_parede(m, pos):
                string += '#'
            else:
                string += '.'

        string += '\n'
    return string[:-1]


# FUNCOES ALTO NIVEL:
def obter_inimigos_adjacentes(m, u):
    enemy_side = tuple(filter(lambda u: u != obter_exercito(u), obter_nome_exercitos(m)))[0]
    return ordenar_unidades(tuple(obter_unidade(m, pos)
                                    for pos in obter_posicoes_adjacentes(obter_posicao(u))
                                    if eh_posicao_unidade(m, pos)
                                    and obter_exercito(obter_unidade(m, pos)) == enemy_side))


def obter_movimento(mapa, unit):

    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

#   FUNCAO AUX:
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

#   FUNCAO PRINCIPAL:
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


########################################################################################################################
#------------------------------------------- FUNCOES ADICIONAIS -------------------------------------------------------#
########################################################################################################################

def calcula_pontos(m, e):

    '''
        Funcao auxiliar que recebe um mapa e uma cadeia de caracteres correspondente ao nome
        de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao dum exercito eh
        o total dos pontos de vida de todas as unidades do exercito.

        Mapa x Str --> Int
    '''

    return sum(obter_vida(unit) for unit in obter_unidades_exercito(m, e))


def simula_turno(m):

    '''
        Funcao auxiliar que modifica o mapa fornecido como argumento de acordo com a simulacao de um
        turno de batalha completo, e devolve o proprio mapa. Isto eh, seguindo a ordem de leitura do labirinto,
        cada unidade (viva) realiza um unico movimento e (eventualmente) um ataque de acordo com as regras descritas.

        Mapa --> Mapa
    '''


    for pos in map(lambda u: obter_posicao(u), obter_todas_unidades(m)):
        if eh_posicao_unidade(m, pos):
            unit = obter_unidade(m, pos)
            # mover
            next_pos = obter_movimento(m, unit)
            mover_unidade(m, unit, next_pos)

            # atacar
            inimigos = obter_inimigos_adjacentes(m, unit)
            if inimigos:
                if unidade_ataca(unit, inimigos[0]):
                    eliminar_unidade(m, inimigos[0])

    return m

def simula_batalha(filename, verbose):

    def parse_infile():
        with open(filename, 'r') as infile:
            dim = eval(infile.readline())
            army1_conf = eval(infile.readline())
            army2_conf = eval(infile.readline())
            walls = tuple(cria_posicao(*pos) for pos in eval(infile.readline()))
            units1 = tuple(cria_unidade(cria_posicao(*pos), army1_conf[1], army1_conf[2], army1_conf[0])
                            for pos in eval(infile.readline()))
            units2 = tuple(cria_unidade(cria_posicao(*pos), army2_conf[1], army2_conf[2], army2_conf[0])
                            for pos in eval(infile.readline()))

        return cria_mapa(dim, walls, units1, units2)

    def box_score():
        string = '[ '
        for side in obter_nome_exercitos(mapa):
            string += (side + ':')
            string += (str(calcula_pontos(mapa, side)) + ' ')
        string += ']'

        return string

    def print_mapa_score(mapa):
        print(mapa_para_str(mapa))
        print(box_score())

    mapa = parse_infile()
    army1, army2 = obter_nome_exercitos(mapa)

    print_mapa_score(mapa)

    while obter_unidades_exercito(mapa, army1) and obter_unidades_exercito(mapa, army2):
        mapa_old = cria_copia_mapa(mapa)
        mapa = simula_turno(mapa)
        if verbose:
            print_mapa_score(mapa)

        if mapas_iguais(mapa, mapa_old):
            if not verbose:
                print_mapa_score(mapa)

            return 'EMPATE'

    if not verbose:
        print_mapa_score(mapa)

    return army1 if calcula_pontos(mapa, army1) else army2
