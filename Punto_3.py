import numpy as np
import random as rd
import matplotlib.pyplot as plt
from collections import defaultdict

class ScheduleOptimizer:
    def __init__(self):
        self.teachers = ["ProfA", "ProfB", "ProfC", "ProfD"]
        self.subjects = ["Matemáticas", "Ciencias", "Historia", "Arte"]
        self.groups = ["Grupo1", "Grupo2", "Grupo3"]
        self.time_slots = ["Lun-9:00", "Lun-11:00", "Mar-9:00", "Mar-11:00", 
                          "Mie-9:00", "Mie-11:00", "Jue-9:00", "Jue-11:00", 
                          "Vie-9:00", "Vie-11:00"]
        
        self.subject_preferences = {
            "Matemáticas": ["9:00"],
            "Ciencias": ["9:00", "11:00"],
            "Historia": ["11:00"],
            "Arte": ["11:00"]
        }
        
        self.teacher_availability = {
            "ProfA": ["Lun-9:00", "Lun-11:00", "Mar-9:00", "Mie-9:00"],
            "ProfB": ["Mar-11:00", "Jue-9:00", "Jue-11:00", "Vie-9:00"],
            "ProfC": ["Lun-9:00", "Mar-9:00", "Mie-11:00", "Vie-11:00"],
            "ProfD": ["Lun-11:00", "Mar-11:00", "Jue-9:00", "Vie-9:00"]
        }
        
        self.population_size = 50
        self.mutation_rate = 0.1
        self.elite_size = 5

    def create_individual(self):
        """Crear un horario individual (cromosoma)"""
        individual = []
        for time in self.time_slots:
            for group in self.groups:
                teacher = rd.choice(self.teachers)
                subject = rd.choice(self.subjects)
                individual.append((time, group, teacher, subject))
        return individual

    def create_population(self, size):
        """Crear población inicial"""
        return [self.create_individual() for _ in range(size)]

    def evaluate_schedule(self, schedule):
        """Calcular fitness del horario"""
        score = 1000  # Puntuación base
        
        group_time_slots = defaultdict(set)
        teacher_time_slots = defaultdict(set)
        subject_distribution = defaultdict(lambda: defaultdict(int))
        
        for time, group, teacher, subject in schedule:
            if time in group_time_slots[group]:
                score -= 50  
            group_time_slots[group].add(time)
            
            if time not in self.teacher_availability[teacher]:
                score -= 30
            
            if time in teacher_time_slots[teacher]:
                score -= 40  
            teacher_time_slots[teacher].add(time)
            
            hour = time.split('-')[1]
            if hour in self.subject_preferences[subject]:
                score += 10
            
            subject_distribution[group][subject] += 1
        
        for group in self.groups:
            subject_counts = list(subject_distribution[group].values())
            if subject_counts:
                balance_score = 1.0 / (max(subject_counts) - min(subject_counts) + 1)
                score += balance_score * 20
        
        return max(score, 1)  

    def selection(self, population, fitnesses):
        """Selección por torneo"""
        selected = []
        tournament_size = 3
        
        for _ in range(len(population)):
            tournament = rd.sample(list(zip(population, fitnesses)), tournament_size)
            winner = max(tournament, key=lambda x: x[1])[0]
            selected.append(winner)
        
        return selected

    def crossover(self, parent1, parent2):
        """Cruce de dos puntos"""
        point1 = rd.randint(1, len(parent1) // 3)
        point2 = rd.randint(2 * len(parent1) // 3, len(parent1) - 1)
        
        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
        
        return child1, child2

    def mutate(self, individual):
        """Mutación de genes"""
        if rd.random() < self.mutation_rate:
            idx = rd.randint(0, len(individual) - 1)
            time, group, _, _ = individual[idx]
            
            if rd.random() < 0.5:
                new_teacher = rd.choice(self.teachers)
                individual[idx] = (time, group, new_teacher, individual[idx][3])
            else:
                new_subject = rd.choice(self.subjects)
                individual[idx] = (time, group, individual[idx][2], new_subject)
        
        return individual

    def run_genetic_algorithm(self, generations=100, mutation_rate=0.1):
        """Ejecutar algoritmo genético"""
        self.mutation_rate = mutation_rate
        population = self.create_population(self.population_size)
        best_fitness_history = []
        avg_fitness_history = []
        
        for generation in range(generations):
            fitnesses = [self.evaluate_schedule(ind) for ind in population]
            
            best_fitness = max(fitnesses)
            avg_fitness = sum(fitnesses) / len(fitnesses)
            best_fitness_history.append(best_fitness)
            avg_fitness_history.append(avg_fitness)
            
            elite_indices = np.argsort(fitnesses)[-self.elite_size:]
            elite = [population[i] for i in elite_indices]
            
            selected = self.selection(population, fitnesses)
            
            children = []
            for i in range(0, len(selected) - 1, 2):
                child1, child2 = self.crossover(selected[i], selected[i+1])
                children.extend([child1, child2])
            
            mutated_children = [self.mutate(child) for child in children]
            
            population = elite + mutated_children[:self.population_size - self.elite_size]
            
            if generation % 10 == 0:
                print(f"Generación {generation}: Mejor fitness = {best_fitness}, Promedio = {avg_fitness:.2f}")
        
        final_fitnesses = [self.evaluate_schedule(ind) for ind in population]
        best_index = np.argmax(final_fitnesses)
        best_schedule = population[best_index]
        
        return best_schedule, best_fitness_history, avg_fitness_history

    def print_schedule(self, schedule):
        """Imprimir horario de forma organizada"""
        print("\n" + "="*60)
        print("HORARIO OPTIMIZADO")
        print("="*60)
        
        for group in self.groups:
            print(f"\n--- {group} ---")
            group_classes = [cls for cls in schedule if cls[1] == group]
            group_classes.sort(key=lambda x: x[0])  # Ordenar por tiempo
            
            for time, _, teacher, subject in group_classes:
                print(f"{time}: {subject} - {teacher}")

    def plot_convergence(self, best_history, avg_history, mutation_rate):
        """Visualizar convergencia del fitness"""
        plt.figure(figsize=(12, 6))
        plt.plot(best_history, label='Mejor Fitness', linewidth=2)
        plt.plot(avg_history, label='Fitness Promedio', linewidth=2)
        plt.title(f'Convergencia del Algoritmo Genético (Mutación: {mutation_rate})')
        plt.xlabel('Generación')
        plt.ylabel('Fitness')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

def experimentar_mutaciones():
    optimizer = ScheduleOptimizer()
    mutation_rates = [0.01, 0.05, 0.1, 0.2]
    
    results = {}
    
    for rate in mutation_rates:
        print(f"\n{'='*50}")
        print(f"EXPERIMENTO CON TASA DE MUTACIÓN: {rate}")
        print(f"{'='*50}")
        
        best_schedule, best_history, avg_history = optimizer.run_genetic_algorithm(
            generations=100, mutation_rate=rate
        )
        
        results[rate] = {
            'best_schedule': best_schedule,
            'best_history': best_history,
            'avg_history': avg_history,
            'final_fitness': max(best_history)
        }
        
        optimizer.print_schedule(best_schedule)
        
        optimizer.plot_convergence(best_history, avg_history, rate)
    
    print("\n" + "="*60)
    print("COMPARACIÓN DE TASAS DE MUTACIÓN")
    print("="*60)
    for rate, data in results.items():
        print(f"Tasa {rate}: Fitness final = {data['final_fitness']}")

if __name__ == "__main__":
    experimentar_mutaciones()