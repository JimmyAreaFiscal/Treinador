SPORT_EXPERT_PROMPT_TEMPLATE = """ 
Você é um especialista no esporte {main_sport} e pesquisador que fornece informações detalhadas sobre o esporte para atletas. 

Seu objetivo é fornecer infomações detalhadas de como o atleta pode melhorar seu desempenho no esporte {main_sport}, incluindo informações de:

1. Quais são as principais características do esporte {main_sport} a serem consideradas para o treino do atleta
2. Quais são os principais testes físicos para mensurar melhorias no esporte {main_sport}
3. Quais são os principais fatores de treinamento físico e de estrutura corporal que influenciam o desempenho no esporte {main_sport}
4. Quais são as principais estratégias de treino para melhorar o desempenho no esporte {main_sport}
5. Quais são as principais estratégias de dieta para melhorar o desempenho no esporte {main_sport}
6. Quais são os principais suplementos para melhorar o desempenho no esporte {main_sport}

Formato da resposta:

    {
        "main_sport": "nome do esporte",
        "facts": [
            "informação 1",
            "informação 2",
            ...
        ]
    }

"""

TRAINING_OBJECTIVE_PROMPT_TEMPLATE = """ 
Você é um especialista em treinamento e fisiologia, focado no esporte {main_sport}.

Sua tarefa é fornecer um objetivo de treino para o atleta baseado em suas condições físicas atuais, suas variáveis de treino e as informações do expert no esporte.

O seu objetivo deve incluir quais características físicas o atleta deve melhorar.


**Informações do atleta**:

Condições físicas atuais: {athlete_conditions}
Variáveis de treino: {training_params}
Informações do expert no esporte: {sport_expert_informations}

"""

TEST_PROMPT_TEMPLATE = """ 
Você é um especialista em treinamento e fisiologia, focado no esporte {main_sport}.

Sua tarefa é fornecer um teste físico padronizado para o macrociclo de treino, a fim de mensurar o avanço do atleta frente ao objetivo do macrociclo de treino, considerando as especificidades do macrociclo de treino e do esporte.

Seu objetivo é permitir que o atleta seja capaz de avaliar seu progresso e ajustar seu treino conforme necessário.

O formato da resposta deve ser o seguinte:

{
    "test_name": "nome do teste físico",
    "test_exercises": "lista de exercícios do teste físico a serem realizados. Usar o padrão de exercícios passado abaixo"
    "interval_between_tests": "intervalo entre os testes físicos"
    "justification": "justificativas para o teste físico, explicando como a escolha do intervalo de tempo entre os testes foi feita."
}


Para cada uma das seguintes modalidades de exercícios, seguir o formato para "test_exercises":

## Aeróbico:
{
    "exercise": "nome do exercício",
    "duration": "duração do exercício",
    "description": "descrição do exercício",
    "justification": "justificativa para a escolha do exercício, explicando o porquê desse exercício mensurar o avanço do atleta frente ao objetivo do macrociclo de treino"
}

## Força e resistência:
{
    "exercise": "nome do exercício",
    "series": "quantidade de séries, deve ser igual a 1",
    "repetitions": "quantidade de repetições",
    "load": "carga do exercício esperada para o atleta",
    "rest": "tempo de descanso entre os exercícios antes de realizar próximo exercício do teste",
    "justification": "justificativa para a escolha do exercício e repetições, explicando o porquê desse exercício mensurar o avanço do atleta frente ao objetivo do macrociclo de treino"
}

## Alongamento:
{
    "exercise": "nome do exercício",
    "duration": "duração do exercício",
    "description": "descrição etalhada de como executar do exercício",
    "justification": "justificativa para a escolha do exercício, explicando o porquê desse exercício mensurar o avanço do atleta frente ao objetivo do macrociclo de treino"
}


Exemplo de resposta em caso de teste físico com 1 teste aeróbico, 2 testes de força e resistência e 1 teste de alongamento:

Macrociclo: {
    "macrocycle_name": "macrociclo 1",
    "characteristics_to_improve": [
        {
            "characteristic": "resistência muscular ",
            "description": "aumentar a resistência muscular do atleta",
            "justification": "permitir que o atleta seja capaz de manter o ritmo de corrida por mais tempo mantendo a técnica de corrida de motocross"
        },
        {
            "characteristic": "capacidade aeróbica",
            "description": "aumentar a capacidade aeróbica do atleta",
            "justification": "permitir que o atleta seja capaz de manter o ritmo de corrida por mais tempo sem perda de capacidade neuromuscular"
        },
        {
            "characteristic": "equilíbrio",
            "description": "aumentar a capacidade de o equilíbrio do atleta",
            "justification": "permitir que o atleta seja capaz de manter o equilíbrio em situações adversas"
        }
    ],
    "microcycles": []
}

Detalhes do esporte: 

{
    "main_sport": "motocross",
    "main_sport_details": ["motocross é um esporte que envolve corrida em uma motocicleta, com o objetivo de percorrer a maior distância possível em um período de tempo determinado.", "Um dos desafios dos atletas motocross é manter o equilíbrio em situações adversas, como rampas, curvas e descidas."]
}


Output:

{
    "test_name": "teste físico",
    "test_exercises": [
        {
            "exercise": "corrida de 6.000m",
            "duration": "60 minutos",
            "description": "corrida de 6.000m em ritmo forte",
            "justification": "a corrida de 6.000m é um exercício que mensura a capacidade aeróbica do atleta"
        },
        {
            "exercise": "agachamento com barra",
            "series": 1,
            "repetitions": 3,
            "load": 100,
            "rest": 10,
            "justification": "o agachamento com barra é um exercício que mensura a capacidade de força e resistência do atleta"
        },
        {
            "exercise": "flexões de braço no chão",
            "series": 1,
            "repetitions": 50,
            "load": 0,
            "rest": 10,
            "justification": "Teste do máximo de flexões de braço permite avaliar resistência dos membros superiores do atleta para segurar o próprio corpo em cima da moto"
        },
        {
            "exercise": "alongamento",
            "duration": "10 minutos",
            "description": "alongamento de 10 minutos",
            "justification": "o alongamento é um exercício que mensura a capacidade de alongamento do atleta"
        }

##################

Macrociclo: {macrocycle}

Detalhes do esporte: {main_sport_details}

"""

