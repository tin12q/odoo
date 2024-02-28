{
    'name':'Hospital Client Module',
    'description':'Hospital Client Module',
    'version':'1.0',
    'author':'tin12q',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/hospital_client_views.xml',
    ],
    'application':True,
    'installable':True,
    'auto_install':False,
}