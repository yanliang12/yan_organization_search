#####################server_path.py#####################
import time
import logging
import argsparser
from flask import *
from flask_restplus import *

import yan_organization_kg_search

######

ns = Namespace('knowledge_graph', description='')
args = argsparser.prepare_args()

parser = ns.parser()
parser.add_argument('organization_name', type=str, location='json')

###

req_fields = {
	'organization_name': fields.String(),
	'organization_logo_path': fields.String(),
	}
jessica_api_req = ns.model('knowledge_graph', req_fields)

rsp_fields = {\
	'status':fields.String,\
	'source_url':fields.String,\
	'running_time':fields.Float\
	}

jessica_api_rsp = ns.model('knowledge_graph', rsp_fields)

@ns.route('/organization_search')
class jessica_api(Resource):
	def __init__(self, *args, **kwargs):
		super(jessica_api, self).__init__(*args, **kwargs)
	@ns.marshal_with(jessica_api_rsp)
	@ns.expect(jessica_api_req)
	def post(self):		
		start = time.time()
		try:			
			args = parser.parse_args()
			output = {}
			if args["organization_name"] is not None:
				output['source_url'] = yan_organization_kg_search.search_organization_by_name(
					organization_name = args["organization_name"],
					)
			if args["organization_logo_path"] is not None:
				output['source_url'] = yan_organization_kg_search.search_organization_by_logo(
					organization_logo_path = args["organization_logo_path"],
					)
			output['status'] = 'success'
			output['running_time'] = float(time.time()- start)
			return output, 200
		except Exception as e:
			output = {}
			output['status'] = str(e)
			output['running_time'] = float(time.time()- start)
			return output

#####################server_path.py#####################