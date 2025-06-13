"""

This is the main class that will be used to generate the full sport specific schedule for the athlete, including the workout and diet plans.

The process is as follows:

1. The athlete will provide the sport name and the macrocycle objective.
2. The research manager will plan the searches to perform for the query.
3. The research manager will perform the searches and write the report.
4. The report will be sent to the athlete.

"""
from custom_agents.research_agent.research_planner_agent import WebSearchPlan, WebSearchItem, research_planner_agent
from custom_agents.research_agent.research_agent import search_agent
from custom_agents.research_agent.writer_agent import ReportData, writer_agent
from custom_agents.user_data_format.user_condition import UserInput

from agents import Runner, trace, gen_trace_id
import asyncio

from custom_agents.workout_trainer import microcycle_planner
from custom_agents.workout_trainer.macrocycle_planner import macrocycle_agent, Objectives, Macrocycle
from custom_agents.workout_trainer.microcycle_planner import Microcycle, microcycle_planner_agent

class Coach:

    def __init__(self, user_input: UserInput, sport_name: str = "Superbike Racing"):
        self.user_input = user_input
        self.sport_name = sport_name



    async def run(self):
        """ Run the deep research process and generate the macrocycle plan, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        
        with trace("Research trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            
            
            print("First step: Starting research...")
            search_plan = await self.plan_searches()
            yield "Searches planned, starting to search..."     
            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report..."
            report = await self.write_report(search_results)
            yield "Report written..."
            yield report.markdown_report

            print("Second step: Generating workout plan...")
            yield "Thinking about the macrocycle objective, which microcycle objectives should be done and which tests should be performed..."
            objectives = await self.generate_macrocycle(report)
            yield "Workout objectives generated..."

            i = 1
            microcycles = []
            for objective in objectives.microcycles:
                yield f"Generating {i}º microcycle..."
                microcycle = await self.generate_microcycle(objective, report)

                yield f"{i}º microcycle generated successfully..."

                microcycles.append(microcycle)
                i += 1

            yield "Writting the macrocycle plan..."
            macrocycle = Macrocycle(
                description=objectives.description,
                microcycles=microcycles,
                tests=objectives.tests
            )
            yield "Macrocycle plan generated successfully..."
            yield macrocycle.model_dump_json()


        

    async def plan_searches(self) -> WebSearchPlan:
        """ Plan the searches to perform for the query """
        print("Planning searches for more information about the sport...")
        result = await Runner.run(
            research_planner_agent,
            f"Sport: {self.sport_name}",
        )
        print(f"Will perform {len(result.final_output.searches)} searches")
        return result.final_output_as(WebSearchPlan)

    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        """ Perform the searches to improve the workout and diet plans """
        print("Searching...")
        num_completed = 0
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
            num_completed += 1
            print(f"Searching... {num_completed}/{len(tasks)} completed")
        print("Finished searching")
        return results

    async def search(self, item: WebSearchItem) -> str | None:
        """ Perform a search for a specific item in the search plan """
        input = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(
                search_agent,
                input,
            )
            return str(result.final_output)
        except Exception:
            return None
        
    async def write_report(self, search_results: list[str]) -> ReportData:
        """ Write the report for the sport specific details """
        print("Thinking about report...")
        input = f"Sport name: {self.sport_name}\nSummarized search results: {search_results}"
        result = await Runner.run(
            writer_agent,
            input,
        )

        print("Finished writing report")
        return result.final_output_as(ReportData)
    
    async def generate_macrocycle(self, report: ReportData):
        result = await Runner.run(
            macrocycle_agent,
            f"Sport name: {self.sport_name}\nSport specific details: {report.markdown_report}\nUser input: {self.user_input.model_dump_json()}"
        )
        return result.final_output_as(Objectives)

    async def generate_microcycle(self, microcycle_objective: str, report: ReportData) -> Microcycle:
        input = (
            f"Microcycle objective: {microcycle_objective}\n"
            f"User health and physical condition: {self.user_input.user_health_condition}\n"
            f"User training availability: {self.user_input.user_training_availability}\n"
            f"Sport specific details: {report.markdown_report}"
        )
        result = await Runner.run(microcycle_planner_agent, input)
        return result.final_output_as(Microcycle)
    


    