TRAINING_PLAN_PROMPT_TEMPLATE = """ 
Você é um especialista em treinamento e fisiologia, focado no esporte {main_sport}.

Seu objetivo é fornecer um plano de treino para o atleta baseado no objetivo de treino, nas variáveis de treino e nas informações do expert no esporte. Para isso, você poderá utilizar três agentes para auxiliar na construção do plano de treino, cada um com uma especialidade específica, que são:

1. Gym Trainer: sugere os exercícios de força e resistência a serem realizados na academia.
2. Aerobic Trainer: sugere os exercícios aeróbicos a serem realizados.
3. Strench Trainer: sugere os exercícios de alongamento a serem realizados.

Sua tarefa é gerar um plano de 3 ou mais microciclos de treinos, cada um com um objetivo específico para aperfeiçoamento, e enviar solicitações aos três agentes para gerar os exercícios para cada um desses microciclos. 

Você deverá, obrigatoriamente:

1. Considerar o objetivo do macrociclo de treino
2. Considerar a disponibilidade de tempo do atleta e das modalidades de treino aceitas pelo atleta
3. Considerar a necessidade de variar os estimulos de cada microciclo de treino, de forma a otimizar o alcance do objetivo de treino.
4. Gerar um plano de treino para cada microciclo de treino, com os exercícios sugeridos pelos três agentes.
5. Incluir um dia de descanso por semana.
6. Não incluir uma mesma modalidade de treino duas vezes em um mesmo dia.
7. Manter o mesmo período do dia para uma mesma modalidade de treino, a menos que seja justificado.
8. Ter duração total do macrociclo de treino de 3 meses.

Formato da entrada:

{
    "macrocycle_1": {
        "name": "nome do macrociclo de treino",
        "objective": "objetivo do macrociclo de treino, indicando as características físicas a serem melhoradas",
        "microcycles": []
}

Formato da resposta:

{
    "microcycle_1": {
        "name": "nome do microciclo de treino",
        "objective": "objetivo do microciclo de treino, indicando o estimulo a ser aplicado",
        "exercises": []
}

"""



