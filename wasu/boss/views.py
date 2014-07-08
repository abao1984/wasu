from django.shortcuts import render
from django.db import connections
import simplejson
from django.http import HttpResponse

def get_cursor():
    try:
        # oracle 9.2.0.0 in boss server is too old, so
        # will thow exception ora-01882:timezone region not found
        # at first time
        cursor = connections['boss'].cursor()
    except:
        cursor = connections['boss'].cursor()
        return cursor
    return None

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc],row))
        for row in cursor.fetchall()
        ]

def test_view(request):
    query = get_cursor().execute('select * from rmss where subscriberno=\'D_C01_00004556\'')
    res = dictfetchall(query)
    return json_response(res)
    
def json_response(data):
    json_str = simplejson.dumps(data, ensure_ascii=False,indent=4,separators=(',\n',':'))
    return HttpResponse(json_str)
    
# Create your views here.
def search_view(request):
    page = request.GET.get('page','1')
    form_dict = request.GET
    query = 'where 1=1 '
    for key,value in form_dict.items():
        if key == 'page':
            continue
        
        if value:
            query += " and %s='%s'" % (key,value)
    sql = 'select rownum as rowno, t.* from rmss t %s' % query
    sql = 'select * from (%s and rownum<=%s*100) table_alias where table_alias.rowno>=(%s-1)*100' %(sql,page,page)
    q = get_cursor().execute(sql)
    res = dictfetchall(q)
    return json_response(res)
