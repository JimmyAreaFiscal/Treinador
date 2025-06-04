import json
from typing import TypedDict, List, Dict, Annotated, Literal, Any, Union
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.documents import Document
from typing import Optional


# Input parameters and conditions 

class AthleteConditions(BaseModel):
    height: float 
    weight: float 
    age: int 
    gender: str 
    body_type: str 
    body_fat: float 

class TrainingParams(BaseModel):
    main_sport: str 
    training_modalities: List[Literal["corrida", "ciclismo", "musculação", "alongamento"]]
    objective: str
    constraints: List[str]
    athlete_availability: str 
    suplement_already_taken: List[str]

class ExpertInformations(BaseModel):
    main_sport: str 
    facts: List[str]


# Supervisors states 

class GeneralSupervisor(BaseModel):
    next: Literal['training_expert', 'diet_expert', 'reviewer'] = Field(
        description="Determine qual especialista deve ser chamado para continuar o processo: "
        "'training_expert' quando não houver um plano de treino"
        "'diet_expert' quando não houver um plano de dieta ou este for inadequado"
        "'reviewer' quando houver um plano de treino e de dieta e não houver feedback atualizado")
    
    reason: str = Field(
        description="Forneça uma justificativa detalhada para a decisão de roteamento, explicando a razão pela qual foi selecionado o especialista particular e como isso avança a tarefa em direção à conclusão."
    )


# Training routines

class AerobicExercice(BaseModel):
    """ Dados de exercício aeróbico """
    type: Literal["aerobic"]
    modality: str
    duration: str
    description: str
    justification: str

class WeighedExercice(BaseModel):
    """ Dados de exercício de força e resistência """
    type: Literal["weighed"]
    exercise: str
    series: int
    repetitions: str
    load: str
    rest: int
    justification: str

class StretchingExercice(BaseModel):
    """ Dados de exercício de alongamento """
    type: Literal["stretching"]
    exercise: str
    duration: str
    description: str
    justification: str

    
class RestDay(BaseModel):
    """ Dia de descanso """
    type: Literal["rest"]
    description: str
    suggestions: Optional[List[str]]
    justification: str


class TrainingDay(BaseModel):
    day: str = Literal["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
    period: str = Literal["manhã", "tarde", "noite"]
    training_routine : Union[AerobicExercice, WeighedExercice, RestDay]

class PhysicalTest(BaseModel):
    test_name: str
    test_exercises: List[Union[AerobicExercice, WeighedExercice]]
    interval_between_tests: int
    justification: str



# Diet routines

class MealUnit(BaseModel):
    name: str
    description: str
    amount: int
    unit: str
    calories: int
    protein: int
    carbs: int
    fat: int
    
    
class MealTime(BaseModel):
    period: str = Literal["café da manhã", "lanche da manhã", "almoço", "lanche da tarde", "jantar", "ceia"]
    meals: List[MealUnit]


class DietDay(BaseModel):
    diet_objective: str
    diet_routine: List[MealTime]
    duration_in_days: int
    total_calories: int
    total_protein: int
    total_carbs: int
    total_fat: int

class DietPlan(BaseModel):
    diet_days: List[DietDay]



# Agent state 

class AgentState(TypedDict):

    # Input parameters
    training_params: TrainingParams
    athlete_conditions: AthleteConditions
    sport_expert_informations: ExpertInformations

    # training routine
    training_objective: str
    physical_test: PhysicalTest
    training_feedback: List[str]
    training_approved: bool

    # diet routine
    diet_plan: DietPlan
    diet_feedback: List[str]
    diet_approved: bool

    # After the sport_expert_agent
    sport_expert_agent_main_informations: List[str]




class GradeDietPlanWithTrainingPlan(BaseModel):
    score: str = Field(description="O plano alimentar é adequado para o plano de treino e o objetivo do atleta? Responda com 'Sim' se sim ou 'Não' se não")
    justification: str = Field(description="Justifique sua resposta")


class GradeTrainingPlan(BaseModel):
    score: str = Field(description="O plano de treino é adequado para o objetivo do atleta? Responda com 'Sim' se sim ou 'Não' se não")
    justification: str = Field(description="Justifique sua resposta")

class GradeDietPlan(BaseModel):
    score: str = Field(description="O plano alimentar é adequado para o objetivo do atleta? Responda com 'Sim' se sim ou 'Não' se não")
    justification: str = Field(description="Justifique sua resposta")