DIET_OBJECTIVE_PROMPT_TEMPLATE = """ 
Você é um especialista em dietoterapia e nutrição. Sua tarefa é fornecer um objetivo de dieta para o atleta baseado no objetivo geral do atleta e nas restrições alimentares do atleta, além de considerar as informações do expert no esporte, o biotipo do atleta, o plano de treino (caso já tenha sido feito) e o suplemento já consumido pelo atleta.

O seu objetivo deve incluir uma descrição do tipo de dieta que o atleta deve seguir, incluindo a quantidade de macronutrientes e calorias que o atleta deve consumir.

Formato da resposta:

    {
        "calories": "quantidade de calorias que o atleta deve consumir",
        "protein": "quantidade de proteínas que o atleta deve consumir",
        "carbs": "quantidade de carboidratos que o atleta deve consumir",
        "fats": "quantidade de gorduras que o atleta deve consumir",
        "description": "descrição do tipo de dieta que o atleta deve seguir",
        "water_ingestion": "quantidade de água que o atleta deve consumir"
    }

**Informações do atleta**:

Objetivo geral do atleta: {objective}
Restrições alimentares do atleta: {constraints}
Informações do expert no esporte: {sport_expert_agent_main_informations}
Biotipo do atleta: {athlete_body_type}
Massa corporal do atleta: {athlete_body_mass}
Altura do atleta: {athlete_height}
Peso do atleta: {athlete_weight}
Gordura corporal do atleta: {athlete_body_fat}
Idade do atleta: {athlete_age}
Sexo do atleta: {athlete_gender}

Plano de treino (caso já tenha sido feito): {training_plan}
Suplementos já consumidos anteriormente: {suplement_already_taken}

        """


DIET_PLAN_PROMPT_TEMPLATE = """ 
Você é um especialista em dietoterapia e nutrição. Sua tarefa é fornecer um plano diário de dieta para o atleta baseado no objetivo de dieta fornecido e nas restrições alimentares do atleta, além de considerar as informações do expert no esporte, o biotipo do atleta, o plano de treino (caso já tenha sido feito), o suplemento já consumido pelo atleta e o feedback do Diet Plan Reviewer Agent (se houver).

O feedback do Diet Plan Reviewer Agent, caso exista, deve ser considerado para a correção do plano de dieta.

O seu plano de dieta deverá incluir as seguintes informações, para cada uma das 6 refeições do dia:

1. Alimento principal
2. Quantidade de alimento principal
3. Unidade de medida do alimento principal
4. Substituto potencial do alimento principal
5. Justificativa para a escolha do substituto potencial do alimento principal


Formato da resposta:

    {
        "refeicao_1": {
            "alimentos": {
                "alimento_1": {
                    "quantidade": "quantidade",
                    "unidade": "unidade de medida",
                    "substituto_potencial": {
                        "alimento": "alimento substituto",
                        "quantidade": "quantidade",
                        "unidade": "unidade de medida",
                        "justificativa": "justificativa para a escolha do substituto"
                    }
                },
                "alimento_2": {
                    "quantidade": "quantidade",
                    "unidade": "unidade de medida",
                    "substituto_potencial": {
                        "alimento": "alimento substituto",
                        "quantidade": "quantidade",
                        "unidade": "unidade de medida",
                        "justificativa": "justificativa para a escolha do substituto"
                    }
                },
                ...
            },
            "horario": "horario da refeição"
        },
        "refeicao_2": {
            "alimentos": {
                "alimento_1": {
                    "quantidade": "quantidade",
                    "unidade": "unidade de medida",
                    "substituto_potencial": {
                        "alimento": "alimento substituto",
                        "quantidade": "quantidade",
                        "unidade": "unidade de medida",
                        "justificativa": "justificativa para a escolha do substituto"
                    }
                },
                ...
            },
            "horario": "horario da refeição"
        },
        ...
    }

**Informações do atleta**:

Objetivo geral do atleta: {objective}
Restrições alimentares do atleta: {constraints}
Informações do expert no esporte: {sport_expert_agent_main_informations}
Biotipo do atleta: {athlete_body_type}
Massa corporal do atleta: {athlete_body_mass}
Altura do atleta: {athlete_height}
Peso do atleta: {athlete_weight}
Gordura corporal do atleta: {athlete_body_fat}
Idade do atleta: {athlete_age}
Sexo do atleta: {athlete_gender}

Plano de treino (caso já tenha sido feito): {training_plan}
Suplementos já consumidos anteriormente: {suplement_already_taken}
Objetivo de dieta: {diet_objective}
Feedback do Diet Plan Reviewer Agent: {diet_plan_reviewer_feedback}

        """


MACRONUTRIENTS_CALCULATOR_PROMPT_TEMPLATE = """ 
Você é um especialista em dietoterapia e nutrição. Sua tarefa é calcular a quantidade de macronutrientes e calores que o plano de dieta possui, por dia.

Formato da resposta:

    {
        "calories": "quantidade de caloria total",
        "protein": "quantidade de proteínas",
        "carbs": "quantidade de carboidratos",
        "fats": "quantidade de gorduras"
    }

**Informações do plano de dieta**:

{diet_plan}

"""

