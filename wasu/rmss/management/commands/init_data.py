from rmss.models import Area, MachineRoomType,MachineRoom
from django.core.management.base import BaseCommand,NoArgsCommand, CommandError
import os
import sys
import codecs
import csv
from StringIO import StringIO as BytesIO

class Recoder(object):
    def __init__(self, stream, decoder, encoder, eol='\r\n'):
        self._stream = stream
        self._decoder = decoder if isinstance(decoder, codecs.IncrementalDecoder) else codecs.getincrementaldecoder(decoder)()
        self._encoder = encoder if isinstance(encoder, codecs.IncrementalEncoder) else codecs.getincrementalencoder(encoder)()
        self._buf = ''
        self._eol = eol
        self._reachedEof = False

    def read(self, size=None):
        r = self._stream.read(size)
        raw = self._decoder.decode(r, size is None)
        return self._encoder.encode(raw)

    def __iter__(self):
        return self

    def __next__(self):
        if self._reachedEof:
            raise StopIteration()
        while True:
            line,eol,rest = self._buf.partition(self._eol)
            if eol == self._eol:
                self._buf = rest
                return self._encoder.encode(line + eol)
            raw = self._stream.read(1024)
            if raw == '':
                self._decoder.decode(b'', True)
                self._reachedEof = True
                return self._encoder.encode(self._buf)
            self._buf += self._decoder.decode(raw)
    next = __next__

    def close(self):
        return self._stream.close()


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
            name = line.replace('\n','')
            t = MachineRoomType(name=name)
            t.save()
        f.close()

    def init_machineroom(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        file_path = os.path.join(self.base_dir,'machine_room.csv')
        f = open(file_path,'rb')
        f = f.read().decode('utf-16').encode('utf-8')
        for index,line in enumerate(csv.reader(BytesIO(f))):
            print index
            if len(line)<30:
                continue
            m = MachineRoom()
            m.room_id=line[1]
            room_type = line[9]
            if len(room_type)>0:
                m.room_type = MachineRoomType.objects.filter(name=line[9])[0]
            else:
                m.room_type = MachineRoomType.objects.get(pk=1)
            m.name = line[2]
            m.area = Area.objects.get(pk=1)
            m.address = line[3]
            m.cover_range= ''
            m.remark = line[10]
            m.is_all_net = False 
            m.phone = ''
            m.save()

    def handle_noargs(self, **options):
        self.init_area()
        self.init_machineroom_type()
        self.init_machineroom()

