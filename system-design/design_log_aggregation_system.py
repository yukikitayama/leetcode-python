from typing import List


class LogAggregator:
    def __init__(self, machines: int, services: int):
        self.machines = [[] for _ in range(machines)]
        self.services = [[] for _ in range(services)]
        self.logs = {}

    def pushLog(self, logId: int, machineId: int, serviceId: int, message: str) -> None:
        self.machines[machineId].append(logId)
        self.services[serviceId].append(logId)
        self.logs[logId] = message

    def getLogsFromMachine(self, machineId: int) -> List[int]:
        return self.machines[machineId]

    def getLogsOfService(self, serviceId: int) -> List[int]:
        return self.services[serviceId]

    def search(self, serviceId: int, searchString: str) -> List[str]:
        log_ids = self.services[serviceId]

        ans = []
        for log_id in log_ids:
            if searchString in self.logs[log_id]:
                ans.append(self.logs[log_id])
        return ans


if __name__ == '__main__':
    machines = 3
    services = 3
    obj = LogAggregator(machines, services)
