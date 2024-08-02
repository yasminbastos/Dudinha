class Tarefa:
    def __init__(self, id, descricao, concluido=False):
        self.id = id
        self.descricao = descricao
        self.concluido = concluido

tarefas = []
t = Tarefa(1, "Comer")
tarefas.append(t)
t2 = Tarefa(2, "Domir", True)
tarefas.append(t2)