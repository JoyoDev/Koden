import docker
from koden.task.config import Config


class DockerResult:
    def __init__(self, error: str = "", action: str = "", container_id: str = "", result: str = ""):
        self.error = error
        self.action = action
        self.container_id = container_id
        self.result = result


class DockerClient:
    def __init__(self, task_config: Config):
        self.client = docker.from_env()
        self.config = task_config
        self.container_id = None

    def run(self) -> DockerResult:
        try:
            self.client.images.pull(self.config.image, all_tags=False)
        except Exception as e:
            return DockerResult(error=str(e))

        host_config = self.client.api.create_host_config(
            restart_policy={"Name": self.config.restart_policy},
            mem_reservation=self.config.memory,
            publish_all_ports=True
        )

        try:
            container = self.client.api.create_container(name=self.config.name, image=self.config.image,
                                                         environment=self.config.env, command=self.config.cmd,
                                                         host_config=host_config, detach=True)
        except Exception as e:
            print(e)
            return DockerResult(error=str(e))

        try:
            self.client.api.start(container)
        except Exception as e:
            print(e)
            return DockerResult(error=str(e))

        out = self.client.api.logs(container["Id"])

        return DockerResult(container_id=container["Id"], action="start", result="success")


if __name__ == "__main__":
    config = Config(image="nginx", name="Nginx", restart_policy="always")
    d = DockerClient(task_config=config)
    res = d.run()
    print(res.container_id)