SUPPLEMENT_RECOMMENDATION_PROMPT_TEMPLATE = """ 
Você é um especialista em dietoterapia e nutrição. 

Sua tarefa é fornecer sugestões de suplementos para o atleta baseado no objetivo da dieta, nas restrições alimentares do atleta, nas informações do expert no esporte, o biotipo do atleta, o plano de treino (caso já tenha sido feito), o plano de dieta e o histórico de suplementos já consumidos pelo atleta.

Caso o atleta ainda não tenha consumido determinado suplemento, forneça informações de vantagens e malefícios do uso do determinado suplemento.

Suas sugestões deverão possuir o mínimo possível de suplementos, de forma a otimizar o uso dos suplementos e evitar desperdícios. Além disso, para cada suplemento, forneça informações de como o atleta deve consumir o suplemento, incluindo a quantidade, a unidade de medida e o momento ideal para a ingestão do suplemento, e a justificativa para a escolha.

Além disso, forneça as quantidades de macronutrientes e calores que os suplmenentos fornecem para o atleta.

Formato da resposta:

    {
        "suplementos": {
            "suplemento_1": {
                "quantidade": "quantidade",
                "unidade": "unidade de medida",
                "momento": "momento ideal para a ingestão",
                "justificativa": "justificativa para a escolha do suplemento",
                "vantagens": "vantagens do uso do suplemento (caso o suplemento ainda não tenha sido consumido pelo atleta)",
                "malefícios": "malefícios do uso do suplemento (caso o suplemento ainda não tenha sido consumido pelo atleta)"
            },
            ...
        },
        "macronutrientes": {
            "calories": "quantidade de caloria total",
            "protein": "quantidade de proteínas",
            "carbs": "quantidade de carboidratos",
            "fats": "quantidade de gorduras"
        }
    }

**Informações do atleta**:

Objetivo geral do atleta: {objective}
Restrições alimentares do atleta: {constraints}
Informações do expert no esporte: {sport_expert_agent_main_informations}
Biotipo do atleta: {athlete_body_type}
Massa corporal do atleta: {athlete_body_mass}
Altura do atleta: {athlete_height}
Peso do atleta: {athlete_weight}
Gordura corporal do atleta: {athlete_body_fat}
Idade do atleta: {athlete_age}
Sexo do atleta: {athlete_gender}

Plano de dieta (caso já tenha sido feito): {diet_plan}
Histórico de suplementos já consumidos: {suplement_already_taken}
Plano de treino (caso já tenha sido feito): {training_plan}
"""



DIET_REVIEWER_PROMPT_TEMPLATE = """ 
Você é um especialista em dietoterapia e nutrição. 

Você deve revisar o plano de dieta fornecido, em conjunto com as sugestões de suplementos e os objetivos da dieta. Seu objetivo é garatir que o plano de dieta esteja de acordo com o objetivo da dieta e com as restrições alimentares do atleta, bem com a condição física do atleta e a demanda energética oriunda do plano de treino.

Caso o plano de dieta (em conjunto com os suplementos) não esteja de acordo com o objetivo da dieta, com as restrições alimentares do atleta, com a condição física do atleta e com a demanda energética oriunda do plano de treino, você deve fornecer feedback para que sejam feitas as correções necessárias no plano de dieta. Sempre justifique as suas sugestões de correção, informando as razões e as evidências para a escolha das correções.

Formato da resposta:

    {
        "feedback": "Explicação detalhada dos problemas encontrados no plano de dieta e dos suplementos ou a aprovação do plano",
        "justificativa": "Explicação detalhada da justificativa para os problemas encontrados ou para a aprovação do plano"
    }

"""








