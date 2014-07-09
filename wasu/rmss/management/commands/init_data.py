from rmss.models import Area, MachineRoomType
from django.core.management.base import BaseCommand,NoArgsCommand, CommandError
import os

class Command(NoArgsCommand):
    base_dir = os.path.dirname(os.path.dirname(__file__))

    def init_area(self):
        file_path = os.path.join(self.base_dir,'init_area.yaml')
        f = open(file_path,'r')
        for line in f.readlines():
            name = line.split(':')[-1].strip()
            print name
            a = Area(name=name)
            a.save()
        f.close()
    
    def init_machineroom_type(self):
        file_path = os.path.join(self.base_dir,'machine_room_type.txt')
        f = open(file_path,'r')
        for line in f.readlines():
            print line
            t = MachineRoomType(name=line)
            t.save()
        f.close()

    def handle_noargs(self, **options):
        self.init_area()
        self.init_machineroom_type()
