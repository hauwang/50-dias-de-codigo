class Tarefa:
    def __init__(self, id, titulo, status="pendente"):
        self.id = id
        self.titulo = titulo
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.titulo} - Status: {self.status}"


class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def criar_tarefa(self, titulo):
        if not titulo.strip():
            print("❌ O título não pode ser vazio.")
            return

        tarefa = Tarefa(self.proximo_id, titulo)
        self.tarefas.append(tarefa)
        self.proximo_id += 1

        print("✅ Tarefa criada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("📭 Nenhuma tarefa cadastrada.")
            return

        print("\n📋 Lista de Tarefas:")
        for tarefa in self.tarefas:
            print(tarefa)

    def buscar_tarefa_por_id(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                return tarefa
        return None


if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()
    gerenciador.criar_tarefa("Estudar Python")
    gerenciador.criar_tarefa("Fazer o desafio da Semana 2")
    gerenciador.listar_tarefas()

    tarefa = gerenciador.buscar_tarefa_por_id(1)
    if tarefa:
        print("\n🔍 Tarefa encontrada:")
        print(tarefa)
    else:
        print("\n❌ Tarefa não encontrada.")