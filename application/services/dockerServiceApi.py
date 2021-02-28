import docker
from dateutil import parser


class DockerServiceApi:
    def __init__(self):
        self.client = docker.from_env()

    def getAllInstalledImages(self):
        """same as docker images ls"""
        listOfImages = []
        for image in self.client.images.list():
            # print(image.attrs['RepoTags'], image.attrs['Id'], image.attrs['Created'], image.attrs['Container'])
            listOfImages.append([image.attrs['RepoTags'], image.attrs['Id'],
                                 parser.isoparse(image.attrs['Created']).strftime('%d/%m/%Y %H:%M')])
        return listOfImages

    def deleteImageById(self, image_id: str):
        try:
            self.client.images.remove(image=image_id)
            return True
        except:
            return False

    def getAllContainers(self):
        listOfContainers = []
        for container in self.client.containers.list(all=True):
            # print(container)
            listOfContainers.append({'id': container.attrs['Id'],
                                     'createdAt': parser.isoparse(container.attrs['Created']).strftime(
                                         '%d/%m/%Y %H:%M'), 'image': container.attrs['Image'],
                                     'state': container.attrs['State'],
                                     'name': container.attrs['Name'],
                                     'command': container.attrs['Path']
                                     })
        return listOfContainers

    def getLogsFromContainerById(self, container_id: str):
        try:
            return self.client.containers.get(container_id=container_id).logs()
        except:
            return []
