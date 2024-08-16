import subprocess


class GitIntegration:

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def create_diff_description(self, branch_1: str, branch_2: str) -> str:
        try:
            # Navega até o diretório do repositório
            result = subprocess.run(
                ['git', 'diff', branch_1, branch_2],
                cwd=self.repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if result.returncode != 0:
                raise Exception(f"Error executing git diff: {result.stderr}")

            return result.stdout
        except Exception as e:
            return str(e)


# Exemplo de uso


if __name__ == '__main__':
    repo_path = 'C:/Users/Dinopc/Documents/Projetos/Repositorios/java_examples'
    git_integration = GitIntegration(repo_path)
    diff_description = git_integration.create_diff_description('origin/main', 'test/branch')
    print(diff_description)