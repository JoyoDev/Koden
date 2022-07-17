from koden.task.config import Config
import docker
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


class DockerResult:
    """
    Result of docker run operation
    """

    def __init__(self, error: str = None, action: str = None, container_id: str = "", result: str = None):
        self.error = error
        self.action = action
        self.container_id = container_id
        self.result = result


class DockerClient:
    """
    Communicates with docker api in order to start container for specific task's config
    """

    def __init__(self, task_config: Config):
        self.client = docker.from_env()
        self.config = task_config

    # run container with specified image
    def run(self) -> DockerResult:
        try:
            self.client.images.pull(self.config.image, all_tags=False)
        except Exception as e:
            logger.error(f"Error pulling image: {self.config.image}")
            return DockerResult(error=str(e))

        host_config = self.client.api.create_host_config(
            restart_policy={"Name": self.config.restart_policy},
            mem_reservation=self.config.memory,
            publish_all_ports=True
        )

        try:
            container = self.client.api.create_container(name=self.config.name, image=self.config.image,
                                                         environment=self.config.env, command=self.config.cmd,
                                                         host_config=host_config)
        except Exception as e:
            logger.error(f"Error creating container using image {self.config.image}")
            return DockerResult(error=str(e))

        try:
            self.client.api.start(container)
        except Exception as e:
            logger.error(f"Error starting container with image {self.config.image}")
            return DockerResult(error=str(e))

        out = self.client.api.logs(container["Id"])
        logger.debug(f"Container logs: {str(out)}")

        return DockerResult(container_id=container["Id"], action="start", result="success")

    # remove container with given id
    def stop(self, container_id: str):
        logger.info(f"Attempting to stop container {container_id}")
        try:
            self.client.api.stop(container_id)
            logger.debug(f"Container {container_id} stopped")
        except Exception as e:
            logger.critical(f"Failed to stop container {container_id}")
            return DockerResult(error=str(e))

        logger.info(f"Attempting to remove container {container_id}")
        try:
            self.client.api.remove_container(container_id, v=True, link=False, force=False)
            logger.info(f"Container {container_id} removed")
            return DockerResult(container_id=container_id, action="stop", result="success")
        except Exception as e:
            logger.critical(f"Failed to remove container {container_id}")
            return DockerResult(error=str(e))
