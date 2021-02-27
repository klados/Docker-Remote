import docker
from dateutil import parser


class DockerServiceApi:
    def __init__(self):
        self.client = docker.from_env()
        # print(client.images.list()[0].__dict__)

    def getAllInstalledImages(self):
        """same as docker images ls"""
        listOfImages = []
        for image in self.client.images.list():
            # print(image.attrs['RepoTags'], image.attrs['Id'], image.attrs['Created'], image.attrs['Container'])
            listOfImages.append([image.attrs['RepoTags'], image.attrs['Id'],
                                 parser.isoparse(image.attrs['Created']).strftime('%d/%m/%Y %H:%M')])
        return listOfImages

    def getAllRunningContainers(self):
        for container in self.client.containers.list():
            print(container)

    def getAllContainers(self):
        pass
