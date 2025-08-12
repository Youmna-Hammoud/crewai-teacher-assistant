from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TeacherAssistant():
    """TeacherAssistant crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def note_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['note_reader'], # type: ignore[index]
            verbose=True
        )

    @agent
    def lesson_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['lesson_planner'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def quiz_maker(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_maker'], # type: ignore[index]
            verbose=True
        )

    @agent
    def teaching_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['teaching_advisor'], # type: ignore[index]
            verbose=True
        )
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def parse_notes(self) -> Task:
        return Task(
            config=self.tasks_config['parse_notes'], # type: ignore[index]
            output_file='parsed_notes.json'
        )

    @task
    def generate_lesson_plan(self) -> Task:
        return Task(
            config=self.tasks_config['generate_lesson_plan'], # type: ignore[index]
            output_file='lesson_plan.md'
        )
    
    @task
    def generate_quiz(self) -> Task:
        return Task(
            config=self.tasks_config['generate_quiz'], # type: ignore[index]
            output_file='quiz.md'
        )

    @task
    def teaching_suggestions(self) -> Task:
        return Task(
            config=self.tasks_config['teaching_suggestions'], # type: ignore[index]
            output_file='suggestions.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TeacherAssistant crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
