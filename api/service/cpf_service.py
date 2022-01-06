

from utils.paths import PROJECT_ROOT


class CPFService:
    def __init__(self, cpf: str):
        self.cpf = cpf

    def limpar_cpf(self, cpf):
        return cpf.replace('.', '').replace('-', '').replace('\n', '')

    def obter_cpfs_blacklist(self):
        with open(PROJECT_ROOT + r"\blacklist.txt") as f:
            cpfs_blacklist = [self.limpar_cpf(item) for item in f.readlines()]

        return cpfs_blacklist

    def validar(self) -> bool:
        return self.cpf.isnumeric() and len(self.cpf) == 11

    def verificar_blacklist(self) -> bool:
        cpfs_blacklist = self.obter_cpfs_blacklist()

        return self.cpf in cpfs_blacklist