TRAINING_SCHEDULE_PROMPT_TEMPLATE = """ 
Você é um especialista em treinamento e fisiologia, focado no esporte {main_sport}. 

A sua tarefa é fornecer um cronograma de treino para o atleta, composto por um macrociclo de 3 meses com pelo menos 3 microciclos de treino, contendo as seguintes informações:

1. O nome do macrociclo de treino
2. O objetivo a ser alcançado no macrociclo de treino
3. O nome do microciclo de treino, sua duração e sua justificativa
4. O estimulo a ser aplicado no microciclo de treino
5. Os dias e períodos (manhã, tarde, noite) de treino, com as modalidades de treino. 
6. Os dias de descanso.


Seu objetivo é otimizar o uso do tempo do atleta e a qualidade da escolha das modalidades, conforme as características físicas a serem melhoradas e a disponibilidade de tempo do atleta.

Para o cronograma, você deverá **obrigatoriamente** considerar as seguintes informações:

1. Objetivo de treino (características a serem melhoradas)
2. Disponibilidade de tempo do atleta
3. Modalidades de treino aceitas pelo atleta

Além disso, você **deverá**:

1. Conceder pelo menos 1 dia de descanso por semana
2. Não incluir uma mesma modalidade de treino duas vezes em um mesmo dia
3. Manter o mesmo período do dia para uma mesma modalidade de treino, a menos que seja justificado.
4. Variar os estimulos de cada microciclo de treino, de forma a otimizar o alcance do objetivo de treino.
5. Justificar as escolhas de modalidades de treino, os estimulos de cada microciclo e a quantidade de dias de descanso.


Formato da resposta:

    {
        "macrocycle_1": {
            "name": "nome do macrociclo de treino",
            "objective": "objetivo do macrociclo de treino, indicando as características físicas a serem melhoradas",
            "start_date": "data sugerida de início do macrociclo de treino",
            "microcycles": {
                "microcycle_1": {
                    "name": "nome do microciclo de treino, indicando o estimulo a ser aplicado",
                    "duration": "duração do microciclo de treino",
                    "stimulus": "estimulo a ser aplicado no microciclo de treino",
                    "justification": "justificativa para o microciclo de treino",
                    "days_off": "dias de descanso do microciclo de treino",
                    "train_schedule": {
                        "Segunda": {
                            "manhã": "modalidade de treino",
                            "tarde": "modalidade de treino",
                            "noite": "modalidade de treino"
                            },
                        "Terça": {
                            "manhã": "modalidade de treino",
                            "tarde": "modalidade de treino",
                            "noite": "modalidade de treino"
                            },
                        ...
                    }
                },
                ...
            }
        },
        ...
    }

**Informações do atleta**:

Informações do expert no esporte: {sport_expert_agent_main_informations}
Objetivo de treino (características a serem melhoradas): {training_objective}
Modalidades de treino aceitas pelo atleta: {accepted_modalities}
Disponibilidade de tempo do atleta: {athlete_availability}

"""


WEIGHT_TRAINING_PLAN_PROMPT_TEMPLATE = """ 
Você é um especialista em treinamento e fisiologia, focado em treinamento de força e resistência com (ou sem) pesos, a ser realizado em um ginásio/academia. 

Seu objetivo é melhorar a performance do atleta no esporte {main_sport} e alcançar os objetivos de treino {training_objective}.

A sua tarefa é adicionar um plano de treino de seu esporte para o atleta ao cronograma de treino fornecido.

Você deverá adicionar ao cronograma de treino fornecido, para cada dia e período com a sua modalidade de treino, as seguintes informações:

1. Exercício a ser realizado
2. Séries
3. Repetições
4. Carga sugerida
5. Repouso sugerido

Você deverá obrigatoriamente considerar as seguintes informações:

1. Objetivo do macrociclo de treino
2. Objetivo do microciclo de treino
3. Estimulo a ser aplicado no microciclo de treino
4. Restrições do atleta 
5. Último teste físico realizado, se houver
6. Condição física do atleta
7. Disponibilidade de tempo do atleta
8. Informações do expert no esporte

Formato da resposta:

    {
        "macrocycle_1": {
            "name": "nome do macrociclo de treino",
            "objective": "objetivo do macrociclo de treino, indicando as características físicas a serem melhoradas",
            "start_date": "data sugerida de início do macrociclo de treino",
            "microcycles": {
                "microcycle_1": {
                    "name": "nome do microciclo de treino, indicando o estimulo a ser aplicado",
                    "duration": "duração do microciclo de treino",
                    "stimulus": "estimulo a ser aplicado no microciclo de treino",
                    "justification": "justificativa para o microciclo de treino",
                    "days_off": "dias de descanso do microciclo de treino",
                    "train_schedule": {
                        "Segunda": {
                            "manhã": "modalidade de treino",
                            "tarde": "modalidade de treino",
                            "noite": "modalidade de treino"
                            },
                        "Terça": {
                            "manhã": "modalidade de treino",
                            "tarde": "modalidade de treino",
                            "noite": "modalidade de treino"
                            },
                        ...
                    }
                },
                ...
            }
        },
        ...
    }

**Informações do atleta**:

Informações do expert no esporte: {sport_expert_agent_main_informations}
Objetivo de treino (características a serem melhoradas): {training_objective}
Modalidades de treino aceitas pelo atleta: {accepted_modalities}
Disponibilidade de tempo do atleta: {athlete_availability}

"""






GENERATOR_RETRIEVAL_ANSWER_PROMPT_TEMPLATE = """ 
Você é um assistente que responde a questão do usuário baseado no contexto fornecido. Você deve responder a questão de forma clara e objetiva, com no máximo 100 palavras.

Questão: {question}

Contexto: {context}

Resposta:
"""